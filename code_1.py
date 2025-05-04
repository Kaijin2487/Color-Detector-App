import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

root = tk.Tk()
root.title("Color Picker from Image")
root.geometry("800x470+100+100")
root.configure(bg="#e4ebeb")
root.resizable(False, False)

def showimage():
    global filename, lbl
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image File',
        filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'), ('All files', '*.*'))
    )
    img = Image.open(filename)
    img = img.resize((310, 270))  # Resize image to fit canvas
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

def Findcolor():
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    colors_rgb = palette[:10]
    colors_hex = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in colors_rgb]

    for i, color in enumerate(colors_hex):
        if i < 5:
            colors.itemconfig(ids[i], fill=color)
            hex_labels[i].config(text=color)
        else:
            colors2.itemconfig(ids[i], fill=color)
            hex_labels[i].config(text=color)

# Icon
image_icon = ImageTk.PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# Top Bar
tk.Label(root, width=120, height=2, bg="#42729f").pack()

# Frame
frame = tk.Frame(root, width=760, height=370, bg="#fff")
frame.place(x=20, y=50)

# Logo
logo = ImageTk.PhotoImage(file="logo.png")
tk.Label(frame, image=logo, bg="#fff").place(x=10, y=10)

# Color Panel 1
colors = tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors.place(x=20, y=90)

ids = []
ids.append(colors.create_rectangle((10, 10, 50, 50), fill="#b8255f"))
ids.append(colors.create_rectangle((10, 50, 50, 100), fill="#db4035"))
ids.append(colors.create_rectangle((10, 100, 50, 150), fill="#ff9933"))
ids.append(colors.create_rectangle((10, 150, 50, 200), fill="#fad000"))
ids.append(colors.create_rectangle((10, 200, 50, 250), fill="#afb83b"))

hex_labels = []
hex_labels.append(tk.Label(colors, text="#b8255f", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[0].place(x=60, y=15)

hex_labels.append(tk.Label(colors, text="#db4035", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[1].place(x=60, y=65)

hex_labels.append(tk.Label(colors, text="#ff9933", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[2].place(x=60, y=115)

hex_labels.append(tk.Label(colors, text="#fad000", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[3].place(x=60, y=165)

hex_labels.append(tk.Label(colors, text="#afb83b", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[4].place(x=60, y=215)

# Color Panel 2
colors2 = tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors2.place(x=180, y=90)

ids.append(colors2.create_rectangle((10, 10, 50, 50), fill="#7ecc49"))
ids.append(colors2.create_rectangle((10, 50, 50, 100), fill="#299438"))
ids.append(colors2.create_rectangle((10, 100, 50, 150), fill="#6accbc"))
ids.append(colors2.create_rectangle((10, 150, 50, 200), fill="#158fad"))
ids.append(colors2.create_rectangle((10, 200, 50, 250), fill="#14aaf5"))

hex_labels.append(tk.Label(colors2, text="#7ecc49", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[5].place(x=60, y=15)

hex_labels.append(tk.Label(colors2, text="#299438", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[6].place(x=60, y=65)

hex_labels.append(tk.Label(colors2, text="#6accbc", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[7].place(x=60, y=115)

hex_labels.append(tk.Label(colors2, text="#158fad", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[8].place(x=60, y=165)

hex_labels.append(tk.Label(colors2, text="#14aaf5", fg="#000", font="arial 12 bold", bg="white"))
hex_labels[9].place(x=60, y=215)

# Select Image Panel
selectimage = tk.Frame(frame, width=340, height=350, bg="#d6dee5")
selectimage.place(x=350, y=10)

f = tk.Frame(selectimage, bd=3, bg="black", width=320, height=280, relief=tk.GROOVE)
f.place(x=10, y=10)

lbl = tk.Label(f, bg="black")
lbl.place(x=0, y=0)

tk.Button(selectimage, text="Select Image", width=12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
tk.Button(selectimage, text="Find Colors", width=12, height=1, font="arial 14 bold", command=Findcolor).place(x=176, y=300)

root.mainloop()
