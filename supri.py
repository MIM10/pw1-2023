# import package tkinter
from tkinter import *
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import ttk

# buat objek root dari class Tk
root = ttk.Window(themename="morph")

# atur lebar dan tinggi tampilan  aplikasi
root.geometry('500x500')

# atur title aplikasi
root.title("Aplikasi Penghitung Luas Segitiga")

# buat teks
ttk.Label(root, text="Aplikasi Penghitung Luas Segitiga").pack()

ttk.Label(root, text="Aplikasi Penghitung Luas Segitiga", font=('calibri', 15, 'bold')).pack()

ttk.Label(root, text="Masukan alas:").pack()

# buat input
alas = Entry()
alas.insert(END, 0)
alas.pack()

ttk.Label(root, text="Masukan tinggi ")

# buat input tinggi
tinggi = Entry()