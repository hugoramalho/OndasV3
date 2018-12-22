from tkinter import Frame, LabelFrame, StringVar, Label, N, S, W, E, Scrollbar, Menu, Toplevel, Spinbox, HORIZONTAL, \
    VERTICAL, CENTER, GROOVE, FLAT, IntVar, DoubleVar
from tkinter import font as tkfont, ttk
from tkinter.filedialog import askopenfilename

import PIL.Image
import PIL.ImageTk

from app.model.modelsApp import models_app


class wd_Entry(Frame):
    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.grid()

        self.tit_Entry_text = kwargs.get('tit_Entry', 'Título')
        self.set_Entry_default = kwargs.get('set_Entry_default', 'Opções')
        self.state_Entry = kwargs.get('state_Entry', 'enabled')
        self.width_Entry = kwargs.get('width', 20)

        self.frameLocal = Frame(framePai)
        self.tit_Entry = Label(self.frameLocal, text=self.tit_Entry_text)
        self.var_Entry = StringVar()
        self.Entry = ttk.Entry(self.frameLocal, textvariable=self.var_Entry, width=self.width_Entry,
                               state=self.state_Entry)

    def config_Entry(self, **kwargs):
        self.Entry.config(kwargs)

    def get(self):
        return self.var_Entry.get()

    def retorna_entr(self):
        return self.var_Entry.get()

    def insert(self, txt):
        self.Entry.insert_Entry(txt)

    def insert_Entry(self, txt):
        if self.Entry['state'] != 'enabled':
            state = self.Entry['state']
            self.Entry.config(state='enabled')
            self.Entry.delete(0, "end")
            self.Entry.insert('end', txt)
            self.Entry.config(state=state)
        else:
            self.Entry.delete(0, "end")
            self.Entry.insert('end', txt)

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 2)
        padx = kwargs.get('padx', 2)

        self.tit_Entry.grid(row=0, column=0, sticky=W, columnspan=columnspan)
        self.Entry.grid(row=1, column=0, sticky=sticky, columnspan=columnspan)
        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def delete(self):
        self.Entry.delete(0, "end")

    def limpa_entr(self):
        self.Entry.delete(0, "end")

class wd_GUI_Image(Frame):
    def __init__(self, frameMaster, **kwargs):
        super().__init__(frameMaster, padx=11, pady=11)
        # self.grid()

        self.pic_name = kwargs.get('pic_name', 'VAZIO1')
        self.pic_resolution = kwargs.get('pic_resolution', (100, 100))
        kwargs['pic_type'] = 'gui'

        self.PhotoImage_ = models_app.my_PhotoImage(**kwargs)

        self.PhotoImage = self.PhotoImage_.PhotoImage
        self.photo = self.PhotoImage

        self.pic_portrait = Label(self, image=self.photo)
        self.pic_portrait.grid(row=0, column=0)
        self.pic_portrait.image = self.photo  # keep a reference!

    def toTreeview(self):
        kwTreeview = {'id': self.pic_id, 'photo': self.photo, 'text': '', 'value': (self.pic_name, '')}
        return kwTreeview


class wd_Menu(Menu):
    def __init__(self, frameMaster, **kwargs):
        super().__init__(frameMaster, tearoff=0)

        self.frameMaster = frameMaster

        self.nome_op1 = kwargs.get('nome_B1', 'Opção 1')
        #self.nome_op2 = kwargs.get('nome_B2', 'Opção 2')

        self.command_op1 = kwargs.get('command_op1', None)
        #self.command_op2 = kwargs.get('command_op2', None)

        self.add_command(label=self.nome_op1, command=self.command_op1)
        #self.add_command(label=self.nome_op2, command=self.command_op2)

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

