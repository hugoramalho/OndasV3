import sqlite3
import os.path
from os import listdir, getcwd

from PIL import Image, ImageTk
import base64
import io

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

tkMaster = tk.Tk()
master = tk.Frame(tkMaster)
master.grid()



class padraoImagem(tk.Frame):
    def __init__(self, frameMaster, pic_fileIn):
        super().__init__(frameMaster)
        self.grid()
        self.config(padx = 11, pady = 11)
        self.tit_p = tk.Label(self, text = 'teste')
        self.tit_p.grid(row = 1, column = 0)
        try:
            pic_file = pic_fileIn
            pic_file = Image.open(pic_file)
            #pic_file = Image.frombytes(mode = 'RGB', size = (200,200), data = pic_fileIn)
            
            self.image = pic_file.resize((100, 100),Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.image)
            self.label_photo = tk.Label(self, image=self.photo)
            self.label_photo.image = self.photo # keep a reference!
            self.label_photo.grid(row = 0, column = 0)
        except Exception as Expt:
            print(Expt, type(Expt))
            #self.noPic()
            

    def noPic(self):
        imageIn = Image.open('vazio.jpg')
        self.image = imageIn.resize((100, 100),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label_photo = tk.Label(self, image=self.photo)
        self.label_photo.image = self.photo # keep a reference!
        self.label_photo.grid(row = 0, column = 0)
        
        

def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print ('abs_path =', abs_path)
    dir_files = os.listdir(abs_path)
    #print dir_files
    return dir_files

picture_list = get_picture_list('pictures')
print(picture_list)

#Image.open('.\pictures\Chrysanthemum50.jpg')





def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print('Creating schema')
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT, TYPE_PIC TEXT, PIC_NAME TEXT, PIC_DESCR TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print('Schema exists\n')
    return conn


    
def insert_picture(conn, picture_file):
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

conn = create_or_open_db('picture_db.sqlite')


picture_file = "./pictures/Chrysanthemum50.jpg"
insert_picture(conn, picture_file)
conn.close()

def extract_picture(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
   
    
    output_file = io.BytesIO(ablob)
    print(output_file)
    return output_file
    

conn = create_or_open_db('picture_db.sqlite')
cur = conn.cursor()
filename = extract_picture(cur, 1)

#filePic = extract_picture(cur, 1)
img = padraoImagem(master, filename)
img.grid()
tkMaster.mainloop()
cur.close()
conn.close()
#Image.open('./'+filename)



conn = create_or_open_db('picture_db.sqlite')
#conn.execute("DELETE FROM PICTURES")
'''
for fn in picture_list:
    picture_file = "./pictures/"+fn
    insert_picture(conn, picture_file)
'''
     
for r in conn.execute("SELECT FILE_NAME FROM PICTURES"):
    print (r[0])
 
conn.close()




def main(args):





    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
