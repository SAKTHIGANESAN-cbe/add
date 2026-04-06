#!/usr/bin/env python
"""
OpenAI API Key Verification Script
Run this to verify your setup is correct
"""

import os
import sys

print("=" * 60)
print("🔍 OpenAI API Key Configuration Checker")
print("=" * 60)

# Check 1: dotenv installed
print("\n✓ Checking python-dotenv installation...")
try:
    from dotenv import load_dotenv
    print("  ✅ python-dotenv is installed")
except ImportError:
    print("  ❌ python-dotenv not installed")
    print("  Install with: pip install python-dotenv")
    sys.exit(1)

# Check 2: Load .env file
print("\n✓ Loading .env file...")
load_dotenv()

env_exists = os.path.exists(".env")
print(f"  .env file exists: {'✅ Yes' if env_exists else '❌ No'}")

if not env_exists:
    print("\n  ⚠️  .env file not found!")
    print("  Please create .env file with your OpenAI API key")

# Check 3: Check if API key is set
print("\n✓ Checking OPENAI_API_KEY...")
api_key = os.getenv('OPENAI_API_KEY', '')

if api_key:
    print(f"  ✅ API Key Found: {api_key[:15]}...{api_key[-5:]}")
    print(f"  Full length: {len(api_key)} characters")
else:
    print("  ❌ OPENAI_API_KEY not set")
    print("\n  📝 Add to .env file:")
    print("     OPENAI_API_KEY=sk-your-key-here")

# Check 4: openai module installed
print("\n✓ Checking openai module...")
try:
    import openai
    print(f"  ✅ openai module installed (version: {openai.__version__ if hasattr(openai, '__version__') else 'unknown'})")
except ImportError:
    print("  ❌ openai module not installed")
    print("  Install with: pip install openai")
    sys.exit(1)

# Check 5: Test API key validity (basic check)
if api_key and api_key.startswith('sk-'):
    print(f"\n  ✅ API Key format looks correct (starts with 'sk-')")
else:
    print(f"\n  ⚠️  API Key format warning:")
    print(f"     - Should start with 'sk-'")
    print(f"     - Current: {api_key[:20] if api_key else 'NOT SET'}...")

# Summary
print("\n" + "=" * 60)
print("📋 Summary:")
print("=" * 60)

all_good = env_exists and api_key and api_key.startswith('sk-')

if all_good:
    print("✅ All checks passed! Your setup is ready.")
    print("\nNext steps:")
    print("  1. Restart Flask: python app.py")
    print("  2. Go to http://127.0.0.1:5000")
    print("  3. Login with: demo_user / password123")
    print("  4. Test chatbot: Click 'Chat with AI Assistant'")
else:
    print("❌ Some checks failed. Please fix the issues above.")

print("=" * 60)
