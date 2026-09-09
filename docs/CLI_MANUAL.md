````markdown name=CLI_MANUAL.md
# AI Hacking Tool - Complete CLI Manual

## Table of Contents
1. [Installation & Setup](#installation--setup)
2. [Getting Started](#getting-started)
3. [Core Commands](#core-commands)
4. [Advanced Scanning](#advanced-scanning)
5. [Analysis & Reporting](#analysis--reporting)
6. [Real-World Examples](#real-world-examples)
7. [Troubleshooting](#troubleshooting)

---

## Installation & Setup

### Prerequisites
- Python 3.11 or 3.12
- Virtual Environment (venv)
- pip package manager

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-hacking-tool.git
cd ai-hacking-tool

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Getting Started

### Verify Installation
```bash
(venv) python -m src.cli --help
```

This should show you all available commands.

### View Specific Command Help
```bash
(venv) python -m src.cli [command] --help
```

---

## Core Commands

### 1. Network Scanning

Discover active hosts on a network.

#### Syntax:
```bash
python -m src.cli scan <target> --type <network|host>
```

#### Parameters:
- `<target>`: IP address or CIDR range (e.g., 192.168.1.0/24, 10.0.0.1)
- `--type`: Scan type - `network` (range) or `host` (single IP)

#### Examples:

**Scan entire network:**
```bash
(venv) python -m src.cli scan 192.168.1.0/24 --type network
```

**Scan single host:**
```bash
(venv) python -m src.cli scan 192.168.1.100 --type host
```

**Scan with custom timeout:**
```bash
(venv) python -m src.cli scan 10.0.0.0/25 --type network --timeout 5
```

#### Output:
```
Active Hosts Found:
┌──────────────┬──────────────┬────────────┐
│ IP Address   │ Hostname     │ Mac Address│
├──────────────┼──────────────┼────────────┤
│ 192.168.1.1  │ gateway.local│ AA:BB:CC.. │
│ 192.168.1.50 │ server.local │ DD:EE:FF.. │
└──────────────┴──────────────┴────────────┘
```

---

### 2. Port Scanning

Identify open ports and services on target.

#### Syntax:
```bash
python -m src.cli ports <target> [--ports <port_list>]
```

#### Parameters:
- `<target>`: IP address or domain name
- `--ports`: Specific ports to scan (default: common ports)

#### Examples:

**Scan common ports on domain:**
```bash
(venv) python -m src.cli ports google.com
```

**Scan specific ports:**
```bash
(venv) python -m src.cli ports 192.168.1.100 --ports 22,80,443,3306,5432
```

**Scan all ports (1-65535):**
```bash
(venv) python -m src.cli ports example.com --all-ports
```

#### Output:
```
Port Scan Results for google.com:
┌──────┬────────────┬──────────┐
│ Port │ Service    │ Status   │
├──────┼────────────┼──────────┤
│ 80   │ HTTP       │ OPEN     │
│ 443  │ HTTPS      │ OPEN     │
│ 22   │ SSH        │ CLOSED   │
└──────┴────────────┴──────────┘
```

---

### 3. DNS Enumeration

Retrieve DNS records for domain.

#### Syntax:
```bash
python -m src.cli dns <domain> [--records <record_types>]
```

#### Parameters:
- `<domain>`: Target domain name
- `--records`: DNS record types (A, MX, NS, TXT, CNAME, SOA)

#### Examples:

**Get all DNS records:**
```bash
(venv) python -m src.cli dns google.com
```

**Get specific record types:**
```bash
(venv) python -m src.cli dns example.com --records A,MX,NS
```

**Get mail server records:**
```bash
(venv) python -m src.cli dns company.com --records MX
```

#### Output:
```
DNS Records for google.com:
┌────────┬─────────────────────────────┐
│ Type   │ Value                       │
├────────┼─────────────────────────────┤
│ A      │ 142.250.185.46              │
│ MX     │ aspmx.l.google.com (10)     │
│ NS     │ ns1.google.com              │
│ TXT    │ v=spf1 include:_spf...      │
└────────┴─────────────────────────────┘
```

---

## Advanced Scanning

### 4. SQL Injection Scanner

Detect SQL injection vulnerabilities in web applications.

#### Syntax:
```bash
python -m src.cli sqli <url> [--param <parameters>] [--deep]
```

#### Parameters:
- `<url>`: Target URL with parameters (e.g., https://example.com?id=1)
- `--param`: Specific parameters to test (comma-separated)
- `--deep`: Perform deep scanning with more payloads

#### Examples:

**Basic SQL injection test:**
```bash
(venv) python -m src.cli sqli https://example.com?id=1
```

**Test specific parameters:**
```bash
(venv) python -m src.cli sqli https://example.com?user=admin&id=1 --param id,user
```

**Deep scan:**
```bash
(venv) python -m src.cli sqli https://example.com?id=1 --deep
```

#### Output:
```
SQL Injection Vulnerability Test:
Target: https://example.com?id=1

VULNERABLE - SQL Injection Found!
├─ Parameter: id
├─ Payload: ' OR '1'='1
├─ Severity: HIGH
└─ Description: Application appears vulnerable to SQL injection

Affected Parameters: 1
Total Vulnerabilities: 1
```

---

### 5. XSS Vulnerability Scanner

Identify Cross-Site Scripting (XSS) vulnerabilities.

#### Syntax:
```bash
python -m src.cli xss <url> [--deep] [--payload-file <file>]
```

#### Parameters:
- `<url>`: Target website URL
- `--deep`: Perform comprehensive scanning
- `--payload-file`: Custom XSS payloads file

#### Examples:

**Basic XSS scan:**
```bash
(venv) python -m src.cli xss https://example.com
```

**Deep XSS scanning:**
```bash
(venv) python -m src.cli xss https://example.com --deep
```

**Use custom payloads:**
```bash
(venv) python -m src.cli xss https://example.com --payload-file custom_xss.txt
```

#### Output:
```
XSS Vulnerability Scan Results:
Target: https://example.com

Vulnerabilities Found: 2
┌─────┬──────────────────┬─────────────────────┐
│ ID  │ Type             │ Location            │
├─────┼──────────────────┼─────────────────────┤
│ 1   │ Reflected XSS    │ /search?q=<payload> │
│ 2   │ DOM-based XSS    │ JavaScript functions│
└─────┴──────────────────┴─────────────────────┘
```

---

### 6. SSL/TLS Certificate Analysis

Analyze SSL/TLS certificates for security issues.

#### Syntax:
```bash
python -m src.cli ssl <domain> [--detailed] [--chain]
```

#### Parameters:
- `<domain>`: Target domain or domain:port
- `--detailed`: Show detailed certificate information
- `--chain`: Show certificate chain

#### Examples:

**Basic SSL check:**
```bash
(venv) python -m src.cli ssl google.com
```

**Detailed analysis:**
```bash
(venv) python -m src.cli ssl google.com --detailed
```

**Check specific port:**
```bash
(venv) python -m src.cli ssl example.com:8443 --detailed
```

**Show certificate chain:**
```bash
(venv) python -m src.cli ssl google.com --chain
```

#### Output:
```
SSL/TLS Certificate Analysis:
Domain: google.com
Port: 443

Certificate Information:
├─ Issuer: Google Internet Authority G3
├─ Subject: *.google.com
├─ Valid From: 2023-01-10
├─ Valid Until: 2024-04-02
├─ Days to Expiry: 234
├─ Status: ✓ Valid
└─ Signature Algorithm: sha256WithRSAEncryption

Security Issues Found: 0
Protocol Support: TLS 1.2, TLS 1.3
Cipher Suites: Strong encryption detected
```

---

### 7. Subdomain Enumeration

Discover all subdomains for a target domain.

#### Syntax:
```bash
python -m src.cli subdomains <domain> [--wordlist <file>] [--deep]
```

#### Parameters:
- `<domain>`: Target domain
- `--wordlist`: Custom wordlist file for subdomain brute-forcing
- `--deep`: Use larger wordlist and more sources

#### Examples:

**Basic subdomain enumeration:**
```bash
(venv) python -m src.cli subdomains google.com
```

**Use custom wordlist:**
```bash
(venv) python -m src.cli subdomains example.com --wordlist custom_subdomains.txt
```

**Deep enumeration:**
```bash
(venv) python -m src.cli subdomains google.com --deep
```

#### Output:
```
Subdomain Enumeration Results for google.com:
Subdomains Found: 47

Active Subdomains:
├─ www.google.com (142.250.185.46)
├─ mail.google.com (142.250.185.46)
├─ drive.google.com (142.250.185.46)
├─ maps.google.com (142.250.185.46)
├─ photos.google.com (142.250.185.46)
└─ ... (42 more)
```

---

### 8. Credential Breach Checker

Check if email/username appears in data breaches.

#### Syntax:
```bash
python -m src.cli breach <email_or_username> [--type <email|username>]
```

#### Parameters:
- `<email_or_username>`: Email address or username to check
- `--type`: Specify type (email or username)

#### Examples:

**Check email address:**
```bash
(venv) python -m src.cli breach admin@example.com
```

**Check username:**
```bash
(venv) python -m src.cli breach johndoe --type username
```

#### Output:
```
Credential Breach Check for: admin@example.com

Status: FOUND IN 3 BREACHES

Breaches:
┌──────────────────┬─────────────┬─────────────┐
│ Breach Name      │ Date        │ Records     │
├──────────────────┼─────────────┼─────────────┤
│ LinkedIn Breach  │ 2021-06-22  │ 700M users  │
│ Facebook Breach  │ 2019-09-03  │ 540M users  │
│ Yahoo Breach     │ 2014-12-14  │ 3B users    │
└──────────────────┴─────────────┴─────────────┘

Recommendation: Change password immediately!
```

---

### 9. WAF Detection

Detect Web Application Firewall (WAF) presence.

#### Syntax:
```bash
python -m src.cli waf <url> [--aggressive] [--fingerprint]
```

#### Parameters:
- `<url>`: Target website URL
- `--aggressive`: Use aggressive detection methods
- `--fingerprint`: Attempt to identify specific WAF

#### Examples:

**Basic WAF detection:**
```bash
(venv) python -m src.cli waf google.com
```

**Aggressive detection:**
```bash
(venv) python -m src.cli waf example.com --aggressive
```

**Identify WAF type:**
```bash
(venv) python -m src.cli waf example.com --fingerprint
```

#### Output:
```
WAF Detection Analysis:
Target: example.com

WAF DETECTED: YES

Detected WAF: Cloudflare
├─ Confidence: 98%
├─ Indicators:
│  ├─ Server: cloudflare
│  ├─ CF-Ray header present
│  └─ Cookie: __cfruid detected

Bypass Methods:
├─ Try rotating User-Agent
├─ Use proxy chain
└─ Wait between requests
```

---

### 10. Exploit Database Searcher

Search for known exploits for software/vulnerabilities.

#### Syntax:
```bash
python -m src.cli exploit <software> [--version <version>] [--cve <cve_id>]
```

#### Parameters:
- `<software>`: Software name
- `--version`: Specific version to search
- `--cve`: Search by CVE ID

#### Examples:

**Search for Apache exploits:**
```bash
(venv) python -m src.cli exploit Apache
```

**Search for specific version:**
```bash
(venv) python -m src.cli exploit Apache 2.4.1
```

**Search by CVE:**
```bash
(venv) python -m src.cli exploit --cve CVE-2021-44228
```

#### Output:
```
Exploit Database Search Results:

Software: Apache
Version: 2.4.1
Results: 12 exploits found

┌────────┬──────────────────────────────┬────────────┐
│ CVE ID │ Title                        │ Severity   │
├────────┼──────────────────────────────┼────────────┤
│ CVE... │ Remote Code Execution        │ CRITICAL   │
│ CVE... │ Information Disclosure       │ HIGH       │
│ CVE... │ Denial of Service            │ HIGH       │
└────────┴──────────────────────────────┴────────────┘

Download: https://www.exploit-db.com/exploits/...
```

---

### 11. Malware URL Checker

Check if URL is known to host malware.

#### Syntax:
```bash
python -m src.cli malware <url> [--batch <file>] [--verbose]
```

#### Parameters:
- `<url>`: URL to check or file with URLs
- `--batch`: Check multiple URLs from file
- `--verbose`: Show detailed results

#### Examples:

**Check single URL:**
```bash
(venv) python -m src.cli malware https://suspicious-site.com
```

**Check batch of URLs:**
```bash
(venv) python -m src.cli malware urls.txt --batch
```

**Verbose output:**
```bash
(venv) python -m src.cli malware https://example.com --verbose
```

#### Output:
```
Malware URL Check:
URL: https://suspicious-site.com

Status: ⚠️ MALICIOUS

Detection Details:
├─ Detected by: 15 security vendors
├─ Categories: Trojan, Phishing, Malware
├─ Last Detection: 2024-01-15
└─ Threat Level: CRITICAL

Detections:
├─ Kaspersky: Trojan.Win32.Generic
├─ McAfee: Heur/Suspicious.PE
└─ Avast: Win32:Malware-gen
```

---

## Analysis & Reporting

### 12. Report Generation

Generate comprehensive security reports.

#### Syntax:
```bash
python -m src.cli report <results_file> --format <json|html|pdf|txt> [--output <path>]
```

#### Parameters:
- `<results_file>`: JSON file with scan results
- `--format`: Output format (json, html, pdf, txt)
- `--output`: Output file path

#### Examples:

**Generate JSON report:**
```bash
(venv) python -m src.cli report scan_results.json --format json
```

**Generate HTML report:**
```bash
(venv) python -m src.cli report scan_results.json --format html --output report.html
```

**Generate PDF report:**
```bash
(venv) python -m src.cli report scan_results.json --format pdf --output report.pdf
```

**Generate text report:**
```bash
(venv) python -m src.cli report scan_results.json --format txt
```

#### Output Formats:

**JSON**: Machine-readable structured data
```json
{
  "scan_date": "2024-01-15",
  "target": "example.com",
  "vulnerabilities": [
    {"type": "SQL Injection", "severity": "HIGH"},
    {"type": "XSS", "severity": "MEDIUM"}
  ]
}
```

**HTML**: Professional visual report (browser-compatible)

**PDF**: Printable formatted report

**TXT**: Simple text-based report

---

### 13. Threat Detection

Analyze network traffic for threats.

#### Syntax:
```bash
python -m src.cli threats <pcap_file> [--filter <filter>] [--ai-analyze]
```

#### Parameters:
- `<pcap_file>`: Network capture file (PCAP format)
- `--filter`: Filter traffic (protocol, IP, port)
- `--ai-analyze`: Use AI for threat detection

#### Examples:

**Analyze PCAP file:**
```bash
(venv) python -m src.cli threats capture.pcap
```

**Filter by protocol:**
```bash
(venv) python -m src.cli threats capture.pcap --filter tcp.port==443
```

**AI-powered analysis:**
```bash
(venv) python -m src.cli threats capture.pcap --ai-analyze
```

---

## Real-World Examples

### Example 1: Complete Website Security Audit

```bash
# 1. Check DNS records
(venv) python -m src.cli dns example.com

# 2. Scan all ports
(venv) python -m src.cli ports example.com --all-ports

# 3. Check SSL certificate
(venv) python -m src.cli ssl example.com --detailed

# 4. Detect WAF
(venv) python -m src.cli waf https://example.com

# 5. Test for SQL injection
(venv) python -m src.cli sqli https://example.com?id=1 --deep

# 6. Test for XSS
(venv) python -m src.cli xss https://example.com --deep

# 7. Check for known exploits
(venv) python -m src.cli exploit Apache

# 8. Generate report
(venv) python -m src.cli report results.json --format html --output audit_report.html
```

### Example 2: Reconnaissance on Target Domain

```bash
# 1. Enumerate subdomains
(venv) python -m src.cli subdomains example.com --deep

# 2. Get DNS records
(venv) python -m src.cli dns example.com --records A,MX,NS

# 3. Scan discovered subdomains for open ports
(venv) python -m src.cli ports api.example.com
(venv) python -m src.cli ports mail.example.com

# 4. Check SSL for all subdomains
(venv) python -m src.cli ssl api.example.com --detailed
```

### Example 3: Check for Exposed Credentials

```bash
# Check if admin email is in breaches
(venv) python -m src.cli breach admin@example.com

# Check if staff emails are compromised
(venv) python -m src.cli breach john.doe@example.com
(venv) python -m src.cli breach jane.smith@example.com

# Generate report of compromised accounts
(venv) python -m src.cli report breach_results.json --format html
```

### Example 4: Search for Exploits Before Patching

```bash
# Check for exploits for Apache version
(venv) python -m src.cli exploit Apache 2.4.49

# Check for known vulnerabilities
(venv) python -m src.cli exploit --cve CVE-2021-41773

# Search for PHP exploits
(venv) python -m src.cli exploit PHP 7.4.0
```

---

## Troubleshooting

### Common Issues & Solutions

#### Issue 1: "Module not found" error
```bash
# Solution: Ensure PYTHONPATH is set
(venv) set PYTHONPATH=%PYTHONPATH%;.
(venv) python -m src.cli --help
```

#### Issue 2: SSL certificate verification error
```bash
# Solution: Use --insecure flag (not recommended for production)
(venv) python -m src.cli ssl example.com --insecure
```

#### Issue 3: Network scan timing out
```bash
# Solution: Reduce timeout or scan smaller range
(venv) python -m src.cli scan 192.168.1.0/25 --type network --timeout 3
```

#### Issue 4: Permission denied on Windows
```bash
# Solution: Run command prompt as Administrator
# Right-click Command Prompt → Run as Administrator
```

#### Issue 5: Port scan shows all closed
```bash
# Solution: Check if target is accessible
ping example.com
# Try specific ports
(venv) python -m src.cli ports example.com --ports 80,443
```

### Getting Help

```bash
# View all commands
(venv) python -m src.cli --help

# Get help for specific command
(venv) python -m src.cli scan --help
(venv) python -m src.cli ports --help
(venv) python -m src.cli sqli --help

# View command examples
(venv) python -m src.cli [command] --examples
```

---

## Important Legal Notice

⚠️ **DISCLAIMER**: This tool is intended for **authorized security testing only**. 

- Always obtain **written permission** before testing any systems
- Unauthorized access to computer systems is **illegal**
- Misuse of this tool may result in **criminal charges**
- Use only in controlled environments with proper authorization
- The authors are **not responsible** for misuse

---

## Version & Support

- **Version**: 1.0.0
- **Last Updated**: January 2024
- **Python Compatibility**: 3.11+
- **Repository**: https://github.com/kikokulit329-lgtm/ai-hacking-tool
- **Issues**: Report bugs and request features on GitHub

---

## Quick Command Cheat Sheet

```bash
# Reconnaissance
python -m src.cli dns example.com
python -m src.cli subdomains example.com --deep
python -m src.cli ports example.com

# Vulnerability Testing
python -m src.cli sqli https://example.com?id=1
python -m src.cli xss https://example.com
python -m src.cli ssl example.com

# Threat Intelligence
python -m src.cli breach email@example.com
python -m src.cli waf example.com
python -m src.cli exploit Apache 2.4.1
python -m src.cli malware https://suspicious.com

# Reporting
python -m src.cli report results.json --format html
```

---

End of CLI Manual
````
