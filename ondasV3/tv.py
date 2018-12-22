#import view.UI_app
#from modelsApp import models_app
#import programInit
#import os
#import tkinter as tk
#import tkinter.ttk as ttk
#from PIL import Image, ImageTk

#~ class padroes_view(ttk.Frame):

    #~ def __init__(self, master, path):
        #~ ttk.Frame.__init__(self, master)
        #~ self.tree = ttk.Treeview(self)
        #~ ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        #~ xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        #~ self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        #~ self.tree.heading('#0', text='Directory', anchor='w')

        #~ abspath = os.path.abspath(path)
        #~ i = 'vazio2.gif'
        #~ root_pic1 = Image.open(i)                           # Open the image like this first
        #~ self.root_pic2 = ImageTk.PhotoImage(root_pic1)      # Then with PhotoImage. NOTE: self.root_pic2 =     and not     root_pic2 =

        #~ root_node = self.tree.insert('', 'end', text=abspath, open=True, image=self.root_pic2)
        #~ l1_node = self.tree.insert(root_node, 'end', text='level 1', open=True)
        #~ l2_node = self.tree.insert(l1_node, 'end', text='level 2', open=True)
        #~ l3_node = self.tree.insert(l2_node, 'end', text='level 3', open=True)
        #~ l2a_node = self.tree.insert(l1_node, 'end', text='level 2a', open=True)
        #~ l3a_node = self.tree.insert(l2a_node, 'end', text='level 3a', open=True)

        #~ self.tree.grid(row=0, column=0)
        #~ ysb.grid(row=0, column=1, sticky='ns')
        #~ xsb.grid(row=1, column=0, sticky='ew')
        #~ self.grid()

#~ root = tk.Tk()
#~ path_to_my_project = os.getcwd()
#~ app = padroes_view(root, path=path_to_my_project)
#~ app.mainloop()


#~ from tkinter import *
#~ from tkinter import ttk
#~ from PIL import ImageTk,Image
#~ win=Tk()


#~ chromelogo=Image.open("vazio2.gif")#open the image using PIL
#~ imwidth=50#the new width you want 

#~ #the next three lines of codes are used to keep the aspect ration of the image
#~ wpersent=(imwidth/float(chromelogo.size[0]))
#~ hsize=int(float(chromelogo.size[1])*float(wpersent))#size[1] means the height and the size[0] means the width you can read more about this in th PIL documentation
#~ chromelogo=ImageTk.PhotoImage(chromelogo.resize((imwidth,hsize),Image.ANTIALIAS))# set the width and put it back in the chromelogo variable

#~ treeview=ttk.Treeview(win)
#~ treeview.pack(fill=BOTH,expand=False)
#~ treeview.insert('','0','Chrome',text='Chrome', image=chromelogo)
#~ treeview.image = chromelogo#this one is for telling tkinter not to count the image as garbage
#~ treeview.grid(row=0,rowspan=2,columnspan=2,padx=220,sticky=N+W,pady=20)

#~ chromelogo2=ImageTk.PhotoImage(Image.open("vazio2.gif"))
#~ treeview.insert('Chrome','0',"shit",text="shit",image=chromelogo2)#here you can also insert the unresized logo so you could see it as big as it is

#~ treeview.insert('','1','Chrome3',text='Chrome3')

#~ win.mainloop()



#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
import tkinter as tk
import tkinter.ttk as ttk


class wd_Menu(tk.Menu):
    def __init__(self, frameMaster, **kwargs):
        super().__init__(frameMaster, tearoff=0)

        self.frameMaster = frameMaster

        self.nome_op1 = kwargs.get('nome_B1', 'Opção 1')
        self.nome_op2 = kwargs.get('nome_B2', 'Opção 2')

        self.command_op1 = kwargs.get('command_op1', None)
        self.command_op2 = kwargs.get('command_op2', None)

        self.add_command(label=self.nome_op1, command=self.command_op1)
        self.add_command(label=self.nome_op2, command=self.command_op2)

        # ~ self.bind(self.framePai)

    def config_nome_B1(self, tit):
        # index_B1 = self.menu.index(self.nome_op1)
        self.entryconfig(0, label=tit)

    def config_nome_B2(self, tit):
        # index_B2 = self.menu.index(self.nome_op2)
        self.entryconfig(1, label=tit)

    def config_comando_B1(self, comando):
        # index_B1 = self.menu.index(self.nome_op1)
        self.entryconfig(0, command=comando)

    def config_comando_B2(self, comando):
        # index_B2 = self.menu.index(self.nome_op2)
        self.entryconfig(1, command=comando)

    def popup(self, event):
        self.post(event.x_root, event.y_root)

    def bind(self, pointer):
        pointer.bind("<Button-3>", self.popup)


