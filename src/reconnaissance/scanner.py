"""
Network Scanner - Reconnaissance and Discovery
"""

import logging
from typing import List, Dict, Tuple
import socket
import threading
from datetime import datetime

logger = logging.getLogger(__name__)


class NetworkScanner:
    """Performs network scanning and host discovery."""

    def __init__(self, timeout: int = 2):
        self.timeout = timeout
        self.results = []
        self.lock = threading.Lock()

    def ping_host(self, host: str) -> bool:
        """
        Ping a host to check if it's alive.
        
        Args:
            host: Target host IP or hostname
            
        Returns:
            bool: True if host is reachable
        """
        try:
            socket.gethostbyaddr(host)
            return True
        except socket.herror:
            return False

    def scan_network(self, network: str) -> List[Dict]:
        """
        Scan a network range for active hosts.
        
        Args:
            network: Network range (e.g., '192.168.1.0/24')
            
        Returns:
            List of discovered hosts with details
        """
        logger.info(f"Starting network scan on {network}")
        self.results = []
        
        # Parse network range
        try:
            from ipaddress import ip_network
            net = ip_network(network, strict=False)
            hosts = list(net.hosts())
            
            threads = []
            for host in hosts:
                t = threading.Thread(
                    target=self._scan_host,
                    args=(str(host),)
                )
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()
                
        except Exception as e:
            logger.error(f"Error scanning network: {e}")
        
        logger.info(f"Scan complete. Found {len(self.results)} active hosts")
        return self.results

    def _scan_host(self, host: str):
        """Internal method to scan individual host."""
        try:
            if self.ping_host(host):
                host_info = {
                    "ip": host,
                    "hostname": socket.getfqdn(host),
                    "status": "online",
                    "timestamp": datetime.now().isoformat()
                }
                with self.lock:
                    self.results.append(host_info)
        except Exception as e:
            logger.debug(f"Error scanning {host}: {e}")

    def resolve_host(self, hostname: str) -> str:
        """
        Resolve hostname to IP address.
        
        Args:
            hostname: Target hostname
            
        Returns:
            IP address string
        """
        try:
            return socket.gethostbyname(hostname)
        except socket.gaierror as e:
            logger.error(f"Failed to resolve {hostname}: {e}")
            return None

    def get_reverse_dns(self, ip: str) -> str:
        """
        Perform reverse DNS lookup.
        
        Args:
            ip: Target IP address
            
        Returns:
            Hostname string
        """
        try:
            return socket.getfqdn(ip)
        except Exception as e:
            logger.error(f"Reverse DNS lookup failed: {e}")
            return None
