##### The Gateway API consists of three main components:

##### GatewayClass: 

Think of this as a template or a blueprint for setting up Gateways. It defines a group of Gateways that share the same configuration and are managed by a controller that follows the specifications of the class.

##### Gateway: 
This is where the traffic handling happens. A Gateway is like an entry point to your cluster, such as a cloud load balancer, that directs incoming traffic to the appropriate destinations based on your configuration.

##### HTTPRoute: 
This is where you set the rules for how HTTP traffic gets routed. It helps map traffic from the Gateway to your backend services, such as those running in Kubernetes Pods, based on things like URL paths, headers, or hosts.