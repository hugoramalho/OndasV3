from tkinter import *


class sub_Text(tk.Frame):

    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.tit = kwargs.get('tit', 'Título')
        self.state = kwargs.get('state', NORMAL)
        self.width = kwargs.get('width', 50)
        self.height = kwargs.get('height', 4)
        self.scrollbarx = kwargs.get('scrollbarx', True)
        self.scrollbary = kwargs.get('scrollbary', True)

        #Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frameLocal = tk.Frame(self)


        self.tit_text = ttk.Label(self.frameLocal, text = self.tit )
        self.tit_text.grid(row = 0, column = 0, sticky = W)
        
        self.blocoText = tk.Text(self.frameLocal, insertborderwidth = 5, bd = 3, font = "Arial 9", wrap = WORD, width = self.width, height = self.height, state = self.state, autoseparators=True)
        self.blocoText.grid(row = 1, column = 0)


        self.__scrollbar_constr__()


        #~ self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        #~ self.separador1.grid(row = 5, column = 0, columnspan = 5, sticky = "we")


    def return_text(self):
        text = self.blocoText.get(1.0, "end")
        return (text)

    def config_tit_text(self, text):
        self.tit_text.config(text = text)
        

    def __scrollbar_constr__(self):
        if self.scrollbarx == True:
            self.scrollbarX = tk.Scrollbar(self.frameLocal, command = self.blocoText.xview, orient = HORIZONTAL)
            self.scrollbarX.grid(row= 2, column = 0, sticky = E+W)
            self.blocoText.config(xscrollcommand = self.scrollbarX.set)
            
            
        if self.scrollbary == True:
            self.scrollbarY = tk.Scrollbar(self.frameLocal, command = self.blocoText.yview, orient = VERTICAL)
            self.scrollbarY.grid(row = 1, column = 1,sticky=N+S)
            self.blocoText.config(yscrollcommand = self.scrollbarY.set)


    def insert_text(self, txtStr):
        self.blocoText.config(state = NORMAL)
        self.blocoText.delete(1.0, END)
        self.blocoText.insert(1.0, txtStr)
        self.blocoText.config(state = DISABLED)
    
    def clear_text(self):
        self.blocoText.config(state=NORMAL)
        self.blocoText.delete('1.0', END)
        self.blocoText.config(state=DISABLED)


    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan, pady = pady, padx = padx, sticky = sticky)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def destroy_frame(self):
        
        self.frameLocal.destroy()


