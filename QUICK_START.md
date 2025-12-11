# 🚀 Quick Start Guide - Get Running in 5 Minutes!

This guide will help you get the AI Zero-Trust Security Orchestrator up and running quickly, just like VirusTotal!

## 📋 Prerequisites

You only need these installed on your computer:
- **Docker Desktop** (Download from: https://www.docker.com/products/docker-desktop)
- **Git** (Download from: https://git-scm.com/downloads)

That's it! Docker will handle everything else.

## ⚡ Installation (3 Simple Steps)

### Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/Hemant617/ai-zerotrust-security-orchestrator.git
cd ai-zerotrust-security-orchestrator
```

### Step 2: Start the Platform

Run this single command:

```bash
docker-compose up -d
```

This will:
- Download all required components
- Set up databases automatically
- Start all services
- Configure everything for you

**Wait 2-3 minutes** for everything to start up.

### Step 3: Access the Platform

Open your web browser and go to:

**🌐 Main Dashboard**: http://localhost:8000

**📊 Monitoring Dashboard**: http://localhost:3000 (Grafana - login: admin/admin)

**🎯 API Documentation**: http://localhost:8000/docs

## 🎮 How to Use - Simple Examples

### Example 1: Check if System is Running

Open your browser and visit:
```
http://localhost:8000/health
```

You should see:
```json
{
  "status": "healthy",
  "timestamp": "2025-12-11T03:57:00Z"
}
```

### Example 2: Get Security Dashboard

Visit:
```
http://localhost:8000/dashboard
```

You'll see your complete security status!

### Example 3: Analyze a Potential Threat (Like VirusTotal!)

**Using Browser** (Easy Way):

1. Go to: http://localhost:8000/docs
2. Click on `POST /threat/analyze`
3. Click "Try it out"
4. Paste this example:
```json
{
  "data": {
    "source_ip": "192.168.1.100",
    "destination_ip": "10.0.0.50",
    "port": 443,
    "protocol": "HTTPS"
  }
}
```
5. Click "Execute"
6. See the threat analysis results!

**Using Command Line** (Advanced):

```bash
curl -X POST "http://localhost:8000/threat/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "source_ip": "192.168.1.100",
      "destination_ip": "10.0.0.50",
      "port": 443
    }
  }'
```

### Example 4: Verify User Identity (Zero-Trust)

Go to: http://localhost:8000/docs

Find `POST /zerotrust/verify` and try:

```json
{
  "user_id": "john.doe@company.com",
  "context": {
    "device": {
      "id": "laptop-123",
      "type": "laptop"
    },
    "location": {
      "ip": "192.168.1.100",
      "country": "US"
    }
  }
}
```

You'll get a trust score and verification result!

### Example 5: Encrypt Data with Quantum-Safe Crypto

Try `POST /crypto/encrypt`:

```json
{
  "data": "My sensitive information",
  "algorithm": "CRYSTALS-Kyber"
}
```

Your data will be encrypted with quantum-resistant cryptography!

## 🎯 Web Interface (Coming in Next Update!)

We're building a beautiful web UI similar to VirusTotal. For now, use:

1. **Swagger UI**: http://localhost:8000/docs (Interactive API testing)
2. **Grafana**: http://localhost:3000 (Beautiful dashboards)

## 📱 Common Use Cases

### Use Case 1: Scan Network Traffic for Threats

```bash
# Check if your network traffic is safe
curl -X POST "http://localhost:8000/threat/analyze" \
  -H "Content-Type: application/json" \
  -d '{"data": {"traffic_sample": "your_network_data"}}'
```

### Use Case 2: Check Security Score

```bash
# Get your overall security score
curl http://localhost:8000/dashboard
```

### Use Case 3: Get Security Metrics

```bash
# See all security metrics
curl http://localhost:8000/metrics
```

## 🛠️ Troubleshooting

### Problem: "Port already in use"

**Solution**: Stop other services using ports 8000, 3000, 5432, or change ports in `docker-compose.yml`

### Problem: "Docker command not found"

**Solution**: Install Docker Desktop from https://www.docker.com/products/docker-desktop

### Problem: Services not starting

**Solution**: 
```bash
# Stop everything
docker-compose down

# Remove old containers
docker-compose rm -f

# Start fresh
docker-compose up -d

# Check logs
docker-compose logs -f
```

### Problem: "Connection refused"

**Solution**: Wait 2-3 minutes for all services to fully start, then try again.

## 🎨 Visual Guide

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  YOU → Browser → http://localhost:8000                 │
│                                                         │
│         ↓                                               │
│                                                         │
│  AI Security Platform (Running in Docker)               │
│  ├── Threat Detection Engine                           │
│  ├── Zero-Trust Policy Engine                          │
│  ├── Quantum-Safe Crypto                               │
│  ├── Automated Response                                │
│  └── Analytics Dashboard                               │
│                                                         │
│         ↓                                               │
│                                                         │
│  Results → JSON Response → Your Browser                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 📚 What Each URL Does

| URL | What It Does | Like VirusTotal's |
|-----|--------------|-------------------|
| http://localhost:8000 | Main API | API endpoint |
| http://localhost:8000/docs | Interactive testing | Web interface |
| http://localhost:8000/dashboard | Security overview | Dashboard |
| http://localhost:8000/threat/analyze | Scan for threats | File/URL scan |
| http://localhost:3000 | Monitoring graphs | Analytics |

## 🎓 Learning Path

**Beginner** (Start here!):
1. Visit http://localhost:8000/docs
2. Try the examples above
3. Explore the interactive API

**Intermediate**:
1. Read `examples/basic_usage.py`
2. Modify the examples
3. Create your own security checks

**Advanced**:
1. Read `docs/ARCHITECTURE.md`
2. Customize the ML models
3. Add new threat detection rules

## 🆘 Need Help?

1. **Check logs**: `docker-compose logs -f`
2. **Restart services**: `docker-compose restart`
3. **Full reset**: `docker-compose down && docker-compose up -d`
4. **Open an issue**: https://github.com/Hemant617/ai-zerotrust-security-orchestrator/issues

## 🎉 You're Ready!

The platform is now running! Start by visiting:
👉 **http://localhost:8000/docs**

This is your interactive playground - just like VirusTotal's web interface!

---

**Next Steps:**
- ⭐ Star the repository
- 📖 Read the full documentation
- 🤝 Join our community
- 🚀 Start securing your systems!
