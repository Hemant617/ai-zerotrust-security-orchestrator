@echo off
REM AI Zero-Trust Security Orchestrator - One-Click Installer for Windows
REM This script will install and start everything automatically

echo ================================================================
echo    AI Zero-Trust Security Orchestrator - Installer
echo    Revolutionary Cybersecurity Platform
echo ================================================================
echo.

REM Check if Docker is installed
echo Checking prerequisites...
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed!
    echo.
    echo Please install Docker Desktop from:
    echo https://www.docker.com/products/docker-desktop
    echo.
    pause
    exit /b 1
)

docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker Compose is not installed!
    echo.
    echo Please install Docker Compose from:
    echo https://docs.docker.com/compose/install/
    echo.
    pause
    exit /b 1
)

echo [OK] Docker is installed
echo [OK] Docker Compose is installed
echo.

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not running!
    echo.
    echo Please start Docker Desktop and try again.
    echo.
    pause
    exit /b 1
)

echo [OK] Docker is running
echo.

REM Stop any existing containers
echo Stopping any existing containers...
docker-compose down 2>nul

REM Pull latest images
echo.
echo Pulling required Docker images (this may take a few minutes)...
docker-compose pull

REM Start services
echo.
echo Starting AI Zero-Trust Security Orchestrator...
docker-compose up -d

REM Wait for services to be ready
echo.
echo Waiting for services to start (30 seconds)...
timeout /t 30 /nobreak >nul

REM Check if services are running
echo.
echo Checking service status...
docker-compose ps | findstr "Up" >nul
if errorlevel 1 (
    echo [ERROR] Some services failed to start
    echo.
    echo Check logs with: docker-compose logs
    pause
    exit /b 1
)

echo [OK] Services are running!

REM Display success message
echo.
echo ================================================================
echo               Installation Successful!
echo ================================================================
echo.
echo Your AI Zero-Trust Security Orchestrator is now running!
echo.
echo Access Points:
echo ----------------------------------------------------------------
echo.
echo   Web Interface (VirusTotal-like):
echo   http://localhost:8000/web
echo.
echo   Interactive API Documentation:
echo   http://localhost:8000/docs
echo.
echo   Security Dashboard:
echo   http://localhost:8000/dashboard
echo.
echo   Grafana Monitoring:
echo   http://localhost:3000
echo   (Login: admin / admin)
echo.
echo ----------------------------------------------------------------
echo.
echo Quick Start:
echo   1. Open http://localhost:8000/web in your browser
echo   2. Enter an IP address or URL to analyze
echo   3. Click 'Analyze' to see AI-powered threat detection!
echo.
echo Useful Commands:
echo   View logs:     docker-compose logs -f
echo   Stop services: docker-compose down
echo   Restart:       docker-compose restart
echo   Status:        docker-compose ps
echo.
echo Need Help?
echo   GitHub: https://github.com/Hemant617/ai-zerotrust-security-orchestrator
echo.
echo Happy Securing!
echo.
pause
