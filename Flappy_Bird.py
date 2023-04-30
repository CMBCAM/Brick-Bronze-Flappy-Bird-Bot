# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 00:22:19 2023

@author: cam
"""

from PIL import ImageGrab
from PIL import ImageColor
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import time
import mouse

"""CHECK RGB VALUE"""
def check_rgb(rgb,rgb_range):
    if (rgb[0] >= rgb_range[0] and rgb[0] <= rgb_range[3] and rgb[1] >= rgb_range[1] and rgb[1] <= rgb_range[4] and rgb[2] >= rgb_range[2] and rgb[2] <= rgb_range[5]):
        return True
    else:
        return False
    
rgb_range = [(180,113,58,242,136,70), #beak 0
          (30,70,240,64,134,255), #sky 1
          (200,200,200,255,255,255),#white 2
          (109,79,50,150,111,81), #wood 3
          (125,65,65,135,78,78),#mouth 4
          (74,164,98,74,164,98) #buttron 5
          ]
print('Press Enter To Begin, Switch to Game Screen Immediatly After:')
input()
time.sleep(2)
t0 = time.time()
image = ImageGrab.grab()
#print (time.time()-t0)
#image.show("Screen")
#image.save("Test.png")
imagex = image.size[0]
imagey = image.size[1]
values = []
#f = open("color_output.txt","w")
#f.close()
#f = open("color_output.txt","a")
#for y in range(75, 1004, 7):
 #   for x in range(349, 1570, 7):
 #       color = image.getpixel((x, y))
  #      values.append(color)
 #       text = str(color[0]) + " " + str(color[1]) + " " + str(color[2]) + "\n"
   #     f.write(text)
        #rgb = (color[0]/255,color[1]/255,color[2]/255)
        #plt.bar(xs, ys, color=rgb)
       # plt.show()
       # print(color)
#print(time.time() - t0)
#f.close()
"""TRACK ROWLET"""

def find_rowlet(image,rowlet_y):
    for y in range(75, 1004, 6):
        for x in range(699, 808, 6):
            color = image.getpixel((x, y))
            if check_rgb(color, rgb_range[0]):
                #print("rowlet:",y)
                return y
    else:
        #print("failed to locate rowlet")
        return -1
#print(time.time() - t0)
"""TRACK EXEGGUTOR"""
def find_walls(image):
    for x in range(800,1222+303,1):
        color = image.getpixel((x,76))
        if check_rgb(color, rgb_range[3]):
            #print("tree:",x)
            return x
    else:
        #print('no tree')
        return -1

def find_gap(image,x):
    for y in range(75,630,1):
        color = image.getpixel((x + 30,y))
        if check_rgb(color, rgb_range[4]):
            return (y + 76 + 175)
    else:
        return -1

def click():
    mouse.click()
def play(rowlet_y,target,time_click):
    if (rowlet_y > target) or (time_click > 4) or (1004 - rowlet_y < 350):
        #CLICK
        if (target - rowlet_y < 250):
            click()
        return True
    else:
        #DONT CLICK
        return False
cycle = 0
rowlet_y =  540
rowlet_x = 800
target = 540
time_since_click = 0
wallx = -1
t1 = time.time()
def click_button(image):
    for y in range(0,1080,5):
        for x in range (0,1920,10):
            color = image.getpixel((x,y))
            if check_rgb(color, rgb_range[5]):
                mouse.move(x + 120,y+20,True,1)
                time.sleep(0.2)
                click()
                click()
                click()
                time.sleep(4)
                return True
    else:
        return False
###PLAY PHASE
while True:
    while True:
        t0 = time.time()
        image = ImageGrab.grab()
        if cycle== 3:
            temp = find_walls(image)
            if temp != -1:
                wallx = temp
                temp = find_gap(image,wallx)
                if temp != -1:
                    target = temp
            #print("Target:", target)
            #image.save(str(target) +".png")
            cycle = 0
        temp = find_rowlet(image, rowlet_y)
        if temp != -1:
            rowlet_y = temp
        #else:
            #print("Could not find Rowlet! :( please find rowlet before continuing...")
            #input()
            #break
        #print("Rowlet:",rowlet_y)
        if(play(rowlet_y,target,time_since_click)):
            time_since_click = 0
        else:
            time_since_click += 1
        if(time.time()-t0 < 0.1):
            time.sleep(0.1 - (time.time() - t0))
        #print(time.time() - t0)
        cycle+=1
        #print(time.time() - t0)
        if (rowlet_y >= 950):
            print('Survived for',time.time()-t1,'seconds!')
            break
    time.sleep(10)
    image = ImageGrab.grab()
    if click_button(image) == False:
        print("auhodfdghyuasgysa")
        break
        
# =============================================================================
# f = open("top_output.txt","w")
# f.close()
# f = open("top_output.txt","a")
# for x in range(403, 1222, 1): #up to rowlet (403 cropped) - (1222-43)cropped
#     color = image.getpixel((x+349, 76))
#     text = str(color[0]) + " " + str(color[1]) + " " + str(color[2]) + "\n"
#     f.write(text)
# print(time.time() - t0)
# f.close()
# =============================================================================

#rgb = (color[0]/255,color[1]/255,color[2]/255)
##plt.bar(xs, ys, color=rgb)
input()
"""TO DO"""
# -Calculate Rowlet cetner using x and y pixel shit
# -the exeguutor stuff
# -figure out inputs????
# -constrain and optimize calc time
# - y axis only cause track bird