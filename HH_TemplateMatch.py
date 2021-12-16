#Object Detection by Template Matching -  Store min_loc to a json file
import cv2
import numpy as np
import json
import os

path_to_image = os.environ.get('PATH_TO_HH_SCREENSHOT_IMAGE')

def writeToJSONFile(path, filename, data):
    filePathNameWExt = '/' + path + '/' + filename + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

#Run the template across the screenshot image
img_rgb = cv2.imread(path_to_image + '/HH_FirefoxScreenShot.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(path_to_image + '/Template_Master_NGY00_GCP_Firefox.png', 0)

res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print('min_loc:',min_loc)

#Store the corner of best match to json file  (_offset currently unused)
path = path_to_image
filename = 'HH_TemplateMatch'

coordinate_data = {}
coordinate_data['x_origin'] = min_loc[0]
coordinate_data['y_origin'] = min_loc[1]
coordinate_data['offset_x_global'] = 0
coordinate_data['offset_y_global'] = 30
coordinate_data['offset_x1_im1'] = 0
coordinate_data['offset_y1_im1'] = 0
coordinate_data['offset_x2_im1'] = 110
coordinate_data['offset_y2_im1'] = 195
coordinate_data['offset_x1_im2'] = 165
coordinate_data['offset_y1_im2'] = 0
coordinate_data['offset_x2_im2'] = 210
coordinate_data['offset_y2_im2'] = 195

writeToJSONFile(path, filename, coordinate_data)
