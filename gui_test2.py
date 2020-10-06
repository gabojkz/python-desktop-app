#!/usr/bin/env python3

from guizero import App, Text, CheckBox, Combo, ButtonGroup, PushButton, info

app = App(title="My second GUI app", width=300, height=200, layout="grid")


def do_booking():
    print( film_choice.value )
    print( vip_seat.value )
    print( row_choice.value )
    info("Booking", "Thank you for booking")


film_description = Text(app, 
                        text="Which film?", 
                        grid=[0, 0], 
                        align="left"
                    )
film_choice = Combo(app, 
                    options=["Star Wars", "Frozen", "Lion King"], 
                    grid=[1, 0], 
                    align="left", 
                    width=20
                )

seat_description = Text(app, 
                        text="Seat type", 
                        grid=[0, 1], 
                        align="left"
                    )
vip_seat = CheckBox(app, 
                    text="VIP seat?", 
                    grid=[1, 1], 
                    align="left"
                )

row_description = Text(app, 
                        text="Seat location", 
                        grid=[0, 2], 
                        align="left"
                    )
row_choice = ButtonGroup(app, 
                        options=[["Front", "F"], ["Middle", "M"], ["Back", "B"]],
                        selected="M", 
                        horizontal=True, 
                        grid=[1, 2], 
                        align="left")

PushButton(app, command=do_booking, text="Book seat", grid=[1,3], align="left")

app.display()
