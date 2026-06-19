# HMHS Era Configuration Module
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "models"
DB_DATA_DIR = BASE_DIR / "db_data"
LOGS_DIR = BASE_DIR / "logs"

# Create directories if they don't exist
MODELS_DIR.mkdir(exist_ok=True)
DB_DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# HMHS Engine Configuration
HMHS_CONFIG = {
    "model_path": os.getenv("HMHS_MODEL_PATH", str(MODELS_DIR)),
    "enable_gpu": os.getenv("HMHS_GPU", "false").lower() == "true",
    "max_tokens": int(os.getenv("HMHS_MAX_TOKENS", 512)),
    "temperature": float(os.getenv("HMHS_TEMPERATURE", 0.7)),
    "vector_db_path": str(DB_DATA_DIR),
    "verbose": os.getenv("HMHS_VERBOSE", "false").lower() == "true",
}

# Logging configuration
LOG_CONFIG = {
    "level": os.getenv("LOG_LEVEL", "INFO"),
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": str(LOGS_DIR / "hmhs_era.log"),
}

# Performance monitoring
PERFORMANCE_CONFIG = {
    "enable_fps_monitoring": os.getenv("HMHS_FPS_MONITOR", "true").lower() == "true",
    "fps_interval": int(os.getenv("HMHS_FPS_INTERVAL", 1000)),  # milliseconds
    "enable_dll_acceleration": os.getenv("HMHS_DLL_ACCELERATION", "true").lower() == "true",
    "dll_acceleration_level": int(os.getenv("HMHS_ACCELERATION_LEVEL", 8)),  # 0-10
    "dll_path": os.getenv("HMHS_DLL_PATH", "./HMHSFPS.dll"),
}

# Security & Privacy
SECURITY_CONFIG = {
    "air_gapped_mode": True,
    "no_api_calls": True,
    "data_privacy": "strict",
    "hardware_isolation": True,
}

# HMHSFPS.dll Configuration
DLL_CONFIG = {
    "enabled": PERFORMANCE_CONFIG.get("enable_dll_acceleration"),
    "path": PERFORMANCE_CONFIG.get("dll_path"),
    "default_acceleration_level": PERFORMANCE_CONFIG.get("dll_acceleration_level"),
    "fallback_to_python": True,  # Use Python monitoring if DLL fails
}
