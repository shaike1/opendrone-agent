import assert from 'node:assert/strict'
import { afterEach, describe, it } from 'node:test'
import { getHealth, getVersion, isHealthResponse, isVersionResponse } from './api.ts'

const originalFetch = globalThis.fetch

afterEach(() => {
  globalThis.fetch = originalFetch
})

describe('status response validation', () => {
  it('accepts the documented health and version responses', () => {
    assert.equal(isHealthResponse({ status: 'healthy' }), true)
    assert.equal(isVersionResponse({ name: 'opendrone-agent', version: '0.1.0' }), true)
  })

  it('rejects malformed, empty, and missing fields', () => {
    assert.equal(isHealthResponse({}), false)
    assert.equal(isHealthResponse({ status: '   ' }), false)
    assert.equal(isHealthResponse({ status: 200 }), false)
    assert.equal(isVersionResponse({ name: 'opendrone-agent' }), false)
    assert.equal(isVersionResponse({ name: [], version: '0.1.0' }), false)
    assert.equal(isVersionResponse(null), false)
  })
})

describe('status API boundary', () => {
  it('returns a validated response and requests JSON', async () => {
    globalThis.fetch = async (input, init) => {
      assert.equal(input, '/health')
      assert.deepEqual(init?.headers, { Accept: 'application/json' })
      return Response.json({ status: 'healthy' })
    }

    await assert.doesNotReject(async () => {
      assert.deepEqual(await getHealth(), { status: 'healthy' })
    })
  })

  it('rejects a malformed successful response at the boundary', async () => {
    globalThis.fetch = async () => Response.json({ version: 1 })

    await assert.rejects(getVersion(), /Invalid response from \/version/)
  })

  it('preserves HTTP failures as request errors', async () => {
    globalThis.fetch = async () => new Response(null, { status: 503 })

    await assert.rejects(getHealth(), /Request failed with status 503/)
  })
})
