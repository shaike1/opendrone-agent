export interface HealthResponse {
  status: string
}

export interface VersionResponse {
  name: string
  version: string
}

async function getJson<T>(path: string): Promise<T> {
  const response = await fetch(path, { headers: { Accept: 'application/json' } })

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`)
  }

  return response.json() as Promise<T>
}

export function getHealth(): Promise<HealthResponse> {
  return getJson<HealthResponse>('/health')
}

export function getVersion(): Promise<VersionResponse> {
  return getJson<VersionResponse>('/version')
}
