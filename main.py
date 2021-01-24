from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter.filedialog as fd
import tkinter.simpledialog as sd


def load_image(filepath):
    global im
    im = Image.open(filepath)

    # Resize photo
    size = im.size
    resized = calculate_new_image_size(size)
    im = im.resize((resized[0], resized[1]), Image.ANTIALIAS)

    # Resize window
    window.geometry(f"{resized[0] + 50}x{resized[1] + 200}")

    show_image_in_label(im)


def calculate_new_image_size(size):
    ratio = size[1] / size[0]
    new_width = 600
    new_height = int(600 * ratio)
    return new_width, new_height


def show_image_in_label(image):
    # Get rid of old label
    labels = window.grid_slaves(row=2)
    for label in labels:
        label.destroy()

    # Create the label
    tkim = ImageTk.PhotoImage(image)
    image_label = Label(window, image=tkim)
    image_label.image = tkim
    image_label.grid(row=2, columnspan=3, pady=30)


def select_image_from_file():
    file_path = fd.askopenfilename(title="Select an image file")
    if file_path:
        add_watermark_button.config(state="normal")
        save_image_button.config(state="normal")
        load_image(file_path)


def save_image_to_file():
    file_path = fd.asksaveasfilename()
    if file_path:
        file_path += ".png"  # I need to do better with this
        im.save(fp=file_path)


def add_watermark():
    global im
    watermark_text = sd.askstring("Input", "Watermark text:", parent=window)
    if watermark_text:
        base = im.convert('RGBA')
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
        font = ImageFont.truetype('acherusgrotesque-regular.otf', 50)
        draw = ImageDraw.Draw(txt)
        draw.text((50, 50), watermark_text, font=font, fill=(255, 255, 255, 128))
        im = Image.alpha_composite(base, txt)
        show_image_in_label(im)


# Global variable for the image object
im = Image.open("photo.png")

# Create the tkinter window
window = Tk()
window.title("Watermarker")
window.config(padx=20, pady=20)
window.resizable(width=True, height=True)
window.geometry("800x800")

# Load up the widgets
load_image("photo.png")
open_file = Button(window, text='Open image', command=select_image_from_file).grid(row=1, column=0)
add_watermark_button = Button(window, text='Add watermark', command=add_watermark)
add_watermark_button.grid(row=1, column=1)
add_watermark_button.config(state="disabled")
save_image_button = Button(window, text='Save image', command=save_image_to_file)
save_image_button.grid(row=1, column=2)
save_image_button.config(state="disabled")

window.mainloop()
