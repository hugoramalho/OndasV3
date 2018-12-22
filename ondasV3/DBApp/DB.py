import sqlite3
import io

class conexao_BD_prog:
    def __init__(self):
        try:

            self.conn = sqlite3.connect(".\data_base\APP_DB.db")

            self.con_status = True
            self.conn.commit()
            self.cursor = self.conn.cursor()
            # self.data = self.cursor.fetchone()
            #self.conn.close()
            self.con_status = False
            self.create_or_open_db()


        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __conect_BD__(self):
        try:
            if (self.con_status == False):
                self.conn = sqlite3.connect(".\data_base\APP_DB.db")
                self.con_status = True
                self.conn.commit()
                self.cursor = self.conn.cursor()
                # self.data = self.cursor.fetchone()
            else:
                raise Exception('Conexão indisponível ou já em uso')
                pass
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __disconect_BD__(self):
        self.con_status = False
        self.conn.close()

    def __select_fetchone__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __lastrowid__(self):
        return (self.cursor.lastrowid)

    def __execute_fetchone__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __select_fetchall__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __execute_fetchall__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    '''
    def __execute_commit__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.__disconect_BD__()  # Conexão fechada com o BD!

        except Exception as Expt:
            self.__expt_msg__(Expt)
    '''

    def __execute_commit__(self, sql='', tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()  # Conexão fechada com o BD!

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def finaliza_conexao(self):
        self.__disconect_BD__()

    def __expt_msg__(self, Expt):
        self.finaliza_conexao()
        print(str(Expt))
        return (None)

    ##---------------------------------------------------------------------------------------------------------------##
    #   MÉTODOS DE INSERÇÃO:


    def create_or_open_db(self):
        sql = '''create table if not exists PICTURES_EXP(ID INTEGER PRIMARY KEY AUTOINCREMENT, PICTURE BLOB, PIC_FORMAT TEXT, FILE_NAME TEXT, PIC_NAME TEXT UNIQUE, PIC_DESCR TEXT);'''
        self.__execute_commit__(sql)

        sql = '''create table if not exists EXPERIMENTOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, PIC_ID INTEGER, PIC_FORMAT TEXT, FILE_NAME TEXT, PIC_NAME TEXT UNIQUE, PIC_DESCR TEXT);'''

        sql = '''create table if not exists PICTURES_GUI(ID INTEGER PRIMARY KEY AUTOINCREMENT, PICTURE BLOB, PIC_FORMAT TEXT, PIC_NAME TEXT UNIQUE);'''
        self.__execute_commit__(sql)




    def insert_gui_picture(self, **dic_pic):
        PIC_BYTES = dic_pic.get('pic_bytes')
        PIC_FORMAT = dic_pic.get('pic_format')
        PIC_NAME = dic_pic.get('pic_name')

        sql = '''INSERT INTO PICTURES_GUI(PICTURE, PIC_FORMAT, PIC_NAME) VALUES(?, ?, ?);'''

        try:
            self.__execute_commit__(sql, [sqlite3.Binary(PIC_BYTES), PIC_FORMAT, PIC_NAME])

        except Exception as axpt:
            print(axpt)


    def insert_picture(self, **dic_pic):
        print(dic_pic)
        PIC_BYTES = dic_pic.get('pic_bytes')
        PIC_FORMAT = dic_pic.get('pic_format')
        PIC_NAME = dic_pic.get('pic_name')
        FILE_NAME = dic_pic.get('file_name')
        PIC_DESCR = dic_pic.get('pic_descr')

        sql = '''INSERT INTO PICTURES(PICTURE, PIC_FORMAT, FILE_NAME, PIC_NAME, PIC_DESCR) VALUES(?, ?, ?, ?, ?);'''
        try:
            self.__execute_commit__(sql, [sqlite3.Binary(PIC_BYTES), PIC_FORMAT, FILE_NAME, PIC_NAME, PIC_DESCR])

        except Exception as axpt:
            print(axpt)


    ##---------------------------------------------------------------------------------------------------------------##
        #   MÉTODOS DE COLETA:



    def load_range_freq(self):
        sql = "SELECT FROM_, TO_, TIPO FROM VALUES_SPINBOX;"
        lst = self.__execute_fetchall__(sql)
        dic_range = {}
        for elem in lst:
            tipo = elem[2]
            if tipo == 'CORDA':
                dic_range['corda_from'] = elem[0]
                dic_range['corda_to'] =  elem[1]
            elif tipo == 'SUP':
                dic_range['sup_from'] = elem[0]
                dic_range['sup_to'] = elem[1]
        return dic_range



    def extract_picture(self, PIC_NAME = '', PIC_ID = ''):
        #PIC_ID = str(kwargs.get('pic_id', ''))
        #PIC_NAME = kwargs.get('pic_name', '')

        if PIC_NAME is '' and PIC_ID is not '':
            sql = "SELECT ID, PICTURE, PIC_FORMAT, FILE_NAME FROM PICTURES WHERE id = " + PIC_ID + ";"
        elif PIC_ID is '' and PIC_NAME is not '':
            sql = 'SELECT ID, PICTURE, PIC_FORMAT, FILE_NAME, PIC_NAME, PIC_DESCR FROM PICTURES WHERE PIC_NAME = "' + PIC_NAME + '";'
            #sql = 'SELECT * FROM PICTURES;'

        # lst = self.__execute_fetchone__()
        PIC_ID, PIC_BYTES, TYPE, FILE_NAME, PIC_NAME, PIC_DESCR = self.__execute_fetchone__(sql)

        # ABAIXO A FOTO É COLOCADA EM UM OBJETO DA CLASSE BytesIO:
        PIC_FILE = io.BytesIO(PIC_BYTES)
        dic_pic = {}
        dic_pic['pic_id'] = PIC_ID
        dic_pic['pic_bytes'] = PIC_FILE
        dic_pic['pic_format'] = TYPE
        dic_pic['pic_file'] = FILE_NAME
        dic_pic['pic_name'] = PIC_NAME
        dic_pic['pic_descr'] = PIC_DESCR
        return dic_pic

    def load_all_exp_sup(self):
        sql = '''SELECT EXPERIMENTOS.ID, PICTURES.PICTURE, EXPERIMENTOS.FREQ, EXPERIMENTOS.COMPRIMENTO, EXPERIMENTOS.MASSA, EXPERIMENTOS.DENSIDADE, EXPERIMENTOS.TIPO_EXP, EXPERIMENTOS.PIC_ID FROM EXPERIMENTOS INNER JOIN PICTURES ON (EXPERIMENTOS.PIC_ID = PICTURES.ID) WHERE EXPERIMENTOS.TIPO_EXP = 'SUP' OR EXPERIMENTOS.TIPO_EXP = 'SUP_APR';'''
        lst = self.__execute_fetchall__(sql)
        lst_return = []
        for elem in lst:
            dic_exp = {}
            dic_exp['id'] = elem[0]
            dic_exp['pic_bytes'] = io.BytesIO(elem[1])
            dic_exp['freq'] = elem[2]
            dic_exp['comprimento'] = elem[3]
            dic_exp['massa'] = elem[4]
            dic_exp['densidade'] = elem[5]
            dic_exp['tipo'] = elem[6]
            dic_exp['pic_id'] = elem[7]
            lst_return.append(dic_exp)

        return lst_return

    def load_all_exp(self):
        sql = '''SELECT EXPERIMENTOS.ID, PICTURES.PICTURE, EXPERIMENTOS.FREQ, EXPERIMENTOS.COMPRIMENTO, EXPERIMENTOS.MASSA, EXPERIMENTOS.DENSIDADE, EXPERIMENTOS.TIPO_EXP, EXPERIMENTOS.PIC_ID FROM EXPERIMENTOS INNER JOIN PICTURES ON (EXPERIMENTOS.PIC_ID = PICTURES.ID);'''
        lst = self.__execute_fetchall__(sql)
        lst_return = []
        for elem in lst:
            dic_exp = {}
            dic_exp['id'] = elem[0]
            dic_exp['pic_bytes'] = io.BytesIO(elem[1])
            dic_exp['freq'] = elem[2]
            dic_exp['comprimento'] = elem[3]
            dic_exp['massa'] = elem[4]
            dic_exp['densidade'] = elem[5]
            dic_exp['tipo'] = elem[6]
            dic_exp['pic_id'] = elem[7]
            lst_return.append(dic_exp)

        return lst_return


    def extract_gui_picture(self, PIC_NAME = '', PIC_ID = ''):
        #PIC_ID = str(kwargs.get('pic_id', ''))
        #PIC_NAME = kwargs.get('pic_name', '')

        if PIC_NAME is '' and PIC_ID is not '':
            sql = "SELECT ID, PICTURE, PIC_FORMAT, PIC_NAME FROM PICTURES_GUI WHERE id = " + PIC_ID + ";"
        elif PIC_ID is '' and PIC_NAME is not '':
            sql = 'SELECT ID, PICTURE, PIC_FORMAT, PIC_NAME FROM PICTURES_GUI WHERE PIC_NAME = "' + PIC_NAME + '";'
            #sql = 'SELECT * FROM PICTURES;'

        # lst = self.__execute_fetchone__()
        PIC_ID, PIC_BYTES, TYPE, PIC_NAME, = self.__execute_fetchone__(sql)

        # ABAIXO A FOTO É COLOCADA EM UM OBJETO DA CLASSE BytesIO:
        PIC_FILE = io.BytesIO(PIC_BYTES)

        dic_pic = {}
        dic_pic['pic_id'] = PIC_ID
        dic_pic['pic_bytes'] = PIC_FILE
        dic_pic['pic_format'] = TYPE
        dic_pic['pic_name'] = PIC_NAME

        return dic_pic

    #<_io.BytesIO object at 0x056D3F60>

    def extract_pictures(self):
    #pic_bytes:  <_io.BytesIO object at 0x061E5810>
        sql = "SELECT ID, PICTURE, PIC_FORMAT, FILE_NAME, PIC_NAME, PIC_DESCR FROM PICTURES"
        #self.__execute_commit__(sql)
        lst = self.__execute_fetchall__(sql)
        #print(lst)

        # ABAIXO A FOTO É COLOCADA EM UM OBJETO DA CLASSE BytesIO:
        lst_pics = []
        for elem in lst:

            dic_pic = {}
            PIC_FILE = io.BytesIO(elem[1])
            dic_pic['pic_id'] = elem[0]
            dic_pic['pic_bytes'] = PIC_FILE
            dic_pic['pic_format'] = elem[2]
            dic_pic['pic_name'] = elem[4]
            dic_pic['pic_descr'] = elem[5]
            lst_pics.append(dic_pic)
            #print(dic_pic)

        return lst_pics

        ##---------------------------------------------------------------------------------------------------------------##
        #   MÉTODOS DE UPDATE:


    def update_exp(self, **kwargs):
        # def update_picture(self, PIC_ID, **kwargs):
        # if type(PIC_ID) != str:
        # cliente_id = str(PIC_ID)

        ID = str(kwargs.get('id'))

        strAux = ''
        FREQ = kwargs.get('freq', '')
        if FREQ != '':
            strAux = strAux + ' FREQ = "' + FREQ + '",'

        COMPRIMENTO = kwargs.get('comprimento', '')
        if COMPRIMENTO != '':
            strAux = strAux + ' COMPRIMENTO = "' + COMPRIMENTO + '",'

        MASSA = kwargs.get('massa', '')
        if MASSA != '':
            strAux = strAux + ' MASSA = "' + MASSA + '",'

        TIPO_EXP = kwargs.get('tipo_exp', '')
        if TIPO_EXP != '':
            strAux = strAux + ' TIPO_EXP = "' + TIPO_EXP + '",'

        DENSIDADE = kwargs.get('densidade', '')
        if DENSIDADE != '':
            strAux = strAux + ' DENSIDADE = "' + DENSIDADE + '",'

        TIPO_EXP = kwargs.get('tipo_exp', '')
        if TIPO_EXP != '':
            strAux = strAux + ' TIPO_EXP = "' + TIPO_EXP + '",'


        PICTURE = kwargs.get('pic_bytes','')
        if PICTURE != '':

            PIC_ID = kwargs.get('pic_id', '')
            PIC_NAME = kwargs.get('pic_name')
            PIC_FORMAT = kwargs.get('pic_format')
            #PIC_RES = kwargs.get('pic_res')
            PIC_BYTES = kwargs.get('pic_bytes')
            #dic_pic = {'PIC_ID': PIC_ID, 'PICTURE': sqlite3.Binary(PICTURE), 'PIC_NAME':PIC_NAME, 'PIC_FORMAT': PIC_FORMAT}

            dic_pic = {'PIC_ID': PIC_ID, 'PICTURE': sqlite3.Binary(PIC_BYTES), 'PIC_NAME': PIC_NAME, 'PIC_FORMAT': PIC_FORMAT}
            self.update_picture(**dic_pic)

        if strAux != '':
            strAux = strAux.strip(', ')

            sql = 'UPDATE EXPERIMENTOS SET ' + strAux + ' WHERE ID = ' + ID + ';'
            # sql = 'UPDATE PICTURES_ONDAS SET ' + strAux + ' WHERE PIC_NAME = ' + PIC_NAME + ';'
            print(sql)
            self.__execute_commit__(sql)


    def update_range_freq(self, **kwargs):
        corda_from = str(kwargs.get('corda_from', ''))
        if corda_from != '':
            sql = 'UPDATE VALUES_SPINBOX SET FROM_ = "' + corda_from + '" WHERE TIPO = "CORDA";'
            self.__execute_commit__(sql)

        corda_to = str(kwargs.get('corda_to', ''))
        if corda_to != '':
            sql = 'UPDATE VALUES_SPINBOX SET TO_ = "' + corda_to + '" WHERE TIPO = "CORDA";'
            self.__execute_commit__(sql)

        sup_to = str(kwargs.get('sup_to', ''))
        if sup_to != '':
            sql = 'UPDATE VALUES_SPINBOX SET TO_ = "' + sup_to + '" WHERE TIPO = "SUP";'
            self.__execute_commit__(sql)

        sup_from = str(kwargs.get('sup_from', ''))
        if sup_to != '':
            sql = 'UPDATE VALUES_SPINBOX SET FROM_ = "' + sup_from + '" WHERE TIPO = "SUP";'
            self.__execute_commit__(sql)






    def update_picture(self, **kwargs):
        # def update_picture(self, PIC_ID, **kwargs):
        # if type(PIC_ID) != str:
        # cliente_id = str(PIC_ID)

        PIC_ID = str(kwargs.get('PIC_ID'))

        strAux = ''
        PIC_NAME = kwargs.get('PIC_NAME', '')
        if PIC_NAME != '':
            strAux = strAux + ' PIC_NAME = "' + PIC_NAME + '",'

        PIC_DESCR = kwargs.get('PIC_DESCR', '')
        if PIC_DESCR != '':
            strAux = strAux + ' PIC_DESCR = "' + PIC_DESCR + '",'

        PIC_FORMAT = kwargs.get('PIC_FORMAT', '')
        if PIC_FORMAT != '':
            strAux = strAux + ' PIC_FORMAT = "' + PIC_FORMAT + '",'

        FILE_NAME = kwargs.get('FILE_NAME', '')
        if FILE_NAME != '':
            strAux = strAux + ' FILE_NAME = "' + FILE_NAME + '",'

        PICTURE = kwargs.get('PICTURE', '')
        if PICTURE != '':
            sql = 'UPDATE PICTURES SET  PICTURE = ? WHERE ID = ' + PIC_ID + ';'
            self.__execute_commit__(sql, [PICTURE])
            print(sql)
        if strAux != '':
            strAux = strAux.strip(', ')



        sql = 'UPDATE PICTURES SET ' + strAux + ' WHERE ID = ' + PIC_ID + ';'
        #sql = 'UPDATE PICTURES_ONDAS SET ' + strAux + ' WHERE PIC_NAME = ' + PIC_NAME + ';'
        print(sql)
        self.__execute_commit__(sql)

        ##---------------------------------------------------------------------------------------------------------------##
        #   MÉTODOS DE DELEÇÃO:

    def del_photo(self, PIC_NAME):
        sql = 'DELETE FROM PICTURES_ONDAS WHERE PIC_NAME = ' + PIC_NAME + ';'
        self.__execute_commit__(sql)
