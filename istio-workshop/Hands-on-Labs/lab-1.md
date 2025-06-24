# Istio 
Istio provides a huge step forward in simplifying and improving service-to-service communication in microservices architectures. Istio helps enterprises construct durable and scalable distributed systems by solving difficulties such as traffic management, security, observability, and resilience.

## What is a Service Mesh? 
A service mesh can be defined as a dedicated infrastructure layer designed to handle service-to-service communication within a distributed application.


## High-level Istio architecture
Two planes:

#### Control plane: 
Istiod — issues certs, distributes configuration, service discovery, policies, telemetry hooks.
Data plane: Envoy (sidecar or shared proxies in ambient mode) — intercepts traffic, enforces policies, collects telemetry.