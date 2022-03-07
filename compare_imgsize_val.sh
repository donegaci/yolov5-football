#! /bin/bash

for i in {6144,4096,2560,2160,1920,1280,852,640}
do
  python val.py --data arama_dataset.yaml \
    --weights yolov5s.pt \
    --batch-size 1 \
    --img  $i \
    --name "yolov5s_imagesize${i}"
done