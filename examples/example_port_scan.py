"""
Example 2: Port Scanning and Service Detection

This script scans a target for open ports and attempts to detect services.
"""

from src.vulnerability import PortScanner
import json

def main():
    print("[*] Starting Port Scan Example")
    print("=" * 50)
    
    # Initialize port scanner
    ps = PortScanner(timeout=1)
    
    # Define target
    target = "192.168.1.100"
    print(f"[*] Scanning ports on: {target}\n")
    
    # Scan common ports
    open_ports = ps.scan_target(target)
    
    print(f"[+] Found {len(open_ports)} open ports\n")
    
    for port_info in open_ports:
        print(f"  Port: {port_info['port']}")
        print(f"  Service: {port_info['service']}")
        print(f"  Status: {port_info['status']}")
        
        # Try to grab banner
        try:
            banner = ps.get_service_version(target, port_info['port'])
            if banner:
                print(f"  Banner: {banner[:50]}...")
        except:
            pass
        print()
    
    # Save results
    output_file = "port_scan_results.json"
    with open(output_file, 'w') as f:
        json.dump(open_ports, f, indent=2)
    print(f"[+] Results saved to {output_file}")

if __name__ == "__main__":
    main()
