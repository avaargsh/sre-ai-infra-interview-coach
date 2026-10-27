# Scenario design and domain rotation

Each scenario has one primary failure mechanism and at most a few plausible competing explanations. Rotate domains and avoid disguising the same mechanism with a different product name.

## Domain matrix

| Domain | Scenario families | Evidence to include |
|---|---|---|
| Linux/kernel | FD exhaustion, memory reclaim, filesystem latency, CPU steal, cgroup v2 pressure | process state, kernel counters/logs, resource limits, syscalls/I/O |
| Network/security | asymmetric routing, fragmentation, TLS rotation, conntrack, TCP resets, proxy mismatch | flow direction, packet evidence, counters, endpoint identity, config diff |
| DNS/service discovery | stale records, negative caching, resolver saturation, EndpointSlice, dual stack | node/client comparisons, TTL, endpoint state, resolver path |
| Kubernetes/runtime | scheduling, probes, rollout capacity, PDB/eviction, kubelet, container runtime, CSI | events, scheduler decisions, Pod/Node state, requests vs capacity |
| Observability/reliability | broken SLI denominator, scrape gaps, cardinality, burn-rate mismatch, capacity forecast | raw samples, labels, query semantics, SLO windows |
| Go/service runtime | GC tail latency, goroutine leaks, blocked channels, lock contention, FD leak | pprof, runtime metrics, traces, queue depth, cancellation behavior |
| Database/cache/queues | replica lag, lock contention, cache stampede, hot partition, ordering, DLQ growth | query/queue behavior, offsets/LSNs, concurrency, transaction semantics |
| Release/security/DR | artifact provenance, secret rotation, dependency upgrade, restore mismatch, region failover | immutable digest, deployment diff, rollback preconditions, audit trail |
| GPU device/scheduling | unhealthy allocation, MIG mismatch, time-slicing, topology, driver regression | host/container views, GPU UUID/profile, clocks/power/errors, allocation |
| LLM inference | KV fragmentation, prefill bottleneck, decode slowdown, batching regression, model loading storm | TTFT/TPOT, queue time, batch size, cache usage, token lengths |
| RDMA/distributed GPU | asymmetric RDMA path, PFC/ECN, NIC mismatch, collective tail | link counters, per-rank timing, errors, topology, test scale |
| Agent runtime/control plane | duplicate Run side effects, lease expiry, cancellation race, stale state, event replay gap | stable IDs, state machine, event sequence, idempotency, external side effects |

## Rotation rules

- Prefer a different primary domain than the previous scenario.
- Avoid the same core failure mechanism for at least the next 8–10 scenarios.
- Treat these distinctions separately: TCP handshake vs HTTP delivery; DNS answer vs endpoint reachability; Pod Ready vs business readiness; GPU visible vs GPU healthy; primary healthy vs committed data preserved; one Run record vs one external side effect.
- Include at least one plausible distractor that explains only part of the symptoms.
- Keep metrics internally consistent. Correlation is not causation.
- Add constraints that force explicit trade-offs: blast radius, capacity, data integrity, tenant isolation, rollback, or time to mitigate.

## Scenario checklist

- [ ] One primary scenario and a few plausible alternatives.
- [ ] Baseline, incident window, and at least three observations from distinct layers.
- [ ] A constraint that makes naive mitigation unsafe.
- [ ] Three or four progressive questions.
- [ ] No answer, solution order, hint, or unique-root-cause giveaway.
- [ ] Distinct from recent practice.
- [ ] Answerable in 5–10 minutes.
