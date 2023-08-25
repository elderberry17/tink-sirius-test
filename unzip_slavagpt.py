import zipfile

if __name__ == '__main__':
    directory_to_extract_to = 'ruDialoGPT-medium-finetuned_v1'
    with zipfile.ZipFile('slavagpt.zip', 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
