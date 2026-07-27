export interface HealthResponse {
  status: string
}

export interface VersionResponse {
  name: string
  version: string
}

type ResponseValidator<T> = (value: unknown) => value is T

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}

function isNonEmptyString(value: unknown): value is string {
  return typeof value === 'string' && value.trim().length > 0
}

export function isHealthResponse(value: unknown): value is HealthResponse {
  return isRecord(value) && isNonEmptyString(value.status)
}

export function isVersionResponse(value: unknown): value is VersionResponse {
  return isRecord(value) && isNonEmptyString(value.name) && isNonEmptyString(value.version)
}

async function getJson<T>(path: string, isValid: ResponseValidator<T>): Promise<T> {
  const response = await fetch(path, { headers: { Accept: 'application/json' } })

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`)
  }

  const body: unknown = await response.json()
  if (!isValid(body)) {
    throw new Error(`Invalid response from ${path}`)
  }

  return body
}

export function getHealth(): Promise<HealthResponse> {
  return getJson('/health', isHealthResponse)
}

export function getVersion(): Promise<VersionResponse> {
  return getJson('/version', isVersionResponse)
}