class painel_config_view(Toplevel):
    def __init__(self, controller):
        super().__init__(padx = 10, pady = 10)
        self.update()
        self.deiconify()
        self.resizable(False, False)
        self.controller = controller
        self.range_spinBox = models_app.range_freq()
        self.range_spinBox.load()

        self.buttonCancel = ttk.Button(self, command = self.cancel_config, text = 'Cancelar')
        self.buttonCancel.grid(row = 3, column = 0, sticky = 'WEN', padx=11)

        self.frame1 = LabelFrame(self, text = 'Experimento da onda na corda')
        self.frame1.grid(row = 1, column = 0, padx = 11, pady = 11, ipady = 11, sticky = 'N')
        self.label_frame1 = ttk.Label(self.frame1, text = 'Alterar resolução da frequência:')
        self.label_frame1.grid(column = 0, row = 0, columnspan = 2)

        self.label_spinbox1_frame1 =  ttk.Label(self.frame1, text = 'Frequencia inicial: (Hz) ')
        self.label_spinbox1_frame1.grid(row = 1, column = 0)
        self.spinbox1_frame1 = Spinbox(self.frame1, from_ = self.range_spinBox.corda_from, to = self.range_spinBox.corda_to)
        self.spinbox1_frame1.grid(column = 0, row = 2, pady = 10, padx = 11)

        self.label_spinbox2_frame1 =  ttk.Label(self.frame1, text = 'Frequencia final: (Hz) ')
        self.label_spinbox2_frame1.grid(row = 1, column = 1)
        self.spinbox2_frame1 = Spinbox(self.frame1, from_ = self.range_spinBox.corda_from, to = self.range_spinBox.corda_to)
        self.spinbox2_frame1.grid(column = 1, row = 2, pady = 10, padx = 11)
        self.spinbox2_frame1.delete(0, "end")
        self.spinbox2_frame1.insert(0, str(self.range_spinBox.corda_to))

        self.button1_frame1 = ttk.Button(self.frame1, text = 'Salvar alterações', command = self.save_config)
        self.button1_frame1.grid(row=3, column=0, pady = 10, padx = 11, sticky = 'we')
        self.button2_frame1 = ttk.Button(self.frame1, text = 'Restaurar valores padrão', command = self.restore_config_corda)
        self.button2_frame1.grid(row=3, column=1, pady = 10, padx = 11, sticky = 'we')

        self.frame2 = LabelFrame(self, text='Experimento da onda na superfície')
        self.frame2.grid(row=2, column=0, padx=11, pady=11, ipady = 11, sticky = 'N')
        self.label_frame2 = ttk.Label(self.frame2, text = 'Alterar resolução da frequência:')
        self.label_frame2.grid(column = 0, row = 0, columnspan = 2)

        self.label_spinbox1_frame2 =  ttk.Label(self.frame2, text = 'Frequencia inicial: (Hz) ')
        self.label_spinbox1_frame2.grid(row = 1, column = 0)
        self.spinbox1_frame2 = Spinbox(self.frame2, from_ = self.range_spinBox.sup_from, to = self.range_spinBox.sup_to)
        self.spinbox1_frame2.grid(column = 0, row = 2, pady = 10, padx = 11)

        self.label_spinbox2_frame2 =  ttk.Label(self.frame2, text = 'Frequencia final: (Hz) ')
        self.label_spinbox2_frame2.grid(row = 1, column = 1)
        self.spinbox2_frame2 = Spinbox(self.frame2, from_ = self.range_spinBox.sup_from, to = self.range_spinBox.sup_to)
        self.spinbox2_frame2.grid(column = 1, row = 2, pady = 10, padx = 11)
        self.spinbox2_frame2.delete(0, "end")
        self.spinbox2_frame2.insert(0, str(self.range_spinBox.sup_to))

        self.button1_frame2 = ttk.Button(self.frame2, text='Salvar alterações', command = self.save_config)
        self.button1_frame2.grid(row = 3, column = 0, pady = 10, padx = 11, sticky = 'we')
        self.button2_frame2 = ttk.Button(self.frame2, text='Restaurar valores padrão', command = self.restore_config_sup)
        self.button2_frame2.grid(row = 3, column = 1, pady = 10, padx = 11, sticky = 'we')


        self.padroesView = padroes_view(self, self.controller)
        self.padroesView.grid(row = 1, column = 1, rowspan = 10)



    def cancel_config(self):
        self.destroy()

    def restore_config_corda(self):
        #O range é restaurado:
        self.controller.restore_model(self.range_spinBox, tipo = 'corda')
        #SpinBox são reiniciadas:
        self.spinbox1_frame1.delete(0, "end")
        self.spinbox1_frame1.insert(0, str(self.range_spinBox.corda_from))
        self.spinbox2_frame1.delete(0, "end")
        self.spinbox2_frame1.insert(0, str(self.range_spinBox.corda_to))

    def restore_config_sup(self):
        # O range é restaurado:
        self.controller.restore_model(self.range_spinBox, tipo='sup')

        self.spinbox1_frame2.delete(0, "end")
        self.spinbox1_frame2.insert(0, str(self.range_spinBox.sup_from))
        self.spinbox2_frame2.delete(0, "end")
        self.spinbox2_frame2.insert(0, str(self.range_spinBox.sup_to))

    def save_config(self):
        corda_from = self.spinbox1_frame1.get()
        corda_to =self.spinbox2_frame1.get()
        sup_from = self.spinbox1_frame2.get()
        sup_to = self.spinbox2_frame2.get()
        self.controller.update_model(self.range_spinBox, corda_from = corda_from, corda_to = corda_to, sup_from = sup_from, sup_to = sup_to)


    def update_view(self):
        self.padroesView.update_view()
        self.update()
        self.deiconify()

    def altera_exp(self):
        self.controller.show_frame('padroes_view')



