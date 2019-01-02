#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
from shutil import copyfile

label_names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

def conv_mnist(img_file,label_file, num, path):

    if not os.path.exists(path):
        os.mkdir(path)
    imgs=open(img_file,"rb").read()
    imgs=np.fromstring(imgs,dtype=np.uint8)
    imgs=imgs[16:] # skip header
    imgs=imgs.reshape((num,28,28))

    labels=open(label_file,"rb").read()
    labels=np.fromstring(labels,dtype=np.uint8)
    labels=labels[8:] # skip header

    for i in range(num):
        class_id = labels[i]
        img_name = "%d_%s.png" % (i, label_names[class_id])
        img_path = path+"/"+img_name
        cv2.imwrite(img_path,imgs[i])
    return

data_files=["train-images-idx3-ubyte.gz",
"train-labels-idx1-ubyte.gz",
"t10k-images-idx3-ubyte.gz",
"t10k-labels-idx1-ubyte.gz"]

for data_file in data_files:
    if not os.path.exists(data_file):
        os.system('curl -O http://yann.lecun.com/exdb/mnist/'+data_file)
        os.system('gunzip '+data_file)

cwd = os.getcwd()
img_path=cwd+"/mnist_images"

if not os.path.exists(img_path):
    os.mkdir("mnist_images")

conv_mnist("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte", 10000, img_path+"/train")
conv_mnist("train-images-idx3-ubyte", "train-labels-idx1-ubyte", 60000, img_path+"/test")

copyfile("labels.txt", img_path+"/labels.txt")