class padroes_view(ttk.Frame):
    def __init__(self, parent=None, controller = None):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.popUpMenu = wd_Menu(self, nome_B1='Alterar', command_op1 = self.alterar)

        style = ttk.Style(self.parent)
        style.configure('Treeview', rowheight=110)

        # Create Treeview 
        self.tree = ttk.Treeview(self, column=('A','B'), height=5, selectmode='browse')
        self.tree.grid(row=0, column=0, sticky='nsew', padx = 20, pady=15)

        # Setup column heading
        self.tree.heading('#0', text=' Padrão esperado', anchor='center')
        self.tree.heading('#1', text=' Frequência (Hz): ', anchor='center')
        self.tree.heading('#2', text=' Tipo do experimento:', anchor='center')
        # #0, #01, #02 denotes the 0, 1st, 2nd columns

        # Setup column
        self.tree.column('A', anchor='center', width=100, stretch = True)
        self.tree.column('B', anchor='center', width=115, stretch = True)

        # Insert image to #0
        #self._img = tk.PhotoImage(file="vazio2.gif") #change to your file path
        #self._img = view.UI_app.wd_GUI_Image(self, pic_name='VAZIO1', pic_resolution= (80,80)).photo
        #self.tree.insert('', 'end', text="#0's text", image=self._img, value=("A's value", "B's value"), open=True)

        #self._img2 = view.UI_app.wd_GUI_Image(self, pic_name='IFES1', pic_resolution= (80,80)).photo
        #self.tree.insert('', 'end', text="#0's text", image=self._img2, value=("A's value", 'something'))

        self.__insert_treeView__()

        self.tree.bind('<<TreeviewSelect>>', lambda event: self.bind_select())
        self.tree.bind('<Button-3>', lambda event: self.bind_B3(event))
        self.id_pic_sel = None

    def __insert_treeView__(self):
        self.lst_pics = models_app.my_list().loadAllExp()
        self.insert_list(self.lst_pics.toTreeview())

    def alterar(self):
        pic_sel = self.lst_pics.search_pic(self.id_pic_sel)
        self.controller.show_frame('altera_padrao', padrao = pic_sel)

    def bind_B3(self, event):
        self.popUpMenu.popup(event)

    def bind_select(self):
        try:
            self.id_pic_sel = int(self.tree.selection()[0])
        except ValueError:
            self.id_pic_sel = self.tree.selection()[0]
        print(self.id_pic_sel)

    def update_pic(self, wd_pic: view.UI_app.wd_GUI_Image, pic_nome):
        wd_pic.update(PIC_NAME = pic_nome)

    def insert_list(self, lst:list):
        for elem in lst:
            self.insert_kw(**elem)

    def insert_kw(self, **kwargs):
        idd = kwargs.get('id', '')
        image = kwargs.get('image', '')
        text =  kwargs.get('text', '')
        value = kwargs.get('value', ('',''))
        try:
            self.tree.insert('', 'end', iid=idd, text=str(text), image=image, value=value)
        except Exception as Expt:
            print('Erro no insert treeView(): ', Expt)
            self.tree.insert('', 'end', text=str(text), image=image, value=value)



class controller:
    def __init__(self):
        pass
    def show_frame(self, frame_nome, **kwargs):
        padrao = kwargs.get('experimento')
        view.UI_app.altera_exp_view(self, self, padrao)
'''



'''
if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry('800x600')
    control = controller()
    app = padroes_view(root, control)
    app.grid(row=0, column=0, sticky='nsew')

    root.rowconfigure(0, weight=2)
    root.columnconfigure(0, weight=1)

    root.mainloop()
'''



'''
import os
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class padroes_view(ttk.Frame):

    def __init__(self, master, path):
        ttk.Frame.__init__(self, master)
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set, selectmode='browse')
        self.tree.heading('#0', text='Directory', anchor='w')

        #abspath = os.path.abspath(path)
        #i = './icon/Home-icon_16.gif'
        #root_pic1 = Image.open(i)                           # Open the image like this first
        #self.root_pic2 = ImageTk.PhotoImage(root_pic1)      # Then with PhotoImage. NOTE: self.root_pic2 =     and not     root_pic2 =
        root_pic1 = view.UI_app.wd_GUI_Image(self, pic_name='VAZIO1', pic_resolution=(50, 50)).pic_file
        self.root_pic2 = view.UI_app.wd_GUI_Image(self, pic_name='VAZIO1', pic_resolution=(50, 50)).photo


        root_node = self.tree.insert('', 'end', text='something', open=True, image=self.root_pic2)
        l1_node = self.tree.insert(root_node, 'end', text='level 1', open=True)
        l2_node = self.tree.insert(l1_node, 'end', text='level 2', open=True)
        l3_node = self.tree.insert(l2_node, 'end', text='level 3', open=True)
        l2a_node = self.tree.insert(l1_node, 'end', text='level 2a', open=True)
        l3a_node = self.tree.insert(l2a_node, 'end', text='level 3a', open=True)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        self.grid()

root = tk.Tk()
path_to_my_project = os.getcwd()
app = padroes_view(root, path=path_to_my_project)
app.mainloop()
'''