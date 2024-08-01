# Gateway API 

The Gateway API is a Kubernetes API that provides a way to dynamically configure load balancing and service mesh capabilities on Kubernetes. The Gateway API allows defining routes and policies to manage external traffic to Kubernetes services in a centralized, declarative way.

## The main resources in Gateway API are the following:

GatewayClass: Defines a set of gateways with a common configuration and behavior. It is like the concept of StorageClass for persistent volumes.

Gateway: Defines a set of routes for a given hostname. This binds GatewayClass, TLS certificate, and other configurations to a set of routes.

HTTPRoute/TCPRoute: Defines the actual routes to Kubernetes services and their policies, such as timeouts, retries, and so on.