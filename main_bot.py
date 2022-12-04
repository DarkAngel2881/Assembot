#import keys from Costants file as token from Botfather
#import all from telegram.ext
#refer to the case of answers from the bot as 'R' taken from Responses
import Costants as keys
from telegram.ext import *
import Responses as R

#terminal start confirmation
print("Bot initialized...")


#functions to make the bot reply to the commands (start the bot, ask for help, make an assembly request)
def start_command(update, context):
    update.message.reply_text(f'Hello, {update.message.from_user.username}!\nI\'m assembot and I\'m able to send an assembly request to one or more teachers and then directly send it to the school office to approve it!')

#//
def help_command(update, context):
    update.message.reply_text('If have any questions or you have no idea how to use it ask to @Assistance')

#//
def request_command(update, context):
    update.message.reply_text('You are (name of the user), rapresentant of (user\'s class).\nThis is your time table of the week:\n(image of the time table of the class)\nWich are the teacher/s you need to ask for the assembly?\n(Enter the full name of the teacher):')
    update.message.reply_photo(open("AC.png", 'rb'))

#function to make the bot reply to any user's text messages based on the filters created in 'Responses'
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)


#function to print on the admin termina the error and all the details
def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    #declare the updater for all the relative functions and the dispatcher for teh execution
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    #execution of the commands (/ ones)
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("request", request_command))

    #execution of simple replies to normal user's messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    #execution in case of errors
    dp.add_error_handler(error)

    #updater anti-depolling
    updater.start_polling()
    updater.idle()

#start
main()
