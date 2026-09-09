"""
Subdomain Discovery - Find subdomains of target domain
"""

import logging
from typing import Set, List
import socket
import dns.resolver
import threading

logger = logging.getLogger(__name__)


class SubdomainFinder:
    """Discovers subdomains of a target domain."""

    def __init__(self, wordlist: str = None):
        self.wordlist = wordlist or self._get_default_wordlist()
        self.found_subdomains: Set[str] = set()
        self.lock = threading.Lock()

    def _get_default_wordlist(self) -> List[str]:
        """Returns a basic subdomain wordlist."""
        return [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp',
            'pop', 'ns', 'webdisk', 'ns1', 'ns2', 'cpanel', 'whm',
            'autodiscover', 'autoconfig', 'admin', 'test', 'dev',
            'api', 'app', 'staging', 'prod', 'cdn', 'images',
            'blog', 'shop', 'git', 'jenkins', 'docs', 'dashboard'
        ]

    def find_subdomains(self, domain: str, threads: int = 10) -> Set[str]:
        """
        Find subdomains using wordlist.
        
        Args:
            domain: Target domain
            threads: Number of threads to use
            
        Returns:
            Set of discovered subdomains
        """
        logger.info(f"Starting subdomain discovery for {domain}")
        self.found_subdomains.clear()
        
        wordlist = self.wordlist if isinstance(self.wordlist, list) else [self.wordlist]
        chunk_size = len(wordlist) // threads
        thread_list = []
        
        for i in range(threads):
            start = i * chunk_size
            end = start + chunk_size if i < threads - 1 else len(wordlist)
            t = threading.Thread(
                target=self._check_subdomains,
                args=(domain, wordlist[start:end])
            )
            thread_list.append(t)
            t.start()
        
        for t in thread_list:
            t.join()
        
        logger.info(f"Found {len(self.found_subdomains)} subdomains")
        return self.found_subdomains

    def _check_subdomains(self, domain: str, wordlist: List[str]):
        """Internal method to check subdomains."""
        for subdomain in wordlist:
            full_domain = f"{subdomain}.{domain}"
            try:
                socket.gethostbyname(full_domain)
                with self.lock:
                    self.found_subdomains.add(full_domain)
                logger.debug(f"Found subdomain: {full_domain}")
            except socket.gaierror:
                pass
            except Exception as e:
                logger.debug(f"Error checking {full_domain}: {e}")
