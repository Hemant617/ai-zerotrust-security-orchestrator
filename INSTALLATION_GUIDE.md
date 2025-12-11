# 📹 Complete Installation & Usage Guide

## 🎯 What You'll Learn

This guide will show you **exactly** how to install and use the AI Zero-Trust Security Orchestrator - step by step, with screenshots and examples.

---

## 📋 **Step 0: Prerequisites (5 minutes)**

### What You Need:
1. **A Computer** (Windows, Mac, or Linux)
2. **Docker Desktop** - Download from: https://www.docker.com/products/docker-desktop
3. **Git** - Download from: https://git-scm.com/downloads

### Installing Docker Desktop:

**Windows:**
1. Download Docker Desktop from the link above
2. Run the installer
3. Follow the installation wizard
4. Restart your computer
5. Open Docker Desktop - you'll see a whale icon in your taskbar

**Mac:**
1. Download Docker Desktop for Mac
2. Drag Docker to Applications folder
3. Open Docker from Applications
4. Grant permissions when asked
5. Wait for Docker to start (whale icon in menu bar)

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker.io docker-compose

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker
```

### Verify Docker is Working:

Open Terminal (Mac/Linux) or Command Prompt (Windows) and type:

```bash
docker --version
```

You should see something like: `Docker version 24.0.0`

---

## 🚀 **Step 1: Download the Project (2 minutes)**

### Option A: Using Git (Recommended)

Open your terminal and run:

```bash
# Navigate to where you want to save the project
cd Desktop  # or any folder you prefer

# Clone the repository
git clone https://github.com/Hemant617/ai-zerotrust-security-orchestrator.git

# Enter the project folder
cd ai-zerotrust-security-orchestrator
```

### Option B: Download ZIP

1. Go to: https://github.com/Hemant617/ai-zerotrust-security-orchestrator
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file
5. Open terminal in that folder

---

## ⚡ **Step 2: Install & Start (3 minutes)**

### Automatic Installation (Easiest!)

**For Windows:**
```bash
# Just double-click install.bat
# OR run in Command Prompt:
install.bat
```

**For Mac/Linux:**
```bash
# Make the script executable
chmod +x install.sh

# Run the installer
./install.sh
```

The installer will:
- ✅ Check if Docker is running
- ✅ Download all required components (this takes 2-3 minutes)
- ✅ Start all services
- ✅ Show you the access URLs

### Manual Installation (If automatic doesn't work)

```bash
# Start all services
docker-compose up -d

# Wait 30 seconds for everything to start
# You can check status with:
docker-compose ps
```

---

## 🌐 **Step 3: Access the Platform (1 minute)**

Once installation is complete, open your web browser and visit:

### **Main Web Interface (Like VirusTotal!)**
```
http://localhost:8000/web
```

This is your main interface - beautiful, simple, and powerful!

### **Other Access Points:**

| URL | What It Does |
|-----|--------------|
| http://localhost:8000/docs | Interactive API testing (Swagger UI) |
| http://localhost:8000/dashboard | JSON security dashboard |
| http://localhost:3000 | Grafana monitoring (login: admin/admin) |

---

## 🎮 **Step 4: Using the Platform**

### **Example 1: Analyze a Threat (Web Interface)**

1. Open http://localhost:8000/web
2. You'll see a beautiful interface with an input box
3. Enter one of these examples:
   - IP Address: `192.168.1.100`
   - URL: `https://example.com`
   - Hash: `5d41402abc4b2a76b9719d911017c592`
4. Click the **"🔍 Analyze"** button
5. Wait 1-2 seconds
6. See the AI-powered analysis results!

**What You'll See:**
- ✅ Threat Status (Safe/Warning/Danger)
- 📊 Threat Score (0-100%)
- 🤖 Analysis Type (AI Behavioral Analysis)
- ⏰ Timestamp
- 📋 Additional details

### **Example 2: Using the Interactive API**

1. Go to http://localhost:8000/docs
2. You'll see a list of all available endpoints
3. Click on **`POST /threat/analyze`**
4. Click the **"Try it out"** button
5. You'll see a text box with example JSON
6. Replace it with:

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

7. Click **"Execute"**
8. Scroll down to see the response!

### **Example 3: Check Security Dashboard**

1. Go to http://localhost:8000/dashboard
2. You'll see JSON data with:
   - Current status
   - Uptime
   - Threats detected
   - Policies enforced
   - Security score
   - Active alerts

### **Example 4: Verify User Identity (Zero-Trust)**

1. Go to http://localhost:8000/docs
2. Find **`POST /zerotrust/verify`**
3. Click "Try it out"
4. Enter:

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

5. Click "Execute"
6. See the trust score and verification result!

### **Example 5: Encrypt Data (Quantum-Safe)**

1. Go to http://localhost:8000/docs
2. Find **`POST /crypto/encrypt`**
3. Click "Try it out"
4. Enter:

```json
{
  "data": "My super secret message",
  "algorithm": "CRYSTALS-Kyber"
}
```

