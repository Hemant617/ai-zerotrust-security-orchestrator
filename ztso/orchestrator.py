"""
Security Orchestrator - Main coordination engine
"""

import asyncio
import logging
from typing import Dict, Any, Optional
from datetime import datetime

from .detection import ThreatDetector
from .zerotrust import PolicyEngine
from .crypto import QuantumSafeCrypto
from .response import AutomatedResponse
from .analytics import SecurityAnalytics

logger = logging.getLogger(__name__)


class SecurityOrchestrator:
    """
    Main orchestration engine coordinating all security components.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Security Orchestrator.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.threat_detector = ThreatDetector(self.config)
        self.policy_engine = PolicyEngine(self.config)
        self.crypto_engine = QuantumSafeCrypto(self.config)
        self.response_engine = AutomatedResponse(self.config)
        self.analytics = SecurityAnalytics(self.config)
        
        self.is_running = False
        self.start_time = None
        
        logger.info("Security Orchestrator initialized")
    
    async def start(self):
        """Start all security components."""
        logger.info("Starting Security Orchestrator...")
        
        self.is_running = True
        self.start_time = datetime.utcnow()
        
        # Start all components in parallel
        await asyncio.gather(
            self.threat_detector.start(),
            self.policy_engine.start(),
            self.response_engine.start(),
            self.analytics.start()
        )
        
        logger.info("Security Orchestrator started successfully")
    
    async def stop(self):
        """Stop all security components."""
        logger.info("Stopping Security Orchestrator...")
        
        self.is_running = False
        
        await asyncio.gather(
            self.threat_detector.stop(),
            self.policy_engine.stop(),
            self.response_engine.stop(),
            self.analytics.stop()
        )
        
        logger.info("Security Orchestrator stopped")
    
    def start_threat_detection(self):
        """Enable threat detection engine."""
        logger.info("Starting threat detection...")
        return self.threat_detector.enable()
    
    def enforce_zero_trust(self):
        """Enable zero-trust policy enforcement."""
        logger.info("Enforcing zero-trust policies...")
        return self.policy_engine.enforce_all_policies()
    
    def get_dashboard(self) -> Dict[str, Any]:
        """
        Get current security dashboard data.
        
        Returns:
            Dashboard data dictionary
        """
        return {
            "status": "running" if self.is_running else "stopped",
            "uptime": (datetime.utcnow() - self.start_time).total_seconds() if self.start_time else 0,
            "threats_detected": self.threat_detector.get_threat_count(),
            "policies_enforced": self.policy_engine.get_policy_count(),
            "incidents_responded": self.response_engine.get_incident_count(),
            "security_score": self.analytics.calculate_security_score(),
            "active_alerts": self.analytics.get_active_alerts()
        }
    
    async def handle_threat(self, threat_data: Dict[str, Any]):
        """
        Handle detected threat with automated response.
        
        Args:
            threat_data: Threat information
        """
        logger.warning(f"Threat detected: {threat_data.get('type')}")
        
        # Analyze threat severity
        severity = self.analytics.assess_threat_severity(threat_data)
        
        # Execute automated response
        response = await self.response_engine.respond(threat_data, severity)
        
        # Update analytics
        self.analytics.record_threat(threat_data, response)
        
        return response
    
    def get_security_posture(self) -> Dict[str, Any]:
        """
        Get comprehensive security posture assessment.
        
        Returns:
            Security posture data
        """
        return self.analytics.get_security_posture()
