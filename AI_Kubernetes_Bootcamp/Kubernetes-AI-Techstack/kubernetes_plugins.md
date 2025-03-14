# Kubernetes Plugins 

### CNI Plugin 

CNI is a software add-on that implements container network specifications. 
They adhere to the K8s networking tenets and are responsible for allocating IP addresses to K8s Pods and enabling them to communicate with each other within the cluster. 

Examples: 
1. Cilium 
2. Calico 
3. Amazon VPC CNI

### CSI Plugin 

 CSI is a software add-on that implements container storage interface specifications. They are responsible for providing persistent storage volumes to K8s Pods and managing the lifecycle of those volumes.

 Examples: 
 1. Amazon EBS CSI driver
 2. Portworx CSI Driver 


 ### CoreDNS

 CoreDNS is an essential software add-on that provides DNS resolution within the cluster. Containers launched in K8s worker nodes automatically include this DNS server in their DNS searches.

 ### Device plugins

 