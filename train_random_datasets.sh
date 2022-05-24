#! /bin/bash

BASE_PATH="/home/donegaci/arama_dataset/16_10_21_center_400imgs/random_set_[0-2]"


for RANDOM_SET in $BASE_PATH; do
 echo $RANDOM_SET
 SET=$(basename $RANDOM_SET)

 FILES="${RANDOM_SET}/train144
        ${RANDOM_SET}/train216
        ${RANDOM_SET}/train288
        ${RANDOM_SET}/train72"
 for DATA in $FILES; do
    echo $DATA
    SIZE=`echo $DATA | sed 's/.*train//'`
    sed -i "/train:/c train: $SET/train$SIZE" random_datasets0.yaml
    python train.py --img 1920 --device 0 --batch 4 --epochs 200 --data random_datasets0.yaml --weights yolov5s.pt --name $SET/train$SIZE
  done

done &


BASE_PATH="/home/donegaci/arama_dataset/16_10_21_center_400imgs/random_set_[3-6]"


for RANDOM_SET in $BASE_PATH; do
 echo $RANDOM_SET
 SET=$(basename $RANDOM_SET)

 FILES="${RANDOM_SET}/train144
        ${RANDOM_SET}/train216
        ${RANDOM_SET}/train288
        ${RANDOM_SET}/train72"
 for DATA in $FILES; do
    echo $DATA
    SIZE=`echo $DATA | sed 's/.*train//'`
    sed -i "/train:/c train: $SET/train$SIZE" random_datasets1.yaml
    python train.py --img 1920 --device 1 --batch 4 --epochs 200 --data random_datasets1.yaml --weights yolov5s.pt --name $SET/train$SIZE
  done

done &


BASE_PATH="/home/donegaci/arama_dataset/16_10_21_center_400imgs/random_set_[7-9]"


for RANDOM_SET in $BASE_PATH; do
 echo $RANDOM_SET
 SET=$(basename $RANDOM_SET)

 FILES="${RANDOM_SET}/train144
        ${RANDOM_SET}/train216
        ${RANDOM_SET}/train288
        ${RANDOM_SET}/train72"
 for DATA in $FILES; do
    echo $DATA
    SIZE=`echo $DATA | sed 's/.*train//'`
    sed -i "/train:/c train: $SET/train$SIZE" random_datasets2.yaml
    python train.py --img 1920 --device 2 --batch 4 --epochs 200 --data random_datasets2.yaml --weights yolov5s.pt --name $SET/train$SIZE
  done

done &

