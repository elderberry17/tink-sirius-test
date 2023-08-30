import gdown
import yaml
from yaml.loader import SafeLoader

if __name__ == '__main__':
    with open('config.yaml') as f:
        conf = yaml.load(f, Loader=SafeLoader)

    # url for model in .zip archive
    url = conf['download_model_url']
    output_file = "model.zip"
    gdown.download(url, output_file, quiet=False, fuzzy=True)
