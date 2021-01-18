import os
from PIL import Image
import random
import configparser

config = configparser.RawConfigParser()
config.read("setting.ini")
PATH = str(config.items("IMAGE_DIRECTORY")[0][1])

def filename_list(mode):
    if mode == 'random':
        list = os.listdir(PATH)
        random.shuffle(list)
        return list
    elif mode == 'default':
        return os.listdir(PATH)

def size_list(filename_list):
    list = []
    for index, i in enumerate(filename_list):
        list.append(Image.open(PATH + '/' + i).size)
    return list
