"""
DNS Enumeration - Domain and DNS Reconnaissance
"""

import logging
from typing import List, Dict, Set
import dns.resolver
import dns.zone
import dns.query

logger = logging.getLogger(__name__)


class DNSEnumerator:
    """Performs DNS enumeration and reconnaissance."""

    def __init__(self):
        self.resolver = dns.resolver.Resolver()
        self.results = {}

    def enumerate_dns_records(self, domain: str) -> Dict:
        """
        Enumerate DNS records for a domain.
        
        Args:
            domain: Target domain
            
        Returns:
            Dictionary of DNS records
        """
        logger.info(f"Enumerating DNS records for {domain}")
        records = {}
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'SOA', 'TXT', 'CNAME', 'SRV']
        
        for record_type in record_types:
            try:
                answers = self.resolver.resolve(domain, record_type)
                records[record_type] = [str(rdata) for rdata in answers]
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, Exception) as e:
                records[record_type] = None
        
        self.results = records
        return records

    def get_mx_records(self, domain: str) -> List[str]:
        """
        Get MX records for email servers.
        
        Args:
            domain: Target domain
            
        Returns:
            List of MX records
        """
        try:
            mx_records = self.resolver.resolve(domain, 'MX')
            return [str(record.exchange) for record in mx_records]
        except Exception as e:
            logger.error(f"Failed to get MX records: {e}")
            return []

    def get_nameservers(self, domain: str) -> List[str]:
        """
        Get authoritative nameservers.
        
        Args:
            domain: Target domain
            
        Returns:
            List of nameservers
        """
        try:
            ns_records = self.resolver.resolve(domain, 'NS')
            return [str(ns.target) for ns in ns_records]
        except Exception as e:
            logger.error(f"Failed to get nameservers: {e}")
            return []

    def get_txt_records(self, domain: str) -> List[str]:
        """
        Get TXT records (SPF, DKIM, DMARC).
        
        Args:
            domain: Target domain
            
        Returns:
            List of TXT records
        """
        try:
            txt_records = self.resolver.resolve(domain, 'TXT')
            return [str(record) for record in txt_records]
        except Exception as e:
            logger.error(f"Failed to get TXT records: {e}")
            return []
