#!/usr/bin/env python3

from guizero import App, Text, TextBox, PushButton, Slider, Picture, info, system_config, Window, Box
import time
from _thread import *
from tkinter import Spinbox
from tkinter.ttk import Progressbar

__all__ = ("error", "LockType", "start_new_thread", "interrupt_main", "exit", "allocate_lock", "get_ident", "stack_size", "acquire", "release", "locked")


app = App(title="Countdown", layout="grid")

print(system_config.supported_image_types)

def print_time(time):
    counter_description.value = time

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r")
        print_time(timer)
        time.sleep(1) 
        t -= 1

    info(app, 'Fire in the hole!!') 

counter_description = TextBox(app, text="Time:", grid=[0, 0], align="left")

# start_new_thread( countdown, (10, ) )


box = Box(app, border=True, grid=[0, 3])

# add a progress bar to the boc
pb = Progressbar(box.tk)
box.add_tk_widget(pb)
pb.start()


app.display()
