import os 
from PIL import Image

def load_image(path : str) -> Image:

    if os.path.exists(path):
        return Image.open(path)

    raise FileNotFoundError