from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_TOKEN")

bot = Updater(os.getenv("TG_BOT_TOKEN"),
              use_context=True)


print(os.getenv("TG_BOT_TOKEN"))
print(os.getenv("OPEN_AI_TOKEN"))


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Hello UNRIVALLEDKING, Welcome to the Bot.Please write\
		/help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /generate_image - To generate Image
	/youtube - To get the youtube URL
	/linkedin - To get the LinkedIn profile URL
	/gmail - To get gmail URL
	/instagram - To get the instagram URL""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "I am not giving mine for security reasons 😝😝")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/@unrivalledking")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
            "LinkedIn URL => \
		https://www.linkedin.com/in/unrivalledking/")


def insta_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "instagram URL => https://www.instagram.com/unrivalled___king")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def generate_image(update: Update, context: CallbackContext):
    image = openai.Image.create(
        prompt=update["message"]["text"][16:], n=2, size="1024x1024")
    update.message.photo(
        chat_id=update["message"]["message_id"], photo='https://telegram.org/img/t_logo.png')
    print("generate", update)


def response(update: Update, context: CallbackContext):
    ResponseGenerate = openai.Completion.create(
        model="text-davinci-003",
        prompt=update["message"]["text"],
        max_tokens=256,
        temperature=0
    )
    res = ResponseGenerate["choices"][0]["text"]
    update.message.reply_text(res)
    print(context, update)


bot.dispatcher.add_handler(CommandHandler('start', start))
bot.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
bot.dispatcher.add_handler(CommandHandler('help', help))
bot.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
bot.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
bot.dispatcher.add_handler(CommandHandler('instagram', insta_url))
bot.dispatcher.add_handler(
    CommandHandler('generate_image', generate_image))
bot.dispatcher.add_handler(MessageHandler(Filters.text, response))

bot.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

bot.start_polling()
