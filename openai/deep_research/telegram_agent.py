import os
from typing import Dict
import requests

from agents import Agent, function_tool
from dotenv import load_dotenv

load_dotenv(override=True)
telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")
url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"


@function_tool
def send_telegram_message(body: str):
    """ Send a message with the given body to all readers. """
    max_len = 4096
    for i in range(0, len(body), max_len):
        chunk = body[i: i + max_len]
        payload = {"chat_id": chat_id, "text": body}
        try:
            response = requests.post(url, data=payload)
            if response.status_code != 200:
                print("Failed to send chunk:", response.text)
                break
        except Exception as e:
            print("Error sending Telegram message:", e)
            break
    else:
        print("All chunks sent successfully!")


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

telegram_agent = Agent(
    name="Telegram Agent",
    instructions=INSTRUCTIONS,
    tools=[send_telegram_message],
    model="gpt-4o-mini",
)