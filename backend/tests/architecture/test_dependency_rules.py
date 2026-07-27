from __future__ import annotations

import ast
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest

APP_ROOT = Path(__file__).resolve().parents[2] / "app"

ALLOWED_APP_IMPORTS = {
    "domain": ("app.domain",),
    "application": ("app.application", "app.domain", "app.ports"),
    "ports": ("app.domain", "app.ports"),
}


@dataclass(frozen=True)
class Violation:
    source: str
    imported_module: str


def _is_allowed_prefix(module: str, prefixes: tuple[str, ...]) -> bool:
    return any(module == prefix or module.startswith(f"{prefix}.") for prefix in prefixes)


def _resolve_relative_module(
    node: ast.ImportFrom,
    *,
    current_package: tuple[str, ...],
) -> str:
    if node.level == 0:
        return node.module or ""

    keep = len(current_package) - (node.level - 1)
    base = current_package[: max(keep, 0)]
    suffix = tuple((node.module or "").split(".")) if node.module else ()
    return ".".join((*base, *suffix))


def _literal_dynamic_import(node: ast.Call) -> str | None:
    if not node.args or not isinstance(node.args[0], ast.Constant):
        return None
    if not isinstance(node.args[0].value, str):
        return None

    if isinstance(node.func, ast.Name) and node.func.id == "__import__":
        return node.args[0].value
    if isinstance(node.func, ast.Attribute) and node.func.attr == "import_module":
        return node.args[0].value
    return None


def _imported_modules(
    source: str,
    *,
    current_package: tuple[str, ...],
) -> list[str]:
    tree = ast.parse(source)
    modules: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            module = _resolve_relative_module(node, current_package=current_package)
            if module:
                modules.append(module)
        elif isinstance(node, ast.Call):
            module = _literal_dynamic_import(node)
            if module:
                modules.append(module)

    return modules


def _violations_for_source(
    source: str,
    *,
    layer: str,
    source_name: str = "<fixture>",
    current_package: tuple[str, ...] | None = None,
) -> list[Violation]:
    package = current_package or ("app", layer)
    violations: list[Violation] = []

    for module in _imported_modules(source, current_package=package):
        root = module.partition(".")[0]
        if root == "app":
            if not _is_allowed_prefix(module, ALLOWED_APP_IMPORTS[layer]):
                violations.append(Violation(source_name, module))
        elif root not in sys.stdlib_module_names and root != "__future__":
            violations.append(Violation(source_name, module))

    return violations


def _violations_for_layer(layer: str) -> list[Violation]:
    layer_root = APP_ROOT / layer
    violations: list[Violation] = []

    for path in sorted(layer_root.rglob("*.py")):
        relative_parent = path.parent.relative_to(APP_ROOT)
        current_package = ("app", *relative_parent.parts)
        violations.extend(
            _violations_for_source(
                path.read_text(encoding="utf-8"),
                layer=layer,
                source_name=str(path.relative_to(APP_ROOT.parent)),
                current_package=current_package,
            )
        )

    return violations


@pytest.mark.parametrize("layer", sorted(ALLOWED_APP_IMPORTS))
def test_implemented_layers_obey_dependency_rules(layer: str) -> None:
    assert _violations_for_layer(layer) == []


@pytest.mark.parametrize(
    ("layer", "source", "forbidden_module"),
    [
        ("domain", "import fastapi", "fastapi"),
        ("domain", "from app.application import services", "app.application"),
        ("application", "from app.api import routes", "app.api"),
        ("ports", "from app.adapters import vehicle", "app.adapters"),
        (
            "application",
            'import importlib\nimportlib.import_module("app.core.config")',
            "app.core.config",
        ),
    ],
)
def test_representative_boundary_violations_are_rejected(
    layer: str,
    source: str,
    forbidden_module: str,
) -> None:
    assert _violations_for_source(source, layer=layer) == [
        Violation("<fixture>", forbidden_module)
    ]
