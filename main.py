#!/usr/bin/env python3

from guizero import App, Text, TextBox, PushButton, Slider, Picture


def say_my_name():
    welcome_message.value = my_name.value
    return my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title="Hello world")

welcome_message = Text(app, text="Hola paula como estais?")

Text(app, "some message", size=40, color="blue")

my_name = TextBox(app, width=2000)

update_text = PushButton(app, command=say_my_name, text="Display my name")

text_size = Slider(app, command=change_text_size, start=10, end=80)

my_cat = Picture(app, image="2b1fc52d1d08a6a625ffe6b0eb69b8b2.gif")

app.display()
