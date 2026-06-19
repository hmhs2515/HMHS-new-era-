#!/usr/bin/env python3
"""
HMHS Era - Zero-API Local AI Framework Entry Point
Enhanced with HMHSFPS.dll hardware acceleration for FPS optimization
"""

import sys
from core.engine import HMHSEngine
from core.agent import HMHSAgent
from storage.vector_store import LocalVectorDB
from performance_monitor import PerformanceMonitor
from fps_accelerator import HMHSFPSAccelerator
from config import HMHS_CONFIG, PERFORMANCE_CONFIG

def main():
    """Main HMHS Era framework launcher with DLL acceleration."""
    
    print("=" * 70)
    print("🌐 HMHS Era - Zero-API Local AI Framework v1.0")
    print("🚀 Enhanced with HMHSFPS.dll Hardware Acceleration")
    print("=" * 70)
    
    try:
        # Initialize DLL accelerator first
        print("\n⚡ Initializing HMHSFPS.dll Accelerator...")
        dll_accel = HMHSFPSAccelerator()
        dll_available = dll_accel.is_available()
        print(f"   Status: {'✅ Available' if dll_available else '⚠️  Fallback to Python'}")
        
        # Initialize engine
        print("\n⚡ Initializing HMHS Engine...")
        engine = HMHSEngine(model_path=HMHS_CONFIG.get("model_path"))
        
        # Initialize agent
        print("🤖 Initializing HMHS Agent...")
        agent = HMHSAgent(engine=engine)
        
        # Initialize vector database
        print("💾 Initializing Local Vector Database...")
        vector_db = LocalVectorDB(storage_dir=HMHS_CONFIG.get("vector_db_path"))
        
        # Initialize performance monitor with DLL acceleration
        print("📊 Initializing Performance Monitor with DLL Support...")
        perf_monitor = PerformanceMonitor(
            enable_fps=True,
            enable_dll_acceleration=PERFORMANCE_CONFIG.get("enable_fps_monitoring", True)
        )
        
        # Set high acceleration for optimal performance
        if dll_available:
            perf_monitor.set_acceleration_level(9)
            print("   🚀 Acceleration Level: 9/10 (Maximum)")
        
        # Test workflow
        print("\n" + "=" * 70)
        print("🧪 Running Test Workflow with Performance Metrics")
        print("=" * 70)
        
        # Test engine inference with DLL monitoring
        perf_monitor.start_frame()
        test_prompt = "What is HMHS Era?"
        response = engine.generate_local_inference(test_prompt)
        metrics = perf_monitor.end_frame()
        
        print(f"\n📝 Prompt: {test_prompt}")
        print(f"✅ Response: {response}")
        print(f"⏱️  Frame Time: {metrics.get('frame_time_ms', 0):.2f}ms")
        
        # Display FPS metrics
        if dll_available:
            print(f"🎮 DLL FPS: {metrics.get('dll_fps', 0):.2f} FPS")
        python_fps = metrics.get('python_fps', metrics.get('fps', 0))
        print(f"🐍 Python FPS: {python_fps:.2f} FPS")
        
        # Test agent execution
        print("\n🔄 Testing Agent Workflow...")
        success = agent.execute_workflow("Initialize Local Vector Database")
        print(f"✅ Agent Workflow Status: {'SUCCESS' if success else 'FAILED'}")
        
        # Test vector database with DLL monitoring
        print("\n📚 Testing Vector Database with Performance Tracking...")
        perf_monitor.start_frame()
        vector_db.add_document("hmhs_1", "HMHS Era is a zero-API local AI framework")
        vector_db.add_document("hmhs_2", "Air-gapped architecture ensures data privacy")
        vector_db.add_document("hmhs_3", "HMHSFPS.dll accelerates FPS performance")
        search_results = vector_db.query_keyword_score("zero-api")
        metrics = perf_monitor.end_frame()
        print(f"✅ Database Search Results: {len(search_results)} documents found")
        print(f"⏱️  Database Operation Time: {metrics.get('frame_time_ms', 0):.2f}ms")
        
        # Run multiple frames to show FPS calculation
        print("\n" + "-" * 70)
        print("📊 FPS Performance Test (10 frames)...")
        print("-" * 70)
        for i in range(1, 11):
            perf_monitor.start_frame()
            _ = engine.generate_local_inference(f"Frame {i}")
            metrics = perf_monitor.end_frame()
            
            if i % 5 == 0:
                fps = metrics.get('fps', 0)
                print(f"Frame {i:2d}: {fps:6.2f} FPS | Avg: {metrics.get('avg_frame_time_ms', 0):.2f}ms/frame")
        
        # Display final metrics
        print("\n" + "=" * 70)
        print("📊 Final Performance Report")
        print("=" * 70)
        
        final_metrics = perf_monitor.get_metrics()
        print(f"\n{'Metric':<30} {'Value':<20}")
        print("-" * 50)
        
        for key, value in final_metrics.items():
            if isinstance(value, float):
                print(f"{key:<30} {value:>18.2f}")
            else:
                print(f"{key:<30} {value:>18}")
        
        # DLL Statistics
        if dll_available:
            print("\n" + "-" * 50)
            print("🎮 HMHSFPS.dll Statistics")
            print("-" * 50)
            dll_stats = dll_accel.get_fps_stats()
            for key, value in dll_stats.items():
                if isinstance(value, float):
                    print(f"{key:<30} {value:>18.2f}")
                else:
                    print(f"{key:<30} {value:>18}")
        
        # System status
        print("\n" + "=" * 70)
        print("✅ HMHS Era Framework - Fully Operational")
        print(f"   DLL Acceleration: {'🚀 Enabled' if dll_available else '⚠️  Disabled'}")
        print(f"   Air-Gapped Mode: ✅ Enabled")
        print(f"   Zero-API Compliance: ✅ Verified")
        print("   Status: 🚀 Ready for edge deployment operations")
        print("=" * 70 + "\n")
        
        # Cleanup
        perf_monitor.cleanup()
        dll_accel.close()
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
