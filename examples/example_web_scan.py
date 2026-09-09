"""
Example 3: Web Application Vulnerability Scanning

This script scans a web application for common vulnerabilities.
"""

from src.vulnerability import WebScanner
import json

def main():
    print("[*] Starting Web Vulnerability Scan Example")
    print("=" * 50)
    
    # Initialize web scanner
    scanner = WebScanner(timeout=5)
    
    # Define target
    target_url = "https://example.com"
    print(f"[*] Scanning: {target_url}\n")
    
    # Perform scan
    vulnerabilities = scanner.scan_target(target_url)
    
    print(f"[+] Found {len(vulnerabilities)} vulnerabilities\n")
    
    # Group by severity
    by_severity = {}
    for vuln in vulnerabilities:
        severity = vuln.get('severity', 'Unknown')
        if severity not in by_severity:
            by_severity[severity] = []
        by_severity[severity].append(vuln)
    
    # Display by severity
    for severity in ['Critical', 'High', 'Medium', 'Low']:
        if severity in by_severity:
            print(f"\n[{severity.upper()}] - {len(by_severity[severity])} found:")
            for vuln in by_severity[severity]:
                print(f"  - {vuln.get('type', 'Unknown')}")
                if 'url' in vuln:
                    print(f"    URL: {vuln['url']}")
    
    # Save results
    output_file = "web_scan_results.json"
    with open(output_file, 'w') as f:
        json.dump(vulnerabilities, f, indent=2)
    print(f"\n[+] Results saved to {output_file}")

if __name__ == "__main__":
    main()
