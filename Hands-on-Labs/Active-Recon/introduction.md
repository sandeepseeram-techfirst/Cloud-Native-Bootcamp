# Active Recon: Enumeration and Fuzzing

## What is Active Reconnaissance?

**Active Reconnaissance** is a phase in ethical hacking or penetration testing where the tester directly interacts with the target system or network to gather detailed information. Unlike **passive recon**, which avoids direct contact, **active recon** involves scanning, probing, and interacting with systems—often triggering logs or alerts.

---

## Enumeration

### Definition:
**Enumeration** is the process of extracting detailed information from a target system, such as:

- Usernames
- Group names
- Shares
- Services
- Network resources
- System banners
- Operating system details

### Techniques:
- **NetBIOS Enumeration**
- **SNMP Enumeration**
- **SMTP Enumeration**
- **DNS Zone Transfers**
- **LDAP Enumeration**
- **NFS/SMB Shares Listing**

### Tools:
- `nmap` (with service/version detection)
- `enum4linux`
- `rpcclient`
- `snmpwalk`
- `dig` and `nslookup`
- `LDAPsearch`

### Example:
```bash
enum4linux -a 192.168.1.100
