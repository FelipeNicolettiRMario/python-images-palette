import os
import shutil
from io import BytesIO
import base64
from utils.MathOperations import distance_3d_points
from PIL import Image

class RGBPallete:

    def __init__(self, image : Image.Image) -> None:
        self.__image = image

    def get_image_dimension(self) -> tuple:
        return  (self.__image.width,self.__image.height)

    def _get_colors_from_image(self) -> list:
        return Image.Image.getcolors(self.__image,maxcolors=self.__image.size[0] * self.__image.size[1])

    @staticmethod
    def _get_top_colors(colors_tuples : list) -> dict:

        return sorted(colors_tuples,reverse=True)

    @staticmethod
    def _get_unsimilar_rgbs(rgbs : list, max_rgbs : int) -> list:

        unsimilar_rgbs = list()
        unsimilar_rgbs.append(rgbs[0])

        for rgb in rgbs:
            
            distances_unsimilar_rgbs = []

            for rgb_unsimilar in unsimilar_rgbs:
                
                distance_between_rgbs = distance_3d_points(rgb[1],rgb_unsimilar[1])
                distances_unsimilar_rgbs.append(distance_between_rgbs)

            if all(i>=70 for i in distances_unsimilar_rgbs):
                unsimilar_rgbs.append(rgb)

            if len(unsimilar_rgbs) == max_rgbs:
                return unsimilar_rgbs

        return unsimilar_rgbs

    @staticmethod
    def _save_palette_colors(rgbs_list : tuple, base_image_size : tuple):

        pallete_image_dimmension = (int(base_image_size[1]/len(rgbs_list)),int(base_image_size[0] * 0.20))

        palette_i = 0

        os.mkdir('tmp')
        for _,rgb in rgbs_list:

            img = Image.new('RGB',pallete_image_dimmension,color=rgb)
            img.save(f'tmp/{palette_i}.jpeg')
            palette_i+=1

    @staticmethod
    def _get_pallete_images() -> list:

        for root,dir,files in os.walk('./tmp'):
            return files

    def _create_palette_image(self):

        pallet_images_list = self._get_pallete_images()
        pallet_images_object = [Image.open(f'./tmp/{image}') for image in pallet_images_list]

        base_img_width_paste_reference = 0
        for image_object in pallet_images_object:
            
            self.__image.paste(image_object,(0,base_img_width_paste_reference))
            base_img_width_paste_reference += image_object.width

        #self.__image.save(f'./outputs/output.{self.__image.format}')
        shutil.rmtree('./tmp')


    def generate_rgb_image_bytes(self):

        colors = self._get_colors_from_image()
        colors_sorted = self._get_top_colors(colors)
        unsimilar_rgbs = self._get_unsimilar_rgbs(colors_sorted,7)

        self._save_palette_colors(unsimilar_rgbs, self.get_image_dimension())
        self._create_palette_image()

        return self.__image.tobytes()

    
        

