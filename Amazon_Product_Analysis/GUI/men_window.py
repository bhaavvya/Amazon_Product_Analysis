from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

from scipy.ndimage.measurements import label
from Graph import men_pd

def button_clicked(index,men):
    if(index==0):
        return men_pd.show_graph(men,index)
    elif(index==1):
        return men_pd.show_graph(men,index)
    elif(index==2):
        return men_pd.show_graph(men,index)

def MenNotebook(men):
    men.pack(expand=True)

    labels = []
    buttons = []
    list=["Shirts","T-Shirts","Jeans"]

    image_paths = ["./images/men_shirt.webp", "./images/men_tshirt.webp", "./images/men_jeans.webp"]
    images = [Image.open(path).resize((400,400)) for path in image_paths]
    photo_images = [ImageTk.PhotoImage(image) for image in images]

    for i in range(3):
        label = tk.Label(men, image=photo_images[i],bd=5,relief=SUNKEN)
        label.image=photo_images[i]
        labels.append(label)
        label.grid(row=0, column=i,padx=50,pady=20)

        button = tk.Button(men,font=("Courier",16,"bold"),bg="gold", text="Analyse " + list[i].format(i+1),command=lambda index=i: button_clicked(index,men),bd=5, relief=RAISED)
        buttons.append(button)
        button.grid(row=1, column=i)
