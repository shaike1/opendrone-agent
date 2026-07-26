interface StatusCardProps {
  label: string
  value: string
  isHealthy?: boolean
}

export function StatusCard({ label, value, isHealthy = false }: StatusCardProps) {
  return (
    <section className="status-card">
      <h2>{label}</h2>
      <p className={isHealthy ? 'status-value status-value--healthy' : 'status-value'}>
        {isHealthy && <span className="status-dot" aria-hidden="true" />}
        {value}
      </p>
    </section>
  )
}
