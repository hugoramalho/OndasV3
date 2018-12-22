import io
from tkinter import PhotoImage

import PIL.Image
import PIL.ImageTk

from DBApp import API_DB
from DBApp import conexao_BD_prog
from  app.view import UI_app


class DB_Stream:
    def __init__(self):
        self.picture_dic = {}
        self.con_db = conexao_BD_prog()
        #self.__insert_pattern_pictures__()

    def search_pic(self, **kwargs):
        pic_name = kwargs.get('pic_name', '')
        pic_id = kwargs.get('pic_id', '')
        pic_type = kwargs.get('pic_type', '')

        if pic_type == 'gui':
            picBytesIO = self.con_db.extract_gui_picture(pic_name)
        else:
            picBytesIO = self.con_db.extract_picture(pic_name)

        return picBytesIO



    def update(self, **kwargs):
        self.con_db.update_picture(**kwargs)


    def insert_picture(self, **kwargs):
        PIC_FILE = kwargs.get('pic_file')
        FILE_NAME = PIC_FILE.filename
        PIC_NAME = kwargs.get('pic_name', PIC_FILE.filename[:-4])
        PIC_DESCR = kwargs.get('pic_descr', '')
        PIC_FORMAT = PIC_FILE.format

        stream = io.BytesIO()
        PIC_FILE.save(stream, format=PIC_FILE.format)
        PIC_BYTES = stream.getvalue()
        dic_pic = {'pic_bytes': PIC_BYTES, 'file_name': FILE_NAME, 'pic_name': PIC_NAME, 'pic_descr': PIC_DESCR,
                   'pic_format': PIC_FORMAT}
        feedBack = self.con_db.insert_picture(**dic_pic)

        return feedBack



    def __ins_pic__(self, pic_dir: str):
        picture_file = Image.open(pic_dir)
        stream = io.BytesIO()
        picture_file.save(stream, format=picture_file.format)
        PIC_BYTES = stream.getvalue()
        FILE_NAME = picture_file.filename
        PIC_NAME = picture_file.filename[:-4]
        PIC_FORMAT = picture_file.format
        PIC_DESCR = 'Imagem inserida pela __insert_pattern_pictures__()'

        dic_pic = {'pic_bytes': PIC_BYTES, 'file_name': FILE_NAME, 'pic_name': PIC_NAME, 'pic_descr': PIC_DESCR,
                   'pic_format': PIC_FORMAT}
        feedBack = self.con_db.insert_picture(**dic_pic)


    def __ins_gui_pic__(self, pic_dir: str):
        picture_file = Image.open(pic_dir)
        stream = io.BytesIO()
        picture_file.save(stream, format=picture_file.format)
        PIC_BYTES = stream.getvalue()
        PIC_NAME = picture_file.filename[:-4]
        PIC_FORMAT = picture_file.format

        dic_pic = {'pic_bytes': PIC_BYTES, 'pic_name': PIC_NAME, 'pic_format': PIC_FORMAT}

        self.con_db.insert_gui_picture(**dic_pic)



    def __ins_pic2__(self, **kwargs):
        PIC_FILE = kwargs.get('picture_file', None)
        FILE_NAME = kwargs.get('file_name', '')
        PIC_NAME = kwargs.get('pic_name')
        PIC_FORMAT = kwargs.get('pic_format', 'NULL')
        PIC_DESCR = kwargs.get('pic_descr', 'Imagem inserida pela __insert_pattern_pictures__()')

        if PIC_FILE is None:
            PIC_BYTES = io.BytesIO().getvalue()
        else:
            stream = io.BytesIO()
            PIC_FILE.save(stream, format=PIC_FILE.format)
            PIC_BYTES = stream.getvalue()


        dic_pic = {'pic_bytes': PIC_BYTES, 'file_name': FILE_NAME, 'pic_name': PIC_NAME, 'pic_descr': PIC_DESCR,
                   'pic_format': PIC_FORMAT}
        print('stream dict: ', dic_pic)
        self.con_db.insert_picture(**dic_pic)


    def extract_pictures(self):
        return self.con_db.extract_pictures()


    def __insert_pattern_pictures__(self):
        '''
        self.__ins_pic__("padrao1.jpg")

        self.__ins_pic__("padrao2.jpg")

        self.__ins_pic__("padrao3.jpg")

        self.__ins_pic__("padrao4.jpg")

        self.__ins_pic__("padrao5.jpg")

        self.__ins_pic__("padrao6.jpg")

        self.__ins_pic__("padraoApr1.jpg")

        self.__ins_pic__("padraoApr2.jpg")

        self.__ins_pic__("padraoApr3.jpg")

        self.__ins_pic__("padraoApr4.jpg")

        self.__ins_pic__("padraoApr5.jpg")

        self.__ins_pic__("padraoApr6.jpg")

        self.__ins_pic__("padraoApr7.jpg")

        self.__ins_pic__("padraoApr8.jpg")

        self.__ins_pic__("padraoApr8.jpg")

        self.__ins_pic2__(pic_name = 'padraoCorda1')

        self.__ins_pic2__(pic_name= 'padraoCorda2')

        self.__ins_pic2__(pic_name= 'padraoCorda3')

        self.__ins_pic2__(pic_name= 'padraoCorda4')

        self.__ins_pic2__(pic_name= 'padraoCorda5')

        self.__ins_pic2__(pic_name= 'padraoCorda6')

        '''
        self.__ins_gui_pic__('VAZIO1.jpg')
        self.__ins_gui_pic__('VAZIO2.gif')
        self.__ins_gui_pic__('PYTHON_POWERED.png')
        self.__ins_gui_pic__('IFES1.bmp')
        self.__ins_gui_pic__('IFES2.png')
        self.__ins_gui_pic__('IFES3.png')

