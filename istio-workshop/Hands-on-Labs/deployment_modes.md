## Istio deployment modes (1.27+)

#### Sidecar mode: 
injects an Envoy sidecar per pod. Fine-grained control, full feature set (pod-level telemetry, per-pod mTLS, advanced L7 features). Higher resource and operational overhead.

#### Ambient mode: 
node-level shared proxies (ztunnel/waypoint). Lower resource usage, easier onboarding, still supports mTLS and basic L7 for services marked for waypoint. May lack some per-pod granularity.