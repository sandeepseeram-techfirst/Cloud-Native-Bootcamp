# 🛡️ Falco Architecture

Falco is a cloud-native runtime security tool that detects anomalous behavior in containers, Kubernetes, and hosts by monitoring system calls and applying rules.

---

## 📐 High-Level Architecture

```text
           +----------------------+
           |  Syscall Source      |
           | (eBPF/Kmod/Userspace)|
           +----------+-----------+
                      |
                      v
             +------------------+
             |  Event Processor |
             |  (Libscap +      |
             |   Libsinsp)      |
             +--------+---------+
                      |
                      v
             +------------------+
             |   Rules Engine   |
             | (YAML Rules +    |
             |  Conditions)     |
             +--------+---------+
                      |
                      v
             +------------------+
             |   Alert Engine   |
             | (JSON, Syslog,   |
             |  Webhook, etc.)  |
             +--------+---------+
                      |
                      v
             +------------------+
             |  Integrations    |
             | (Falcosidekick,  |
             |  Prometheus, etc.)|
             +------------------+
