"""
Database initialization script
"""

import asyncio
import logging
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base = declarative_base()


class Threat(Base):
    """Threat detection records."""
    __tablename__ = 'threats'
    
    id = Column(Integer, primary_key=True)
    threat_type = Column(String(100))
    severity = Column(String(20))
    score = Column(Float)
    detected_at = Column(DateTime, default=datetime.utcnow)
    resolved = Column(Boolean, default=False)
    resolved_at = Column(DateTime, nullable=True)


class Policy(Base):
    """Zero-trust policy records."""
    __tablename__ = 'policies'
    
    id = Column(Integer, primary_key=True)
    policy_name = Column(String(200))
    policy_type = Column(String(50))
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Incident(Base):
    """Security incident records."""
    __tablename__ = 'incidents'
    
    id = Column(Integer, primary_key=True)
    incident_type = Column(String(100))
    severity = Column(String(20))
    status = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)
    actions_taken = Column(String(1000))


class AuditLog(Base):
    """Audit log records."""
    __tablename__ = 'audit_logs'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100))
    action = Column(String(200))
    resource = Column(String(200))
    timestamp = Column(DateTime, default=datetime.utcnow)
    success = Column(Boolean)


def init_database():
    """Initialize database schema."""
    logger.info("Initializing database...")
    
    # Get database URL from environment
    database_url = os.getenv('DATABASE_URL', 'postgresql://ztso:ztso_secure@localhost:5432/ztso')
    
    # Create engine
    engine = create_engine(database_url)
    
    # Create all tables
    Base.metadata.create_all(engine)
    
    logger.info("Database initialized successfully!")
    logger.info(f"Created tables: {', '.join(Base.metadata.tables.keys())}")
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Add sample data
    logger.info("Adding sample data...")
    
    sample_policies = [
        Policy(policy_name="Continuous Authentication", policy_type="authentication"),
        Policy(policy_name="Least Privilege Access", policy_type="authorization"),
        Policy(policy_name="Micro-Segmentation", policy_type="network"),
        Policy(policy_name="Device Trust Verification", policy_type="device"),
    ]
    
    session.add_all(sample_policies)
    session.commit()
    
    logger.info(f"Added {len(sample_policies)} sample policies")
    
    session.close()
    logger.info("Database initialization complete!")


if __name__ == "__main__":
    init_database()
