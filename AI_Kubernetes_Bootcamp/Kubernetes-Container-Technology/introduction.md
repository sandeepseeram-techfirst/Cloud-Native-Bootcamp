# Container Technology 

Container technology is made possible because of namespaces and cgroups (control groups) in the Linux kernel.
They form the foundational building blocks to provide isolation and resource limits.

#### Linux Namespace
is an abstraction over resources in the operating system. 
It partitions OS-level resources such that different sets of processes see a different set of resources (network, file system, etc.,) even though they are running on the same OS kernel.

#### Cgroups
govern the isolation and usage of system resources, such as CPU, memory, and network, for a group of processes and optionally enforce limits and constraints.

These capabilities let containers abstract the operating system components for modern applications.


# Container Terminology

