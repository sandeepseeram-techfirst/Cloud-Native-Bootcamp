#### AppArmor

AppArmor (Application Armor) is a Linux security module that enforces mandatory access control (MAC) policies to restrict programs' capabilities.

AppArmor works by applying profiles to individual applications, defining the files, network access, capabilities, and resources they can interact with.

It operates on a per-process basis and enforces security rules using the Linux Security Modules (LSM) framework.

##### Profiles:

Profiles can run in:
1. Enforcing mode: Actively enforces the policy.
2. Complain mode: Logs policy violations without enforcing them.

AppArmor profiles are loaded into the kernel via systemd, aa-enforce, or aa-complain.