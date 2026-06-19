"""
HMHS.AI Era - Chatbot DLL Wrapper (Optional Enhancement)
Recommended but not required for local chatbot applications
"""

import os
import ctypes
from typing import Optional


class HMHSChatbotDLLWrapper:
    """
    RECOMMENDED: Optional wrapper for chatbot DLL enhancement
    
    Benefits (if using DLL):
    - ✅ Faster response generation
    - ✅ Advanced local NLP
    - ✅ Optimized embeddings
    - ✅ Better context management
    
    Note: Application works fine without DLL using pure Python
    """
    
    def __init__(self, dll_path: Optional[str] = None):
        self.dll_path = dll_path or self._find_dll()
        self.dll_loaded = False
        self.dll_instance = None
        
        if self.dll_path and os.path.exists(self.dll_path):
            self._load_dll()
    
    def _find_dll(self) -> Optional[str]:
        """Find chatbot DLL in standard locations"""
        search_paths = [
            "./HMHS_ChatBot.dll",
            "./bin/HMHS_ChatBot.dll",
            "./dlls/HMHS_ChatBot.dll",
        ]
        
        for path in search_paths:
            if os.path.exists(path):
                return os.path.abspath(path)
        
        return None
    
    def _load_dll(self) -> bool:
        """Load chatbot DLL safely"""
        try:
            if os.name == 'nt':  # Windows only
                self.dll_instance = ctypes.CDLL(self.dll_path)
                self._init_functions()
                self.dll_loaded = True
                print(f"✅ Chatbot DLL loaded: {self.dll_path}")
                return True
        except Exception as e:
            print(f"⚠️  Could not load chatbot DLL: {str(e)}")
            print("   Continuing with Python-only mode (recommended)")
            return False
    
    def _init_functions(self):
        """Initialize DLL function signatures"""
        if not self.dll_instance:
            return
        
        try:
            # Initialize
            self.dll_instance.HMHS_Chat_Initialize.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            self.dll_instance.HMHS_Chat_Initialize.restype = ctypes.c_int
            
            # Process input
            self.dll_instance.HMHS_Chat_Process.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            self.dll_instance.HMHS_Chat_Process.restype = ctypes.c_char_p
            
            # Get context
            self.dll_instance.HMHS_Chat_GetContext.argtypes = [ctypes.c_char_p]
            self.dll_instance.HMHS_Chat_GetContext.restype = ctypes.c_char_p
            
            # Sentiment analysis
            self.dll_instance.HMHS_Chat_Sentiment_Analyze.argtypes = [ctypes.c_char_p]
            self.dll_instance.HMHS_Chat_Sentiment_Analyze.restype = ctypes.c_float
            
            # Cleanup
            self.dll_instance.HMHS_Chat_Cleanup.argtypes = []
            self.dll_instance.HMHS_Chat_Cleanup.restype = ctypes.c_int
            
            print("   📊 DLL functions initialized")
        except AttributeError as e:
            print(f"   ⚠️  Function signature mismatch: {str(e)}")
            self.dll_loaded = False
    
    def process_input(self, user_input: str, context: str, personality: str = "helpful") -> str:
        """RECOMMENDED: Process input using DLL (faster)"""
        if not self.is_available():
            return None
        
        try:
            user_bytes = user_input.encode('utf-8')
            context_bytes = context.encode('utf-8')
            
            result = self.dll_instance.HMHS_Chat_Process(user_bytes, context_bytes)
            return result.decode('utf-8') if result else None
        except Exception as e:
            print(f"❌ DLL processing error: {str(e)}")
            return None
    
    def analyze_sentiment(self, text: str) -> float:
        """RECOMMENDED: Analyze sentiment using DLL"""
        if not self.is_available():
            return 0.0
        
        try:
            text_bytes = text.encode('utf-8')
            return self.dll_instance.HMHS_Chat_Sentiment_Analyze(text_bytes)
        except Exception as e:
            print(f"❌ DLL sentiment analysis error: {str(e)}")
            return 0.0
    
    def is_available(self) -> bool:
        """Check if DLL is available"""
        return self.dll_loaded and self.dll_instance is not None
    
    def cleanup(self):
        """Cleanup DLL resources"""
        if self.is_available():
            try:
                self.dll_instance.HMHS_Chat_Cleanup()
                print("✅ Chatbot DLL cleaned up")
            except Exception as e:
                print(f"⚠️  Error during DLL cleanup: {str(e)}")
