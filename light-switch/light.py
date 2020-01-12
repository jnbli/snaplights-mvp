from tkinter import *
from PIL import ImageTk, Image

root = Tk()

path = ["images/blackbulb.gif", "images/yellowbulb.gif"]

left_idx = 0
center_idx = 0
right_idx = 0

left_bulb = ImageTk.PhotoImage(Image.open(path[left_idx]))
center_bulb = ImageTk.PhotoImage(Image.open(path[center_idx]))
right_bulb = ImageTk.PhotoImage(Image.open(path[right_idx]))

left_panel = Label(root, image=left_bulb)
center_panel = Label(root, image=center_bulb)
right_panel = Label(root, image=right_bulb)

left_panel.pack(side="left", fill="both", expand="yes")
center_panel.pack(side="left", fill="both", expand="yes")
right_panel.pack(side="left", fill="both", expand="yes")


# def toggle_left(e):
def toggle_left():
    global left_idx
    left_idx = 1 - left_idx
    img2 = ImageTk.PhotoImage(Image.open(path[left_idx]))
    left_panel.configure(image=img2)
    left_panel.image = img2

def toggle_center():
    global center_idx
    center_idx = 1 - center_idx
    img2 = ImageTk.PhotoImage(Image.open(path[center_idx]))
    center_panel.configure(image=img2)
    center_panel.image = img2

def toggle_right():
    global right_idx
    right_idx = 1 - right_idx
    img2 = ImageTk.PhotoImage(Image.open(path[right_idx]))
    right_panel.configure(image=img2)
    right_panel.image = img2

def printty(e):
    print('yea')

# root.bind("<Left>", toggle_left)
# root.bind("<Down>", toggle_center)
# root.bind("<Right>", toggle_right)
root.bind("<Up>", printty)
# root.mainloop()

while True:

    tap_stat = ""
    with open('../clap-detection/clap_log.txt', 'r+') as f:
        if f.read() == 'tap!':
            with open('../gaze-detection/gaze_log.txt', 'r+') as g:
                gaze_direction = g.read()
                if gaze_direction == 'RIGHT':
                    toggle_left()
                    g.truncate(0)
                elif gaze_direction == 'CENTER':
                    toggle_center()
                    g.truncate(0)
                elif gaze_direction == 'LEFT':
                    toggle_right()
                    g.truncate(0)

            f.truncate(0)
            

    root.update()
