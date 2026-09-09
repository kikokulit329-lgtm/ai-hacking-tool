# User Guide

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Usage](#basic-usage)
3. [Reconnaissance](#reconnaissance)
4. [Vulnerability Scanning](#vulnerability-scanning)
5. [AI-Powered Analysis](#ai-powered-analysis)
6. [Report Generation](#report-generation)
7. [Advanced Usage](#advanced-usage)
8. [Best Practices](#best-practices)

## Getting Started

### Command-Line Interface

The tool can be run from the command line:

```bash
python -m src.cli --help
```

### Python API

For programmatic access:

```python
from src.reconnaissance import NetworkScanner

scanner = NetworkScanner()
results = scanner.scan_network("192.168.1.0/24")
print(results)
```

## Basic Usage

### Network Scanning

```bash
# Scan a network range
python -m src.cli scan 192.168.1.0/24 --type network

# Scan a single host
python -m src.cli scan 192.168.1.100 --type host
```

### Port Scanning

```bash
# Scan common ports
python -m src.cli ports 192.168.1.100

# Scan specific ports
python -m src.cli ports 192.168.1.100 --ports 22,80,443,3306
```

## Reconnaissance

### Network Discovery

```python
from src.reconnaissance import NetworkScanner

scanner = NetworkScanner(timeout=2)
active_hosts = scanner.scan_network("192.168.1.0/24")

for host in active_hosts:
    print(f"Found: {host['ip']} - {host['hostname']}")
```

### DNS Enumeration

```python
from src.reconnaissance import DNSEnumerator

dns = DNSEnumerator()
records = dns.enumerate_dns_records("example.com")

print(f"A Records: {records['A']}")
print(f"MX Records: {records['MX']}")
print(f"TXT Records: {records['TXT']}")
```

### Subdomain Discovery

```python
from src.reconnaissance import SubdomainFinder

finder = SubdomainFinder()
subdomains = finder.find_subdomains("example.com", threads=10)

for subdomain in subdomains:
    print(f"Found subdomain: {subdomain}")
```

## Vulnerability Scanning

### Port Scanning with Service Detection

```python
from src.vulnerability import PortScanner

ps = PortScanner(timeout=1)
open_ports = ps.scan_target("example.com")

for port_info in open_ports:
    print(f"Port {port_info['port']}: {port_info['service']} ({port_info['status']})")
    
    # Try to grab banner
    banner = ps.get_service_version("example.com", port_info['port'])
    if banner:
        print(f"  Banner: {banner}")
```

### Web Application Scanning

```python
from src.vulnerability import WebScanner

web_scanner = WebScanner(timeout=5)
vulnerabilities = web_scanner.scan_target("https://example.com")

for vuln in vulnerabilities:
    print(f"Found: {vuln['type']} - Severity: {vuln['severity']}")
    print(f"  URL: {vuln.get('url', 'N/A')}")
```

### CVE Checking

```python
from src.vulnerability import CVEChecker

cve_checker = CVEChecker()
cves = cve_checker.check_cves("Apache", "2.4.39")

for cve in cves:
    print(f"Found: {cve['cve']} - Severity: {cve['severity']}")
    
# Get detailed CVE information
details = cve_checker.get_cve_details("CVE-2021-44228")
print(f"CVSS Score: {details['cvss_score']}")
```

## AI-Powered Analysis

### Threat Detection

```python
from src.ai_engine import ThreatDetector

detector = ThreatDetector()

# Prepare sample traffic data
traffic_data = [
    {'payload': 'GET / HTTP/1.1', 'flags': 'SYN'},
    {'payload': 'shell exec /bin/bash', 'flags': 'PSH'},
]

# Detect threats
threats = detector.analyze_traffic(traffic_data)

for threat in threats:
    print(f"Threat Level: {threat['threat_level']}")
    print(f"Score: {threat['threat_score']}")
```

### Anomaly Detection

```python
from src.ai_engine import AnomalyDetector

anomalies = AnomalyDetector()

# Establish baseline from normal traffic
normal_traffic = [
    {'size': 100, 'rate': 10},
    {'size': 110, 'rate': 12},
]
anomalies.establish_baseline(normal_traffic)

# Detect anomalies
suspicious_traffic = [
    {'size': 5000, 'rate': 100},  # Large packet, high rate
]
detections = anomalies.detect_anomalies(suspicious_traffic)

for detection in detections:
    print(f"Anomaly Severity: {detection['severity']}")
    print(f"Score: {detection['anomaly_score']}")
```

## Report Generation

### Generate Comprehensive Report

```python
from src.reporting import ReportGenerator

# Prepare scan results
scan_results = {
    'target': '192.168.1.100',
    'vulnerabilities': [
        {'type': 'Open Port', 'severity': 'High', 'asset': '192.168.1.100:22'},
        {'type': 'Missing Header', 'severity': 'Medium', 'asset': 'https://192.168.1.100'},
    ]
}

# Generate report
reporter = ReportGenerator()
report = reporter.generate_full_report(scan_results)

print(f"Title: {report['title']}")
print(f"Total Vulnerabilities: {report['summary']['total_vulnerabilities']}")
print(f"Risk Level: {report['summary']['overall_risk']}")
```

### Export Reports

```python
# Export as JSON
reporter.export_json("reports/security_report.json")

# Export as Text
reporter.export_text("reports/security_report.txt")
```

## Advanced Usage

### Complete Security Assessment Workflow

```python
from src.reconnaissance import NetworkScanner, DNSEnumerator, SubdomainFinder
from src.vulnerability import PortScanner, WebScanner
from src.ai_engine import ThreatDetector
from src.reporting import ReportGenerator

# 1. Reconnaissance
print("[*] Starting reconnaissance...")
network_scanner = NetworkScanner()
hosts = network_scanner.scan_network("192.168.1.0/24")
print(f"[+] Found {len(hosts)} hosts")

# 2. Port Scanning
print("[*] Scanning ports...")
port_scanner = PortScanner()
for host in hosts:
    ports = port_scanner.scan_target(host['ip'])
    print(f"[+] {host['ip']}: {len(ports)} open ports")

# 3. Vulnerability Assessment
print("[*] Assessing vulnerabilities...")
web_scanner = WebScanner()
if ports:
    for port_info in ports:
        if port_info['port'] in [80, 443]:
            url = f"http://{host['ip']}:{port_info['port']}"
            vulns = web_scanner.scan_target(url)
            print(f"[+] Found {len(vulns)} web vulnerabilities")

# 4. Generate Report
print("[*] Generating report...")
reporter = ReportGenerator()
report = reporter.generate_full_report({
    'target': '192.168.1.0/24',
    'vulnerabilities': []
})
reporter.export_json("reports/full_assessment.json")
print("[+] Report generated successfully")
```

## Best Practices

### 1. Authorization
- **Always** obtain written permission before testing
- Document all authorized targets
- Keep detailed logs of all activities

### 2. Ethical Considerations
- Use only for defensive security purposes
- Follow responsible disclosure practices
- Report findings to system owners promptly
- Don't abuse discovered vulnerabilities

### 3. Configuration
- Adjust timeouts based on network conditions
- Use appropriate number of threads for your system
- Configure logging level as needed
- Regularly update CVE databases

### 4. Performance
- Use threading for parallel scans
- Set realistic scan timeouts
- Monitor resource usage
- Break large networks into smaller ranges

### 5. Security
- Run on secure networks
- Use VPN for remote testing
- Protect scan results and reports
- Store credentials securely

## Common Scenarios

### Scenario 1: Quick Network Assessment

```bash
python -m src.cli scan 192.168.1.0/24 --type network
python -m src.cli ports 192.168.1.1 --ports 22,80,443
```

### Scenario 2: Web Application Security Test

```python
from src.vulnerability import WebScanner

scanner = WebScanner()
vulns = scanner.scan_target("https://target.com")

for vuln in vulns:
    if vuln['severity'] in ['High', 'Critical']:
        print(f"[!] {vuln['type']}: {vuln['url']}")
```

### Scenario 3: AI-Powered Threat Analysis

```python
from src.ai_engine import ThreatDetector

detector = ThreatDetector()
threats = detector.analyze_traffic(pcap_data)

for threat in sorted(threats, key=lambda x: x['threat_score'], reverse=True):
    print(f"[ALERT] {threat['threat_level']}: {threat['threat_score']}")
```

## Troubleshooting

### Issue: Timeout errors
**Solution**: Increase timeout values in `config/settings.yaml`

### Issue: High false positives
**Solution**: Adjust AI engine sensitivity in config

### Issue: Memory usage high
**Solution**: Reduce number of threads or scan smaller ranges

## Further Reading

- [API Reference](API_REFERENCE.md)
- [Examples Directory](../examples/)
- [GitHub Issues](https://github.com/kikokulit329-lgtm/ai-hacking-tool/issues)

---
**Last Updated**: 2026-09-09
