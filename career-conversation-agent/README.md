Follow along code for the udemy course **https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/**

Career conversation agent utilizng some tool calling functionalities to handle unknown and known questions using OpenAI SDK


## Setup Instructions

1. Clone the repo.
2. Under **me** directory, upload your LinkedIn pdf file as **Profile.pdf** and a summary.txt file describing yourself.
3. Create an .env file with the following variables:

   ```bash
    OPENAI_API_KEY=your_api_key_here
    PUSHOVER_TOKEN=your_pushover_token
    PUSHOVER_USER=your_pushover_user_key
    TELEGRAM_BOT_TOKEN=you_telegram_bot_token
    TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

4. Make sure uv is installed and run the following:
   ```bash
   uv sync
   cd career-conversation-agent
   uv run app.py
   ```

