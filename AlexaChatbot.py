import sys
import os
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters

from handlers import all_handlers


updater = Updater("1596501040:AAHOOUx-1a4vnCZNzpxwrVUmXN4cfzSHjuE")

for handler in all_handlers:
    if len(handler) == 2:
        updater.dispatcher.add_handler(
            handler[0],
            handler[1]
        )
    else:
        updater.dispatcher.add_handler(
            handler[0]
        )


def stop_and_restart():
    updater.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)


def restart(update, contex):
    update.message.reply_text("Restarting...")
    Thread(
        target=stop_and_restart
    ).start()


updater.dispatcher.add_handler(
    CommandHandler(
        "r",
        restart,
        filters=Filters.user(
            [
                1229419906,
                1180249738
            ]
        )
    )
)
updater.start_polling()
updater.idle()
