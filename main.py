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


# print(os.getenv("TG_BOT_TOKEN"))
# print(os.getenv("OPEN_AI_TOKEN"))


def start(update: Update, context: CallbackContext):
    first_name = update["message"]["chat"]["first_name"]
    update.message.reply_text(
            "Hello " + first_name + ", I'm Pacifista Bot. Please write\
		/help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /generate_image {image you want}
    /telegram - to get my Telegram ID
    /snapchat - to get my snapchat ID
	/youtube - To get the youtube URL
	/linkedin - To get the LinkedIn profile URL
	/gmail - To get gmail URL
	/instagram - To get the instagram URL""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "I am not giving mine for security reasons 😝😝")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Here is my Master's Youtube Link =>\
	https://www.youtube.com/@unrivalledking")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Here is my Master's LinkedIn URL => \
		https://www.linkedin.com/in/unrivalledking/")


def snapchat_id(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Here is my Master's LinkedIn URL => \
		https://www.snapchat.com/add/unrivalledking")


def insta_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Here is my Master's instagram URL => https://www.instagram.com/unrivalled___king")


def telegram_id(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Here is my Master's Telegram ID => @UNRIVALLEDKING")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def generate_image(update: Update, context: CallbackContext):
    if len(update["message"]["text"][16:]) > 0:
        image = openai.Image.create(
            prompt=update["message"]["text"][16:], n=2, size="1024x1024")
        update.message.reply_photo(image["data"][0]["url"])
    else:
        update.message.reply_photo("https://i.ibb.co/Q6H1fzL/image.png")


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
bot.dispatcher.add_handler(CommandHandler('telegram', telegram_id))
bot.dispatcher.add_handler(CommandHandler('snapchat', snapchat_id))
bot.dispatcher.add_handler(
    CommandHandler('generate_image', generate_image))
bot.dispatcher.add_handler(MessageHandler(Filters.text, response))

bot.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

bot.start_polling()