5. Click "Execute"
6. Your data is now encrypted with quantum-resistant cryptography!

---

## 📊 **Step 5: Monitoring (Optional)**

### **Grafana Dashboard**

1. Open http://localhost:3000
2. Login with:
   - Username: `admin`
   - Password: `admin`
3. You'll see beautiful graphs and metrics
4. Explore the dashboards!

---

## 🛠️ **Common Commands**

### **Check if Everything is Running**
```bash
docker-compose ps
```

You should see all services with "Up" status.

### **View Logs (Troubleshooting)**
```bash
# View all logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f orchestrator
```

### **Stop the Platform**
```bash
docker-compose down
```

### **Restart the Platform**
```bash
docker-compose restart
```

### **Start Fresh (Clean Install)**
```bash
# Stop and remove everything
docker-compose down -v

# Start again
docker-compose up -d
```

---

## 🆘 **Troubleshooting**

### **Problem: "Cannot connect to Docker daemon"**

**Solution:**
1. Make sure Docker Desktop is running
2. Look for the whale icon in your taskbar/menu bar
3. If not running, open Docker Desktop
4. Wait for it to fully start (icon stops animating)
5. Try again

### **Problem: "Port 8000 is already in use"**

**Solution:**
1. Stop any other services using port 8000
2. OR edit `docker-compose.yml`:
   - Find `ports: - "8000:8000"`
   - Change to `ports: - "8080:8000"`
   - Now use http://localhost:8080 instead

### **Problem: "Services not starting"**

**Solution:**
```bash
# Stop everything
docker-compose down

# Remove old containers
docker-compose rm -f

# Pull fresh images
docker-compose pull

# Start again
docker-compose up -d

# Wait 30 seconds
# Check logs
docker-compose logs -f
```

### **Problem: "Web interface shows connection error"**

**Solution:**
1. Wait 30-60 seconds after starting (services need time to initialize)
2. Check if backend is running: `docker-compose ps`
3. Check logs: `docker-compose logs orchestrator`
4. Make sure you're using `http://` not `https://`

### **Problem: "Docker Desktop won't start"**

**Solution:**
1. Restart your computer
2. Make sure virtualization is enabled in BIOS
3. On Windows: Enable WSL 2
4. Reinstall Docker Desktop if needed

---

## 🎓 **Learning Path**

### **Beginner (Day 1)**
1. ✅ Install the platform
2. ✅ Open the web interface
3. ✅ Try analyzing a few IPs/URLs
4. ✅ Explore the API docs

### **Intermediate (Week 1)**
1. 📖 Read the [Quick Start Guide](QUICK_START.md)
2. 💻 Try the Python examples in `examples/basic_usage.py`
3. 🔧 Customize the configuration in `.env`
4. 📊 Set up Grafana dashboards

### **Advanced (Month 1)**
1. 🏗️ Read the [Architecture Documentation](docs/ARCHITECTURE.md)
2. 🤖 Train custom ML models
3. 🔌 Integrate with your existing security tools
4. 🚀 Deploy to production

---

## 📚 **Additional Resources**

### **Documentation**
- [Quick Start Guide](QUICK_START.md) - 5-minute setup
- [Architecture Guide](docs/ARCHITECTURE.md) - Deep technical dive
- [Contributing Guide](CONTRIBUTING.md) - How to contribute

### **Code Examples**
- `examples/basic_usage.py` - Python usage examples
- `tests/` - Unit tests showing how to use each component

### **Configuration**
- `.env.example` - All configuration options
- `docker-compose.yml` - Service configuration
- `config/prometheus.yml` - Monitoring configuration

---

## 🎉 **You're All Set!**

Congratulations! You now have a **revolutionary AI-powered cybersecurity platform** running on your computer!

### **What to Do Next:**

1. ⭐ **Star the repository** on GitHub
2. 🔍 **Explore the web interface** at http://localhost:8000/web
3. 📖 **Read the documentation** to learn more
4. 🤝 **Join the community** and share your experience
5. 🚀 **Start securing** your systems!

---

## 💡 **Pro Tips**

1. **Bookmark these URLs** for quick access:
   - http://localhost:8000/web (Main interface)
   - http://localhost:8000/docs (API docs)
   - http://localhost:3000 (Grafana)

2. **Keep Docker Desktop running** in the background

3. **Check logs regularly** to understand what's happening:
   ```bash
   docker-compose logs -f
   ```

4. **Experiment safely** - you can always restart fresh:
   ```bash
   docker-compose down -v && docker-compose up -d
   ```

5. **Read the examples** in the `examples/` folder

---

## 🆘 **Still Need Help?**

1. **Check the logs**: `docker-compose logs -f`
2. **Search GitHub Issues**: https://github.com/Hemant617/ai-zerotrust-security-orchestrator/issues
3. **Open a new issue**: Describe your problem with screenshots
4. **Join our Discord**: Get help from the community

---

**Happy Securing! 🛡️**

Made with ❤️ by the AI-ZTSO Team
