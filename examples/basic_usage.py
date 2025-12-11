"""
Basic Usage Examples for AI Zero-Trust Security Orchestrator
"""

import asyncio
from ztso import SecurityOrchestrator, ThreatDetector, PolicyEngine, QuantumSafeCrypto


async def example_threat_detection():
    """Example: Threat Detection"""
    print("=== Threat Detection Example ===\n")
    
    detector = ThreatDetector(config={})
    await detector.start()
    
    # Analyze network traffic
    result = await detector.analyze_network_traffic()
    print(f"Network Analysis: {result}\n")
    
    # Detect anomalies
    anomalies = await detector.detect_anomalies()
    print(f"Anomalies Detected: {len(anomalies)}\n")
    
    await detector.stop()


async def example_zero_trust():
    """Example: Zero-Trust Policy Enforcement"""
    print("=== Zero-Trust Example ===\n")
    
    engine = PolicyEngine(config={})
    await engine.start()
    
    # Verify user identity
    context = {
        'device': {'id': 'device-123', 'type': 'laptop'},
        'location': {'ip': '192.168.1.100', 'country': 'US'},
        'time': '2025-12-11T10:00:00Z'
    }
    
    result = await engine.verify_identity('user-456', context)
    print(f"Identity Verification: {result}\n")
    
    # Enforce least privilege
    access = await engine.enforce_least_privilege('user-456', '/api/data')
    print(f"Access Control: {access}\n")
    
    await engine.stop()


def example_quantum_crypto():
    """Example: Quantum-Safe Cryptography"""
    print("=== Quantum-Safe Crypto Example ===\n")
    
    crypto = QuantumSafeCrypto(config={'hybrid_mode': True})
    
    # Encrypt data
    data = b"Sensitive information that needs quantum-safe protection"
    encrypted = crypto.encrypt_pqc(data, algorithm='CRYSTALS-Kyber')
    
    print(f"Algorithm: {encrypted['algorithm']}")
    print(f"Hybrid Mode: {encrypted['hybrid_mode']}")
    print(f"Encrypted Size: {encrypted['metadata']['data_size']} bytes\n")
    
    # Decrypt data
    decrypted = crypto.decrypt_pqc(
        encrypted['encrypted_data'],
        encrypted['public_key'],  # In real use, this would be the private key
        algorithm='CRYSTALS-Kyber'
    )
    
    print(f"Decryption successful: {decrypted == data}\n")


async def example_full_orchestration():
    """Example: Full Security Orchestration"""
    print("=== Full Orchestration Example ===\n")
    
    # Initialize orchestrator
    orchestrator = SecurityOrchestrator(config={
        'anomaly_threshold': 0.75,
        'threat_threshold': 0.85,
        'continuous_auth_interval': 300
    })
    
    # Start all components
    await orchestrator.start()
    
    # Enable threat detection
    orchestrator.start_threat_detection()
    print("✓ Threat detection enabled")
    
    # Enforce zero-trust
    orchestrator.enforce_zero_trust()
    print("✓ Zero-trust policies enforced")
    
    # Get dashboard
    dashboard = orchestrator.get_dashboard()
    print(f"\nDashboard:")
    print(f"  Status: {dashboard['status']}")
    print(f"  Security Score: {dashboard['security_score']}")
    print(f"  Threats Detected: {dashboard['threats_detected']}")
    
    # Get security posture
    posture = orchestrator.get_security_posture()
    print(f"\nSecurity Posture:")
    print(f"  Overall Score: {posture['overall_score']}")
    print(f"  Threat Level: {posture['threat_level']}")
    print(f"  Compliance: {posture['compliance_status']}")
    
    # Stop orchestrator
    await orchestrator.stop()
    print("\n✓ Orchestrator stopped")


async def main():
    """Run all examples"""
    print("AI Zero-Trust Security Orchestrator - Examples\n")
    print("=" * 60 + "\n")
    
    await example_threat_detection()
    await example_zero_trust()
    example_quantum_crypto()
    await example_full_orchestration()
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
