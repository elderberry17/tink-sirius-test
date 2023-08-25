import gdown

if __name__ == '__main__':
    url =
    output_file = "slavagpt.zip"
    gdown.download(url, output_file, quiet=False, fuzzy=True)