class padroes_view(Frame):
    def __init__(self, frameMaster, controller = None):
        super().__init__(frameMaster, padx = 10, pady = 10)
        self.frameMaster = frameMaster
        self.controller = controller
        self.lst_pics = self.controller.lst_exp
        self.popUpMenu = wd_Menu(self, nome_B1='Alterar experimento', command_op1 = self.alterar)

        style = ttk.Style(self.controller)
        style.configure('Treeview', rowheight=110)

        self.frameLocal = LabelFrame(self, text = 'Alterar padrões esperados')
        self.frameLocal.grid(row = 0, column = 0)

        self.label1 = ttk.Label(self.frameLocal, text = 'Selecione o experimento que deseja alterar:')
        self.label1.grid(row = 0, column = 0, sticky = 'we', padx = 20, pady = 11)
        self.buttonAlterar = ttk.Button(self.frameLocal, text = 'Alterar experimento', state = 'disabled', command = self.alterar)
        self.buttonAlterar.grid(row = 1, column = 0, sticky = 'We', padx = 20)

        #self.buttonCancelar = ttk.Button(self, text = 'Cancelar', state = 'enabled', command = self.cancelar)
        #self.buttonCancelar.grid(row = 2, column = 0, sticky = 'We', padx = 20)

        self.frameTreeview = ttk.Frame(self.frameLocal)
        self.frameTreeview.grid(row = 3, column = 0, padx = 20, pady = 20)
        # Create Treeview
        self.tree = ttk.Treeview(self.frameTreeview, column=('A','B'), height=5, selectmode='browse')
        self.tree.grid(row=0, column=0, sticky='nsew')

        # Setup column heading
        self.tree.heading('#0', text=' Padrão esperado', anchor='center')
        self.tree.heading('#1', text=' Frequência (Hz): ', anchor='center')
        self.tree.heading('#2', text=' Tipo do experimento:', anchor='center')
        # #0, #01, #02 denotes the 0, 1st, 2nd columns

        # Setup column
        self.tree.column('A', anchor='center', width=100, stretch = True)
        self.tree.column('B', anchor='center', width=115, stretch = True)

        # Bloco das Scrollbars(barras de rolagem):
        self.scrollbarY = Scrollbar(self.frameTreeview, command=self.tree.yview)
        self.scrollbarY.grid(row=0, column=1, sticky= N+S)
        # Bloco  Declaradas a Scrollbar, treeView2 é configurado a recebê-las:
        self.tree.config(yscrollcommand=self.scrollbarY.set)

        self.__insert_treeView__()

        self.tree.bind('<<TreeviewSelect>>', lambda event: self.bind_select())
        self.tree.bind('<Button-3>', lambda event: self.bind_B3(event))
        self.id_pic_sel = None

    def cancelar(self):
        self.destroy()

    def __insert_treeView__(self):
        self.lst_pics = self.controller.lst_exp
        self.insert_list(self.lst_pics.toTreeview())

    def update_view(self):
        self.update()
        self.__insert_treeView__()

    def alterar(self):
        exp_sel = self.lst_pics.search_pic(self.id_pic_sel)
        self.controller.show_frame('altera_padrao', experimento = exp_sel)

    def bind_B3(self, event):
        self.popUpMenu.popup(event)

    def bind_select(self):
        try:
            self.id_pic_sel = int(self.tree.selection()[0])
            self.buttonAlterar.config(state = 'enabled')
        except ValueError:
            self.id_pic_sel = self.tree.selection()[0]
        print(self.id_pic_sel)

    def update_pic(self, wd_pic: wd_GUI_Image, pic_nome):
        wd_pic.update(PIC_NAME = pic_nome)

    def insert_list(self, lst:list):
        self.tree.delete(*self.tree.get_children())
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

