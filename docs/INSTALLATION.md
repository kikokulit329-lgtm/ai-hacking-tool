# Installation Guide

## System Requirements

- **OS**: Linux, macOS, or Windows
- **Python**: 3.8 or higher
- **Memory**: Minimum 4GB RAM (8GB+ recommended)
- **Network**: Internet connection for dependency installation

## Prerequisites

Before installation, ensure you have:

```bash
# Check Python version
python --version  # Should be 3.8+

# Check pip is installed
pip --version
```

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/kikokulit329-lgtm/ai-hacking-tool.git
cd ai-hacking-tool
```

### 2. Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Upgrade pip

```bash
pip install --upgrade pip setuptools wheel
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install the Package

```bash
pip install -e .
```

## Verification

Test the installation:

```bash
python -c "import ai_hacking_tool; print('Installation successful!')"
```

## Platform-Specific Setup

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install python3-dev libssl-dev libffi-dev
```

### macOS

```bash
brew install python3
brew install openssl
```

### Windows

Download and install:
- Python 3.8+ from python.org
- Visual C++ Build Tools
- OpenSSL (if not included)

## Docker Installation (Optional)

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

ENTRYPOINT ["python", "-m", "src.cli"]
```

Build and run:
```bash
docker build -t ai-hacking-tool .
docker run -it ai-hacking-tool scan 192.168.1.0/24
```

## Troubleshooting

### Issue: `pip install` fails
**Solution**: Update pip and try again
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: Module not found errors
**Solution**: Ensure virtual environment is activated
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

### Issue: Permission denied (Linux/macOS)
**Solution**: Use `sudo` or fix ownership
```bash
sudo chown -R $USER:$USER .
```

## Optional Dependencies

For advanced features:

```bash
# For GPU acceleration (TensorFlow)
pip install tensorflow-gpu

# For advanced reporting
pip install reportlab openpyxl

# For Shodan integration
pip install shodan
```

## Configuration

Edit `config/settings.yaml` to customize settings:

```yaml
reconnaissance:
  network_scan_timeout: 2
  max_threads: 20

ai_engine:
  threat_detection_threshold: 0.7
  anomaly_sensitivity: 2.0

logging:
  level: "INFO"
  file: "logs/aihack.log"
```

## Next Steps

After installation:
1. Read the [USER_GUIDE.md](USER_GUIDE.md)
2. Check [examples/](examples/) for sample scripts
3. Review [API_REFERENCE.md](API_REFERENCE.md)

## Support

For issues:
- Check documentation in `/docs`
- Open a GitHub issue
- Review example scripts

---
**Last Updated**: 2026-09-09
