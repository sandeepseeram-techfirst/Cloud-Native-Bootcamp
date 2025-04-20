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

## CNI Plugins 

Kubernetes uses a Container Network Interface (CNI) plugin to create a virtual network interface that containers can use. CNI plugins can be used to integrate Kubernetes with a variety of third-party network configuration management platforms, such as those that run natively on public clouds (like Azure Virtual Networks and AWS Network Interfaces).

CNI plugins are also available to support platforms like Project Calico and Weave Net, which are designed to provide a way to standardize networking configurations across heterogeneous or hybrid environments (i.e., environments that combine multiple types of platforms, such as Kubernetes and a public cloud or a private data center).

## Service Meshes 
Service meshes automate the discovery of different resources on a network. Most service meshes also provide network observability and security functionality.

Kubernetes itself does not provide a native service mesh, but it can integrate with most mainstream service meshes, such as Istio, Traefik, and NGINX.


## Network Policy 

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-backend-egress
  namespace: default
  spec:
    podSelector:
    matchLabels:
      tier: backend
      policyTypes:
      - Egress
      egress:
      - to:
         - podSelector:
        matchLabels:
        tier: backend