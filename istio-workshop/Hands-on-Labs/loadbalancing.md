# Load Balancing

Load balancing in a distributed system guarantees the equitable distribution of workloads to prevent the overburdening of any individual resource. Kubernetes conducts liveness and readiness probes at a regular time interval to monitor pod status, ensuring that traffic is allocated to healthy pods. Unhealthy pods are automatically circumvented until they recuperate. Kubernetes enables load balancing in the following ways:

## Internal Load Balancing
Kubernetes uniformly allocates incoming requests among several pods within a service to guarantee optimal resource utilization.

## External Load Balancing
Kubernetes can deliver services to external clients by interfacing with cloud providers or ingress controllers, thereby efficiently directing traffic.

---