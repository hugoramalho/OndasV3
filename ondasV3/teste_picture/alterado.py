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



#~ ImageTk.PhotoImage(, data='''
                #~ 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
                #~ ''')
                

                
                
class pictureStream:
    def __init__(self):
        self.picture_dic = {}
        

    def search(self, **kwargs):
        name_pic = kwargs.get('name_pic', '')
        id_pic =  kwargs.get('id_pic', '')
        
        picBytesIO = DB_api.extract_picture(**kwargs)
        
        return picBytesIO

        
    def update(self, **kwargs):
        pass
    
    def insert_picture(self, **kwargs):
        PIC_FILE = dic_pic.get('pic_file')
        FILE_NAME = PIC_FILE.filename
        PIC_NAME = dic_pic.get('pic_name', PIC_FILE.filename[:-4])
        PIC_DESCR = dic_pic.get('pic_descr', '')
        TYPE = PIC_FILE.format
        
        feedBack = DB_api.insert_picture(**kwargs)


class padraoImagem(tk.Frame):
    def __init__(self, frameMaster, dic_pic):
        super().__init__(frameMaster, padx = 11, pady = 11)
        self.grid()
        self.config()
        #self.pic_stream = DB_Stream()
        try:
            #picBytesIO = self.pic_stream.search_pic(pic_name)

            pic_file = Image.open(dic_pic['pic_file'])
            self.pic_name = tk.Label(self, text = 'teste')
            self.pic_name.grid(row = 1, column = 0)
        

            self.image = pic_file
            
            #A LINHA DE CÓDIGO ABAIXO DEVERIA FUNCIONAR:
            #TODO: INVESTIGAR O MÓTIVO DO NAO FUNCOIONAMENTO
            #pic_file = Image.frombytes(mode = 'RGB', size = (200,200), data = pic_fileIn)
            
            
            self.image = pic_file.resize((100, 100),Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.image)

        
            self.label_photo = tk.Label(self, image=self.photo)
            self.label_photo.image = self.photo # keep a reference!
            self.label_photo.grid(row = 0, column = 0)
        except Exception as Expt:
            print(Expt, type(Expt))
            self.photo = tk.PhotoImage('Imagem não encontrada!', data = '''
                                                                R0lGODlhyADIAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBV
                                                                ZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDV
                                                                mQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMr
                                                                zDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq
                                                                /zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2Yr
                                                                AGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaq
                                                                M2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kA
                                                                ZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmA
                                                                mZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/
                                                                zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV
                                                                /8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/
                                                                AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9V
                                                                M/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//V
                                                                Zv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAADIAMgA
                                                                AAj/APcJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuX
                                                                MGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOK
                                                                HUu2rNmzaNOqXcu2rdu3cOPKnYtR2T67yupBq4d3n166PvEqG0yMsLLChwcfzpQYcV/AMfMqTqzY
                                                                MeXClidrtgt55WTMlTVn/my4senBnUdKHr15M2LWrUMrrpea417ZoEFfLr0792nKp+8K5Fxbomze
                                                                pEu/jt06s2VihYtTPA0buPPBjIllN60bt+btxKUr9WTOXfRxaH3xonf9+zjwv+IPHu9uvvDtiYJD
                                                                j34+mG/8gasZxh9w4WlUH4HL9QdNfOY1aNlIehGInG4C0dYZcghOtqBBBdomIHOOdUZbg+1ZyNBf
                                                                JmZ04G55bSjXegl+hxpLKd7lHmk1usXXfsDhxFd5o8F1oGPR5bTehJTBt5Z3m7mok2KfVJejWMTd
                                                                aFpBFu5103wEqrUjaSEO9aOEiPlnFomgEWSikzSlCGOGM5L144Bx/sSmjUTyRhaXid2ZkJI3oQcb
                                                                MX5uRZ5hTL1pXZ1c6ffhbAdNydOIiyooqVXs9abYQIXqVOONRTYaY3KbDnTpTyuG/5rVmJmC2eFR
                                                                cD5WlV2Clqcci0xhiJlWrFrGFzSIfdJaomQO1ulSFuo645ya7nPskxy2lxdVGzpaKoASImrQqU8y
                                                                OVxBrxpVbIeK0oesg+EmmidhCZGKmZnOGsWsnlF9ad2dFtqbrVJH8ieVe4XVyGamiC1VKaO5Xldt
                                                                QsAeTIyaQpnIJ0HpCtUqwxSTmmS84jY3LcRH+VYwQjnqu9uzP62rKr+wGadMlLytnMkkk2Qys801
                                                                13xzzjf3rPPPmUha8UO1dpkUbfZSiN91/RW0M885Q/30zFHvzJhwH7EaWq7MVbjgqU7eeqVfAmWC
                                                                htQ6+6y22jwTpKVtvl3LsU9K3v8m8kRZtjrj1zbjbDXQfkvdMxpXh2RyYgbHNlHYoyJOENU/E872
                                                                5FDXTLKBpII81IeIodzQog8C2PfagPeMsxtpz5yj5w4hOXRg7FWIN7Z6q2k22n8/XTXPmQj0dkdi
                                                                P3xU0pNx2FCOj9I7HDFA48475ZOQDVJy9hVFGzTgOR6Rdn1/7Dtjxbp9e/Y29n221X6bnv76Ny+N
                                                                HNabr/v6QcxTXXiFhDWcmZqvLzYJ6n+THM1+Vjma2cxUD8kUrJDDLYQo43zn6x3FrhOw6aDveYDD
                                                                YCaENzeGPKqCQ7EbaVjntNHdjIPLcx24FGIivqAvd5VTG0Sq1BoS2gRJFGHe7jb/GDZrjexT33Kg
                                                                /QyYNp0pZn0onKF1VvYT4skNIqOTWhIHFSe8bNBmYfqdMnLnN2KkaIsD/MR05EeUflUGQBFRhgHT
                                                                V7M4FY0+4dkiBA1YxYGYrmod6tskkshCt82HKPUghrAScz+JkA5nk+AMpTxGKNvxzoCNpNgQccbH
                                                                fTBPckTj33KYCLth5TCGP3NDErc4KpmRbmVgRJ+LOLNFLFZkMzDbXG9sWMIMWk0ZPbxRiuphv52J
                                                                skDaAVolISfGiCQLQ7LcTAsjcki1jZI/aRLdBWv2xfQRbpQ9q6RDtDayoACJlgQJ5gWnJrxkNY5R
                                                                Lzyf7O6yw0b6z28V0V9pkqkZ/4uwMXA+EyW4hhQeXhLukRLkG0CvaE1tts48FqNOeGgJw3vODJcZ
                                                                i1EW/TLJ9j1umpBD5PxIxqKN1iRz64RI/Sb3N3Id7DBadCgK1ajH5unxgCFlSLUQ1MCajGk59jwk
                                                                QINoKo+h1JFqcxJAixg1gxqvIOsqJlAw5NGDUA6f1NTcXcCXIJlJbURlG+ca08Ypl/lrqd6xiDhd
                                                                CrgJMu5iHPNZIsMpOFsa1YOOiti+0AjFoUI1PNrB5m+6OVWexfGfiIQqTKeDTKA0LDgVIYYbtOqz
                                                                8Hzimvvk0i5nhjq87kyAaHvrQm4VSVQpriK9fCQAa7bSSVwzjnSyKhpKq1abjf+2bxZxT03bpFCx
                                                                4pOLa62QOAt5F4mWSqB4fa3zNhhb/XxitjMhkT3tKjhJ8ixUeiNUiogLIMGNU4KEfQ44X3LYymwI
                                                                ueG87k7jxVK/RtRBYfNd2ciaO82OR2xBYdZruspMot5WZ7ZTaxIPW9UOWUi8a6PvnwwCR6F0N39S
                                                                bch9BZvb9Q6OuvhDKRk55NKGule9kRXQdl9iLfAidbhsXGgRKftMgHWIpfcFYM9iSx8Pw+RwTTXI
                                                                S0naNunVr3kQFZ216jQYDeLuwlhy1oDoObYOKnir94SaiGEovA0dWDZOG+hAi6tdi5kLgSJl8PpI
                                                                i1Szsa2fnPOuxIgB2OECOVr/xyFyNCci2IYSDphI9rIXaedT4gDLx+l7ZWG96ZwNW1JyAAba9apL
                                                                wJuB+ZxfHKtgzzxoG8U1oY9CmiGrxlirrRM949PjavepMnQWumYRFHDrYlSU/WyYe0lONQ+xBMbm
                                                                copEcgMWoB95Zv4hlChii7EdJ1lhqEF2W6282ZuRqim+8jLOsF1c3HQtk6JtbSIj7fUd7WdU1Hgv
                                                                Yz6Nslob/Dk6Pxsox0yzkRnSUACnr2JfBNcm53lRV0vvoFcmSnf4+pCX2pK99mMU8lbI1FLZ5djC
                                                                NKZfMrRAArnYkmsst12zibVOxZGfC80dfpJ38OQ2y5ALbnNbT4iwged1neecCbOpvPzQBNIuT/9I
                                                                Yc3XRFrmhuLO5Sb02TXPqrEP4xd+Q3N2n4pSLd2AMMsbN+GI1RdFyBHxpSh804QXhD3T1tovrEnK
                                                                y8zDUPbukLm8jnlGSZvLmHkau+M2yJFIw9MmhpOBzKTaaHcXtbbz2tcDBPX4THvoiT2u1oF8FM/V
                                                                TXVRc/RQhxr7emz0o/XcxtrXFrK7/u27GIdPKTvOF65d1/GDugfLHbt1UJx0U4K/G/PymTezb2JO
                                                                BIXdUwV58mXw9SzQKdLPNRmQ8BQ5edZwclsbkt/od2IlqXO2eJdaZWt4yzKxuakoyqre5Yaj0GQ1
                                                                JTa3TyYcszQlGFce8o2L6eSpd31n1efppC//FPQ5A/uZNK6bD4djuHZ/w2WzPyZvS1XHDxd9roGp
                                                                /vEFEY97e6tVgh7y2RInFUcTClU8A8E07xcUdPIxTlJ+LcEeIbIiiTcVTMJJAwgTyUMfwYJgU/Ep
                                                                1fF/duJtxbJuCdgTd+Io0eSALfFF3KdcWCExDlOCNCF6KuQ11OJH/fZ5macsTyQqPiSD5id/QDg8
                                                                MNM18mEk7WJ73acVXsduZYcqjlaAZ1KEe2Z2IuhJZdErIBUYaESCa0YlE+Qu9NYTARgmakF5kEKG
                                                                efJVbFErPLKEGBiATnh6Y6E1cIITkuEqc6h9Z4GGBviEzlJ9CKElv9MupnJ4Bdg5c5EfsjcZ8SXz
                                                                EDXVF0CUPA1ygWHReb/Xgw7EMU7mYiOigZVSGyKkMUSyFyc4HQeBiG9YGiq4Jwq1hv0hKwOWRuOn
                                                                MJYoFsgzfhJINhvmKtVxGFFSiDoIF34SZoDnGHyhF5KiJdxHQR01hF4xJQ/XjIwUZiKzV3pTGbGE
                                                                Mf+RQtW4gIO0Rf3WaSvSjSZnjHpoK5l4fskTKeYIV3KoMVYCeKyYLq14FsskH26ofupIg/qxP+8Y
                                                                EZ2ySChIj9C0GQFZEQ0UIRDnc/12iwlpTLcxdv3liMIYkZk0ixcBe5ICkRj5kSAZkiI5kiRZkiZ5
                                                                kiiZkiq5kizZki4o+ZIwGZMyOZM0WZM2eZM4mZM6uZM82ZM++ZNAGZRCOZREWZRGGZQBAQA7
                                                                '''
                                                                )

            

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