class my_list(list):
    def __init__(self):
        super().__init__()
        self.stream = DB_Stream()

    def loadAllPics(self, **kwargs):
        pattern = kwargs.get('pattern', '')
        if pattern == '':
            lst_pic = API_DB.extract_pictures()
            lst_return = my_list()

            for elem in lst_pic:
                photo = UI_app.wd_Image2(None, **elem)
                padrao = UI_app.PadraoExp(pic_id = photo.pic_id, picture = photo, freq=photo.pic_name)
                lst_return.append(padrao)
            return lst_return

    def loadAllExp(self, **kwargs):
        tipo_exp = kwargs.get('tipo', '')

        lst_dics = API_DB.loadAllExp(tipo = tipo_exp)
        lst_return = my_list()
        for elem in lst_dics:
            exp = PadraoExp(**elem)
            lst_return.append(exp)
        return lst_return

    def toTreeview(self):
        lst = []
        for elem in self:
            try:
                lst.append(elem.toTreeview())
            except Exception as Exp:
                kwTreeview = {'id': '', 'text': Exp, 'value': (Exp, 'ERROR!')}
                lst.append(kwTreeview)
        return lst

    def search_pic(self, id_item):
        if type(id_item) is not int:
            id_item = int(id_item)

        for elem in self:
            if elem.id == id_item:
                return elem


class my_PhotoImage:
    def __init__(self, **kwargs):
        self.pic_bytes = kwargs.get('pic_bytes', None)
        self.ImageObject = kwargs.get('ImageObject', None)
        self.pic_resolution = kwargs.get('pic_resolution', (100, 100))
        self.pic_id = kwargs.get('pic_id', '')
        self.pic_name = kwargs.get('pic_name', '')
        self.pic_type = kwargs.get('pic_type')

        if self.pic_bytes is None and self.ImageObject is None and self.pic_name is not '':
            if self.pic_type == 'gui':
                dic_pic = API_DB.search_gui_pic(**kwargs)
                self.pic_bytes = dic_pic['pic_bytes']

                if self.pic_bytes is None:
                    self.no_pic()
                self.pic_name = dic_pic['pic_name']
                self.pic_id = dic_pic['pic_id']

                # Objeto Image instanciado:
                self.pic_file = PIL.Image.open(self.pic_bytes).resize(self.pic_resolution, PIL.Image.ANTIALIAS)
                self.PhotoImage = PIL.ImageTk.PhotoImage(self.pic_file)
                self.photo = self.PhotoImage
        else:
            try:
                self.pic_file = PIL.Image.open(self.pic_bytes).resize(self.pic_resolution, PIL.Image.ANTIALIAS)
                self.PhotoImage = PIL.ImageTk.PhotoImage(self.pic_file)
                self.photo = self.PhotoImage
            except Exception as Expt:
                # print(Expt)
                self.no_pic()


    def no_pic(self):
        self.PhotoImage = PhotoImage(data=ImageNotFound).subsample(2, 2)
        self.photo = self.PhotoImage
        #self.pic_stream = models_app.DB_Stream()
        #dic_pic = self.pic_stream.search_pic(pic_name='VAZIO2', pic_type='gui')
        #print(dic_pic)
        #self.pic_bytes = dic_pic['pic_bytes']
        #self.Image = PIL.Image.open(self.pic_bytes).resize((100, 100), PIL.Image.ANTIALIAS)
        #super().__init__(self.photo)


