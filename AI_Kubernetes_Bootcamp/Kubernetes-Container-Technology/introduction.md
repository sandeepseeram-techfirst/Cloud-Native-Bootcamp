# Container Technology 

Container technology is made possible because of namespaces and cgroups (control groups) in the Linux kernel.
They form the foundational building blocks to provide isolation and resource limits.

#### Linux Namespace
is an abstraction over resources in the operating system. 
It partitions OS-level resources such that different sets of processes see a different set of resources (network, file system, etc.,) even though they are running on the same OS kernel.

