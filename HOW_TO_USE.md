# 🎯 How to Use - Visual Guide

## 🚀 **3 Simple Steps to Get Started**

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Install (One Command)                              │
│  ────────────────────────────────────────────────────────   │
│                                                              │
│  Windows:  install.bat                                       │
│  Mac/Linux: ./install.sh                                     │
│                                                              │
│  ⏱️  Takes: 3-5 minutes                                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Open Browser                                        │
│  ────────────────────────────────────────────────────────   │
│                                                              │
│  Go to: http://localhost:8000/web                           │
│                                                              │
│  ⏱️  Takes: 5 seconds                                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Start Analyzing!                                    │
│  ────────────────────────────────────────────────────────   │
│                                                              │
│  Enter IP/URL → Click Analyze → See Results                 │
│                                                              │
│  ⏱️  Takes: 1-2 seconds per scan                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🌐 **What You'll See - Web Interface**

### **Main Screen:**

```
╔══════════════════════════════════════════════════════════════╗
║  🛡️  AI Zero-Trust Security Orchestrator                    ║
║  Revolutionary AI-Powered Cybersecurity Platform             ║
╚══════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────┐
│  Analyze Threat - Like VirusTotal!                           │
│                                                               │
│  ┌────────────────────────────────────────┐  ┌────────────┐ │
│  │ Enter IP address, URL, or hash...      │  │ 🔍 Analyze │ │
│  └────────────────────────────────────────┘  └────────────┘ │
└──────────────────────────────────────────────────────────────┘

┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────┐
│ 🤖 AI       │  │ 🔒 Zero     │  │ ⚛️  Quantum │  │ ⚡ Auto │
│ Threat      │  │ Trust       │  │ Safe        │  │ Response│
│ Detection   │  │ Security    │  │ Crypto      │  │         │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────┘

┌──────────────────────────────────────────────────────────────┐
│  📊 Live Statistics                                           │
│  ─────────────────────────────────────────────────────────   │
│  Threats: 0    Security Score: 85    Policies: 4    <1s      │
└──────────────────────────────────────────────────────────────┘
```

---

## 🎮 **Usage Examples - Step by Step**

### **Example 1: Scan an IP Address**

**What to do:**
```
1. Open: http://localhost:8000/web
2. Type: 192.168.1.100
3. Click: 🔍 Analyze
4. Wait: 1-2 seconds
5. See: Results appear below!
```

**What you'll see:**
```
┌──────────────────────────────────────────────────────────────┐
│  ✅ Analysis Results                                          │
│  ─────────────────────────────────────────────────────────   │
│                                                               │
│  Status: ✅ Safe                                              │
│  Threat Score: 15.23%                                         │
│  Analysis Type: AI Behavioral Analysis                        │
│  Timestamp: 2025-12-11 09:37:58                              │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### **Example 2: Scan a URL**

**What to do:**
```
1. Type: https://example.com
2. Click: 🔍 Analyze
3. See: Instant results!
```

**What you'll see:**
```
┌──────────────────────────────────────────────────────────────┐
│  ⚠️  Analysis Results                                         │
│  ─────────────────────────────────────────────────────────   │
│                                                               │
│  Status: ⚠️  Suspicious                                       │
│  Threat Score: 67.89%                                         │
│  Analysis Type: AI Behavioral Analysis                        │
│  Threat Type: network_anomaly                                 │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### **Example 3: Using the API (For Developers)**

**Step 1: Open API Docs**
```
Go to: http://localhost:8000/docs
```

**Step 2: Find an Endpoint**
```
Look for: POST /threat/analyze
Click: "Try it out"
```

**Step 3: Enter Data**
```json
{
  "data": {
    "source_ip": "192.168.1.100",
    "destination_ip": "10.0.0.50",
    "port": 443
  }
}
```

**Step 4: Execute**
```
Click: "Execute"
Scroll down: See response!
```

---

## 📊 **Understanding the Results**

### **Status Indicators:**

```
✅ Safe          → Threat Score: 0-50%    → No action needed
⚠️  Suspicious   → Threat Score: 50-75%   → Monitor closely
🚨 Threat        → Threat Score: 75-100%  → Immediate action
```

### **What Each Field Means:**

| Field | What It Tells You |
|-------|-------------------|
| **Status** | Overall safety assessment |
| **Threat Score** | How dangerous (0-100%) |
| **Analysis Type** | How it was analyzed |
| **Timestamp** | When the scan happened |
| **Threat Type** | Specific threat category |

---

## 🎯 **Different Ways to Use**

### **Method 1: Web Interface (Easiest!)**
```
✅ Best for: Quick scans, beginners
✅ Access: http://localhost:8000/web
✅ Features: Beautiful UI, instant results
```

### **Method 2: Interactive API (Swagger)**
```
✅ Best for: Testing, exploring features
✅ Access: http://localhost:8000/docs
✅ Features: Try all endpoints, see examples
```

