"""/start command"""
from telegram import Update
from telegram.ext import ContextTypes

from module.data import START_CMD_TEXT

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
        Called by the /start command
        Sends a welcome message

        Args:
            update: update event
            context: context passed by the handler
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=START_CMD_TEXT
    )
