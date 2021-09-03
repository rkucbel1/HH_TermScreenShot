#Crop Screenshot Image into two images. term and price images
from PIL import Image
import json
import os

path_to_image = os.environ.get('PATH_TO_HH_SCREENSHOT_IMAGE')

#Load the initial points to crop from (One initial point per image)
with open(path_to_image + '/HH_TemplateMatch.json', 'r') as f:
    f_contents = f.read()

data = json.loads(f_contents)

x1_img1 = data['x_origin'] + data['offset_x_global'] + data['offset_x1_im1']
y1_img1 = data['y_origin'] + data['offset_y_global'] + data['offset_y1_im1']
x2_img1 = data['x_origin'] + data['offset_x_global'] + data['offset_x2_im1']
y2_img1 = data['y_origin'] + data['offset_y_global'] + data['offset_y2_im1']

x1_img2 = data['x_origin'] + data['offset_x_global'] + data['offset_x1_im2']
y1_img2 = data['y_origin'] + data['offset_y_global'] + data['offset_y1_im2']
x2_img2 = data['x_origin'] + data['offset_x_global'] + data['offset_x2_im2']
y2_img2 = data['y_origin'] + data['offset_y_global'] + data['offset_y2_im2']

img = Image.open(path_to_image + '/HH_FirefoxScreenShot.png')

imgCropped1 = img.crop(box = (x1_img1,y1_img1,x2_img1,y2_img1))
imgCropped2 = img.crop(box = (x1_img2,y1_img2,x2_img2,y2_img2))

imgCropped1.save(path_to_image + '/HH_Cropped1FF.png')
imgCropped2.save(path_to_image + '/HH_Cropped2FF.png')
