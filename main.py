from lib import get_image, transform_image, info
import pygame
from pygame.locals import *
import sys
import time
import threading
import datetime
import configparser
import gd_sync

count = [0, 0]

def counter():
    global count
    del count[-1]
    count.append(1)

def main():
    config = configparser.RawConfigParser()
    config.read("setting.ini")
    w = int(config.items("DISPLAY")[0][1])
    h = int(config.items("DISPLAY")[1][1])
    display_time = int(config.items("DISPLAY_TIME")[0][1])
    mode = str(config.items("DISPLAY_MODE")[0][1])
    Font = 'lib/font/NotoSansCJKsc-Regular.otf'
    bg_size = (w, round(h / 6))
    pygame.init()
    pygame.display.set_mode((w, h), FULLSCREEN)
    screen = pygame.display.get_surface()
    pygame.mouse.set_visible(False)
    bg = pygame.image.load('lib/bg.png').convert_alpha()
    bg = pygame.transform.smoothscale(bg, bg_size)
    rect_bg = bg.get_rect()
    date_font = pygame.font.Font(Font, 35)
    time_font = pygame.font.Font(Font, 80)
    temperature_font = pygame.font.Font(Font, 50)
    path = get_image.PATH
    image_list = get_image.filename_list(mode)
    iw_ih = get_image.size_list(image_list)
    get_weather = threading.Thread(target = info.get_weather)
    get_weather.start()
    get_temperature = threading.Thread(target = info.get_temperature)
    get_temperature.start()
    #sync = threading.Thread(target = gd_sync.sync)
    #sync.start()
    while True:
        for index, image in enumerate(image_list):
            file_directory_and_name = path + '/' + image
            image = pygame.image.load(file_directory_and_name).convert()
            iw = iw_ih[index][0]
            ih = iw_ih[index][1]
            transform_size = transform_image.transform(w, h, iw, ih)
            image = pygame.transform.smoothscale(image, transform_size)
            weather = info.weather_link_list[-1]
            today_weather_icon = pygame.image.load(weather[0]).convert_alpha()
            today_weather = pygame.transform.smoothscale(today_weather_icon, (100, 100))
            today_temperature = info.today_temperature_list[-1]
            today_temperature_min = temperature_font.render(today_temperature[0], True, (255,255,255))
            today_temperature_max = temperature_font.render(today_temperature[1], True, (255,255,255))
            tomorrow_weather_icon = pygame.image.load(weather[1]).convert_alpha()
            tomorrow_weather = pygame.transform.smoothscale(tomorrow_weather_icon, (100, 100))
            tomorrow_temperature = info.tomorrow_temperature_list[-1]
            tomorrow_temperature_min = temperature_font.render(tomorrow_temperature[0], True, (255,255,255))
            tomorrow_temperature_max = temperature_font.render(tomorrow_temperature[1], True, (255,255,255))
            rect_image = image.get_rect()
            rect_image.center = (w / 2, h / 2)
            rect_bg.center = (w / 2, h-50)
            rect_today_weather = today_weather.get_rect()
            rect_today_weather.bottomleft = (w / 8, h - 10)
            rect_tomorrow_weather = tomorrow_weather.get_rect()
            rect_tomorrow_weather.bottomright = (round((7 * w ) / 8), h - 10)
            rect_today_temperature_min = today_temperature_min.get_rect()
            rect_today_temperature_min.bottomleft = (320, h-60)
            rect_today_temperature_max = today_temperature_max.get_rect()
            rect_today_temperature_max.bottomleft = (320, h - 5)
            rect_tomorrow_temperature_min = tomorrow_temperature_min.get_rect()
            rect_tomorrow_temperature_min.bottomright = (w - 320, h - 60)
            rect_tomorrow_temperature_max = tomorrow_temperature_max.get_rect()
            rect_tomorrow_temperature_max.bottomright = (w - 320, h - 5)
            screen.fill((0, 0, 0, 0))
            screen.blit(image, rect_image)
            screen.blit(bg, rect_bg)
            pygame.display.update()
            wait = threading.Timer(display_time, counter)
            wait.start()
            while count[-1] == 0:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                nowtime = datetime.datetime.now()
                yad = date_font.render(info.get_datetime(nowtime)[0], True, (255,255,255))
                rect_yad = yad.get_rect()
                rect_yad.center = (w / 2, h-100)
                ham = time_font.render(info.get_datetime(nowtime)[1], True, (255,255,255))
                rect_ham = ham.get_rect()
                rect_ham.center = (w / 2, h-40)
                screen.blit(image, rect_image)
                screen.blit(bg, rect_bg)
                screen.blit(yad, rect_yad)
                screen.blit(ham, rect_ham)
                screen.blit(today_weather, rect_today_weather)
                screen.blit(tomorrow_weather, rect_tomorrow_weather)
                screen.blit(today_temperature_min, rect_today_temperature_min)
                screen.blit(today_temperature_max, rect_today_temperature_max)
                screen.blit(tomorrow_temperature_min, rect_tomorrow_temperature_min)
                screen.blit(tomorrow_temperature_max, rect_tomorrow_temperature_max)
                pygame.display.update(rect_bg)
                pygame.time.wait(200)
            count.append(0)


if __name__ == '__main__':
    main()
