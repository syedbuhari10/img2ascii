import cv2
import math
import os
from time import time as timer, sleep
import sys
import Video_to_frames

def image2ascii(image):
    # image = cv2.imread('fumo-fuck-you.jpg', 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image.shape[0:2]
    aspect_ratio = width / height
    new_width = 40
    height, width = math.floor(new_width * aspect_ratio), math.floor(new_width * 2.5)
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    # luminosity_map = "⠀     ⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
    luminosity_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.         "
    luminosity_map = luminosity_map[::-1]
    lum_map_len = len(luminosity_map)

    ct = 0
    frame = ""
    for i in range(height):
        line = ""
        for j in range(width):
            if ct % width == 0:
                line += "\n"
            line += luminosity_map[math.floor(image[i, j] / 256 * lum_map_len)]
            ct += 1
        frame += line
    print(frame)
  

fps = 15
frame_time = 1 / fps
clear = lambda: os.system('clear')

path = os.getcwd()
frames_path = os.path.join(path, "frames")
# Video_to_frames.run_vid_to_frames("lagtrain.mp4", fps=15)
len_images = len(os.listdir(frames_path))



for image in range(len_images):
    # clear()
    start = timer() 
    cv2_image = cv2.imread(os.path.join(frames_path, str(image) + ".jpg"))
    image2ascii(cv2_image)
    print_time = timer() - start
    print(image)
    # if print_time < frame_time:
    print(["sleeping", frame_time - print_time])
    if frame_time - print_time > 0:
        print(f"sleeping for {frame_time - print_time}")
        sleep(frame_time - print_time)
