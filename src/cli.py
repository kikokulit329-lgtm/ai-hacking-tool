"""
Command-line Interface for AI Hacking Tool
"""

import logging
import sys
from argparse import ArgumentParser
from src.reconnaissance.scanner import NetworkScanner
from src.vulnerability.port_scanner import PortScanner
from src.ai_engine.threat_detector import ThreatDetector
from src.reporting.report_generator import ReportGenerator

logger = logging.getLogger(__name__)


def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main():
    """Main CLI entry point."""
    parser = ArgumentParser(description='AI Hacking Tool - Ethical Security Testing')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Network scan command
    scan_parser = subparsers.add_parser('scan', help='Scan network or host')
    scan_parser.add_argument('target', help='Target IP, hostname, or network range')
    scan_parser.add_argument('-t', '--type', choices=['network', 'host', 'port'], default='host')
    
    # Port scan command
    port_parser = subparsers.add_parser('ports', help='Scan ports on target')
    port_parser.add_argument('target', help='Target IP or hostname')
    port_parser.add_argument('-p', '--ports', help='Specific ports (comma-separated)')
    
    # Threat detection command
    threat_parser = subparsers.add_parser('threats', help='Detect threats in traffic')
    threat_parser.add_argument('pcap_file', help='PCAP file to analyze')
    
    # Report command
    report_parser = subparsers.add_parser('report', help='Generate security report')
    report_parser.add_argument('input_file', help='Scan results file')
    report_parser.add_argument('-f', '--format', choices=['json', 'html', 'txt'], default='json')
    
    args = parser.parse_args()
    setup_logging()
    
    if args.command == 'scan':
        if args.type == 'network':
            scanner = NetworkScanner()
            results = scanner.scan_network(args.target)
            print(f"Found {len(results)} hosts")
        elif args.type == 'host':
            scanner = NetworkScanner()
            if scanner.ping_host(args.target):
                print(f"Host {args.target} is online")
    
    elif args.command == 'ports':
        ps = PortScanner()
        results = ps.scan_target(args.target)
        for port_info in results:
            print(f"{port_info['port']}: {port_info['service']} - {port_info['status']}")
    
    elif args.command == 'threats':
        print("Threat detection would analyze the provided PCAP file")
    
    elif args.command == 'report':
        reporter = ReportGenerator()
        print(f"Would generate {args.format} report from {args.input_file}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