def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print('Creating schema')
        sql = '''create table if not exists PICTURES(ID INTEGER PRIMARY KEY AUTOINCREMENT, PICTURE BLOB, PIC_FORMAT TEXT, 
        FILE_NAME TEXT, PIC_NAME TEXT UNIQUE, PIC_DESCR TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print('Schema exists\n')
    return conn


    
def insert_picture(conn, picture_file):
    #LEMBRAR QUE EU ESTAVA TENTANDO:
    #picture_bytes = picture_file.tobytes()
    #O OBJETO RETORNAVA SUA VERSÃO SERIALIZADA, PARA SER SALVA NO BD
    #PORÉM NÃO DEU CERTO
    #O PROCEDIMENTO ABAIXO FUNCIONA, PORÉM NÃO ENTENDO O MOTIVO DO PRIMEIRO CASO FALHAR.
    #ABAIXO, É INSTANCIADO UM OBJETO DA CLASSE BytesIO QUE RECEBE A IMAGEM, PELO MÉTODO save()
    #APÓS O MÉTODO save() GRAVAR SEU CONTEÚDO NO OBJETO DA CLASSE BytesIO, A VARIÁVEL picture_bytes
    #RECEBE SEU CONTEÚDO EM BYTES, PARA SER FINALEMENTE SALVO NO BD.
    
    stream = io.BytesIO()
    picture_file.save(stream, format = picture_file.format)
    picture_bytes = stream.getvalue()
    
    FILE_NAME = picture_file.filename
    PIC_NAME = picture_file.filename[:-4]
    
    print('PIC_NAME: ', PIC_NAME, '  FILE_NAME: ', FILE_NAME)
    TYPE = picture_file.format
    
    
    print('FILE_NAME: ', FILE_NAME, ' format: ', TYPE)
    
    sql = '''INSERT INTO PICTURES(PICTURE, PIC_FORMAT, FILE_NAME, PIC_NAME) VALUES(?, ?, ?, ?);'''
    try:
        conn.execute(sql,[sqlite3.Binary(picture_bytes), TYPE, FILE_NAME, PIC_NAME]) 
        conn.commit()
    except Exception as Expt:
        print(Expt)



conn = create_or_open_db('APP_DB.db')

picture_file = Image.open("padrao1.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padrao2.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padrao3.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padrao4.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padrao5.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padrao6.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padrao1.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr1.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr2.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr3.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr4.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr5.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr6.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr7.jpg")
insert_picture(conn, picture_file)

picture_file = Image.open("padraoApr8.jpg")
insert_picture(conn, picture_file)

conn.close()


def extract_picture(cursor, FILE_NAME):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE FILE_NAME = " + FILE_NAME + ';'
    cursor.execute(sql)
    ablob, ext, afile = cursor.fetchone()
    print(ablob, ext, afile)
    filename = afile + ext
   
    output_file = io.BytesIO(ablob)
    #output_file = ablob
    return output_file
    
    
    
def extract_picture(cursor, PIC_NAME):
    dic_pic = {}
    
    sql = "SELECT PICTURE, PIC_FORMAT, FILE_NAME, PIC_NAME, PIC_DESCR FROM PICTURES WHERE PIC_NAME = " + PIC_NAME + ';'
    #EXECUÇÃO DE QUERY:
    cursor.execute(sql)
    print(cursor.execute(sql))
    PIC_BYTES, PIC_FORMAT, FILE_NAME, PIC_NAME, PIC_DESCR = cursor.fetchone()
    
    #A STRING-BYTES GUARDADA NO SQLITE É REINSTANCIADA EM UMA CLASSE BytesIO:
    PIC_FILE = io.BytesIO(PIC_BYTES)
    #O DICIONÁRIO-PICTURE É PREENCHIDO:
    dic_pic['pic_file'] = PIC_FILE
    dic_pic['pic_format'] =  PIC_FORMAT
    dic_pic['pic_file'] = FILE_NAME
    dic_pic['pic_name'] = PIC_NAME
    dic_pic['pic_descr'] = PIC_DESCR
    
    return dic_pic
    




conn = create_or_open_db('APP_DB.db')
cur = conn.cursor()

filePic = extract_picture(cur, '"padraoApr8"')

img = padraoImagem(master, filePic)
img.grid()

cur.close()
conn.close()


conn = create_or_open_db('APP_DB.db')
#conn.execute("DELETE FROM PICTURES")



'''
for fn in picture_list:
    picture_file = "./pictures/"+fn
    insert_picture(conn, picture_file)
'''



for r in conn.execute("SELECT ID, FILE_NAME, PIC_NAME FROM PICTURES"):
    print (r)
 
conn.close()

tkMaster.mainloop()


def main(args):





    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
