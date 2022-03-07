from pathlib import Path
import os
import math
import random
from tqdm import tqdm
import cv2
import numpy as np

dataset_6k_path = '/home/ciaran/arama_dataset/Full_dataset_football'
dataset_hd_crop = '/home/ciaran/arama_dataset/dataset_hd_crops'

# YOLO label format 
# <object-class> <x> <y> <width> <height>


def get_crop_window_coordinates(ball_x, ball_y, full_width, full_height, crop_width, crop_height):
  
  #  coordinates for the window
  min_x = min_y = max_x = max_y = -1

  x_offset = crop_width // 2
  y_offset =  crop_height //2

  # Make sure we don't go outside original 6k image border in the x direction
  if (ball_x - x_offset) < 10:
    min_x = 0
    max_x = crop_width
  elif (ball_x + x_offset) > full_width-10:
    min_x = full_width - crop_width
    max_x = full_width
  else:
    min_x = ball_x - x_offset
    max_x = ball_x + x_offset

  # Repeat the above checks in the y direction
  if (ball_y - y_offset) < 10:
    min_y = 0
    max_y = crop_height
  elif (ball_y + y_offset) > full_height-10:
    min_y = full_height - crop_height
    max_y = full_height
  else:
    min_y = ball_y - y_offset
    max_y = ball_y + y_offset


  return [min_x, min_y,  max_x, max_y]


def main():
  width_6k = 6144
  height_6k = 3456
  width_hd = 1920
  height_hd = 1080 


  # loop over all the label files and extract football coordinates
  labels_list = sorted(Path(dataset_6k_path).glob('*.txt'))
  for label_file in tqdm(labels_list, desc = 'Progress Bar'):

    file_name = Path(label_file).stem

    print(label_file)

    with open(label_file) as f:
      lines = f.readlines()

      # print(lines)
      
    #  if there is a labelled football, make a random crop around the football
    if lines:
      # print("ball found")
      values =  lines[0].split() # split on whitespace
      x_coord = math.floor(float(values[1]) * width_6k)
      y_coord = math.floor(float(values[2]) * height_6k)
      x_bb_width= math.floor(float(values[3]) * width_6k)
      y_bb_height = math.floor(float(values[4]) * height_6k)

      #  add some random noise 
      y_noise = random.randint(-540, 540)
      x_noise = random.randint(-960, 960)
      noisy_x = x_coord + x_noise
      noisy_y =  y_coord + y_noise


      # edges = [min_x, min_y,  max_x, max_y]
      edges = get_crop_window_coordinates(noisy_x, noisy_y, width_6k, height_6k, width_hd, height_hd)
    # if there is no labelled football, take a random crop from anywhere in the image
    else:
      # print("No ball. Random crop")
      x_coord = random.randint(1, width_6k)
      y_coord = random.randint(1, height_6k)
      edges = get_crop_window_coordinates(x_coord, y_coord, width_6k, height_6k, width_hd, height_hd)

    min_x = edges[0]
    min_y = edges[1] 
    max_x = edges[2]
    max_y = edges[3]

    img_path = os.path.splitext(label_file)[0]+ ".jpg"
    img_6k = cv2.imread(img_path)
    img_crop = img_6k[min_y:max_y, min_x:max_x]

    if lines:
      x_bb_min = (x_coord - min_x) - (x_bb_width//2)
      x_bb_max = (x_coord - min_x) + (x_bb_width//2)
      y_bb_min = (y_coord - min_y) - (y_bb_height//2)
      y_bb_max = (y_coord - min_y) + (y_bb_height//2)
      # img_crop = cv2.rectangle(img_crop, (x_bb_min, y_bb_min), (x_bb_max, y_bb_max), (255,0,0), 2)
      x_center = x_bb_min/width_hd + (2 * float(values[3]))
      y_center = y_bb_min/height_hd + (2 *float(values[4]))
      w = float(values[3]) * 4
      h = float(values[4]) * 4
      string = "0 " + str(x_center) + " " + str(y_center) + " " + str(w) + " " + str(h)
      # print(string)
      with open(dataset_hd_crop + "/" + file_name + ".txt", 'w') as f:
        f.write(string)
    else:
      #  write blank annotation txt file
      with open(dataset_hd_crop + "/" + file_name + ".txt", 'w') as f:
        f.write('')



    # cv2.imshow("6k image", img_6k)
    # cv2.imshow("Cropped", img_crop)
    # cv2.waitKey(0)

    cv2.imwrite(dataset_hd_crop + "/" + file_name + ".jpg", img_crop)




if __name__ == "__main__":
    main()

