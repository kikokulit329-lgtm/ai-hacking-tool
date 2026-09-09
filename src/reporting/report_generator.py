"""
Report Generator - Create comprehensive security reports
"""

import logging
from typing import Dict, List
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generates comprehensive security reports."""

    def __init__(self):
        self.report = {}
        self.timestamp = datetime.now().isoformat()

    def generate_full_report(self, scan_results: Dict) -> Dict:
        """
        Generate a comprehensive security report.
        
        Args:
            scan_results: Results from all scans
            
        Returns:
            Complete report dictionary
        """
        logger.info("Generating comprehensive security report")
        
        self.report = {
            'title': 'Security Assessment Report',
            'timestamp': self.timestamp,
            'summary': self._generate_summary(scan_results),
            'findings': self._organize_findings(scan_results),
            'statistics': self._generate_statistics(scan_results),
            'recommendations': self._generate_recommendations(scan_results),
        }
        
        logger.info("Report generation complete")
        return self.report

    def _generate_summary(self, results: Dict) -> Dict:
        """
        Generate executive summary.
        
        Args:
            results: Scan results
            
        Returns:
            Summary dictionary
        """
        return {
            'target': results.get('target', 'Unknown'),
            'scan_date': self.timestamp,
            'total_vulnerabilities': len(results.get('vulnerabilities', [])),
            'critical_count': len([v for v in results.get('vulnerabilities', []) if v.get('severity') == 'Critical']),
            'high_count': len([v for v in results.get('vulnerabilities', []) if v.get('severity') == 'High']),
            'overall_risk': 'High' if len(results.get('vulnerabilities', [])) > 10 else 'Medium',
        }

    def _organize_findings(self, results: Dict) -> List[Dict]:
        """
        Organize findings by category.
        
        Args:
            results: Scan results
            
        Returns:
            Organized findings
        """
        findings = []
        
        for vuln in results.get('vulnerabilities', []):
            finding = {
                'title': vuln.get('type', 'Unknown'),
                'severity': vuln.get('severity', 'Unknown'),
                'description': vuln.get('description', ''),
                'affected_asset': vuln.get('asset', ''),
                'remediation': vuln.get('remediation', ''),
            }
            findings.append(finding)
        
        return findings

    def _generate_statistics(self, results: Dict) -> Dict:
        """
        Generate statistical analysis.
        
        Args:
            results: Scan results
            
        Returns:
            Statistics dictionary
        """
        vulns = results.get('vulnerabilities', [])
        
        return {
            'total_vulnerabilities': len(vulns),
            'severity_breakdown': {
                'critical': len([v for v in vulns if v.get('severity') == 'Critical']),
                'high': len([v for v in vulns if v.get('severity') == 'High']),
                'medium': len([v for v in vulns if v.get('severity') == 'Medium']),
                'low': len([v for v in vulns if v.get('severity') == 'Low']),
            },
            'asset_count': len(set(v.get('asset', '') for v in vulns)),
        }

    def _generate_recommendations(self, results: Dict) -> List[str]:
        """
        Generate recommendations.
        
        Args:
            results: Scan results
            
        Returns:
            List of recommendations
        """
        recommendations = [
            "Update all software to the latest versions",
            "Enable security headers on all web applications",
            "Implement proper authentication controls",
            "Regular security assessments and penetration testing",
            "Deploy intrusion detection/prevention systems",
            "Maintain comprehensive security logs and monitoring",
        ]
        
        return recommendations

    def export_json(self, filepath: str):
        """
        Export report as JSON.
        
        Args:
            filepath: Output file path
        """
        try:
            with open(filepath, 'w') as f:
                json.dump(self.report, f, indent=2)
            logger.info(f"Report exported to {filepath}")
        except Exception as e:
            logger.error(f"Failed to export report: {e}")

    def export_text(self, filepath: str):
        """
        Export report as plain text.
        
        Args:
            filepath: Output file path
        """
        try:
            with open(filepath, 'w') as f:
                f.write(f"{'='*80}\n")
                f.write(f"{self.report.get('title')}\n")
                f.write(f"{'='*80}\n\n")
                f.write(f"Report Date: {self.report.get('timestamp')}\n\n")
                
                summary = self.report.get('summary', {})
                f.write(f"SUMMARY\n")
                f.write(f"-" * 40 + "\n")
                for key, value in summary.items():
                    f.write(f"{key}: {value}\n")
                
            logger.info(f"Report exported to {filepath}")
        except Exception as e:
            logger.error(f"Failed to export report: {e}")
