# Secure Kubernetes Architecture

Kubernetes environments come in many shapes, forms, and sizes. 
Some are inherently more secure than others.

A multi-cluster environment may be more secure in some respects than one that runs everything in a single cluster (although multiple clusters also increase complexity, which is a con from a security standpoint).

 ## Workload Isolation 
 Isolation provided by namespaces is limited. 
 Any permissions that you assign via ClusterRoles will be applied to all namespaces. 


## Service Meshes
Service meshes, which manage service discovery and connectivity for resources running inside a Kubernetes cluster, are a critical tool for any Kubernetes environment that includes more than just a handful of services.