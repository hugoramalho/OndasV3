# IMPORTS RELACIONADOS À CLASSE comArduino:


class AppController(Tk):
    def __init__(self):
        super().__init__()
        self.arduinoCom = comArduino()
        self.main_window = main_frame(self, self)
        self.frameCenter = self.main_window.frame_central        
        self.vigia = vigiaArduinoOn(self.arduinoCom, self)
        self.lst_exp = models_app.my_list().loadAllExp()
        self.show_frame('frame_onda_membr')
    
    def show_frame(self, nomeFrame, **kwargs):
        #self.main_window.destroi_framesFilhos_cent()
        
        if nomeFrame == 'frame_onda_corda':
            self.main_window.destroi_framesFilhos_cent()
            self.frame_controle_corda = controle_corda_view(self.frameCenter, self)
            self.frame_controle_corda.grid()
            
        if nomeFrame == 'frame_onda_membr':
            self.main_window.destroi_framesFilhos_cent()
            self.frame_controle_membr = controle_sup_view(self.frameCenter, self)
            self.frame_controle_membr.grid()

        if nomeFrame == 'altera_padrao':
            padrao = kwargs.get('experimento')
            frame = altera_exp_view(self, padrao)

        if nomeFrame == 'padroes_view':
            self.padroes_view = padroes_view(self)

        if nomeFrame == 'painel_config_view':
            self.PainelConfigView = painel_config_view(self)

    def update_model(self, obj_model, **kw_update):
        if type(obj_model) is models_app.PadraoExp:
            obj_model.update(**kw_update)
        elif type(obj_model) is models_app.range_freq:
            obj_model.update(**kw_update)


    def restore_model(self, obj_model, **kw_restore):
        if type(obj_model) is models_app.range_freq:
            obj_model.restore(**kw_restore)

    def atualiza_view(self):
        try:
            self.PainelConfigView.update_view()
        except:
            pass
        try:
            self.frame_controle_corda.update_view()
        except:
            pass
        try:
            self.frame_controle_membr.update_view()
        except:
            pass

    def setArduinoStatus(self, status):
        status = self.arduinoCom.conStatus
        self.main_window.menu.ardStatusLabel(status)

    def enviaFreq(self, freq):
        self.arduinoCom.enviaFreq(freq)
    
    def verfCon(self):
        return(self.arduinoCom.conStatus)

    def verfArduinoPopUp(self):
        status = self.arduinoCom.conStatus
        if status == True:
            self.messagebox_info('Arduino', 'Arduino conectado!')
        else:
            self.messagebox_info('Arduino', 'Arduino não conectado!')


    def arduinoOn(self):
        self.main_window.menu.verfArduino()

    def arduinoOff(self):
        self.main_window.menu.verfArduino()

    def messagebox_info(self, tit, msg):
        messagebox.showinfo(tit, msg)

    def destroyer(self):
        print('Terminando thread arduinoCom . . .')
        self.arduinoCom.terminate()
        print('Terminando thread vigia . . .')
        self.vigia.terminate()