class sub_Treeview(tk.Frame):

    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.quantCol =  kwargs.get('num_cols', 4)
        self.tit = kwargs.get('tit', 'Título')
        self.height = kwargs.get('height', 4)
        self.selectmode = kwargs.get('selectmode', 'browse')
        
        self.frameLocal = tk.Frame(self)
        
        self.tit_treeView = tk.Label(self.frameLocal, text = self.tit)
        self.tit_treeView.grid(row = 0, column = 0, sticky = W)
        
        
        columnTuple = self.__column_tuple__()
        self.treeView = ttk.Treeview(self.frameLocal, height = self.height, style = "Treeview", selectmode='browse', columns = columnTuple)
        self.treeView.grid(row = 1, column = 0)
        
        self.__column_constr__()
        
        
        
            #Bloco das Scrollbars(barras de rolagem):
        self.scrollbarY= tk.Scrollbar(self.frameLocal, command = self.treeView.yview)
        self.scrollbarY.grid(row = 1, column = 1,sticky = N+S)
            #Bloco  Declaradas a Scrollbar, treeView1 é configurado a recebê-las:
        self.treeView.config(yscrollcommand = self.scrollbarY.set)

    def pointer_treeView(self):
        return(self.treeView)


    def config_tit_treeView(self, tit):
        self.tit_treeView.config(text = tit)

    def config_tit_col_treeView(self, col, titulo):
        if type(col) != str:
            col = str(col)
        if col == '0':
            col = '#0'
        self.treeView.heading(col, text = titulo)

    def selection_treeView(self):
        return(self.treeView.selection())

    def idd_selection_treeView(self):
        return(int(self.treeView.selection()[0]))


    def item_treeView(self, idd):
        return(self.treeView.item(idd))

    def __column_tuple__(self):
        
        lstAux = []
        if self.quantCol == 1:
            columnTuple = tuple(lstAux)
        
        else:
            n = 0
            while n < (self.quantCol-1):
                quant = n + 1
                columnAux = str(quant)
                lstAux.append(columnAux)
                n = n + 1
            
            columnTuple = tuple(lstAux)
        
        return(columnTuple)

    def __column_constr__(self):
        self.treeView.heading("#0", text = "text")
        self.treeView.column("#0", width = 220, stretch = 0)
        
        n = 1
        while n < (self.quantCol):
            columnAux = str(n)
            self.treeView.heading(columnAux, text="coluna 1")
            self.treeView.column(columnAux, width=100, stretch = 0)
            n = n + 1


    def insere_elem_treeView(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = '', **kwargs):
        idd = kwargs.get('idd', None)
        elems = (value1, value2, value3, value4)
        self.treeView.insert('', 0, iid = idd, text = value0, values = elems)
        print('Dentro do insere:', *self.treeView.get_children())

    def insere_lst_elem_treeView(self, *lst_itens, **kwargs):
        lst_itens = lst_itens[0] #Desempacotando o argumento
        idd = kwargs.get('idd', None)#Adquirindo a id do elemento
        self.treeView.insert('', 0, iid = idd, text = lst_itens[0], values = lst_itens[1:])


    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan, pady = pady, padx = padx, sticky = sticky)

    def clear_treeView(self):
        self.treeView.delete(*self.treeView.get_children())

    def destroy_frame(self):
        self.treeView.destroy()
        self.frameLocal.destroy()



class sub_Menu:
    def __init__(self, framePai, **kwargs):
        
        self.framePai = framePai
        
        self.menu = tk.Menu(self.framePai, tearoff=0)
        self.menu.add_command(label="Comando 1", command = None)
        self.menu.add_command(label="Comando 2", command = None)
        
        self.bind(self.framePai)
        
    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    
    def bind(self, pointer):
        pointer.bind("<Button-3>", self.popup)






class frame_1T_2abas(LabelFrame):
    
    def __init__ (self, framePai, controller):
        super().__init__(framePai)
        
        #Blobo (1): Configurando frame que conterá as abas, o frameAbas:
        self.config(relief = GROOVE, padx = 15, pady =15)
        
        
        #Bloco (2): O título do frame que contém abas é declarado abaixo, e recebe a variável titulo dado no __init__:
        self.tit1 = Label(self, text = "Título", font = 'Verdana' ,pady = 5, padx = 3, anchor = CENTER)
        self.tit1.grid(row=0, column = 0, sticky = E+W)
        

        #Bloco (3): Aqui, é instanciado o tipo Notebook, que na verdade é um frame que conterá as abas:
        self.abasBarra = ttk.Notebook(self)
        self.abasBarra.grid(row = 1, column = 0, sticky = E+W)
        

        #Bloco (4): Abaixo, cada aba é instanciada, cujo frame pai é o "Abas":
        self.aba1 = ttk.Frame(self.abasBarra)   
        self.abasBarra.add(self.aba1, text = "Aba 1")
        
        self.aba2 = ttk.Frame(self.abasBarra)  
        self.abasBarra.add(self.aba2, text = "Aba 2")
        


    def config_tit1(self, titulo):
        self.tit1.config(text = titulo)

    def config_nome_aba1(self, titulo):
        self.abasBarra.tab(self.aba1, text = titulo)

    def config_nome_aba2(self, titulo):
        self.abasBarra.tab(self.aba2, text = titulo)

