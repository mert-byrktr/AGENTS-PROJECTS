import os
import requests
from dotenv import load_dotenv
from config import PUSHOVER_URL

load_dotenv(override=True)

def pushover_notification(text):
    """Send notification using Pushover API"""
    requests.post(
        PUSHOVER_URL,
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text
        }
    )

def record_user_details(email, name="Name not provided", notes="Not provided"):
    """Record user details and send notification"""
    pushover_notification(f"Recording {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}

def record_unknown_question(question):
    """Record unknown question and send notification"""
    pushover_notification(f"Recording {question}")
    return {"recorded": "ok"}

def read_pdf_content(file_path):
    """Read and extract text content from PDF file"""
    from pypdf import PdfReader
    content = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            content += text
    return content

def read_text_file(file_path):
    """Read and return content from text file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
