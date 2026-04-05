
from google.genai import Client  


API_KEY = "your api_key"

client = Client(api_key=API_KEY)


model_name = "gemini-2.5-flash"

def analyze_ticket(text):
    """
    Analyze a support ticket and return JSON with:
    category, severity, department, sentiment
    """
    prompt = f"""
    Return ONLY JSON.

    Ticket: {text}

    {{
      "category": "",
      "severity": "",
      "department": "",
      "sentiment": ""
    }}
    """
    try:
        response = client.generate_text(model=model_name, prompt=prompt)
        return response.text
    except Exception as e:
        print(f"Error in AI response: {e}")
        return "Error in AI response"

def auto_resolve(text):
    """
    Automatically resolve common tickets based on keywords
    """
    text = text.lower()
    if "password" in text:
        return "Click on 'Forgot Password' to reset your password."
    if "leave" in text:
        return "Apply leave from HR portal."
    return None