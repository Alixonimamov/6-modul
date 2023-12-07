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


# class Car:
#
#     def __init__(self, yil, model, rangi, nomi):
#         self.yil = yil
#         self.model = model
#         self.rangi = rangi
#         self.nomi=nomi
#
#     def harakatlan(self, tezligi):
#         return f"{self.model}, harakatlanyapti {tezligi} km/h tezlikda"
#
#     def eshiq_ochilsin(self):
#         return f"{self.model} eshigi ochildi"
#
#
# ferrari = Car("2023", "G480", "qizil", "Ferrari")
#
# print(f"Moshina yili {ferrari.yil}\n"
#       f"Moshina rangi {ferrari.rangi}\n"
#       f"Moshina modeli {ferrari.model}\n"
#       f"Moshina nomi {ferrari.nomi}")
#
# print(ferrari.harakatlan(420))
# print(ferrari.eshiq_ochilsin())


# class Xayvon:
#     def __init__(self, yoshi, rangi, nomi):
#         self.yoshi=yoshi
#         self.rangi=rangi
#         self.nomi=nomi
#
#     def aviladi(self):
#         return f"{self.nomi} aviladi"
#
# kuchuk=Xayvon("5","qora", "Buldok")
#
# print(f"yoshi {kuchuk.yoshi}\n"
#       f"rangi {kuchuk.rangi}\n"
#       f"nomi {kuchuk.nomi}\n")
# print(kuchuk.aviladi())

#Homework
#dog
# class Xayvon:
#     def __init__(self, yoshi, rangi, nomi):
#         self.yoshi=yoshi
#         self.rangi=rangi
#         self.nomi=nomi
#
#     def aviladi(self):
#         return f"{self.nomi} vav vav kildi"
#
# kuchuk=Xayvon("5","qora", "Buldok")
#
# print(f"yoshi {kuchuk.yoshi}\n"
#       f"rangi {kuchuk.rangi}\n"
#       f"nomi {kuchuk.nomi}\n")
# print(kuchuk.aviladi())






#cat
# class Xayvon:
#     def __init__(self, yoshi, rangi, nomi):
#         self.yoshi=yoshi
#         self.rangi=rangi
#         self.nomi=nomi
#
#     def miavladi(self):
#         return f"{self.nomi} miav miav kildi"
#
# mushuk=Xayvon("1","oq", "Bobik")
#
# print(f"yoshi {mushuk.yoshi}\n"
#       f"rangi {mushuk.rangi}\n"
#       f"nomi {mushuk.nomi}\n")
# print(mushuk.miavladi())








#Horse
# class Xayvon:
#     def __init__(self, yoshi, rangi, nomi):
#         self.yoshi=yoshi
#         self.rangi=rangi
#         self.nomi=nomi
#
#     def igaga(self):
#         return f"{self.nomi} igagaga kildi"
#
# horse=Xayvon("10","gigarang", "biser")
#
# # print(f"yoshi {horse.yoshi}
#
#
#
#
# class Odam:
#      def __init__(self, yoshi, sinfi, ismi):
#          self.yoshi=yoshi
#          self.sinfi=sinfi
#          self.ismi=ismi
#
#      # def miavladi(self):
#      #     return f"{self.nomi} miav miav kildi"
#
# mushuk=Odam("10","4D", "Jimmy")
#
# print(f"yoshi {mushuk.yoshi}\n"
#        f"sinfi {mushuk.sinfi}\n"
#        f"ismi {mushuk.ismi}\n")
# # print(mushuk.miavladi()
#
#
# class Odam:
#     def __init__(self, yoshi, sinfi, ismi):
#         self.yoshi = yoshi
#         self.sinfi = sinfi
#         self.ismi=ismi
#
#     # def miavladi(self):
#     #     return f"{self.nomi} miav miav kildi"
#
#
# mushuk = Odam("15", "9v", "Gabriel")
#
# print(f"yoshi {mushuk.yoshi}\n"
#       f"sinfi {mushuk.sinfi}\n"
#       f"ismi {mushuk.ismi}\n")


# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
#         self.history=[]
#
#     def deposit(self,amout):
#         self.__balance+=amout
#         self.history.append(f"{self.owner} uchun {amout}$ miqdorda pul qoshildi\n"
#                             f"Yangi balans {self.__balance}")
#
#         print(f"{self.owner} uchun {amout}$ miqdorda pul qoshildi")
#
#     def takeoff(self,amout):
#         if amout > self.__balance:
#             print(f"Mablaq' yetarli emas! Xozirgi balans {self.__balance}")
#         else:
#             self.__balance-=amout
#             self.history.append(f"{self.owner} uchun {amout}$ miqdorda pul yechip olindi")


# from abc import ABC,abstractmethod
#
#
# class Animal(ABC):
#     def __init__(self, name):
#         self.name=name
#
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Cat(Animal):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def make_sound(self):
#         print(f"{self.name},Salom")
#
# animal1=Cat("Mushuk")
# animal1.make_sound()
#

# from abc import ABC,abstractmethod
# class Person(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#ё
#
# class Student(Person):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_sound(self):
#         print(f"{self.name},Salom")
#
#
# Student=Student("Alixon")
# Student.make_sound()

 # with open("my_file.txt","w")as f:
 #    print(f.write("Umar\n"
 #                  "Muhammadali\n"
 #                  "Kamron"))




import pygame

pygame.init()

pygame.display.set_caption("My_Game")
screen=pygame.display.set_mode((400,500),pygame.RESIZABLE)

icon=pygame.image.load("C:\\Users\\hp-Alixon\\PycharmProjects\\6-modul\\img_7.png")
pygame.display.set_icon(icon)

white=pygame.Color("#ffff00")
running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        screen.fill(white)
        pygame.display.update()







pygame.quit()