class altera_exp_view(Toplevel):
    def __init__(self, controller, exp: models_app.PadraoExp):
        super().__init__(padx = 20, pady = 15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.controller = controller
        self.experimento = exp

        self.pic_portrait = Label(self)
        self.pic_portrait.grid(row=0, column=0, padx = 20, pady = 15, rowspan = 4)

        self.pic_label = Label(self)
        self.pic_label.grid(row=5, column=0)

        self.entry = wd_Entry(self, tit_Entry='Frequência (Hz):')
        self.entry.grid_frame(row = 0, column = 1)

        self.button = ttk.Button(self, text = 'Alterar', command = lambda: self.command_B1())
        self.button.grid(row=1, column=1, sticky = 'WE')

        self.separatorH = ttk.Separator(self, orient=HORIZONTAL, style="TSeparator")
        self.separatorH.grid(row=2, column=1, columnspan = 5, sticky="WE", padx=2, pady=3)

        self.button = ttk.Button(self, text = 'Alterar foto', command = lambda: self.command_B2())
        self.button.grid(row=3, column=1, sticky = 'WE')

        self.__fill_frame__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def callback(self):
        self.controller.atualiza_view()
        self.destroy()

    def __fill_frame__(self):
        self.pic_portrait.config(image = self.experimento.PhotoImage)
        self.pic_label.config(text=self.experimento.freq)
        self.entry.insert_Entry(self.experimento.freq)

    def command_B1(self):
        freq = self.entry.retorna_entr()
        self.controller.update_model(self.experimento, freq = freq)
        #self.experimento.update(freq = freq)
        self.__fill_frame__()

    def command_B2(self):
        pic_dir = askopenfilename(defaultextension = '.jpg', filetypes= [('Todas',['*.jpg','*.png','*.gif','*.bmp']),('JPG','*.jpg'), ( 'PNG', '*.png'), ( 'GIF','*.gif'),('BMP', '*.bmp')])
        if pic_dir is not '':
            picture_file = PIL.Image.open(pic_dir)
            self.experimento.update(PhotoImage = picture_file)
            self.__fill_frame__()
            self.update()
            self.deiconify()

class wd_Experimento(Frame):
    def __init__(self, frameMaster, padrao: models_app.PadraoExp):
        super().__init__(frameMaster, padx = 11, pady = 11)
        self.PadraoExp = padrao
        self.pic_portrait = Label(self, image=self.PadraoExp.PhotoImage)
        self.pic_portrait.grid(row=0, column=0, rowspan = 4)
        self.pic_portrait.image = self.PadraoExp.PhotoImage  # keep a reference!
        self.pic_label = Label(self, text=self.PadraoExp.freq)
        self.pic_label.grid(row=5, column=0)

class padroes_apr_view(Frame):
    def __init__(self, frameMaster, controller):
        super().__init__(frameMaster)
        self.controller = controller
        self.__fill_frame__()

    def __fill_frame__(self):
        lst_aux = self.controller.lst_exp
        self.lst_exp = []
        for elem in lst_aux:
            if elem.tipo == 'SUP_APR':
                self.lst_exp.append(elem)
        self.padrao1 = wd_Experimento(self, self.lst_exp[0])
        self.padrao1.grid(row=0, column=0)
        self.padrao2 = wd_Experimento(self, self.lst_exp[1])
        self.padrao2.grid(row=0, column=1)
        self.padrao3 = wd_Experimento(self, self.lst_exp[2])
        self.padrao3.grid(row=0, column=2)
        self.padrao4 = wd_Experimento(self, self.lst_exp[3])
        self.padrao4.grid(row=0, column=3)
        self.padrao5 = wd_Experimento(self, self.lst_exp[4])
        self.padrao5.grid(row=1, column=0)
        self.padrao6 = wd_Experimento(self, self.lst_exp[5])
        self.padrao6.grid(row=1, column=1)
        self.padrao5 = wd_Experimento(self, self.lst_exp[6])
        self.padrao5.grid(row=1, column=2)
        self.padrao6 = wd_Experimento(self, self.lst_exp[7])
        self.padrao6.grid(row=1, column=3)

    def update_view(self):
        self.__fill_frame__()
        self.update()

class padroes_exp_view(Frame):
    def __init__(self, frameMaster, controller, **kwargs):
        super().__init__(frameMaster)
        self.controller = controller
        self.tipo = kwargs.get('tipo', 'corda')
        self.__fill_frame__()

    def __fill_frame__(self):
        lst_aux = self.controller.lst_exp
        if self.tipo is 'corda':
            self.lst_exp = []
            for elem in lst_aux:
                if elem.tipo == 'CORDA':
                    self.lst_exp.append(elem)
            self.padrao1 = wd_Experimento(self, self.lst_exp[0])
            self.padrao1.grid(row=0, column=0)
            self.padrao2 = wd_Experimento(self, self.lst_exp[1])
            self.padrao2.grid(row=0, column=1)
            self.padrao3 = wd_Experimento(self, self.lst_exp[2])
            self.padrao3.grid(row=0, column=2)
            self.padrao4 = wd_Experimento(self, self.lst_exp[3])
            self.padrao4.grid(row=1, column=0)
            self.padrao5 = wd_Experimento(self, self.lst_exp[4])
            self.padrao5.grid(row=1, column=1)
            self.padrao6 = wd_Experimento(self, self.lst_exp[5])
            self.padrao6.grid(row=1, column=2)

        elif self.tipo is 'superficie':
            self.lst_exp = []
            for elem in lst_aux:
                if elem.tipo == 'SUP':
                    self.lst_exp.append(elem)
            self.padrao1 = wd_Experimento(self, self.lst_exp[0])
            self.padrao1.grid(row=0, column=0)
            self.padrao2 = wd_Experimento(self, self.lst_exp[1])
            self.padrao2.grid(row=0, column=1)
            self.padrao3 = wd_Experimento(self, self.lst_exp[2])
            self.padrao3.grid(row=0, column=2)
            self.padrao4 = wd_Experimento(self, self.lst_exp[3])
            self.padrao4.grid(row=1, column=0)
            self.padrao5 = wd_Experimento(self, self.lst_exp[4])
            self.padrao5.grid(row=1, column=1)
            self.padrao6 = wd_Experimento(self, self.lst_exp[5])
            self.padrao6.grid(row=1, column=2)

    def update_view(self):
        self.__fill_frame__()
        self.update()

class wd_Scale(Frame):
    def __init__(self, frameMaster, **kwargs):
        super().__init__(frameMaster)
        self.config(pady=10)

        self.inicValueLabel = Label(self, text= str(kwargs.get('from_')) + ' Hz')
        self.inicValueLabel.grid(row=0, column=1, sticky=W + N)

        self.var = DoubleVar()
        self.scaleBar = ttk.Scale(self, **kwargs)
        self.scaleBar.config(variable=self.var)
        self.scaleBar.grid(row=0, column=0, sticky=W + S + N, rowspan=3)
        self.scaleBar.bind('<Motion>', lambda event: self.setValue())

        self.scaleHzLabel = Label(self, text='freq Hz')
        self.scaleHzLabel.grid(row=1, column=1)

        self.endValueLabel = Label(self, text=str(kwargs.get('to')) + ' Hz')
        self.endValueLabel.grid(row=2, column=1, sticky=W + S)

    def setValue(self):
        value = str(round(self.scaleBar.get(), 3))
        # print(value, ' Hz')
        self.scaleHzLabel.config(text=value + ' Hz')

    def set(self, value):
        value = float(value)
        self.scaleBar.set(value)

    def config_scale(self, **kwargs):
        self.scaleBar.config(**kwargs)

    def get(self):
        return (self.scaleBar.get())

class controle_corda_view(Frame):
    def __init__(self, framePai, controller):
        super().__init__(framePai)
        self.controller = controller
        self.range_spinBox = models_app.range_freq()
        self.range_spinBox.load()

        self.frameLocal = LabelFrame(framePai, text='Experimento da onda na corda', relief=GROOVE, padx=15, pady=15)
        self.frameLocal.grid()

        self.freqControlFrame = Frame(self.frameLocal)
        self.freqControlFrame.grid(row=0, column=0)

        self.scaleLabel = Label(self.freqControlFrame, text='Ajuste ou digide a frequência (Hz)')
        self.scaleLabel.grid(row=0, column=0, columnspan=2)

        self.scaleBar = wd_Scale(self.freqControlFrame, orient='vertical', length=150, from_=self.range_spinBox.corda_from, to=self.range_spinBox.corda_to,
                                 command=lambda event: self.comandoScale())

        self.scaleBar.grid(row=1, column=0, sticky=W, rowspan=3)

        self.entr1 = wd_Entry(self.freqControlFrame, tit_Entry='Digite a frequencia: (Hz)', state_Entry='enabled')
        self.entr1.Entry.bind('<Return>', lambda event: self.comandoB1())
        self.entr1.grid_frame(row=4, column=0, columnspan=2)

        # O botao1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao1 = ttk.Button(self.freqControlFrame, text='Enviar', command=lambda: self.comandoB1())

        self.botao1.grid(row=5, column=0, sticky=W + E, padx=2, columnspan=2)


        self.framePadroesCorda = padroes_exp_view(self.frameLocal, self.controller, tipo='corda')
        self.framePadroesCorda.grid(row=0, column=1)

    def comandoB1(self):
        print('comando B1')
        freq = self.entr1.retorna_entr()
        self.scaleBar.set(float(freq))
        if self.controller.verfCon() is True:
            self.controller.enviaFreq(freq)
        else:
            pass

    def comandoScale(self):
        freq = round(float(self.scaleBar.get()), 4)
        self.entr1.insert_Entry(str(freq))
        if self.controller.verfCon() is True:
            self.controller.enviaFreq(freq)
        else:
            pass

    def update_view(self):
        self.framePadroesCorda.update_view()

class wd_2_Tabs(Frame):
    def __init__(self, framePai, controller):
        super().__init__(framePai)
        self.grid()

        # Blobo (1): Configurando frame que conterá as abas, o frameAbas:
        self.config(padx=15, pady=15)

        # Bloco (3): Aqui, é instanciado o tipo Notebook, que na verdade é um frame que conterá as abas:
        self.abasBarra = ttk.Notebook(self)
        self.abasBarra.grid(row=0, column=0, sticky=E + W)

        # Bloco (4): Abaixo, cada aba é instanciada, cujo frame pai é o "Abas":
        self.aba1 = ttk.Frame(self.abasBarra)
        self.abasBarra.add(self.aba1, text="Padroões obtidos")

        self.aba2 = ttk.Frame(self.abasBarra)
        self.abasBarra.add(self.aba2, text="Padroões aproximados")

    def config_nome_aba1(self, titulo):
        self.abasBarra.tab(self.aba1, text=titulo)

    def config_nome_aba2(self, titulo):
        self.abasBarra.tab(self.aba2, text=titulo)

class controle_sup_view(Frame):
    def __init__(self, framePai, controller):
        super().__init__(framePai)
        self.controller = controller
        self.range_spinBox = models_app.range_freq()
        self.range_spinBox.load()

        self.frameLocal = LabelFrame(framePai, text='Experimento da onda na superfície', relief=GROOVE, padx=15,
                                     pady=15)
        self.frameLocal.grid()

        self.freqControlFrame = Frame(self.frameLocal)
        self.freqControlFrame.grid(row=0, column=0)

        self.scaleLabel = Label(self.freqControlFrame, text='Ajuste ou digide a frequência (Hz)')
        self.scaleLabel.grid(row=0, column=0, columnspan=2)

        self.scaleBar = wd_Scale(self.freqControlFrame, orient='vertical', length=150, from_=self.range_spinBox.sup_from, to=self.range_spinBox.sup_to,
                                 command=lambda event: self.comandoScale())
        self.scaleBar.grid(row=1, column=0, sticky=W, rowspan=3)

        self.entr1 = wd_Entry(self.freqControlFrame, tit_Entry='Digite a frequencia: (Hz)', state_Entry='enabled')
        self.entr1.Entry.bind('<Return>', lambda event: self.comandoB1())
        self.entr1.grid_frame(row=4, column=0, columnspan=2, sticky=W)

        # O botao1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao1 = ttk.Button(self.freqControlFrame, text='Enviar', command=lambda: self.comandoB1())
        self.botao1.grid(row=5, column=0, sticky=W + E, padx=2, columnspan=2)

        self.abasFrame = wd_2_Tabs(self.frameLocal, self.controller)
        self.abasFrame.grid(row=0, column=1)

        self.framePadroesSuperf = padroes_exp_view(self.abasFrame.aba1, self.controller, tipo='superficie')
        self.framePadroesSuperf.grid()

        self.framePadroesAprox = padroes_apr_view(self.abasFrame.aba2, self.controller)
        self.framePadroesAprox.grid()

    def update_view(self):
        self.framePadroesAprox.update_view()
        self.framePadroesSuperf.update_view()

    def comandoB1(self):
        freq = self.entr1.retorna_entr()
        self.scaleBar.set(float(freq))
        self.controller.enviaFreq(freq)

    def comandoScale(self):
        freq = round(float(self.scaleBar.get()), 4)
        self.entr1.insert_Entry(str(freq))
        if self.controller.verfCon() is True:
            self.controller.enviaFreq(freq)
        else:
            pass

class menu_esq_view(Frame):
    def __init__(self, framePai, controller):
        super().__init__(framePai)
        self.controller = controller

        # Bloco (2.1): Abaixo, é declarado o frame que conterá o menu. O frame está contido no frame-pai:
        self.frameLocal = Frame(self, padx=2, pady=4)
        self.frameLocal.grid(row=0, column=0, sticky=N + S)

        # Subtítulos do programa:
        # O subTitulo1 é declarado e "fixado"(.grid) dentro do frameLocal com o nome do programa:
        self.tit1 = Label(self.frameLocal, text='Ondas', font='Verdana', anchor=CENTER, relief=GROOVE, padx=3, pady=3)
        self.tit1.grid(row=0, column=0, sticky=E + W, padx=3,
                       pady=3)  # , sticky = E+W)#Subtitulo fixado na origem do "frameLocal"(row=0, column=0)

        self.separadorV1 = ttk.Separator(self.frameLocal, orient=VERTICAL, style="TSeparator")
        self.separadorV1.grid(row=0, column=1, rowspan=13, sticky="ns", padx=2, pady=3)

        # O subtitulo3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.title_font = tkfont.Font(family='Helvetica', size=14, weight="bold", slant="italic")
        self.arduinoStatus = ttk.Label(self.frameLocal, text='Arduino status', font=self.title_font)
        self.arduinoStatus.grid(row=1, column=0, sticky=E + W, padx=3, pady=3)

        # O subtitulo4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.tit3 = Label(self.frameLocal, text='Menu', relief=FLAT, font='Verdana', anchor=CENTER)
        self.tit3.grid(row=2, column=0, sticky=E + W)

        # ttk.Style().configure("Toolbutton", relief = "ridge")
        # ttk.Style().configure('Toolbutton.label', 'sticky' = 'we')
        # ~ print(ttk.Style().layout('Toolbutton'))

        # A variável varRb guardará o valor dos Radiobuttons
        self.varRb = IntVar()
        self.Rb1 = ttk.Radiobutton(self.frameLocal, text="Propagação de ondas na corda", value=1, variable=self.varRb,
                                   style='Toolbutton')
        self.Rb1.config(command=lambda: self.controller.show_frame("frame_onda_corda"))
        self.Rb1.grid(row=3, column=0, sticky=E + W, padx=3, pady=1)

        # O  botao2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb2 = ttk.Radiobutton(self.frameLocal, text="Propagação de ondas na superfície", value=2,
                                   variable=self.varRb, style='Toolbutton')
        self.Rb2.config(command=lambda: self.controller.show_frame("frame_onda_membr"))
        self.Rb2.grid(row=4, column=0, sticky=E + W, padx=3, pady=1)


        # O  botao2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb4 = ttk.Radiobutton(self.frameLocal, text="Levitador acústico", value=2,
                                   variable=self.varRb, style='Toolbutton')
        self.Rb4.config(command=lambda: self.controller.show_frame("frame_onda_membr"))
        self.Rb4.grid(row=6, column=0, sticky=E + W, padx=3, pady=1)


        # O  botao3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb3 = ttk.Button(self.frameLocal, style='Toolbutton', text="Tanque de ondas" )
        self.Rb3.config(command=lambda: self.verfArduinoPopUp())
        self.Rb3.grid(row=5, column=0, sticky=E + W, padx=3, pady=1)

        # O  botao4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb4 = ttk.Radiobutton(self.frameLocal, text='', value=4, variable=self.varRb, style='Toolbutton',
                                   state='disabled')
        self.Rb4.grid(row=6, column=0, sticky=E + W, padx=3, pady=1)

        # O  botao4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb5 = ttk.Radiobutton(self.frameLocal, text='', value=4, variable=self.varRb, style='Toolbutton',
                                   state='disabled')
        self.Rb5.grid(row=7, column=0, sticky=E + W, padx=3, pady=1)

        # O  botao4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb6 = ttk.Radiobutton(self.frameLocal, text='', value=4, variable=self.varRb, style='Toolbutton',
                                   state='disabled')
        self.Rb6.grid(row=8, column=0, sticky=E + W, padx=3, pady=1)

        # O  botao4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb7 = ttk.Radiobutton(self.frameLocal, text='', value=4, variable=self.varRb, style='Toolbutton',
                                   state='disabled')
        self.Rb7.grid(row=9, column=0, sticky=E + W, padx=3, pady=1)

        # O  botao4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb7 = ttk.Radiobutton(self.frameLocal, text='', value=4, variable=self.varRb, style='Toolbutton',
                                   state='disabled')
        self.Rb7.grid(row=10, column=0, sticky=E + W, padx=3, pady=1)

        # imageIn = PIL.Image.open(".\DBApp\pictures\IFES2.png")
        # self.image = imageIn.resize((200, 115), PIL.Image.ANTIALIAS)
        # self.photo = PIL.ImageTk.PhotoImage(self.image)
        # self.label_photo = Label(self.frameLocal, image=self.photo)
        # self.label_photo.image = self.photo  # keep a reference!
        self.wd_photo = wd_GUI_Image(self.frameLocal, pic_name='IFES2', pic_resolution=(200, 115))
        self.wd_photo.grid(row=11, column=0, sticky=S)

    def verfArduinoPopUp(self):
        self.controller.verfArduinoPopUp()

    def ardStatusLabel(self, status):
        if status is True:
            self.arduinoStatus.config(text='Arduino conectado!', foreground='green')
        else:
            self.arduinoStatus.config(text='Arduino não conectado!', foreground='red')

    def desativa_todos_Rb(self):
        self.Rb1.config(state="disabled")
        self.Rb2.config(state="disabled")
        self.Rb3.config(state="disabled")
        # ~ self.Rb4.config(state = "disabled")

    def ativa_todos_Rbs(self):
        self.Rb1.config(state="eneable")
        self.Rb2.config(state="eneable")
        self.Rb3.config(state="eneable")
        # ~ self.Rb4.config(state = "eneable")

    def escolha_Rb(self):
        escolha = self.varRb.get()
        return (escolha)

