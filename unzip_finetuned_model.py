import zipfile
import yaml
from yaml.loader import SafeLoader

if __name__ == '__main__':
    with open('config.yaml') as f:
        conf = yaml.load(f, Loader=SafeLoader)

    directory_to_extract_to = conf['directory_for_model']
    with zipfile.ZipFile('model.zip', 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
