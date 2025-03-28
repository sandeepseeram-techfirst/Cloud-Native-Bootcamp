# Distributed Databases

## 🗃️ What are Distributed Databases?

A **Distributed Database** is a type of database where **data is stored across multiple physical machines**, but behaves as a **single logical database** to the user.

The machines (or nodes) could be:
- In the same data center (on-prem)
- Spread across multiple data centers
- Running in the cloud or hybrid environments



## ⚙️ How Distributed Databases Work

Distributed databases operate by **splitting and replicating data** across nodes to ensure high availability, fault tolerance, and scalability.

### Key Techniques:

| **Technique**        | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **Sharding (Partitioning)** | Splitting data horizontally across nodes                                 |
| **Replication**      | Duplicating data across nodes for redundancy and fault tolerance               |
| **Consensus Protocols** | Mechanisms (e.g., Raft, Paxos) to maintain consistency between distributed nodes |
| **Quorum-based Writes/Reads** | Ensures strong consistency by requiring majority agreement             |
| **Eventual Consistency** | System guarantees data convergence over time, not immediately               | 



