import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

openai.api_key = "YOUR API KEY"

bot = telegram.Bot(token="YOUR TOKKEN")

#Обработчик команды 'start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который может генерировать тексты с помощью OpenAI GPT-3. Напиши мне что-нибудь, и я постараюсь ответить.")

#Обработчик всех текстовых сообщений
def generate_text(update, context):
    text = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_text = response.choices[0].text
    context.bot.send_message(chat_id=update.effective_chat.id, text=generated_text)
    
#бработчики команд и текстовых сообщений
def main():
    updater = Updater(token="6258836777:AAFztJJITWBH2hV8wIowRjBdYyUXr1fHh8w", use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    generate_text_handler = MessageHandler(Filters.text & ~Filters.command, generate_text)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(generate_text_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
