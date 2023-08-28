import os

import telebot
import yaml
from transformers import AutoTokenizer, AutoModelWithLMHead
from yaml.loader import SafeLoader
import torch

from model_functionality import get_model_answer, postprocess_model_answer

with open('config.yaml') as f:
    conf = yaml.load(f, Loader=SafeLoader)
    model_dir = conf['directory_for_model']
    model_subdir = conf['model_subdir_name']

bot = telebot.TeleBot(conf['token'])


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Давай поговорим :)")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    global model, tokenizer
    bot_answer = get_model_answer(model, tokenizer, message.text)
    preprocessed_bot_answer = postprocess_model_answer(bot_answer)
    bot.send_message(message.chat.id, preprocessed_bot_answer)


if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained(os.path.join(model_dir, model_subdir))
    model = AutoModelWithLMHead.from_pretrained(os.path.join(model_dir, model_subdir))
    bot.infinity_polling()
