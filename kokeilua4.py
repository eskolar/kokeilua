import os
import tkinter as tk
from PIL import Image, ImageTk
#from tkinter import *
import numpy as np
import csv

path1 = "/Users/riikkaeskola/Documents/pictures/"
listing = os.listdir(path1)
apustus = len(listing)

lista_elukoista = ["kirahvi", "jellona", "ronsu", "seepra", "virtahepo"]
apustus2 = len(lista_elukoista)


class App:
    def __init__(self, master=tk.Tk()):
        self.ind = 0
        self.elukat = np.empty((apustus,apustus2),dtype=int)
        self.kuvanimi = np.empty(apustus,dtype=object)
        #self.tatat = np.array([elukat,kuvanimi])
        self.master = master
        self.fig_size = [1000, 760]
        self.pic_size =[750, 400]
        self.frame = tk.Frame(master)
        self.canvas = tk.Canvas(self.frame, width=1280, height=800)
        self.canvas.pack()

        self.load_image(path1 + listing[self.ind])
        self.image_label = tk.Label(self.canvas, image=self.fig_image)
        self.image_label.pack()

        self.elukkata = [0,0]
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()

        self.eka = tk.Checkbutton(self.frame, text="kiraffi", variable = self.var1, onvalue=1, offvalue=0)#variable=self.elukkata[0])
        self.eka.pack(fill=tk.Y)
        self.eka.config(font=("Arial", 30))
        self.toka = tk.Checkbutton(self.frame, text="jellona", variable = self.var2, onvalue=1, offvalue=0)#variable=self.elukkata[1])
        self.toka.pack(fill=tk.Y)
        self.toka.config(font=("Arial", 30))
        self.kolmas = tk.Checkbutton(self.frame, text="ronsu", variable = self.var3, onvalue=1, offvalue=0)#variable=self.elukkata[0])
        self.kolmas.pack(fill=tk.Y)
        self.kolmas.config(font=("Arial", 30))
        self.neljas = tk.Checkbutton(self.frame, text="seepra", variable = self.var4, onvalue=1, offvalue=0)#variable=self.elukkata[1])
        self.neljas.pack(fill=tk.Y)
        self.neljas.config(font=("Arial", 30))
        self.viides = tk.Checkbutton(self.frame, text="virtahepo", variable = self.var5, onvalue=1, offvalue=0)#variable=self.elukkata[0])
        self.viides.pack(fill=tk.Y)
        self.viides.config(font=("Arial", 30))
        self.frame.bind("q", self.close)
        self.frame.bind("<Escape>", self.close)
        self.frame.pack()
        self.frame.focus_set()

        self.button_left = tk.Button(self.frame, text="Confirm",
                                     command=self.update)
        self.button_left.pack(fill=tk.X)
        self.button_left.config(font=("Arial", 40))

        self.is_active = True


    def load_image(self, filename):
        self.fig_image = ImageTk.PhotoImage(Image.open(filename).resize(self.pic_size, Image.BILINEAR))


    def update(self, *args):
        #self.elukat[self.ind,0] = self.elukkata[0]
        #self.elukat[self.ind,1] = self.elukkata[1]
        self.elukat[self.ind,0] = self.var1.get()
        self.elukat[self.ind,1] = self.var2.get()
        self.elukat[self.ind,2] = self.var3.get()
        self.elukat[self.ind,3] = self.var4.get()
        self.elukat[self.ind,4] = self.var5.get()

        self.kuvanimi[self.ind] = listing[self.ind]
        if self.ind < apustus-1:
            self.ind = self.ind + 1
            self.load_image(path1 + listing[self.ind])
            self.image_label.config(image=self.fig_image)

        self.eka.deselect()
        self.toka.deselect()
        self.kolmas.deselect()
        self.neljas.deselect()
        self.viides.deselect()


    def close(self, *args):
        print('GUI closed...')
        self.master.quit()
        self.is_active = False


    def is_closed(self):
        return not self.is_active


    def mainloop(self):
        self.master.mainloop()
        print(self.elukat)
        print(self.kuvanimi)

        tatat = np.column_stack((self.kuvanimi,self.elukat))
        f = open('numbers2.csv', 'w')
        with f:
            writer = csv.writer(f)
            for row in tatat:
                writer.writerow(row)
        print('mainloop closed...')


if __name__ == '__main__':
    import time
    app = App()
    app.mainloop()
