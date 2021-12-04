
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Text

import sys





window = Tk()


window.geometry("1152x700")
window.configure(bg = "#AEC0FF")


canvas = Canvas(
    window,
    bg = "#AEC0FF",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1109.0,
    700.0,
    fill="#AEC0FF",
    outline="")

canvas.create_text(
    609.0,
    75.0,
    anchor="nw",
    text="ContraGO",
    fill="#000000",
    font=("AplikaziaMFW Bold", 50 * -1)
)

canvas.create_text(
    609.0,
    142.0,
    anchor="nw",
    text="Log In",
    fill="#000000",
    font=("AplikaziaMFW Bold", 36 * -1)
)



entry_1 = Entry(
    window,
    bd=0,
    bg="#6A79FD",
    highlightthickness=0
)
entry_1.place(
    x=643.0,
    y=328.0,
    width=320.0,
    height=34.0
)




entry_2 = Entry(
    window, 
    bd=0,
    bg="#6A79FD",
    highlightthickness=0
)
entry_2.place(
    x=643.0,
    y=430.0,
    width=320.0,
    height=34.0
)



canvas.create_text(
    609.0,
    284.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("AplikaziaMFW Bold", 24 * -1)
)

canvas.create_text(
    609.0,
    383.0,
    anchor="nw",
    text="Password\n",
    fill="#000000",
    font=("AplikaziaMFW Bold", 24 * -1)
)



button_1 = Button(
    text="Submit",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: db.validationUser(entry_1, entry_2),
    relief="flat"
)

button_1.place(
    x=720.079833984375,
    y=508.1396484375,
    width=133.920166015625,
    height=46.8603515625
)




window.resizable(False, False)
window.mainloop()
