"""
GUI Implementation of spike timer.
Currently supports 1920x1080 screens.
To support other screen resolutions, the code must be tweaked.
"""

import cv2 as cv
import numpy as np
import mss
import time
from PIL import Image, ImageGrab
import tkinter as tk
from tkinter import ttk

running = False

spike_img = cv.imread(r'C:\Users\Gokul Ram\Desktop\Spike Timer\spike1.jpg')

def check_spike(img): #Funtion that checks if the spike is planted or not.
    result = cv.matchTemplate(img,spike_img,cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if max_loc == (4,2) and max_val > 0:
        return True
    else:
        return False

def grab_screen(): #Function that continuosly takes screenshots.
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 14, "left": 914, "width": 90, "height": 93}
        # Grab the data
        sct_img = sct.grab(monitor)
        p_img = np.array(Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX'))
        p_img = p_img[:, :, ::-1].copy()
        return p_img

def main_task():
    global running
    while running:
        if check_spike(grab_screen()):
            spike_status_label.configure(text = "Spike Status: Planted!", fg = "green")
            start_countdown()
            timer_label.configure(text = "00")
            spike_status_label.pack_forget()
            running = False
            

def start_countdown():
    print("Planted!")
    countdown_time = 40
    while countdown_time >= 0 and running:
        timer_label.configure(text = str(countdown_time))
        time.sleep(1)
        countdown_time -= 1
    
def start():
    spike_status_label.pack(padx = 50)
    global running
    running = True

def reset():
    global running
    running = False

# Tkinter gui stuff
root = tk.Tk()
root.title("Spike Timer")
root.geometry("400x220")
button_style = ttk.Style()
button_style.configure('TButton',font = ("Poppins",14))
timer_label = tk.Label(root,text="00",font="DS-Digital 56")
timer_label.pack(padx = 40, pady = 13)
spike_status_label = tk.Label(root,text="Spike Status: Not Planted",font="Poppins 16", fg = 'red')
button_frame = tk.Frame(root)
button_frame.pack(pady = 10)
start_button = ttk.Button(button_frame,style = 'TButton',text = "Start",takefocus = False, command = start)
start_button.pack(side = tk.LEFT,padx = 7)
reset_button = ttk.Button(button_frame,style = 'TButton',text = "Reset",takefocus = False, command = reset)
reset_button.pack(side = tk.LEFT)
root.after(400, main_task)
root.mainloop()