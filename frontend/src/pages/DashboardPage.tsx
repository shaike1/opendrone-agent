import { StatusCard } from '../components/StatusCard'
import { useBackendStatus } from '../hooks/useBackendStatus'

export function DashboardPage() {
  const { health, version, isLoading, error, refresh } = useBackendStatus()

  return (
    <main className="dashboard">
      <header className="dashboard__header">
        <p className="eyebrow">Service dashboard</p>
        <h1>OpenDrone Agent</h1>
        <p>Frontend foundation and backend service information.</p>
      </header>

      {error ? (
        <section className="error-message" role="alert">
          <h2>Unable to connect</h2>
          <p>{error}</p>
          <button type="button" onClick={refresh}>
            Try again
          </button>
        </section>
      ) : (
        <div className="status-grid" aria-busy={isLoading}>
          <StatusCard
            label="Backend status"
            value={isLoading ? 'Checking…' : (health ?? 'Unknown')}
            isHealthy={!isLoading && health === 'healthy'}
          />
          <StatusCard
            label="Backend version"
            value={isLoading ? 'Loading…' : (version ?? 'Unknown')}
          />
        </div>
      )}
    </main>
  )
}
