import re


def get_model_answer(model, tokenizer, text_input: str) -> str:
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
        max_new_tokens=40,
    )

    context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
    return context_with_response[0][len(text_input):]


def postprocess_model_answer(answer):
    regex1 = r'@@ВТОРОЙ@@(.*?)@@ПЕРВЫЙ@@'
    regex2 = r'@@ВТОРОЙ@@(.*?)'
    try:
        result = re.search(regex1, answer)
        extracted_string = result.group(1)
        # print(answer)
    except AttributeError:
        # print(f'ERROR WITH MESSAGE: {answer}')
        try:
            result = re.search(regex2, answer)
            extracted_string = result.group(1)
        except AttributeError:
            extracted_string = f'Все говорят {answer}, а ты купи слона?'

    return extracted_string