class main_frame(Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        # Bloco (1) Configurando frame principal(janela-pai):
        self.controller = controller
        self.master = master
        # Comando abaixo configura a resoluação padrão da janela como sendo a resolução do PC em questão:
        # self.master.geometry("1000x600")
        # self.master.geometry("{}x{}".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # Comando abaixo configura a janela para iniciar como "maximizada":
        # self.master.state('zoomed')
        # Comando abaixo configura o título da janela:
        self.master.title('Ondas - IFES')

        # self.master.iconbitmap('icon.bmp')
        # Comando abaixo printa no terminal a resolução configurada para a máquina em questão:
        # ~ print(self.master.winfo_screenwidth(), self.master.winfo_screenheight())

        # Abaixo é declarada a janela-pai
        self.framePai = self
        self.framePai.grid(sticky=E + W + S + N)

        #
        # Fim do Bloco (1)
        # ------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        # ------------------------------------------------------------------------------------------------------------------#

        # Bloco (2) Declaração do menu superior da janela-pai:
        self.menuSuperior = Menu(self.master)

        self.master.config(menu=self.menuSuperior)

        # Abaixo a declaração e as Sub-opções dentro da opção "Arquivo":
        self.menuArquivo = Menu(self.menuSuperior, tearoff=0)
        #self.menuSuperior.add_cascade(menu=self.menuArquivo, label='Arquivo')
        # Sub-opções dentro da opção "Arquivo":
        #self.menuArquivo.add_command(label="Carregar", command=self.load_pic)
        #self.menuArquivo.add_command(label="Novo", command=self.load_file_txt)
        # Comando abaixo adciona um layout de separação entre as opções do menu:
        #self.menuArquivo.add_separator()  # Esse comando adciona um layout de separação entre as opções do menu

        # Abaixo a declaração e as Sub-opções dentro da opção "Configurações":
        self.menuConfiguracoes = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuConfiguracoes, label='Ferramentas')
        # Sub-opções dentro da opção "Configurações":,
        self.menuConfiguracoes.add_command(label="Configurações", command = self.configuracoes)
        # Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuConfiguracoes.add_separator()

        # Abaixo a declaração e as Sub-opções dentro da opção "Ajuda":
        self.menuAjuda = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuAjuda, label='Ajuda')
        # Sub-opções dentro da opção "Ajuda":
        self.menuAjuda.add_command(label="Tutorial")
        self.menuAjuda.add_command(label="Sobre")
        # Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuAjuda.add_separator()

        # Comando que exibe o menu:
        # master.config(menu=self.menuSuperior)

        # Fim do bloco (2)
        # ------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        # ------------------------------------------------------------------------------------------------------------------#

        # Bloco (3) Declarando sub-frames da janela-pai:
        '''A janela-pai está dividida em três sub-frames, lateral esquerdo, central, lateral direito, e um sub-frame de rodapé.
                Na presente classe, cada um dos três sub-frames não admite sub-divisões, sendo containeres.
                Sendo assim, adimitindo o maior grau de divisão de frames na classe, a janela-pai terá a seguinte divisão:
                
                ______________________________janela-pai______________________________
                |(subFrameLateralEsquerdo)|(subFrameCentral)|(subFrameLateralDireito)|
                |							subFrameInferior-rodapé						 |
                        
        '''

        # Bloco (3.1): Abaixo, é declarado o frame lateral esquerdo. O frame está contido no frame-pai:
        self.frame_esquerdo = Frame(self.framePai, padx="4", pady="4")
        self.menu = menu_esq_view(self.frame_esquerdo, controller)
        self.menu.grid()
        self.frame_esquerdo.grid(row=0, column=0, sticky=N + S)

        # Bloco (3.3): Abaixo, é declarado o frame central. O frame está contido no frame-pai:
        self.frame_central = Frame(self.framePai, padx="20", pady="20")
        self.frame_central.grid(row=0, column=1, sticky=N + S + W + E)

        # Bloco (3.4): Abaixo, é declarado o frame lateral direito. O frame está contido no frame-pai:
        self.frame_direito = Frame(self.framePai, padx="4", pady="4")
        self.frame_direito.grid(row=0, column=2, sticky=N + S)

        # Bloco (3.5): Abaixo, é declarado o frame inferior no rodapé da do frame-pai(note o columnspan = 3):
        self.frame_infe = Frame(self.framePai, padx="4")
        self.frame_infe.grid(row=1, column=0, columnspan=3, sticky=W + E)

    #####################################################################
    #############  FIM DA __init__  #####################################
    #####################################################################

    def configuracoes(self):
        self.controller.show_frame('painel_config_view')


    def load_pic(self):
        try:
            nomePhoto = askopenfilename()
            print("\n" + nomePhoto)
            imageRaw = PIL.Image.open(nomePhoto)
            image = imageRaw.resize((100, 100), PIL.Image.ANTIALIAS)
            photo = PIL.ImageTk.PhotoImage(image)
            caixa = Toplevel()
            label_photo = Label(caixa, image=photo)
            label_photo.image = photo  # keep a reference!
            label_photo.grid()

        except Exception as Expt:
            print(Expt)
            pass

    def destroi_framesFilhos(self, frame):
        if frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].destroy()
                cont = cont + 1
        else:
            return None

    def ungrid_framesFilhos(self, frame):
        if frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].grid_forget()
                # lst_frames[cont].destroy
                cont = cont + 1
        else:
            return None

    def ungrid_framesFilhos_cent(self):
        self.ungrid_framesFilhos(self.frame_central)

    def destroi_framesFilhos_cent(self):
        self.destroi_framesFilhos(self.frame_central)

    def ungrid_framesFilhos_esqr(self):
        self.ungrid_framesFilhos(self.frame_esquerdo)

    def ungrid_framesFilhos_dire(self):
        self.ungrid_framesFilhos(self.frame_direito)

    def ungrid_framesFilhos_infe(self):
        self.ungrid_framesFilhos(self.frame_infe)

    def lst_framesFilhos_cent(self):
        return (self.frame_central.winfo_children())

    def finaliza(self):
        self.framePai.destroy()
