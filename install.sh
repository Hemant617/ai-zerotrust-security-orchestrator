#!/bin/bash

# AI Zero-Trust Security Orchestrator - One-Click Installer
# This script will install and start everything automatically

echo "╔════════════════════════════════════════════════════════════╗"
echo "║   AI Zero-Trust Security Orchestrator - Installer         ║"
echo "║   Revolutionary Cybersecurity Platform                    ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Docker is installed
echo "🔍 Checking prerequisites..."
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed!${NC}"
    echo ""
    echo "Please install Docker Desktop from:"
    echo "https://www.docker.com/products/docker-desktop"
    echo ""
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose is not installed!${NC}"
    echo ""
    echo "Please install Docker Compose from:"
    echo "https://docs.docker.com/compose/install/"
    echo ""
    exit 1
fi

echo -e "${GREEN}✅ Docker is installed${NC}"
echo -e "${GREEN}✅ Docker Compose is installed${NC}"
echo ""

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo -e "${RED}❌ Docker is not running!${NC}"
    echo ""
    echo "Please start Docker Desktop and try again."
    echo ""
    exit 1
fi

echo -e "${GREEN}✅ Docker is running${NC}"
echo ""

# Stop any existing containers
echo "🛑 Stopping any existing containers..."
docker-compose down 2>/dev/null

# Pull latest images
echo ""
echo "📦 Pulling required Docker images (this may take a few minutes)..."
docker-compose pull

# Start services
echo ""
echo "🚀 Starting AI Zero-Trust Security Orchestrator..."
docker-compose up -d

# Wait for services to be ready
echo ""
echo "⏳ Waiting for services to start (30 seconds)..."
sleep 30

# Check if services are running
echo ""
echo "🔍 Checking service status..."

if docker-compose ps | grep -q "Up"; then
    echo -e "${GREEN}✅ Services are running!${NC}"
else
    echo -e "${RED}❌ Some services failed to start${NC}"
    echo ""
    echo "Check logs with: docker-compose logs"
    exit 1
fi

# Display success message
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║              🎉 Installation Successful! 🎉               ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Your AI Zero-Trust Security Orchestrator is now running!"
echo ""
echo "📍 Access Points:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  🌐 Web Interface (VirusTotal-like):"
echo "     http://localhost:8000/web"
echo ""
echo "  📚 Interactive API Documentation:"
echo "     http://localhost:8000/docs"
echo ""
echo "  📊 Security Dashboard:"
echo "     http://localhost:8000/dashboard"
echo ""
echo "  📈 Grafana Monitoring:"
echo "     http://localhost:3000"
echo "     (Login: admin / admin)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎯 Quick Start:"
echo "  1. Open http://localhost:8000/web in your browser"
echo "  2. Enter an IP address or URL to analyze"
echo "  3. Click 'Analyze' to see AI-powered threat detection!"
echo ""
echo "📖 Documentation:"
echo "  • Quick Start: cat QUICK_START.md"
echo "  • Architecture: cat docs/ARCHITECTURE.md"
echo "  • Examples: ls examples/"
echo ""
echo "🛠️  Useful Commands:"
echo "  • View logs:     docker-compose logs -f"
echo "  • Stop services: docker-compose down"
echo "  • Restart:       docker-compose restart"
echo "  • Status:        docker-compose ps"
echo ""
echo "❓ Need Help?"
echo "  • GitHub Issues: https://github.com/Hemant617/ai-zerotrust-security-orchestrator/issues"
echo "  • Documentation: https://github.com/Hemant617/ai-zerotrust-security-orchestrator"
echo ""
echo "⭐ Don't forget to star the repository!"
echo ""
echo "Happy Securing! 🛡️"
echo ""
