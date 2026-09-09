import pytest
from src.reconnaissance import NetworkScanner, DNSEnumerator, SubdomainFinder
from src.vulnerability import PortScanner, WebScanner, CVEChecker
from src.ai_engine import ThreatDetector, AnomalyDetector
from src.reporting import ReportGenerator


class TestReconnaissance:
    """Tests for reconnaissance module."""
    
    def test_network_scanner_initialization(self):
        scanner = NetworkScanner(timeout=2)
        assert scanner.timeout == 2
    
    def test_dns_enumerator_initialization(self):
        dns = DNSEnumerator()
        assert dns.resolver is not None
    
    def test_subdomain_finder_initialization(self):
        finder = SubdomainFinder()
        assert finder.wordlist is not None


class TestVulnerability:
    """Tests for vulnerability module."""
    
    def test_port_scanner_initialization(self):
        ps = PortScanner(timeout=1)
        assert ps.timeout == 1
    
    def test_web_scanner_initialization(self):
        scanner = WebScanner(timeout=5)
        assert scanner.timeout == 5
    
    def test_cve_checker_initialization(self):
        checker = CVEChecker()
        assert checker.cve_database is not None
    
    def test_cve_checker_database_format(self):
        checker = CVEChecker()
        assert isinstance(checker.cve_database, dict)


class TestAIEngine:
    """Tests for AI engine module."""
    
    def test_threat_detector_initialization(self):
        detector = ThreatDetector()
        assert detector.threshold == 0.7
    
    def test_threat_level_classification(self):
        detector = ThreatDetector()
        assert detector._get_threat_level(0.95) == "CRITICAL"
        assert detector._get_threat_level(0.75) == "HIGH"
        assert detector._get_threat_level(0.55) == "MEDIUM"
        assert detector._get_threat_level(0.30) == "LOW"
    
    def test_anomaly_detector_initialization(self):
        detector = AnomalyDetector()
        assert detector.sensitivity == 2.0


class TestReporting:
    """Tests for reporting module."""
    
    def test_report_generator_initialization(self):
        reporter = ReportGenerator()
        assert reporter.report == {}
    
    def test_report_generation(self):
        reporter = ReportGenerator()
        scan_results = {
            'target': 'test.com',
            'vulnerabilities': []
        }
        report = reporter.generate_full_report(scan_results)
        
        assert 'title' in report
        assert 'summary' in report
        assert 'findings' in report
        assert 'statistics' in report
        assert 'recommendations' in report
    
    def test_report_summary_structure(self):
        reporter = ReportGenerator()
        scan_results = {
            'target': 'test.com',
            'vulnerabilities': [
                {'type': 'Test', 'severity': 'Critical'},
                {'type': 'Test2', 'severity': 'High'},
            ]
        }
        report = reporter.generate_full_report(scan_results)
        summary = report['summary']
        
        assert summary['target'] == 'test.com'
        assert summary['total_vulnerabilities'] == 2
        assert summary['critical_count'] == 1
        assert summary['high_count'] == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
