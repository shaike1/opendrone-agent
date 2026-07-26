import { useCallback, useEffect, useState } from 'react'
import { getHealth, getVersion } from '../services/api'

interface BackendStatus {
  health: string | null
  version: string | null
  isLoading: boolean
  error: string | null
  refresh: () => void
}

export function useBackendStatus(): BackendStatus {
  const [health, setHealth] = useState<string | null>(null)
  const [version, setVersion] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const refresh = useCallback(() => {
    setIsLoading(true)
    setError(null)

    Promise.all([getHealth(), getVersion()])
      .then(([healthResponse, versionResponse]) => {
        setHealth(healthResponse.status)
        setVersion(versionResponse.version)
      })
      .catch(() => {
        setHealth(null)
        setVersion(null)
        setError('The backend is unavailable. Make sure it is running, then try again.')
      })
      .finally(() => setIsLoading(false))
  }, [])

  useEffect(() => refresh(), [refresh])

  return { health, version, isLoading, error, refresh }
}
