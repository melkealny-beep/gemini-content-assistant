import google.generativeai as genai
import os

# --- Security Best Practice: Get API Key from Environment Variable ---
# IMPORTANT: Set your GOOGLE_API_KEY environment variable before running this script.
# For example, in your terminal: export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
try:
    api_key = os.environ["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    print("🚨 Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set your API key to run this script.")
    exit()

def generate_post_idea():
    """Generates a new post idea using the Gemini API."""
    model = genai.GenerativeModel('gemini-flash-latest')
    # More specific prompt for a public figure page
    prompt = """
    أنا شخصية عامة صفحتي على فيسبوك هي عن محمد الكيلاني.
    أريد فكرة بوست جديدة ومبتكرة تزيد من تفاعل المتابعين.
    اقترح فكرة واحدة فقط، مع وصف مختصر لكيفية تنفيذها (مثلاً: صورة معينة، سؤال للجمهور، الخ).
    """
    print("\n🤖 جارٍ التفكير في فكرة بوست...")
    response = model.generate_content(prompt)
    print("✨ فكرة مقترحة:")
    print(response.text)
    print("-" * 20)

def generate_caption_for_image():
    """Generates a caption for an image."""
    print("\n🖼️ هذه الميزة قيد التطوير وسيتم إضافتها قريباً.")
    print("سوف نستخدم الصور الموجودة في المشروع: baked_goods_1.jpg, baked_goods_2.jpg, baked_goods_3.jpg")
    print("-" * 20)
    # Placeholder for future implementation using a multimodal model
    # model = genai.GenerativeModel('gemini-pro-vision')
    # ... code to select image and generate caption ...


def main():
    """The main function to run the content assistant."""
    while True:
        print("\n--- مساعد المحتوى - القائمة الرئيسية ---")
        print("مرحباً بك في مساعد المحتوى الخاص بك!")
        print("ماذا تريد أن تفعل اليوم؟")
        print("1. اقتراح فكرة بوست جديدة")
        print("2. كتابة تعليق (caption) لصورة (قيد التطوير)")
        print("3. الخروج")

        choice = input("ادخل اختيارك (1, 2, or 3): ")

        if choice == '1':
            generate_post_idea()
        elif choice == '2':
            generate_caption_for_image()
        elif choice == '3':
            print("👋 مع السلامة!")
            break
        else:
            print("❌ اختيار خاطئ. من فضلك اختر 1, 2, أو 3.")

if __name__ == "__main__":
    main()