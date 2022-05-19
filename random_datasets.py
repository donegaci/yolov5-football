import os
import glob
import random
import shutil


path = "../arama_dataset/16_10_21_center_400imgs/train_216/"


images = glob.glob(path + "*.jpg")
dataset_sizes = [40, 80, 120, 160]

print(images)


for size in dataset_sizes:
  subset_images = random.sample(images, size)
  # remove .jpg extension and replace with .txt
  subset_labels = [os.path.splitext(img)[0] + ".txt" for img in subset_images]

  print(subset_images)
  print(subset_labels)

  new_dataset_name = "../arama_dataset/16_10_21_center_400imgs/" + "train_smaller_" + str(size)
  

  #  is an old folder exists, remove it
  if os.path.exists(new_dataset_name):
    shutil.rmtree(new_dataset_name)

  os.makedirs(new_dataset_name)

  [shutil.copy(img, new_dataset_name) for img in subset_images]
  [shutil.copy(label, new_dataset_name) for label in subset_labels]



