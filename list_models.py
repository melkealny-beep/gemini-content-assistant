

import google.generativeai as genai
import os
import sys

# --- Get API Key from Environment Variable ---
try:
    api_key = os.environ["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    print("🚨 Error: GOOGLE_API_KEY environment variable not set.", file=sys.stderr)
    print("Please set your API key to run this script.", file=sys.stderr)
    exit(1)

print("🔎 Finding available models that support content generation...")
print("-" * 30)

found_model = False
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(f"✅ {m.name}")
    found_model = True

if not found_model:
    print("❌ No models found that support content generation with your current setup.")

print("-" * 30)
