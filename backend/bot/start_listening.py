import os
import logging

import boto3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='[%(asctime)s | %(levelname)s] %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

_TG_TOKEN = str(os.environ.get('TG_TOKEN'))
_AWS_BUCKET_REGION = str(os.environ.get('AWS_BUCKET_REGION'))
_AWS_ACCESS_KEY_ID = str(os.environ.get('AWS_ACCESS_KEY_ID'))
_AWS_SECRET_ACCESS_KEY = str(os.environ.get('AWS_SECRET_ACCESS_KEY'))

s3 = boto3.resource('s3', region_name=_AWS_BUCKET_REGION,
                    aws_access_key_id=_AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=_AWS_SECRET_ACCESS_KEY)

for bucket in s3.buckets.all():
    print(bucket.name)

if not _TG_TOKEN:
    raise SystemError('Can\'t start without TOKEN')


def handle_start(bot, update):
    update.message.reply_text(
        'Hi! We are ready to go. Send me some voice messages.')


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
    updater = Updater(_TG_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", handle_start))
    dp.add_handler(MessageHandler(Filters.voice, handle_voice))
    dp.add_handler(MessageHandler(~Filters.voice, handle_unexpected))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    poll()
