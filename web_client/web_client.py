import os

import streamlit as st
import yaml
from transformers import AutoModelWithLMHead, AutoTokenizer
from yaml.loader import SafeLoader

from model_functionality import get_model_answer, postprocess_model_answer

if __name__ == '__main__':
    with open('config.yaml') as f:
        conf = yaml.load(f, Loader=SafeLoader)
        model_dir = conf['directory_for_model']
        model_subdir = conf['model_subdir_name']

    st.title("Chatbot")

    with st.spinner("Loading model..."):
        tokenizer = AutoTokenizer.from_pretrained(os.path.join(model_dir, model_subdir))
        model = AutoModelWithLMHead.from_pretrained(os.path.join(model_dir, model_subdir))

    user_message = st.chat_input('Say smth:')
    # print(user_message)
    if user_message:
        with st.chat_message("User"):
            st.write(user_message)
        answer = get_model_answer(model, tokenizer, user_message)
        answer = postprocess_model_answer(answer)
        with st.chat_message("MyGPT"):
            st.write(answer)
