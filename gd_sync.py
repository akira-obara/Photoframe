from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import sys
import configparser
import threading
import time
import shutil

def sync():
    while True:
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        drive = GoogleDrive(gauth)
        config = configparser.RawConfigParser()
        config.read("setting.ini")
        PATH = str(config.items("IMAGE_DIRECTORY")[0][1])
        file_list = os.listdir(PATH)
        gfile_list = drive.ListFile({'q': "'' in parents and trashed=false"}).GetList()
        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base))
        for file1 in gfile_list:
            if not (file1['title'] in file_list):
                file = drive.CreateFile({'id':file1['id']})
                file.GetContentFile(file1['title'])
                shutil.move(name + file1['title'], PATH)
        count = []
        while len(count) <= 3:
            count.append(1)
            time.sleep(5)
            if threading.main_thread().is_alive() == False:
                break
        if threading.main_thread().is_alive() == False:
            break
