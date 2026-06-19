"""
HMHS FPS Accelerator - DLL Integration Module
Integrates HMHSFPS.dll for optimized performance monitoring and FPS enhancement
"""

import os
import ctypes
import sys
from typing import Optional, Dict, Any
from pathlib import Path

class HMHSFPSAccelerator:
    """
    Wrapper for HMHSFPS.dll - Advanced FPS optimization and performance acceleration
    Provides hardware-level FPS monitoring and enhancement capabilities
    """
    
    def __init__(self, dll_path: Optional[str] = None):
        self.dll_path = dll_path or self._find_dll()
        self.dll_loaded = False
        self.dll_instance = None
        self.fps_data = {
            "current_fps": 0.0,
            "avg_fps": 0.0,
            "min_fps": 0.0,
            "max_fps": 0.0,
            "frame_count": 0,
            "acceleration_level": 0,
        }
        
        self._load_dll()
    
    def _find_dll(self) -> Optional[str]:
        """Locate HMHSFPS.dll in standard search paths"""
        search_paths = [
            "./HMHSFPS.dll",
            "./bin/HMHSFPS.dll",
            os.path.join(os.path.dirname(__file__), "HMHSFPS.dll"),
            os.path.join(os.path.dirname(__file__), "bin", "HMHSFPS.dll"),
        ]
        
        for path in search_paths:
            if os.path.exists(path):
                return os.path.abspath(path)
        
        return None
    
    def _load_dll(self) -> bool:
        """Safely load HMHSFPS.dll with error handling"""
        if not self.dll_path or not os.path.exists(self.dll_path):
            print(f"⚠️  HMHSFPS.dll not found at {self.dll_path}")
            print("💡 Tip: Place HMHSFPS.dll in project root or ./bin/ folder")
            return False
        
        try:
            if sys.platform == "win32":
                self.dll_instance = ctypes.CDLL(self.dll_path)
                self.dll_loaded = True
                print(f"✅ HMHSFPS.dll loaded successfully from: {self.dll_path}")
                
                # Initialize DLL functions
                self._init_dll_functions()
                return True
            else:
                print("⚠️  HMHSFPS.dll is Windows-only. Falling back to pure Python performance monitoring.")
                return False
                
        except Exception as e:
            print(f"❌ Failed to load HMHSFPS.dll: {str(e)}")
            print("💡 Continuing with standard performance monitoring...")
            return False
    
    def _init_dll_functions(self):
        """Initialize DLL function signatures"""
        if not self.dll_loaded or not self.dll_instance:
            return
        
        try:
            # Define function signatures (adjust based on your HMHSFPS.dll API)
            self.dll_instance.HMHS_InitFPS.argtypes = []
            self.dll_instance.HMHS_InitFPS.restype = ctypes.c_int
            
            self.dll_instance.HMHS_GetFPS.argtypes = []
            self.dll_instance.HMHS_GetFPS.restype = ctypes.c_float
            
            self.dll_instance.HMHS_SetAcceleration.argtypes = [ctypes.c_int]
            self.dll_instance.HMHS_SetAcceleration.restype = ctypes.c_int
            
            print("📊 HMHSFPS.dll functions initialized")
        except AttributeError as e:
            print(f"⚠️  DLL function signature mismatch: {str(e)}")
            self.dll_loaded = False
    
    def init_fps_monitor(self) -> bool:
        """Initialize FPS monitoring in DLL"""
        if not self.dll_loaded:
            return False
        
        try:
            result = self.dll_instance.HMHS_InitFPS()
            return result == 0
        except Exception as e:
            print(f"❌ Error initializing DLL FPS monitor: {str(e)}")
            return False
    
    def get_current_fps(self) -> float:
        """Get current FPS from DLL or fallback"""
        if not self.dll_loaded:
            return 0.0
        
        try:
            fps = self.dll_instance.HMHS_GetFPS()
            self.fps_data["current_fps"] = float(fps)
            return float(fps)
        except Exception as e:
            print(f"⚠️  Error reading DLL FPS: {str(e)}")
            return 0.0
    
    def set_acceleration_level(self, level: int) -> bool:
        """
        Set hardware acceleration level (0-10)
        0 = no acceleration, 10 = maximum optimization
        """
        if not self.dll_loaded:
            return False
        
        level = max(0, min(10, level))  # Clamp between 0-10
        
        try:
            result = self.dll_instance.HMHS_SetAcceleration(level)
            self.fps_data["acceleration_level"] = level
            return result == 0
        except Exception as e:
            print(f"❌ Error setting acceleration level: {str(e)}")
            return False
    
    def get_fps_stats(self) -> Dict[str, Any]:
        """Get comprehensive FPS statistics"""
        return self.fps_data.copy()
    
    def is_available(self) -> bool:
        """Check if DLL is loaded and ready"""
        return self.dll_loaded
    
    def close(self):
        """Cleanup DLL resources"""
        if self.dll_instance:
            try:
                if hasattr(self.dll_instance, "HMHS_Cleanup"):
                    self.dll_instance.HMHS_Cleanup()
                print("✅ HMHSFPS.dll cleaned up")
            except Exception as e:
                print(f"⚠️  Error during DLL cleanup: {str(e)}")