### **Method 3: Command Line (Advanced)**
```
✅ Best for: Automation, scripts
✅ Access: Terminal/Command Prompt
✅ Features: Integrate with other tools
```

### **Method 4: Python Code (Developers)**
```
✅ Best for: Building applications
✅ Access: Import the library
✅ Features: Full programmatic control
```

---

## 🔧 **Common Tasks**

### **Task 1: Check System Health**

**Web:**
```
Visit: http://localhost:8000/health
```

**Command Line:**
```bash
curl http://localhost:8000/health
```

**Expected Result:**
```json
{
  "status": "healthy",
  "timestamp": "2025-12-11T03:57:00Z"
}
```

### **Task 2: View Security Dashboard**

**Web:**
```
Visit: http://localhost:8000/dashboard
```

**What You'll See:**
```json
{
  "status": "running",
  "uptime": 3600,
  "threats_detected": 5,
  "policies_enforced": 12,
  "security_score": 85.5,
  "active_alerts": []
}
```

### **Task 3: Get Security Metrics**

**Web:**
```
Visit: http://localhost:8000/metrics
```

**What You'll See:**
```json
{
  "threats_detected": 5,
  "policies_enforced": 12,
  "incidents_responded": 3,
  "security_score": 85.5
}
```

---

## 🎨 **Visual Workflow**

```
┌─────────────┐
│   You       │
│  (Browser)  │
└──────┬──────┘
       │
       │ Enter IP/URL
       ↓
┌─────────────────────────────────────┐
│  Web Interface                      │
│  http://localhost:8000/web          │
└──────┬──────────────────────────────┘
       │
       │ Send to API
       ↓
┌─────────────────────────────────────┐
│  AI Security Platform               │
│  ├─ Threat Detection Engine         │
│  ├─ Zero-Trust Policy Engine        │
│  ├─ Quantum-Safe Crypto             │
│  └─ Automated Response              │
└──────┬──────────────────────────────┘
       │
       │ Analyze with AI
       ↓
┌─────────────────────────────────────┐
│  Results                            │
│  ✅ Status: Safe/Warning/Danger     │
│  📊 Threat Score: 0-100%            │
│  🤖 AI Analysis Details             │
└──────┬──────────────────────────────┘
       │
       │ Display
       ↓
┌─────────────┐
│   You       │
│  See Results│
└─────────────┘
```

---

## 💡 **Pro Tips**

### **Tip 1: Bookmark These URLs**
```
Main Interface:  http://localhost:8000/web
API Docs:        http://localhost:8000/docs
Dashboard:       http://localhost:8000/dashboard
Monitoring:      http://localhost:3000
```

### **Tip 2: Use Keyboard Shortcuts**
```
In web interface:
- Press Enter after typing → Auto-submit
- Ctrl+R → Refresh results
- Ctrl+L → Focus on input box
```

### **Tip 3: Batch Analysis**
```
Use the API to analyze multiple items:
1. Go to http://localhost:8000/docs
2. Use POST /threat/analyze
3. Send array of items
4. Get all results at once
```

### **Tip 4: Monitor in Real-Time**
```
Open Grafana: http://localhost:3000
Login: admin/admin
See live graphs of:
- Threats detected
- Response times
- System health
```

---

## 🆘 **Quick Troubleshooting**

### **Problem: Can't access web interface**

**Check:**
```bash
# Is Docker running?
docker ps

# Are services up?
docker-compose ps

# Check logs
docker-compose logs orchestrator
```

**Solution:**
```bash
# Restart everything
docker-compose restart

# Wait 30 seconds
# Try again
```

### **Problem: "Connection refused"**

**Reason:** Services still starting

**Solution:** Wait 30-60 seconds after running `docker-compose up -d`

### **Problem: Results not showing**

**Check:**
1. Is backend running? → `docker-compose ps`
2. Any errors in logs? → `docker-compose logs -f`
3. Using correct URL? → `http://` not `https://`

---

## 🎓 **Next Steps**

### **After Your First Scan:**

1. ✅ Try different IPs and URLs
2. ✅ Explore the API docs
3. ✅ Check out Grafana monitoring
4. ✅ Read the architecture docs
5. ✅ Try the Python examples

### **To Learn More:**

- 📖 [Quick Start Guide](QUICK_START.md)
- 🏗️ [Architecture Documentation](docs/ARCHITECTURE.md)
- 💻 [Installation Guide](INSTALLATION_GUIDE.md)
- 🤝 [Contributing Guide](CONTRIBUTING.md)

---

## 🎉 **You're Ready!**

You now know how to:
- ✅ Install the platform
- ✅ Access the web interface
- ✅ Analyze threats
- ✅ Read results
- ✅ Use the API
- ✅ Troubleshoot issues

**Start securing your systems now! 🛡️**

---

**Questions? Open an issue on GitHub!**

Made with ❤️ by the AI-ZTSO Team
