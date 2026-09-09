"""
Example 6: Comprehensive Security Assessment and Report Generation

This script demonstrates a complete security assessment workflow.
"""

from src.reconnaissance import NetworkScanner
from src.vulnerability import PortScanner, WebScanner, CVEChecker
from src.reporting import ReportGenerator
import json
from datetime import datetime

def main():
    print("[*] Starting Comprehensive Security Assessment")
    print("=" * 60)
    
    target = "192.168.1.100"
    vulnerabilities = []
    
    # Phase 1: Reconnaissance
    print(f"\n[PHASE 1] Reconnaissance")
    print("-" * 60)
    scanner = NetworkScanner()
    
    if scanner.ping_host(target):
        print(f"[+] Target {target} is online")
    
    # Phase 2: Port Scanning
    print(f"\n[PHASE 2] Port Scanning")
    print("-" * 60)
    ps = PortScanner()
    open_ports = ps.scan_target(target)
    print(f"[+] Found {len(open_ports)} open ports")
    
    for port_info in open_ports:
        vulnerabilities.append({
            'type': 'Open Port',
            'port': port_info['port'],
            'service': port_info['service'],
            'severity': 'High' if port_info['port'] < 1024 else 'Medium',
            'asset': f"{target}:{port_info['port']}"
        })
    
    # Phase 3: CVE Checking
    print(f"\n[PHASE 3] CVE Analysis")
    print("-" * 60)
    cve_checker = CVEChecker()
    
    software_versions = [
        ('Apache', '2.4.39'),
        ('OpenSSL', '1.0.2k'),
    ]
    
    for software, version in software_versions:
        cves = cve_checker.check_cves(software, version)
        if cves:
            print(f"[+] Found CVEs for {software} {version}:")
            for cve in cves:
                vulnerabilities.append({
                    'type': 'Known CVE',
                    'cve': cve['cve'],
                    'software': software,
                    'severity': cve['severity'],
                    'asset': software
                })
                print(f"    - {cve['cve']} ({cve['severity']})")
    
    # Phase 4: Report Generation
    print(f"\n[PHASE 4] Report Generation")
    print("-" * 60)
    
    scan_results = {
        'target': target,
        'scan_date': datetime.now().isoformat(),
        'vulnerabilities': vulnerabilities
    }
    
    reporter = ReportGenerator()
    report = reporter.generate_full_report(scan_results)
    
    print(f"[+] Report Generated:")
    print(f"    Title: {report['title']}")
    print(f"    Total Vulnerabilities: {report['summary']['total_vulnerabilities']}")
    print(f"    Critical: {report['summary']['critical_count']}")
    print(f"    High: {report['summary']['high_count']}")
    print(f"    Overall Risk: {report['summary']['overall_risk']}")
    
    # Export reports
    reporter.export_json("reports/assessment_report.json")
    reporter.export_text("reports/assessment_report.txt")
    
    print(f"\n[+] Reports exported:")
    print(f"    - reports/assessment_report.json")
    print(f"    - reports/assessment_report.txt")
    
    print(f"\n[*] Assessment Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
