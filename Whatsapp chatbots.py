import time
import requests
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
# ✅ Configuration
GROUP_NAME = "Your_Group_Name"  # Change to your WhatsApp group name
OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama API URL
GOOGLE_API_KEY = "Your_Gemini_API_Key"  # Replace with your actual API key

# Setup WebDriver
EDGE_DRIVER_PATH = r"Your_webdriver_path"  # Change to your WebDriver path

# ✅ Setup Google Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

def ask_gemini(query):
    """Ask Gemini AI and return response."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(query)

        if response and hasattr(response, 'text'):
            return response.text.strip() if isinstance(response.text, str) else "\n".join(response.text).strip()
        
        return "I'm unable to process that request right now."
    
    except Exception as e:
        print(f"⚠️ Error with Gemini AI: {e}")
        return "Error processing your request."

def ask_deepseek(query, model="7b"):
    """Ask DeepSeek AI and return response."""
    payload = {
        "model": f"deepseek-r1:{model}",  # Supports both 7B and 1.5B
        "prompt": query,
        "stream": False  # Ensure a single response
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()

        return result.get("response", "I'm unable to process that request right now.").strip()
    
    except Exception as e:
        print(f"⚠️ Error with DeepSeek AI: {e}")
        return "Error processing your request."

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service, options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Scan the QR code in WhatsApp Web, then press Enter to continue...")

def open_whatsapp_group(group_name):
    """Search and open the WhatsApp group."""
    try:
        print(f"Searching for group: {group_name}")
        search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@role='textbox']")
        search_box.click()
        search_box.clear()
        search_box.send_keys(group_name)
        time.sleep(3)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        print("Group opened successfully!")
    except Exception as e:
        print(f"Error opening group: {e}")

def read_last_message():
    """Read the latest message from the chat."""
    try:
        messages = driver.find_elements(By.XPATH, "//span[@class='_ao3e selectable-text copyable-text']")
        if messages:
            last_message = messages[-1].text.strip()
            print(f"Detected Message: {last_message}")
            return last_message
        else:
            print("No messages detected.")
            return None
    except Exception as e:
        print(f"Error reading message: {e}")
        return None

def send_message(text):
    """Send a message to the WhatsApp group."""
    try:
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")
        actions = ActionChains(driver)
        actions.move_to_element(message_box).click().send_keys(text + Keys.ENTER).perform()
        print(f"Sent Message: {text}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Open WhatsApp Group
open_whatsapp_group(GROUP_NAME)

# Main Bot Loop
print("WhatsApp AI Bot is running...")
send_message("AI Bot is active!")
last_processed_message = ""
while True:
    try:
        last_message = read_last_message()
        if last_message and last_message != last_processed_message:
            print(f"New message detected: {last_message}")
            last_processed_message = last_message

            if last_message.lower().startswith("@gemini"):
                query = last_message.replace("@gemini", "").strip()
                print(f"User Asked Gemini: {query}")
                ai_response = ask_gemini(query)
                print(f"Gemini AI: {ai_response}")
                send_message(ai_response)

            elif last_message.lower().startswith("@deepseek"):
                query = last_message.replace("@deepseek", "").strip()
                print(f"User Asked DeepSeek: {query}")
                ai_response = ask_deepseek(query)
                print(f"DeepSeek AI: {ai_response}")
                send_message(ai_response)
            
        else:
            print("No new messages...")

        time.sleep(2)

    except Exception as e:
        print(f"Error in loop: {e}")
        time.sleep(2)