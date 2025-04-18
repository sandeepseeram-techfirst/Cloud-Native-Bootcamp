# Kubernetes Network Security

In Kubernetes, networks serve two main purposes:

## Internal networks: 
Networks handle internal traffic that facilitates communications between pods, Kubernetes nodes, and other resources within a cluster. Typically, internal networks use private subnets and IP addresses, and are isolated from the public Internet.

## External networks: 
Workloads that need to connect to the Internet use public IP addresses.