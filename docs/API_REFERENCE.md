# API Reference

## Table of Contents

1. [Reconnaissance Module](#reconnaissance-module)
2. [Vulnerability Module](#vulnerability-module)
3. [AI Engine Module](#ai-engine-module)
4. [Reporting Module](#reporting-module)

## Reconnaissance Module

### NetworkScanner

```python
from src.reconnaissance import NetworkScanner

scanner = NetworkScanner(timeout=2)
```

#### Methods

##### `scan_network(network: str) -> List[Dict]`

Scans a network range for active hosts.

**Parameters:**
- `network` (str): Network range in CIDR notation (e.g., '192.168.1.0/24')

**Returns:** List of active hosts with details

**Example:**
```python
results = scanner.scan_network("192.168.1.0/24")
for host in results:
    print(f"IP: {host['ip']}, Hostname: {host['hostname']}")
```

##### `ping_host(host: str) -> bool`

Pings a single host to check if it's alive.

**Parameters:**
- `host` (str): Target IP or hostname

**Returns:** True if host is reachable

##### `resolve_host(hostname: str) -> str`

Resolves hostname to IP address.

**Parameters:**
- `hostname` (str): Target hostname

**Returns:** IP address string

##### `get_reverse_dns(ip: str) -> str`

Performs reverse DNS lookup.

**Parameters:**
- `ip` (str): Target IP address

**Returns:** Hostname string

### DNSEnumerator

```python
from src.reconnaissance import DNSEnumerator

dns = DNSEnumerator()
```

#### Methods

##### `enumerate_dns_records(domain: str) -> Dict`

Enumerates all DNS record types for a domain.

**Parameters:**
- `domain` (str): Target domain

**Returns:** Dictionary of DNS records by type

##### `get_mx_records(domain: str) -> List[str]`

Gets MX records for email servers.

**Parameters:**
- `domain` (str): Target domain

**Returns:** List of MX records

##### `get_nameservers(domain: str) -> List[str]`

Gets authoritative nameservers.

**Parameters:**
- `domain` (str): Target domain

**Returns:** List of nameserver hostnames

##### `get_txt_records(domain: str) -> List[str]`

Gets TXT records (SPF, DKIM, DMARC).

**Parameters:**
- `domain` (str): Target domain

**Returns:** List of TXT record values

### SubdomainFinder

```python
from src.reconnaissance import SubdomainFinder

finder = SubdomainFinder(wordlist=None)
```

#### Methods

##### `find_subdomains(domain: str, threads: int = 10) -> Set[str]`

Finds subdomains using wordlist enumeration.

**Parameters:**
- `domain` (str): Target domain
- `threads` (int): Number of threads (default: 10)

**Returns:** Set of discovered subdomains

## Vulnerability Module

### PortScanner

```python
from src.vulnerability import PortScanner

ps = PortScanner(timeout=1)
```

#### Methods

##### `scan_target(host: str, ports: List[int] = None, threads: int = 50) -> List[Dict]`

Scans target host for open ports.

**Parameters:**
- `host` (str): Target IP or hostname
- `ports` (List[int]): Specific ports to scan (default: common ports)
- `threads` (int): Number of threads (default: 50)

**Returns:** List of open ports with service information

**Example:**
```python
open_ports = ps.scan_target("example.com", ports=[22, 80, 443])
for port_info in open_ports:
    print(f"Port {port_info['port']}: {port_info['service']}")
```

##### `get_service_version(host: str, port: int) -> str`

Attempts to grab service banner.

**Parameters:**
- `host` (str): Target host
- `port` (int): Target port

**Returns:** Service banner string or None

### WebScanner

```python
from src.vulnerability import WebScanner

web_scanner = WebScanner(timeout=5)
```

#### Methods

##### `scan_target(url: str) -> List[Dict]`

Scans web application for vulnerabilities.

**Parameters:**
- `url` (str): Target URL

**Returns:** List of vulnerabilities found

**Example:**
```python
vulns = web_scanner.scan_target("https://example.com")
for vuln in vulns:
    print(f"{vuln['type']}: {vuln['severity']}")
```

### CVEChecker

```python
from src.vulnerability import CVEChecker

cve_checker = CVEChecker()
```

#### Methods

##### `check_cves(software: str, version: str) -> List[Dict]`

Checks if software version has known CVEs.

**Parameters:**
- `software` (str): Software name
- `version` (str): Software version

**Returns:** List of CVEs found

**Example:**
```python
cves = cve_checker.check_cves("Apache", "2.4.39")
for cve in cves:
    print(f"{cve['cve']}: {cve['severity']}")
```

##### `get_cve_details(cve_id: str) -> Dict`

Gets detailed information about a CVE.

**Parameters:**
- `cve_id` (str): CVE identifier (e.g., 'CVE-2021-44228')

**Returns:** CVE details dictionary

## AI Engine Module

### ThreatDetector

```python
from src.ai_engine import ThreatDetector

detector = ThreatDetector()
```

#### Methods

##### `analyze_traffic(data: List[Dict]) -> List[Dict]`

Analyzes network traffic for threats.

**Parameters:**
- `data` (List[Dict]): Network traffic data

**Returns:** List of detected threats

**Example:**
```python
traffic = [
    {'payload': 'GET / HTTP/1.1', 'flags': 'SYN'},
    {'payload': 'shell /bin/bash', 'flags': 'PSH'},
]
threats = detector.analyze_traffic(traffic)
for threat in threats:
    print(f"Level: {threat['threat_level']}, Score: {threat['threat_score']}")
```

##### `train_model(training_data: List[Dict])`

Trains the threat detection model.

**Parameters:**
- `training_data` (List[Dict]): Training dataset

### AnomalyDetector

```python
from src.ai_engine import AnomalyDetector

anomalies = AnomalyDetector()
```

#### Methods

##### `establish_baseline(normal_data: List[Dict])`

Establishes baseline of normal behavior.

**Parameters:**
- `normal_data` (List[Dict]): List of normal traffic samples

##### `detect_anomalies(traffic_data: List[Dict]) -> List[Dict]`

Detects anomalies in traffic data.

**Parameters:**
- `traffic_data` (List[Dict]): Network traffic data

**Returns:** List of detected anomalies

**Example:**
```python
normal = [{'size': 100, 'rate': 10}]
anomalies.establish_baseline(normal)

suspicious = [{'size': 5000, 'rate': 100}]
detections = anomalies.detect_anomalies(suspicious)
for detection in detections:
    print(f"Severity: {detection['severity']}, Score: {detection['anomaly_score']}")
```

## Reporting Module

### ReportGenerator

```python
from src.reporting import ReportGenerator

reporter = ReportGenerator()
```

#### Methods

##### `generate_full_report(scan_results: Dict) -> Dict`

Generates comprehensive security report.

**Parameters:**
- `scan_results` (Dict): Results from all scans

**Returns:** Complete report dictionary

**Example:**
```python
results = {
    'target': '192.168.1.100',
    'vulnerabilities': [
        {'type': 'Open Port', 'severity': 'High'},
    ]
}
report = reporter.generate_full_report(results)
print(f"Total Vulnerabilities: {report['summary']['total_vulnerabilities']}")
```

##### `export_json(filepath: str)`

Exports report as JSON file.

**Parameters:**
- `filepath` (str): Output file path

##### `export_text(filepath: str)`

Exports report as plain text file.

**Parameters:**
- `filepath` (str): Output file path

## Data Structures

### Host Info
```python
{
    'ip': '192.168.1.100',
    'hostname': 'target.local',
    'status': 'online',
    'timestamp': '2026-09-09T12:00:00'
}
```

### Port Info
```python
{
    'port': 22,
    'status': 'open',
    'service': 'SSH',
    'host': '192.168.1.100',
    'timestamp': '2026-09-09T12:00:00'
}
```

### Vulnerability
```python
{
    'type': 'Missing Security Header',
    'severity': 'Medium',
    'url': 'https://example.com',
    'timestamp': '2026-09-09T12:00:00'
}
```

### Threat Detection
```python
{
    'packet': {...},
    'threat_score': 0.85,
    'threat_level': 'HIGH',
    'timestamp': '2026-09-09T12:00:00'
}
```

## Error Handling

All modules raise standard Python exceptions:

```python
try:
    results = scanner.scan_network("invalid_network")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Error occurred: {e}")
```

## Configuration

Modify behavior via `config/settings.yaml`:

```yaml
reconnaissance:
  network_scan_timeout: 2
  dns_timeout: 5
  max_threads: 20

vulnerability:
  port_scan_timeout: 1
  web_scan_timeout: 5

ai_engine:
  threat_detection_threshold: 0.7
  anomaly_sensitivity: 2.0
```

---
**Last Updated**: 2026-09-09
**Version**: 1.0.0
