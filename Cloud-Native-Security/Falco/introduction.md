# Falco

Falco is a cloud native security tool that provides runtime security across hosts, containers, Kubernetes, and cloud environments.

It leverages custom rules on Linux kernel events and other data sources through plugins, enriching event data with contextual metadata to deliver real-time alerts. 

Falco enables the detection of abnormal behavior, potential security threats, and compliance violations.

## Use Cases

### Threat Detection
Detect malicious behavior in hosts and containers, no matter what scale, using the power of eBPF.

### Regulatory Compliance
Stay compliant in cloud-native systems with Falco's intelligent monitoring and rule-based detection.


## How does Falco works? 
Falco uses syscalls to monitor a system's activity, by:

1. Parsing the Linux syscalls from the kernel at runtime
2. Asserting the stream against a powerful rules engine
3. Alerting when a rule is violated