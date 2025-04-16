# Kubernetes Security Contexts

How can you ensure that each resource in Kubernetes has the permissions it requires, while at the same time avoiding over-permissioning? 

In other words, how can you define permissions on a granular basis that adheres to the principle of least privilege?


The answer is Kubernetes security context. 

Security context is a tool that allows admins to define security-related parameters on a resource-by-resource basis. 
As such, it makes it possible to assign each resource the specific permissions that it needs to access resources on the host server while denying access to those that it doesn’t specifically require.

## What Is Kubernetes Security Context?
In Kubernetes, a security context defines privileges for individual pods or containers. 
You can use security context to grant containers or pods permissions such as the right to access an external file or run in privileged mode.


## Internal vs. External Security Contexts
Kubernetes security context is a bit complicated in the sense that some of the rules that you can define are enforced internally via Kubernetes itself, whereas others integrate with external security context tools – namely, AppArmor and SELinux.

Thus, you can think of Kubernetes security context as a way to define certain permissions for pods and containers, as well as to integrate Kubernetes with external security tools that run on the host rather than in Kubernetes itself.

## RBAC vs Security Contexts

RBAC can be applied to a variety of Kubernetes resources, such as pods, Kubernetes nodes, and even entire clusters. 
Security context assigns permissions only to pods.