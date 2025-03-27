# Cloud Native Storage 

Cloud-Native Storage (CNS) refers to storage solutions that are designed specifically for cloud-native applications, which typically run in containerized environments like Kubernetes. 

CNS is dynamic, scalable, API-driven, and integrates tightly with container orchestrators.

## 🛠️ How Cloud-Native Storage Works

Traditional storage is static and manually managed. CNS, on the other hand:

- Is **dynamically provisioned** via APIs or Kubernetes manifests
- Is **mounted per pod/container** using **Persistent Volumes (PVs)**
- Uses **CSI (Container Storage Interface)** to interact with backends
- Is **scalable on demand**, across **zones/regions**
- Offers built-in **replication, backups, snapshots**, and more
