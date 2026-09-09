"""
Example 1: Quick Network Scan

This script performs a quick network scan to discover active hosts.
"""

from src.reconnaissance import NetworkScanner
import json
from datetime import datetime

def main():
    print("[*] Starting Quick Network Scan Example")
    print("=" * 50)
    
    # Initialize scanner
    scanner = NetworkScanner(timeout=2)
    
    # Define target network
    target_network = "192.168.1.0/24"
    print(f"[*] Scanning network: {target_network}")
    
    # Perform scan
    results = scanner.scan_network(target_network)
    
    # Display results
    print(f"\n[+] Found {len(results)} active hosts\n")
    
    for host in results:
        print(f"  IP: {host['ip']}")
        print(f"  Hostname: {host['hostname']}")
        print(f"  Status: {host['status']}")
        print(f"  Time: {host['timestamp']}")
        print()
    
    # Save results
    output_file = "scan_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"[+] Results saved to {output_file}")

if __name__ == "__main__":
    main()
