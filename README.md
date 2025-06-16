
#  WhatsApp AI Chatbot (Gemini + DeepSeek)

This is a Python-based chatbot that automatically responds to messages in a WhatsApp group using **Google Gemini** or **DeepSeek** AI models.

---

##  DISCLAIMER

This script is intended for **educational and personal use only**.  
**Use at your own risk** — automating interactions with WhatsApp Web may **violate their Terms of Service**, and **your account may be restricted or banned**.  
The author is **not responsible** for any misuse, bans, or consequences resulting from the use of this project.

---

##  Features

-  Uses **Google Gemini API** and **DeepSeek (via Ollama)** to answer queries
-  Listens for special prefixes in group messages:
  - `@gemini` → routed to Gemini
  - `@deepseek` → routed to DeepSeek
-  Sends AI-generated responses back to the group using Selenium
-  Runs inside **Edge browser** using WebDriver

---

##  Setup

### Requirements

- Python 3.7+
- Microsoft Edge Browser
- Microsoft Edge WebDriver (matching your Edge version)

### Install Dependencies

```bash
pip install selenium requests google-generativeai
````

---

### Configuration

Edit the top of the script to match your setup:

```python
GROUP_NAME = "Your_Group_Name"  # Name of the WhatsApp group
OLLAMA_URL = "http://localhost:11434/api/generate"  # DeepSeek API (Ollama)
GOOGLE_API_KEY = "Your_Gemini_API_Key"  # Replace with your actual Gemini API key
EDGE_DRIVER_PATH = r"Your_webdriver_path"  # Absolute path to msedgedriver.exe
```

Ensure that:

* You have a working Gemini API key
* Ollama server is running locally for DeepSeek
* `msedgedriver.exe` is present and compatible with your browser version

---

##  How to Use

1. Run the script:

```bash
python "Whatsapp chatbots.py"
```

2. A browser window will open.
   Scan the **QR code** to log in to WhatsApp Web.

3. The script will open the specified group and listen for messages.

---

##  Commands

Within your group, use the following formats:

* `@gemini What is quantum computing?`
* `@deepseek Explain how AI models are trained.`

The bot will detect these prefixes, process the query, and reply.

---

##  Notes

* Ensure that you’re logged into ChatGPT/Gemini/Ollama beforehand if required.
* To avoid rate limits, keep usage reasonable.
* You can adapt the script to add more models, custom commands, or logging.

---

##  Security

* Never share or commit your API keys.
* For safety, consider storing them in environment variables.

---

##  License

This project is for **non-commercial**, educational use only.
Not affiliated with WhatsApp, Google, OpenAI, or DeepSeek.

```

