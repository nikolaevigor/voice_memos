import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='[%(asctime)s | %(levelname)s] %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

_TOKEN = str(os.environ.get('TOKEN'))

if not _TOKEN:
    raise SystemError('Can\'t start without TOKEN')


def handle_start(bot, update):
    update.message.reply_text(
        'Hi! It\'s voice memos bot. Send me your voice message, that you want to store.')


def handle_voice(bot, update):
    update.message.reply_text('Received!')
    # initialize saving to s3


def handle_unexpected(bot, update):
    logger.info(f'Received unexpected message: {update.message.text}')
    update.message.reply_text(
        'I can\'t respond to this, but my creator @nikolaevigor can.')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def poll():
    updater = Updater(_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", handle_start))
    dp.add_handler(MessageHandler(Filters.voice, handle_voice))
    dp.add_handler(MessageHandler(~Filters.voice, handle_unexpected))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    poll()
