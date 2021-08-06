from PIL import Image
from io import BytesIO,BufferedReader
import base64



class ImageHandler:

    def __init__(self,image_representation) -> None:
        self.__image_representaton = image_representation

    def get_image(self) -> Image.Image:

        if isinstance(self.__image_representaton,BufferedReader):
            image = Image.open(self.__image_representaton)

        elif isinstance(self.__image_representaton,bytes):
            image = Image.open(BytesIO(self.__image_representaton))
        
        return image 