class range_freq:
    def __init__(self, **kwargs):
        self.corda_from = kwargs.get('corda_from', 31)
        self.corda_to = kwargs.get('corda_to', 65535)
        self.sup_from = kwargs.get('sup_from', 31)
        self.sup_to = kwargs.get('sup_to', 65535)

    def update(self, **kwargs):
        self.corda_from = kwargs.get('corda_from', self.corda_from)
        self.corda_to = kwargs.get('corda_to', self.corda_to)
        self.sup_from = kwargs.get('sup_from', self.sup_from )
        self.sup_from = kwargs.get('sup_to', self.sup_to)
        API_DB.update_range_freq(**kwargs)

    def restore(self, **kwargs):
        tipo = kwargs.get('tipo', '')
        if tipo == '':
            self.corda_from = 31
            self.corda_to = 65535
            self.sup_from = 31
            self.sup_to = 65535
            dic_restore = {'sup_from': 31, 'sup_to': 65535, 'corda_from': 31, 'corda_to': 65535}

        elif tipo == 'sup':
            self.sup_from = 31
            self.sup_to = 65535
            dic_restore = {'sup_from': 31, 'sup_to': 65535}

        elif tipo == 'corda':
            self.corda_from = 31
            self.corda_to = 65535
            dic_restore = {'corda_from': 31, 'corda_to': 65535}

        API_DB.update_range_freq(**dic_restore)

    def load(self):
        kwargs = API_DB.loadFreqRange()
        self.corda_from = kwargs.get('corda_from', self.corda_from)
        self.corda_to = kwargs.get('corda_to', self.corda_to)
        self.sup_from = kwargs.get('sup_from', self.sup_from )
        self.sup_to = kwargs.get('sup_to', self.sup_to)


class PadraoExp:
    def __init__(self, **kwargs):
        self.freq = kwargs.get('freq', '')
        self.comprimento = kwargs.get('comprimento', '')
        self.massa = kwargs.get('massa', '')
        self.densidade_linear = kwargs.get('densidade', '')
        self.pic_bytes = kwargs.get('pic_bytes', '')
        self.pic_id = kwargs.get('pic_id', '')
        self.id = kwargs.get('id', '')
        self.tipo = kwargs.get('tipo', '')

        self.PhotoImage = my_PhotoImage(pic_bytes=self.pic_bytes).PhotoImage
        self.photo = self.PhotoImage

    def toTreeview(self):
        kwTreeview = {'id': self.id, 'image': self.photo, 'text': '', 'value': (self.freq, self.tipo)}
        print(kwTreeview)
        return kwTreeview

    def update(self, **kwargs):
        self.freq = kwargs.get('freq', self.freq)
        self.comprimento = kwargs.get('comprimento', self.comprimento)
        self.massa = kwargs.get('massa', self.massa)
        self.densidade_linear = kwargs.get('densidade', self.densidade_linear)
        kwargs['id'] = self.id
        picture_file = kwargs.get('PhotoImage', None)
        if picture_file is not None:
            stream_bytes = io.BytesIO()
            PIC_NAME = picture_file.filename[:-4]
            PIC_FORMAT = picture_file.format

            picture_file.save(stream_bytes, format=PIC_FORMAT)

            self.pic_bytes = stream_bytes
            self.PhotoImage = my_PhotoImage(pic_bytes=self.pic_bytes).PhotoImage
            self.photo = self.PhotoImage
            PIC_BYTES = stream_bytes.getvalue()
            kwargs['pic_name'] = PIC_NAME
            kwargs['pic_format'] = PIC_FORMAT
            kwargs['pic_bytes'] = PIC_BYTES
            kwargs['pic_id'] = self.pic_id
        API_DB.update_exp(**kwargs)


ImageNotFound = '''
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