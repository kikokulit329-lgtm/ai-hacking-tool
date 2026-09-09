"""
Example 4: DNS Enumeration and Subdomain Discovery

This script performs DNS enumeration and discovers subdomains.
"""

from src.reconnaissance import DNSEnumerator, SubdomainFinder
import json

def main():
    print("[*] Starting DNS Enumeration Example")
    print("=" * 50)
    
    target_domain = "example.com"
    
    # DNS Enumeration
    print(f"\n[*] Enumerating DNS records for {target_domain}")
    dns = DNSEnumerator()
    dns_records = dns.enumerate_dns_records(target_domain)
    
    print(f"\n[+] DNS Records:")
    for record_type, records in dns_records.items():
        if records:
            print(f"  {record_type}: {records}")
    
    # Subdomain Discovery
    print(f"\n[*] Discovering subdomains for {target_domain}")
    finder = SubdomainFinder()
    subdomains = finder.find_subdomains(target_domain, threads=10)
    
    print(f"\n[+] Found {len(subdomains)} subdomains:")
    for subdomain in sorted(subdomains):
        print(f"  - {subdomain}")
    
    # Save results
    results = {
        'domain': target_domain,
        'dns_records': dns_records,
        'subdomains': list(subdomains)
    }
    
    output_file = "dns_recon_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n[+] Results saved to {output_file}")

if __name__ == "__main__":
    main()
