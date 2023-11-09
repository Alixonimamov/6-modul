# This is a sample Python script.
import time
import tkinter
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# from tkinter import *
# import random
#
# window=Tk()
#
#
# canvas=Canvas(window ,width=600, height=600, background="blue")
# canvas.pack()
#
# score=0
#
# score_label= Label(window, text=f"Score: {score}",font="Arial 30")
# score_label.pack()
#
# savatcha=canvas.create_rectangle(270, 550, 330, 580, fill="green")
#
# objects=[]
#
# for i in range(6):
#     x=random.randint(0, 590)
#     y= random.randint(10, 50)
#
#     objects.append(canvas.create_oval(x, y, x+10, y+10, fill="white"))
#
# def move_basket(event):
#     if event.keysym=="Right":
#         canvas.move(savatcha, 20, 0)
#     if event.keysym=="Left":
#         canvas.move(savatcha, -20, 0)
#
# def move_objects():
#     global score
#     for i in objects:
#         canvas.move(i, 0, 10)
#
#         pos=canvas.coords(i)
#         print(pos[3])
#         if pos[3]>=600:
#             x = random.randint(0, 590)
#             y = random.randint(10, 50)
#             canvas.coords(i, x, y, x+10, y+10)
#         elif len(canvas.find_overlapping(*canvas.coords(savatcha)))>1:
#             x = random.randint(0, 590)
#             y = random.randint(10, 50)
#             canvas.coords(i, x, y, x + 10, y + 10)
#             score+=1
#             score_label.config(text=f"Score {score}")
#     window.after(50, move_objects)
#
#
#
# move_objects()
# canvas.bind_all("<Key>", move_basket)
#
#
#
#
#
#
# window.mainloop()


# import tkinter
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# window=Tk()
# window.geometry("900x900")
# window.title("www.plus2net.com")
#
# filename=filedialog.asksaveasfilename(title="Saqlang", filetypes=[("Text Files", "*.txt")], defaultextension=".txt")
#
# if filename:
#     with open(filename, "w") as file:
#         file.write("hello world")
#     print(f"Fayl saqlandi: {filename}")
# else:print("Bekor qilindi")
#
#
#
#
#
# label=Label(window, text="Add Products", font="Arial 50")
# label.pack()
#
# label=Label(window, text="category", font="Arial 30", fg="blue")
# label.place(x=20, y=100)
#
# label=Label(window, text="Vegetables")
# label.place(x=190, y=100)
#
# combo=ttk.Combobox(window, values=["kartoshka", "piyoz", "baklagan"])
# combo.place(x=190, y=120)
#
# label=Label(window, text="Product", font="Arial 30", fg="Blue")
# label.place(x=20, y=180)
#
# entry=Entry(window, font="Arial 20", width=20)
# entry.place(x=190, y=190)
#
# label=Label(window, text="Size", font="Arial 30", fg="Blue")
# label.place(x=20, y=250)
#
# entry=Entry(window, font="Arial 20", width=20)
# entry.place(x=190, y=250)
#
# label=Label(window, text="Supplier", font="Arial 30", fg="Blue")
# label.place(x=20, y=320)
#
# label=Label(window, text="Raju")
# label.place(x=190, y=310)
#
# combo=ttk.Combobox(window, values=["Coca cola", "Pepsi", "Lays", "Fanta"])
# combo.place(x=190, y=340)
#
# label=Label(window, text="Stock", font="Arial 30")
# label.place(x=20, y=390)
#
# spinbox=ttk.Spinbox(window, from_=1, to=50)
# spinbox.place(x=190, y=405)
#
# label=Label(window, text="Price" ,font="Arial 30")
# label.place(x=20, y=450)
#
# entry=Entry(window, font="Arial 20", width=20)
# entry.place(x=190, y=460)
#
# window.mainloop()


# from tkinter import *
# from tkinter import messagebox
# from random import shuffle
#
# window=Tk()
# window.title("Xotira O'yin")
# window.geometry("1000x800")
#
# time_remaining=5
#
# time_label=Label(window, text=f"Time remainig {time_remaining}", font="Arial 24")
# time_label.pack(pady=20)
#
# blank_image=PhotoImage(file="img_1.png")
#
# image_files=["img_1.png", "img_2.png", "img_3.png", "img_4.png"]
# images=[PhotoImage(file=image) for image in image_files]
#
# images=images+images
#
# shuffle(images)
#
# def time_update():
#     global time_remaining
#     time_remaining-=1
#     time_label.config(text=f"Time remainig {time_remaining}")
#
#     if time_remaining==0:
#         messagebox.showinfo(title="Xabar", message="Times up")
#         window.destroy()
#
#
#     window.after(1000, time_update)
#
# def click_button():
#
#
# button_frame=Frame(window)
# button_frame.pack()
#
# buttons=[]
# clicked_buttons=[]
#
# for i in range(8):
#     button=Button(button_frame, width=200,height=200, image=blank_image)
#     button.grid(row=i//4, column=i%4, padx=20, pady=20)
#     buttons.append(button)
#
#
#
#
#
#
#
# time_update()
# window.mainloop()

# from tkinter import *
# from tkinter import Label
# import time
# import sys
# window=Tk()
# window.title("Digital clock")
#
# def get_time():
#     timeVar=time.strftime("%I:%M:%S %p")
#     clock.config(text=timeVar)
#     clock.after(200, get_time)
#
#
# clock=Label(window, font=("Arial", 100),bg="Black", fg="green")
# clock.pack()
#
# get_time()
#
#
#
#
#
# window.mainloop()

# from tkinter import *
# from tkinter import filedialog
#
# window=Tk()
# window.geometry("600x600")
#
# filename=filedialog.asksaveasfilename(title="Saqlang", filetypes=[("Text Files", "*.txt")], defaultextension="*.txt")
#
# if filename:
#     with open(filename, "w") as file:
#         file.write("im Alixon im student school N171 and PDP Junior")
#     print(f"Fayl saqlandi: {filename}")
#
# else:
#     print("Bekor qilinid")
#
# window.mainloop()

