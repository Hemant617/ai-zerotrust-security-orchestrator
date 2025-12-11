"""
Unit tests for Threat Detection Engine
"""

import pytest
import asyncio
from ztso.detection import ThreatDetector


@pytest.fixture
def detector():
    """Create threat detector instance."""
    config = {
        'anomaly_threshold': 0.75,
        'threat_threshold': 0.85
    }
    return ThreatDetector(config)


@pytest.mark.asyncio
async def test_detector_initialization(detector):
    """Test detector initialization."""
    assert detector is not None
    assert detector.enabled == False
    assert detector.threat_count == 0


@pytest.mark.asyncio
async def test_detector_start_stop(detector):
    """Test detector start and stop."""
    await detector.start()
    assert detector.enabled == True
    
    await detector.stop()
    assert detector.enabled == False


@pytest.mark.asyncio
async def test_network_traffic_analysis(detector):
    """Test network traffic analysis."""
    await detector.start()
    
    result = await detector.analyze_network_traffic()
    
    assert 'status' in result
    assert result['status'] in ['normal', 'threat_detected', 'disabled']
    
    await detector.stop()


@pytest.mark.asyncio
async def test_anomaly_detection(detector):
    """Test anomaly detection."""
    await detector.start()
    
    anomalies = await detector.detect_anomalies()
    
    assert isinstance(anomalies, list)
    
    await detector.stop()


@pytest.mark.asyncio
async def test_threat_identification(detector):
    """Test threat identification."""
    await detector.start()
    
    threats = await detector.identify_threats()
    
    assert isinstance(threats, list)
    
    await detector.stop()


@pytest.mark.asyncio
async def test_user_behavior_analysis(detector):
    """Test user behavior analysis."""
    await detector.start()
    
    activity = {'action': 'login', 'time': '10:00:00'}
    result = await detector.analyze_user_behavior('user-123', activity)
    
    assert 'user_id' in result
    assert 'risk_score' in result
    assert result['user_id'] == 'user-123'
    
    await detector.stop()


@pytest.mark.asyncio
async def test_apt_detection(detector):
    """Test APT detection."""
    await detector.start()
    
    indicators = {'suspicious_activity': True}
    result = await detector.detect_apt(indicators)
    
    assert 'apt_detected' in result
    assert 'confidence' in result
    assert isinstance(result['apt_detected'], bool)
    
    await detector.stop()
