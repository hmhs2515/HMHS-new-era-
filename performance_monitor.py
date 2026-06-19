# HMHS Era Performance Monitor Module
import time
from typing import Dict, Optional
from fps_accelerator import HMHSFPSAccelerator

class PerformanceMonitor:
    """Local performance monitoring with optional HMHSFPS.dll hardware acceleration."""
    
    def __init__(self, enable_fps: bool = True, enable_dll_acceleration: bool = True):
        self.enable_fps = enable_fps
        self.frame_count = 0
        self.start_time = time.time()
        self.metrics = {}
        
        # Initialize DLL accelerator
        self.fps_accelerator = None
        if enable_dll_acceleration:
            self.fps_accelerator = HMHSFPSAccelerator()
            if self.fps_accelerator.is_available():
                self.fps_accelerator.init_fps_monitor()
                self.fps_accelerator.set_acceleration_level(8)  # Default: high optimization
                print("🚀 HMHSFPS.dll acceleration enabled")
        
    def start_frame(self) -> None:
        """Mark the start of a processing frame."""
        self.frame_start = time.time()
    
    def end_frame(self) -> Dict[str, float]:
        """Mark the end of a processing frame and calculate metrics."""
        if not hasattr(self, 'frame_start'):
            return {}
        
        # Get DLL FPS if available
        dll_fps = 0.0
        if self.fps_accelerator and self.fps_accelerator.is_available():
            dll_fps = self.fps_accelerator.get_current_fps()
            metrics["dll_fps"] = dll_fps
        
        if self.enable_fps:
            elapsed = time.time() - self.start_time
            python_fps = self.frame_count / elapsed if elapsed > 0 else 0
            metrics["python_fps"] = python_fps
            metrics["fps"] = dll_fps if dll_fps > 0 else python_fps  # Prefer DLL FPS
        metrics = {
        set_acceleration_level(self, level: int) -> None:
        """Set DLL hardware acceleration level (0-10)."""
        if self.fps_accelerator and self.fps_accelerator.is_available():
            self.fps_accelerator.set_acceleration_level(level)
    
    def reset(self) -> None:
        """Reset monitoring data."""
        self.frame_count = 0
        self.start_time = time.time()
        self.metrics = {}
    
    def cleanup(self) -> None:
        """Cleanup resources including DLL."""
        if self.fps_accelerator:
            self.fps_accelerator.close()
        if self.enable_fps:
            elapsed = time.time() - self.start_time
            metrics["fps"] = self.frame_count / elapsed if elapsed > 0 else 0
            metrics["avg_frame_time_ms"] = (elapsed * 1000) / self.frame_count if self.frame_count > 0 else 0
        
        self.metrics = metrics
        return metrics
    
    def get_metrics(self) -> Dict[str, float]:
        """Get current performance metrics."""
        return self.metrics.copy()
    
    def reset(self) -> None:
        """Reset monitoring data."""
        self.frame_count = 0
        self.start_time = time.time()
        self.metrics = {}
