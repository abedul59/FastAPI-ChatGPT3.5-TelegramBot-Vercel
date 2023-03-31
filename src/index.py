#from telegram import Update, Bot
#from telegram.ext import Dispatcher, MessageHandler, Filters
#from fastapi import FastAPI, Request, HTTPException
#from fastapi.responses import JSONResponse
import os
import openai

import httpx
from fastapi import FastAPI, Request


TOKEN = str(os.getenv("TELEGRAM_BOT_TOKEN"))
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

client = httpx.AsyncClient()

app = FastAPI()

@app.post("/callback/")
async def webhook(req: Request):
    data = await req.json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    await client.get(f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}")

    return data





'''
openai.api_key = os.getenv("OPENAI_API_KEY")
conversation = []

class ChatGPT:
    def __init__(self):
        self.messages = conversation
        self.model = os.getenv("OPENAI_MODEL", default="gpt-3.5-turbo")

    def get_response(self, user_input):
        conversation.append({"role": "user", "content": user_input})
        response = openai.Completion.create(
            engine=self.model,
            prompt=self._format_messages(self.messages) + user_input,
            max_tokens=60,
        )
        conversation.append({"role": "assistant", "content": response["choices"][0]["text"]})
        return response["choices"][0]["text"].strip()

    @staticmethod
    def _format_messages(messages):
        messages_str = ""
        for message in messages:
            role = message["role"]
            content = message["content"]
            messages_str += f"{role}: {content}\n"
        return messages_str


bot_token = str(os.getenv("TELEGRAM_BOT_TOKEN"))
bot = Bot(token=bot_token)

chatgpt = ChatGPT()

dp = Dispatcher(bot, None)
async def webhook_handler(request: Request):
    if request.method == 'POST':
        update = Update.de_json(await request.json(), bot)
        await dp.process_update(update)
        return JSONResponse({'status': 'ok'})

def reply_handler(bot: Bot, update: Update):
    text = update.message.text
    ai_reply_response = chatgpt.get_response(text)
    update.message.reply_text(ai_reply_response)



    
    
dp.add_handler(MessageHandler(filters.text, reply_handler))



if __name__ == '__main__':
    app.run(debug=True)
    '''
