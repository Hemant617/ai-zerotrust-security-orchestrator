"""
Main FastAPI Application
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, Any, Optional
import logging
import os

from .orchestrator import SecurityOrchestrator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Zero-Trust Security Orchestrator",
    description="Revolutionary AI-powered cybersecurity platform",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize orchestrator
orchestrator = SecurityOrchestrator()


# Request models
class ThreatAnalysisRequest(BaseModel):
    data: Dict[str, Any]


class IdentityVerificationRequest(BaseModel):
    user_id: str
    context: Dict[str, Any]


class EncryptionRequest(BaseModel):
    data: str
    algorithm: Optional[str] = None


@app.on_event("startup")
async def startup_event():
    """Initialize on startup."""
    logger.info("Starting AI Zero-Trust Security Orchestrator...")
    await orchestrator.start()


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down AI Zero-Trust Security Orchestrator...")
    await orchestrator.stop()


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "AI Zero-Trust Security Orchestrator",
        "version": "1.0.0",
        "status": "operational",
        "web_interface": "/web",
        "api_docs": "/docs",
        "dashboard": "/dashboard"
    }


@app.get("/web")
async def web_interface():
    """Serve the web interface."""
    web_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "web", "index.html")
    if os.path.exists(web_path):
        return FileResponse(web_path)
    else:
        return {
            "message": "Web interface not found. Please ensure web/index.html exists.",
            "alternative": "Use /docs for interactive API documentation"
        }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": "2025-12-11T03:57:00Z"
    }


@app.get("/dashboard")
async def get_dashboard():
    """Get security dashboard."""
    return orchestrator.get_dashboard()


@app.get("/security-posture")
async def get_security_posture():
    """Get security posture assessment."""
    return orchestrator.get_security_posture()


@app.post("/threat/analyze")
async def analyze_threat(request: ThreatAnalysisRequest):
    """Analyze potential threat."""
    result = await orchestrator.threat_detector.analyze_network_traffic(request.data)
    return result


@app.post("/zerotrust/verify")
async def verify_identity(request: IdentityVerificationRequest):
    """Verify user identity with zero-trust."""
    result = await orchestrator.policy_engine.verify_identity(
        request.user_id,
        request.context
    )
    return result


@app.post("/crypto/encrypt")
async def encrypt_data(request: EncryptionRequest):
    """Encrypt data with quantum-safe crypto."""
    data_bytes = request.data.encode('utf-8')
    result = orchestrator.crypto_engine.encrypt_pqc(
        data_bytes,
        request.algorithm
    )
    
    # Convert bytes to hex for JSON serialization
    return {
        "encrypted_data": result["encrypted_data"].hex(),
        "algorithm": result["algorithm"],
        "hybrid_mode": result["hybrid_mode"],
        "metadata": result["metadata"]
    }


@app.get("/metrics")
async def get_metrics():
    """Get security metrics."""
    return {
        "threats_detected": orchestrator.threat_detector.get_threat_count(),
        "policies_enforced": orchestrator.policy_engine.get_policy_count(),
        "incidents_responded": orchestrator.response_engine.get_incident_count(),
        "security_score": orchestrator.analytics.calculate_security_score()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
