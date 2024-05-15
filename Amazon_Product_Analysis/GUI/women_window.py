from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

from scipy.ndimage.measurements import label
from Graph import women_pd

def button_clicked(index,women):
    if(index==0):
        return women_pd.show_graph(women,index)
    elif(index==1):
        return women_pd.show_graph(women,index)
    elif(index==2):
        return women_pd.show_graph(women,index)

def WomenNotebook(women):
    women.pack(expand=True)

    labels = []
    buttons = []
    list=["Kurtis","Sarees","Jeans"]

    image_paths = ["./images/women_kurti.webp","./images/women_saree.jpg","./images/women_jeans.webp"]
    images = [Image.open(path).resize((400,400)) for path in image_paths]
    photo_images = [ImageTk.PhotoImage(image) for image in images]

    for i in range(3):
        label = tk.Label(women, image=photo_images[i],bd=5,relief=SUNKEN)
        label.image=photo_images[i]
        labels.append(label)
        label.grid(row=0, column=i,padx=50,pady=20)

        button = tk.Button(women,font=("Courier",16,"bold"),bg="gold", text="Analyse " + list[i].format(i+1),command=lambda index=i: button_clicked(index,women),bd=5, relief=RAISED)
        buttons.append(button)
        button.grid(row=1, column=i)
