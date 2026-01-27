
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- Security Best Practice: Get API Key from .env file ---
load_dotenv()

# Check if the API key is available
if "GOOGLE_API_KEY" not in os.environ:
    print("🚨 Error: GOOGLE_API_KEY environment variable not set.")
    print("Please create a .env file and set your API key to run this script.")
    exit()

# --- Initialize the LLM ---
# Using a newer, widely available model to ensure compatibility.
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    convert_system_message_to_human=True,
    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
)

# --- Initialize the Vision LLM ---
# The same modern model can handle both text and vision.
vision_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
)


def generate_post_idea():
    """Generates a new post idea using the LangChain and Gemini API."""
    try:
        print("✨ مرحبًا بك في مولد أفكار المنشورات!")
        print("---")
        topic = input("🤔 ما هو الموضوع الذي يدور في ذهنك؟ (مثال: تسويق بالمحتوى) ")
        platform = input("🎯 ما هي المنصة التي ستنشر عليها؟ (مثال: مدونة, تويتر, انستغرام) ")
        goal = input("🚀 ما هو الهدف من هذا المنشور؟ (مثال: زيادة الوعي, جذب عملاء) ")

        # --- Create the Prompt ---
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="أنت مساعد خبير في إنشاء أفكار للمحتوى على وسائل التواصل الاجتماعي."),
            HumanMessagePromptTemplate.from_template("أريد فكرة منشور حول '{topic}' لمنصة '{platform}'. الهدف هو '{goal}'. اقترح فكرة واحدة مبتكرة وجذابة."),
        ])

        # --- Create the Chain ---
        chain = prompt | llm | StrOutputParser()

        print("\n🤖 حسنًا! أفكر في فكرة رائعة لك...\n")

        # --- Invoke the Chain ---
        response = chain.invoke({"topic": topic, "platform": platform, "goal": goal})

        print("🎉 فكرتك الجديدة للمنشور 🎉")
        print("---")
        print(response)
        print("---separated_spec---")

    except Exception as e:
        print(f"😭 حدث خطأ: {e}")


def generate_caption_for_image():
    """Generates a caption for an image using LangChain and the Gemini Vision API."""
    import base64
    import io
    from PIL import Image

    try:
        print("✨ مرحبًا بك في مولد التعليقات على الصور!")
        print("---")
        
        image_path = input("🖼️ من فضلك أدخل المسار إلى صورتك: ")
        if not os.path.exists(image_path):
            print("❌ عذرًا, لم أتمكن من العثور على الملف في هذا المسار.")
            return

        try:
            # Function to encode the image
            def encode_image(image_path):
                with open(image_path, "rb") as image_file:
                    return base64.b64encode(image_file.read()).decode('utf-8')

            base64_image = encode_image(image_path)
        except Exception as e:
            print(f"❌ لا يمكن فتح أو معالجة الصورة في المسار: {image_path}. تأكد من أنه ملف صورة صالح. الخطأ: {e}")
            return
        
        caption_goal = input("🚀 ما هو الهدف من التعليق؟ (مثال: بيع منتج, زيادة التفاعل) ")
        tone = input("🎭 ما هي نبرة التعليق؟ (مثال: ودود, احترافي, فكاهي) ")
        
        # --- Create the Message ---
        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": f"اكتب تعليقًا لهذه الصورة. الهدف هو '{caption_goal}' والنبرة يجب أن تكون '{tone}'. أضف هاشتاقات ذات صلة.",
                },
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"},
            ]
        )

        print("\n🤖 حسنًا! أقوم بتحليل الصورة وكتابة تعليق...\n")

        # --- Invoke the Model ---
        response = vision_llm.invoke([message])

        print("🎉 تعليقك الجديد 🎉")
        print("---")
        print(response.content)
        print("---separated_spec---")

    except Exception as e:
        print(f"😭 حدث خطأ: {e}")


def main():
    """The main function of the content assistant."""
    print("👋 مرحبًا بك في مساعد المحتوى الخاص بك!")
    print("أنا هنا لمساعدتك في إنشاء محتوى رائع باستخدام Gemini.")

    while True:
        print("\n--- القائمة الرئيسية ---")
        print("1. 💡 إنشاء فكرة منشور جديدة")
        print("2. 📸 إنشاء تعليق على صورة")
        print("3. 👋 الخروج")
        
        choice = input("🔧 ماذا تريد أن تفعل؟ (اختر 1, 2, أو 3): ")

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
