"""
Anomaly Detector - AI-based Anomaly Detection in Network Traffic
"""

import logging
from typing import Dict, List, Tuple
from datetime import datetime
import numpy as np

logger = logging.getLogger(__name__)


class AnomalyDetector:
    """Detects anomalies in network behavior."""

    def __init__(self):
        self.baseline = None
        self.anomalies = []
        self.sensitivity = 2.0  # Standard deviations

    def establish_baseline(self, normal_data: List[Dict]):
        """
        Establish baseline of normal behavior.
        
        Args:
            normal_data: List of normal traffic samples
        """
        logger.info("Establishing baseline from normal traffic")
        
        if not normal_data:
            logger.warning("No baseline data provided")
            return
        
        # Calculate baseline metrics
        self.baseline = {
            'packet_count': len(normal_data),
            'avg_size': np.mean([d.get('size', 0) for d in normal_data]),
            'avg_rate': np.mean([d.get('rate', 0) for d in normal_data]),
        }
        
        logger.info(f"Baseline established: {self.baseline}")

    def detect_anomalies(self, traffic_data: List[Dict]) -> List[Dict]:
        """
        Detect anomalies in traffic data.
        
        Args:
            traffic_data: Network traffic data
            
        Returns:
            List of detected anomalies
        """
        logger.info("Detecting anomalies in traffic")
        self.anomalies = []
        
        if not self.baseline:
            logger.warning("No baseline established")
            return []
        
        for traffic in traffic_data:
            anomaly_score = self._calculate_anomaly_score(traffic)
            
            if anomaly_score > 1.0:
                anomaly = {
                    'traffic': traffic,
                    'anomaly_score': anomaly_score,
                    'severity': 'High' if anomaly_score > 2.0 else 'Medium',
                    'timestamp': datetime.now().isoformat()
                }
                self.anomalies.append(anomaly)
                logger.warning(f"Anomaly detected: {anomaly_score}")
        
        logger.info(f"Found {len(self.anomalies)} anomalies")
        return self.anomalies

    def _calculate_anomaly_score(self, traffic: Dict) -> float:
        """
        Calculate anomaly score for traffic.
        
        Args:
            traffic: Traffic sample
            
        Returns:
            Anomaly score
        """
        score = 0.0
        
        # Compare with baseline
        if traffic.get('size', 0) > self.baseline['avg_size'] * self.sensitivity:
            score += 0.5
        
        if traffic.get('rate', 0) > self.baseline['avg_rate'] * self.sensitivity:
            score += 0.5
        
        return score
