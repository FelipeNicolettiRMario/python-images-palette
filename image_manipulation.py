from PIL import Image
import tempfile
import os
import shutil

def load_image(path : str) -> Image:

    if os.path.exists(path):
        return Image.open(path)

    raise FileNotFoundError

def get_colors_from_image(image : Image) -> list:

    return Image.Image.getcolors(image,maxcolors=image.size[0]*image.size[1])

def save_palette_colors(rgbs_list : tuple, base_image_size : tuple):

    pallete_image_dimmension = (int(base_image_size[1]/len(rgbs_list)),int(base_image_size[0] * 0.20))

    palette_i = 0

    os.mkdir('tmp')
    for _,rgb in rgbs_list:

        img = Image.new('RGB',pallete_image_dimmension,color=rgb)
        img.save(f'tmp/{palette_i}.jpeg')
        palette_i+=1

def get_pallete_images() -> list:

    for root,dir,files in os.walk('./tmp'):
        return files

def create_palette_image(base_imag: Image.Image):

    pallet_images_list = get_pallete_images()
    pallet_images_object = [Image.open(f'./tmp/{image}') for image in pallet_images_list]

    base_img_width_paste_reference = 0
    for image_object in pallet_images_object:
        
        base_imag.paste(image_object,(0,base_img_width_paste_reference))
        base_img_width_paste_reference += image_object.width

    base_imag.save(f'./outputs/output.{base_imag.format}')
    shutil.rmtree('./tmp')


