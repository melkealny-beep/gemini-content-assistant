
import pkg_resources

print("--- Library Version Check ---")

try:
    version = pkg_resources.get_distribution('langchain-google-genai').version
    print(f"langchain-google-genai version: {version}")
except pkg_resources.DistributionNotFound:
    print("langchain-google-genai is not installed or version not found.")

try:
    version = pkg_resources.get_distribution('google-generativeai').version
    print(f"google-generativeai version: {version}")
except pkg_resources.DistributionNotFound:
    print("google-generativeai is not installed or version not found.")

print("--- End of Check ---")
