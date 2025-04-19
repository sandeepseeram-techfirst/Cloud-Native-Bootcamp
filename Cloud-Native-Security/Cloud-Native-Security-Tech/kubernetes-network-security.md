# Kubernetes Network Security

In Kubernetes, networks serve two main purposes:

## Internal networks: 
Networks handle internal traffic that facilitates communications between pods, Kubernetes nodes, and other resources within a cluster. Typically, internal networks use private subnets and IP addresses, and are isolated from the public Internet.

## External networks: 
Workloads that need to connect to the Internet use public IP addresses.


## Kube-Proxy
The service that manages traffic flows within Kubernetes is kube-proxy. 
Kube-proxy runs on each node in a Kubernetes cluster and forwards packets to containers hosted on those nodes based on the containers’ IP addresses and ports.

On the backend, kube-proxy relies on OS-level network services, such as iptables in Linux, to control traffic. 

But because kube-proxy abstracts these services from Kubernetes resources, the underlying network management layer at the node level is not especially important from a Kubernetes network security perspective.

