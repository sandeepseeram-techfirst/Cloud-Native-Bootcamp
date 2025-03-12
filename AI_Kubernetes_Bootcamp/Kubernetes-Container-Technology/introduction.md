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

#### Container runtime: 
This is a host-level process that is responsible for creating, stopping, and starting containers. It interacts with low-level container runtimes such as runc to set up namespaces and cgroups for containers. 

Popular examples include containerd, CRI-O, and so on.

#### Container image 
This is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and configuration files. 

It is created using a Dockerfile, a plain text definition file that includes a set of instructions to install dependencies, applications, and so on. 

1. Self-contained: It encapsulates everything needed to run software applications.
2. Immutable: It is read-only in nature; any changes would require a new image.
3. Layered: Images are built in layers, each layer representing a file system. This is what makes images highly efficient as common layers can be shared across multiple images.
4. Portable: As the image packages the application and all its dependencies, they can be run on any system that supports a container runtime, making them highly portable in nature.

#### Container registry
This is a tool used to manage and distribute container images. 

