# HMHS Era - Quick Start Guide

## 📋 Prerequisites

- **Python**: 3.9 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: 4GB minimum (8GB+ recommended)
- **Storage**: 10GB for models + databases

## 🚀 Installation

### 1. Clone Repository
```bash
git clone https://github.com/hmhs2515/HMHS-new-era-.git
cd HMHS-new-era-
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# Standard installation
pip install -r requirements.txt

# With pre-built wheels (recommended for CPU)
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu

# Development installation
pip install -e ".[dev]"
```

## 📂 Project Structure

```
HMHS-new-era-/
├── core/
│   ├── engine.py          # HMHSEngine - inference core
│   ├── agent.py           # HMHSAgent - workflow orchestrator
│   └── __init__.py
├── storage/
│   ├── vector_store.py    # LocalVectorDB - persistent storage
│   └── __init__.py
├── tests/
│   ├── test_engine.py     # Comprehensive tests
│   └── __init__.py
├── .github/
│   └── workflows/
│       └── blank.yml      # CI/CD pipeline
├── config.py              # Framework configuration
├── performance_monitor.py # Metrics & monitoring
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── setup.py               # Package installation
├── ARCHITECTURE.md        # System design
├── QUICKSTART.md          # This file
├── README.md              # Project overview
└── .env.example           # Configuration template
```

## 🎯 Quick Start

### 1. Download a Model
Place a GGUF model in the `./models/` directory:
```bash
# Example: Download Mistral-7B-Instruct-v0.2.Q4_K_M.gguf
mkdir -p models
# Download your chosen model from Hugging Face or similar
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings
```

### 3. Run the Framework
```bash
# Using main.py
python main.py

# Or using installed command
hmhs-era

# Or import as library
from core.engine import HMHSEngine
engine = HMHSEngine(model_path="./models/your-model.gguf")
response = engine.generate_local_inference("What is HMHS Era?")
```

## 🧪 Run Tests
```bash
# Run all tests
pytest

# With coverage report
pytest --cov=. --cov-report=html

# Specific test
pytest tests/test_engine.py::test_engine_session_generation -v
```

## 🔍 Zero-API Compliance Check
```bash
# Manually verify no cloud API imports
grep -r "openai\|anthropic\|cohere\|google-generativeai" .

# Or run TruffleHog locally
pip install truffleHog
truffleHog filesystem . --json
```

## 📊 Performance Monitoring
```python
from performance_monitor import PerformanceMonitor

monitor = PerformanceMonitor(enable_fps=True)
monitor.start_frame()
# ... do processing ...
metrics = monitor.end_frame()
print(f"FPS: {metrics.get('fps', 0):.2f}")
print(f"Frame Time: {metrics.get('frame_time_ms', 0):.2f}ms")
```

## 🛠️ Development Workflow

### Code Style
```bash
# Format code with Black
black . --line-length 127

# Sort imports with isort
isort .

# Lint with flake8
flake8 . --max-line-length=127
```

### Type Checking
```bash
mypy core/ storage/ --ignore-missing-imports
```

## 🚀 Deployment

### Local Testing
```bash
python main.py
```

### Docker (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### GitHub Actions
- Push to `main` branch triggers CI/CD pipeline
- Automatic testing and Zero-API compliance checks
- TruffleHog scans for secrets/API keys

## 📖 Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system design and component documentation.

## 🔐 Security Features

✅ Air-gapped execution (no internet required)
✅ Local data processing (no cloud transmission)
✅ Zero API dependencies (no external calls)
✅ Hardware-isolated execution
✅ Automatic secret detection via TruffleHog
✅ Comprehensive audit trails

## 🆘 Troubleshooting

### Issue: "llama-cpp-python build fails"
**Solution**: Use pre-built wheels
```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```

### Issue: "Model file not found"
**Solution**: Ensure GGUF model is in `./models/` directory
```bash
ls -la models/
```

### Issue: "Low performance on inference"
**Solution**: Check hardware utilization and monitor performance
```bash
python -c "from performance_monitor import PerformanceMonitor; print('Monitor Ready')"
```

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

**HMHS Era**: Decentralized AI. Local-first. Always. 🚀
