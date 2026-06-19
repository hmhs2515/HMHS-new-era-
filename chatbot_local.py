"""
HMHS.AI Era - Chatbot Engine with Optional DLL Support
A recommended local-first chatbot implementation without API keys
"""

import json
import time
from typing import Dict, List, Optional, Any
from datetime import datetime


class HMHSChatbotConfig:
    """RECOMMENDED: Configuration for local chatbots without APIs"""
    
    def __init__(self):
        self.model_name = "local-model"
        self.personality = "helpful"
        self.max_context_messages = 10
        self.temperature = 0.7
        self.max_tokens = 512
        self.use_embedding = True
        self.use_semantic_search = True
        self.persistent_memory = True
        self.local_only = True  # CRITICAL: No external APIs


class HMHSLocalChatbot:
    """
    RECOMMENDED: Local chatbot engine for HMHS.AI Era
    
    Features:
    - ✅ Zero API dependency
    - ✅ Local context management
    - ✅ Persistent memory
    - ✅ Optional DLL enhancement
    - ✅ Privacy-first design
    """
    
    def __init__(self, config: Optional[HMHSChatbotConfig] = None):
        self.config = config or HMHSChatbotConfig()
        self.conversation_history = []
        self.context_buffer = []
        self.session_id = self._generate_session_id()
        self.personality_traits = self._load_personality()
        self.dll_accelerator = None
        
        # Try to load optional DLL (RECOMMENDED but not required)
        self._try_load_chatbot_dll()
        
        print(f"✅ HMHS Local Chatbot initialized")
        print(f"   Session: {self.session_id}")
        print(f"   Personality: {self.config.personality}")
        print(f"   DLL Support: {'🚀 Enabled' if self.dll_accelerator else '⚠️  Python-only'}")
    
    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        return f"hmhs_{int(time.time())}_{len(self.conversation_history)}"
    
    def _load_personality(self) -> Dict[str, Any]:
        """RECOMMENDED: Load personality traits locally"""
        personalities = {
            "helpful": {
                "tone": "professional",
                "formality": "medium",
                "emoji_level": "minimal",
            },
            "friendly": {
                "tone": "casual",
                "formality": "low",
                "emoji_level": "high",
            },
            "expert": {
                "tone": "technical",
                "formality": "high",
                "emoji_level": "none",
            },
        }
        return personalities.get(self.config.personality, personalities["helpful"])
    
    def _try_load_chatbot_dll(self):
        """RECOMMENDED: Optionally load chatbot DLL for enhancement"""
        try:
            from chatbot_dll_wrapper import HMHSChatbotDLLWrapper
            self.dll_accelerator = HMHSChatbotDLLWrapper()
            if self.dll_accelerator.is_available():
                print("   💫 DLL acceleration available")
            else:
                self.dll_accelerator = None
        except ImportError:
            print("   ℹ️  Chatbot DLL not available (this is OK)")
            self.dll_accelerator = None
    
    def process_user_input(self, user_message: str) -> Dict[str, Any]:
        """
        RECOMMENDED: Process user input without external APIs
        
        Steps:
        1. Validate input (LOCAL)
        2. Retrieve context (LOCAL)
        3. Generate response (LOCAL - using llama.cpp or DLL)
        4. Update memory (LOCAL)
        """
        
        # Step 1: Validate
        if not user_message or len(user_message.strip()) == 0:
            return self._create_error_response("Empty message")
        
        # Step 2: Add to history
        user_entry = {
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat(),
        }
        self.conversation_history.append(user_entry)
        
        # Step 3: Prepare context
        context = self._prepare_context()
        
        # Step 4: Generate response (LOCAL)
        response_text = self._generate_local_response(user_message, context)
        
        # Step 5: Add assistant response to history
        assistant_entry = {
            "role": "assistant",
            "content": response_text,
            "timestamp": datetime.now().isoformat(),
        }
        self.conversation_history.append(assistant_entry)
        
        # Step 6: Return response
        return {
            "status": "success",
            "response": response_text,
            "session_id": self.session_id,
            "message_count": len(self.conversation_history),
            "processing_method": "dll_accelerated" if self.dll_accelerator else "python_local",
        }
    
    def _prepare_context(self) -> str:
        """RECOMMENDED: Prepare context from local history"""
        recent_messages = self.conversation_history[-self.config.max_context_messages:]
        context_lines = []
        
        for msg in recent_messages:
            role = msg["role"].upper()
            content = msg["content"]
            context_lines.append(f"{role}: {content}")
        
        return "\n".join(context_lines)
    
    def _generate_local_response(self, user_input: str, context: str) -> str:
        """
        RECOMMENDED: Generate response using LOCAL resources only
        
        Options:
        1. Use DLL if available (faster)
        2. Fall back to Python implementation
        """
        
        # Prefer DLL if available
        if self.dll_accelerator and self.dll_accelerator.is_available():
            try:
                response = self.dll_accelerator.process_input(
                    user_input=user_input,
                    context=context,
                    personality=self.config.personality,
                )
                return response
            except Exception as e:
                print(f"⚠️  DLL processing failed: {str(e)}, falling back to Python")
        
        # Fall back to Python implementation
        return self._python_generate_response(user_input, context)
    
    def _python_generate_response(self, user_input: str, context: str) -> str:
        """RECOMMENDED: Pure Python response generation (no APIs)"""
        
        # This is a demonstration - in production, use llama.cpp or similar
        # to run local LLMs without external APIs
        
        # Local pattern matching (simple example)
        user_lower = user_input.lower()
        
        responses = {
            "hello": "Hello! How can I help you today?",
            "help": "I'm here to assist. What do you need help with?",
            "what is hmhs": "HMHS Era is a local-first AI framework designed for privacy and independence.",
            "how are you": "I'm functioning well! How can I assist you?",
        }
        
        for pattern, response in responses.items():
            if pattern in user_lower:
                return response
        
        # Generic response
        return f"I understand you said: '{user_input}'. I'm processing this locally without any external APIs."
    
    def _create_error_response(self, error: str) -> Dict[str, Any]:
        """Create error response"""
        return {
            "status": "error",
            "error": error,
            "session_id": self.session_id,
        }
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """RECOMMENDED: Retrieve full conversation (stored locally)"""
        return self.conversation_history.copy()
    
    def save_conversation(self, filepath: str) -> bool:
        """RECOMMENDED: Save conversation to local storage"""
        try:
            data = {
                "session_id": self.session_id,
                "personality": self.config.personality,
                "timestamp": datetime.now().isoformat(),
                "messages": self.conversation_history,
            }
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✅ Conversation saved to {filepath}")
            return True
        except Exception as e:
            print(f"❌ Error saving conversation: {str(e)}")
            return False
    
    def load_conversation(self, filepath: str) -> bool:
        """RECOMMENDED: Load previous conversation (local storage)"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            self.conversation_history = data.get("messages", [])
            self.session_id = data.get("session_id", self.session_id)
            print(f"✅ Conversation loaded from {filepath}")
            return True
        except Exception as e:
            print(f"❌ Error loading conversation: {str(e)}")
            return False
    
    def analyze_sentiment_local(self, text: str) -> float:
        """RECOMMENDED: Analyze sentiment locally (no API)"""
        
        # If DLL available, use it
        if self.dll_accelerator and self.dll_accelerator.is_available():
            return self.dll_accelerator.analyze_sentiment(text)
        
        # Python fallback - simple sentiment analysis
        positive_words = ["good", "great", "excellent", "happy", "love", "wonderful"]
        negative_words = ["bad", "terrible", "hate", "awful", "horrible", "sad"]
        
        text_lower = text.lower()
        score = 0.0
        
        for word in positive_words:
            score += text_lower.count(word) * 0.2
        
        for word in negative_words:
            score -= text_lower.count(word) * 0.2
        
        return max(-1.0, min(1.0, score))  # Clamp to [-1, 1]
    
    def get_session_stats(self) -> Dict[str, Any]:
        """RECOMMENDED: Get session statistics"""
        return {
            "session_id": self.session_id,
            "message_count": len(self.conversation_history),
            "user_messages": len([m for m in self.conversation_history if m["role"] == "user"]),
            "assistant_messages": len([m for m in self.conversation_history if m["role"] == "assistant"]),
            "processing_method": "dll_accelerated" if self.dll_accelerator else "python_local",
            "api_calls_made": 0,  # CRITICAL: Always 0 for local-only
        }


class HMHSChatbotApplication:
    """RECOMMENDED: Simple chatbot application shell"""
    
    def __init__(self):
        print("=" * 70)
        print("🌐 HMHS.AI Era - Local Chatbot Application")
        print("   (Recommended: No API Keys Required)")
        print("=" * 70)
        
        config = HMHSChatbotConfig()
        self.chatbot = HMHSLocalChatbot(config)
    
    def run_interactive(self):
        """Run interactive chatbot session"""
        print("\n💬 Chatbot ready. Type 'quit' to exit, 'save' to save conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() == "quit":
                    print("Goodbye!")
                    break
                
                if user_input.lower() == "save":
                    self.chatbot.save_conversation("conversation.json")
                    continue
                
                if not user_input:
                    continue
                
                # Process message
                result = self.chatbot.process_user_input(user_input)
                
                if result["status"] == "success":
                    print(f"\nBot: {result['response']}\n")
                else:
                    print(f"\nError: {result.get('error', 'Unknown error')}\n")
                
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
    
    def print_stats(self):
        """Print session statistics"""
        stats = self.chatbot.get_session_stats()
        print("\n" + "=" * 70)
        print("📊 Session Statistics")
        print("=" * 70)
        for key, value in stats.items():
            print(f"{key:<25}: {value}")


if __name__ == "__main__":
    # Recommended usage
    app = HMHSChatbotApplication()
    app.run_interactive()
    app.print_stats()
