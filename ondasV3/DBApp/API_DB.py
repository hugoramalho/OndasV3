from . import conexao_BD_prog

conDB = conexao_BD_prog()


def search_pic(**kwargs):
    print(kwargs)
    pic_name = kwargs.get('pic_name', '')
    pic_id = kwargs.get('pic_id', '')
    pic_type = kwargs.get('pic_type', '')

    if pic_type == 'gui':
        dic_pic = conDB.extract_gui_picture(pic_name)
    else:
        dic_pic = conDB.extract_picture(pic_name)

    return dic_pic


def search_gui_pic(**kwargs):
    pic_name = kwargs.get('pic_name', '')
    pic_id = kwargs.get('pic_id', '')

    dic_pic = conDB.extract_gui_picture(pic_name)

    return dic_pic

def update_exp(**kwargs):
    conDB.update_exp(**kwargs)
    #tipo = kwargs.get('tipo')
    #if tipo == 'CORDA':
        #conDB.update_exp(**kwargs)
    #elif tipo == 'SUP' or tipo == 'SUP_APR':
        #conDB.update_exp(**kwargs)


def update_pic(**kwargs):
    conDB.update_picture(**kwargs)


def update_range_freq(**kwargs):
    conDB.update_range_freq(**kwargs)

def loadFreqRange():
    return conDB.load_range_freq()


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


def extract_pictures():
    return conDB.extract_pictures()

def loadAllExp(**kwargs):
    tipo = kwargs.get('tipo', '')
    if tipo == 'CORDA':
        pass
    elif tipo == 'SUP':
        lst_dics = conDB.load_all_exp_sup()
        return lst_dics
    elif tipo == '':
        lst_dics = conDB.load_all_exp()

    return lst_dics




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

    self.__ins_gui_pic__('VAZIO1.jpg')
    self.__ins_gui_pic__('VAZIO2.gif')
    self.__ins_gui_pic__('PYTHON_POWERED.png')
    self.__ins_gui_pic__('IFES1.bmp')
    self.__ins_gui_pic__('IFES2.png')
    self.__ins_gui_pic__('IFES3.png')
 '''