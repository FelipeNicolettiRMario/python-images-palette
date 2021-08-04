from collections_manipulation import get_top_colors, get_unsimilar_rgbs
from image_manipulation import create_palette_image, get_colors_from_image, load_image, save_palette_colors
from math import *

path = 'D:\\Imagens\\tmp\\download (6).jfif'

image_loaded = load_image(path)
colors = get_colors_from_image(image_loaded)
colors_sorted = get_top_colors(colors)
unsimilar_rgbs = get_unsimilar_rgbs(colors_sorted, 8)

image_dimension = (image_loaded.width,image_loaded.height)
save_palette_colors(unsimilar_rgbs,image_dimension)
create_palette_image(image_loaded)