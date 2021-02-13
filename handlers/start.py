from telegram.ext import CommandHandler


def start(update, context):
    update.effective_message.reply_text(
        "Hey there, I'm alive.\nI am an AI ChatBot, Developed with love for interacting with users!"
    )


__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
