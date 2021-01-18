import datetime
import requests
import json
import threading
import time
import pygame

weather_link_list = []
today_temperature_list = []
tomorrow_temperature_list = []
weather_dic = {"晴れ":'1.png',
               "曇り":'6.png',
               "雨":'7.png',
               "雪":'8.png',
               "晴のち曇":'3.png',
               "晴のち雨":'4.png',
               "晴のち雪":'5.png',
               "曇のち晴":'2.png',
               "曇のち雨":"1.png",
               "曇のち雪":'8.png',
               "雨のち晴":'4.png',
               "雨のち曇":'7.png',
               "雨のち雪":'8.png',
               "雪のち晴":'8.png',
               "雪のち雨":'7.png',
               "雪のち曇":'8.png',
               "晴時々曇":'3.png',
               "晴時々雨":'7.png',
               "晴時々雪":'5.png',
               "曇時々晴":'2.png',
               "曇時々雨":'1.png',
               "曇時々雪":'2.png',
               "雨時々晴":'222.png',
               "雨時々曇":'222.png',
               "雨時々雪":'222.png',
               "雪時々晴":'43.png',
               "雪時々曇":'43.png',
               "雪時々雨":'43.png'}

def weather_livedoor():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    payload = {'city' : '130010'}
    date = requests.get(url, params = payload).json()
    w = []
    for weather in date['forecasts']:
        w.append(weather)
    return w

def get_datetime(nowtime):
    time = [str(nowtime.year) + "."
            + str(nowtime.month) + "."
            + str(nowtime.day)]
    if nowtime.hour >= 12:
        time.append(str(nowtime.hour) + ":"
                    + str(nowtime.minute)
                    + str('PM'))
    elif nowtime.hour < 12:
        time.append(str(nowtime.hour) + ":"
                    + str(nowtime.minute)
                    + str('AM'))
    return time

def get_weather():
    global weather_link_list, weather_dic
    while True:
        w = weather_livedoor()
        today_weather = w[0]['telop']
        tomorrow_weather = w[1]['telop']
        PATH = 'lib/icons/'
        today_weather = weather_dic[today_weather]
        tomorrow_weather = weather_dic[tomorrow_weather]
        link_tod = PATH + today_weather
        link_tom = PATH + tomorrow_weather
        tod_and_tom = [link_tod, link_tom]
        weather_link_list.append(tod_and_tom)
        if not (w[0]['temperature']['min'] == None):
            today_temperature_max = w[0]['temperature']['max']['celsius']
            today_temperature_min = w[0]['temperature']['min']['celsius']
            link = [str(today_temperature_min) + " ℃", str(today_temperature_max) + " ℃"]
        else:
            link = ['e', 'e']
        today_temperature_list.append(link)
        if not (w[1]['temperature']['min'] == None):
            tomorrow_temperature_max = w[1]['temperature']['max']['celsius']
            tomorrow_temperature_min = w[1]['temperature']['min']['celsius']
            link = [str(tomorrow_temperature_min) + " ℃", str(tomorrow_temperature_max) + " ℃"]
            tomorrow_temperature_list.append(link)
        else:
            link = ['e', 'e']
        tomorrow_temperature_list.append(link)
        time.sleep(60)
        if threading.main_thread().is_alive() == False:
            break

def get_temperature():
    global today_temperature_list, tomorrow_temperature_list
    while True:
        w = weather_livedoor()
        if not (w[0]['temperature']['min'] == None):
            today_temperature_max = w[0]['temperature']['max']['celsius']
            today_temperature_min = w[0]['temperature']['min']['celsius']
            link = [str(today_temperature_min) + " ℃", str(today_temperature_max) + " ℃"]
            today_temperature_list.append(link)
        else:
            link = ['e', 'e']
            today_temperature_list.append(link)
        if not (w[1]['temperature']['min'] == None):
            tomorrow_temperature_max = w[1]['temperature']['max']['celsius']
            tomorrow_temperature_min = w[1]['temperature']['min']['celsius']
            link = [str(tomorrow_temperature_min) + " ℃", str(tomorrow_temperature_max) + " ℃"]
            tomorrow_temperature_list.append(link)
        else:
            link = ['e', 'e']
            tomorrow_temperature_list.append(link)
        time.sleep(60)
        if threading.main_thread().is_alive() == False:
            break

w = weather_livedoor()
today_weather = w[0]['telop']
tomorrow_weather = w[1]['telop']
PATH = 'lib/icons/'
today_weather = weather_dic[today_weather]
tomorrow_weather = weather_dic[tomorrow_weather]
link_tod = PATH + today_weather
link_tom = PATH + tomorrow_weather
tod_and_tom = [link_tod, link_tom]
weather_link_list.append(tod_and_tom)
if not (w[0]['temperature']['min'] == None):
    today_temperature_max = w[0]['temperature']['max']['celsius']
    today_temperature_min = w[0]['temperature']['min']['celsius']
    link = [str(today_temperature_min) + " ℃", str(today_temperature_max) + " ℃"]
    today_temperature_list.append(link)
else:
    link = ['e', 'e']
    today_temperature_list.append(link)
if not (w[1]['temperature']['min'] == None):
    tomorrow_temperature_max = w[1]['temperature']['max']['celsius']
    tomorrow_temperature_min = w[1]['temperature']['min']['celsius']
    link = [str(tomorrow_temperature_min) + " ℃", str(tomorrow_temperature_max) + " ℃"]
    tomorrow_temperature_list.append(link)
else:
    link = ['e', 'e']
    tomorrow_temperature_list.append(link)
