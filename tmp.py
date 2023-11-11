import urllib.request
import urllib.parse
import urllib.error
import pygame
import sys
import threading
import pygame.font
import requests
from bs4 import BeautifulSoup
import easygui
import random
import lxml
from time import sleep
a = easygui.enterbox("введите 3 офсета через пробел",'взлом минекрафт')

def get_download_url():
    return "https://ice2.androeed.ru/files/2023/10/28/minecraftmainkraft-pocketedition-1593480628-www.androeed.ru.apk"

pygame.font.init()
 
SIZE = (wIDTH, HEIGHT) = (300, 300)
 
background = (18, 123, 5)
 
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Взлом MineCraft")
font = pygame.font.Font('freesansbold.ttf', 18)
text = font.render('Взламываем ваш майнкрафт...',
                   True, (255, 255, 255), background)
textRect = text.get_rect()
textRect.center = (150, 70)
textes = ['Взламываем ваш майнкрафт...', "Обманываем mojang",
    "Встраиваем скрипты", "Пропатчиваем главный класс", "Убиваем проверку лицензии"]
global_done = False
def download():
    global textes, global_done
    print('начало загрузки')
    download_url = get_download_url()
    urllib.request.urlretrieve(download_url, './взломанный_минекрафт.apk')
    print('загрузка завершена')
    textes = ['загрузка завершена']
    global_done = True
 
f = threading.Thread(target=download)
f.start()
 
 
play = True
progress = 0
pos = (10, 140)
width = 300
clock = pygame.time.Clock()
size = (280, 20)
loop = 60
steps = 0
done = False
counter = 0
while play:
	steps += 1
	if global_done:
		text = font.render('готово, загрузчик закроется автоматически', True, (255,255,255), background)
		textRect = text.get_rect()
		textRect.center = (150,70)
	if progress >= 1 and not global_done and steps>loop:
		steps = 0
		textes = ['идет настройка, подождите.','идет настройка, подождите..','идет настройка, подождите...']
		text = font.render(textes[counter],True, (255,255,255), background)
		counter+=1
		if counter >= 2:
			counter = 0
		textRect = text.get_rect()
		textRect.center = (150,70)
		done = True
	if steps > loop and not done and not global_done:
		steps = 0
		text = font.render(random.choice(textes), True, (255, 255, 255), background)
		textRect = text.get_rect()
		textRect.center = (150, 70)
	progress += 0.0025
	if progress>=1:
		progress = 1
	window.fill(background)
	window.blit(text, textRect)
	size = (width * progress, 20)
	rect = pygame.Rect(pos, size)
	pygame.draw.rect(window, (0, 0, 0), rect)
	pygame.display.flip()
	clock.tick(60)
	if global_done:
		play = False
		sleep(2)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			play = False
 
pygame.quit()