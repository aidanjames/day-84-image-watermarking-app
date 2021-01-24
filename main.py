from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
import tkinter.filedialog as fd
import os, sys


def load_image(filepath):
    global im
    global window
    global image_label
    im = Image.open(filepath)

    # Resize photo
    size = im.size
    resized = new_size(size)
    im = im.resize((resized[0], resized[1]), Image.ANTIALIAS)

    # Resize window
    new_window_geometry(resized)

    # Create the label
    tkim = ImageTk.PhotoImage(im)
    image_label = Label(window, image=tkim)
    image_label.image = tkim
    image_label.grid(row=4)



def new_size(size):
    ratio = size[1] / size[0]
    new_width = 600
    new_height = int(600 * ratio)
    return new_width, new_height

def new_window_geometry(image_size):
    window.geometry(f"{image_size[0] + 100}x{image_size[1] + 300}")


def select_image_from_file():
    file = fd.askopenfilename(title="Select an image file")
    load_image(file)



    # print(file)
    # open_image = PhotoImage(file=file)
    # canvas.itemconfig(photo_image, image=open_image)


def save_image_to_file():
    file_path = fd.asksaveasfilename()
    file_path += ".png"
    print(file_path)

    im.save(fp=file_path)

def enhance_contrast():
    # enh = ImageEnhance.Contrast(im)
    # enh.enhance(1.6).show("30% more contrast")
    im.rotate(45)
    tkim = ImageTk.PhotoImage(im)
    panel = Label(window, image=tkim)
    panel.image = tkim
    panel.grid(row=4)

im = Image.open("photo.png")

print(f"The type of im is {type(im)}")

window = Tk()
window.title("Watermarker")
window.config(padx=20, pady=20)
window.resizable(width=True, height=True)
window.geometry("800x800")

image_label = ""

load_image("photo.png")
open_file = Button(window, text='Open image', command=select_image_from_file).grid(row=1, columnspan=4)
enhance_image = Button(window, text='Add watermark', command=enhance_contrast).grid(row=2, columnspan=4)
save_image = Button(window, text='Save image', command=save_image_to_file).grid(row=3, columnspan=4)


# canvas = Canvas(width=600, height=500)
#
# open_image = PhotoImage(file="photo.png")
# try_this_one = PhotoImage(file="/Users/aidanpendlebury/Desktop/Royal Mail tracking FN 4947 7505 1GB .png")
#
# photo_image = canvas.create_image(280, 180, image=open_image)
# canvas.grid(column=1, row=0)
#
# open_file_button = Button(text="Select file", command=select_image_from_file)
# open_file_button.grid(column=2, row=3)
#
# save_image_button = Button(text="Save file", command=save_image_to_file)
# save_image_button.grid(column=1, row=3)




window.mainloop()

# Things that might be of use:

# Pillow (python imaging library)
# https://pypi.org/project/Pillow/

# tkinter.filedialog
# https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog

# Canvas stuff
# canvas = Canvas(window, width=1586, height=2554)
# canvas.pack()
#
# img = ImageTk.PhotoImage(Image.open("day82.png"))
# canvas.create_image(20, 20, anchor=NW, image=img)