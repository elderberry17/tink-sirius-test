import re

import telebot
import yaml
from transformers import AutoTokenizer, AutoModelWithLMHead
from yaml.loader import SafeLoader

with open('config.yaml') as f:
    conf = yaml.load(f, Loader=SafeLoader)

bot = telebot.TeleBot(conf['token'])


def get_bot_answer(text_input: str) -> str:
    global model, tokenizer

    inputs = tokenizer(text_input, return_tensors='pt')
    generated_token_ids = model.generate(
        **inputs,
        top_k=10,
        top_p=0.95,
        num_beams=3,
        num_return_sequences=3,
        do_sample=True,
        no_repeat_ngram_size=2,
        temperature=1.2,
        repetition_penalty=1.2,
        length_penalty=1.0,
        eos_token_id=50257,
        max_new_tokens=40
    )

    context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
    return context_with_response[0][len(text_input):]


def preprocess_bot_answer(answer):
    regex1 = r'@@ВТОРОЙ@@(.*?)@@ПЕРВЫЙ@@'
    regex2 = r'@@ВТОРОЙ@@(.*?)'
    try:
        result = re.search(regex1, answer)
        extracted_string = result.group(1)
        print(answer)
    except AttributeError:
        print(f'ERROR WITH MESSAGE: {answer}')
        try:
            result = re.search(regex2, answer)
            extracted_string = result.group(1)
        except AttributeError:
            extracted_string = 'Я сейчас чуть не упал'

    return extracted_string


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Давай поговорим :)")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot_answer = get_bot_answer(message.text)
    preprocessed_bot_answer = preprocess_bot_answer(bot_answer)
    bot.send_message(message.chat.id, preprocessed_bot_answer)


if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained('ruDialoGPT-medium-finetuned_v1/content/slavagpt')
    model = AutoModelWithLMHead.from_pretrained('ruDialoGPT-medium-finetuned_v1/content/slavagpt')
    bot.infinity_polling()
