import serial.tools.list_ports
import sys
import struct
import threading
import serial
import time

'''
print("=== Auto scan for Arduino Uno connected port===")
print("")
print(platform.system(), platform.release())
print(platform.dist())
print("Python version " + platform.python_version())
print("")
'''

class vigiaArduinoOn(threading.Thread):
    def __init__(self, arduinoCom, controller):
        threading.Thread.__init__(self)
        self.arduinoCom = arduinoCom
        self.controller = controller
        self.name = 'vigiaArduinoOn'
        self.threadViva = True
        self.start()

    def run(self):
        while self.threadViva is True:
            try:
                ajuste = False
                if self.arduinoCom.conStatus is True:

                    while self.arduinoCom.conStatus is True:
                        # print('To verificando. . . ')

                        if ajuste is True:
                            time.sleep(0.2)

                        else:
                            print('Arduino on!')
                            self.controller.setArduinoStatus(self.arduinoCom.conStatus)
                            ajuste = True
                else:
                    while self.arduinoCom.conStatus is False:
                        # print('To verificando. . . ')

                        if ajuste is False:
                            print('Arduino off!')
                            self.controller.setArduinoStatus(self.arduinoCom.conStatus)
                            ajuste = True
                        else:
                            time.sleep(0.2)
            except:
                self.threadViva = False
                pass

        print('Thread: ', self.name, ' terminou!')
        sys.exit(0)

    def terminate(self):
        self.threadViva = False


class procuraArduino (threading.Thread):
    def __init__(self, arduinoCom):
        threading.Thread.__init__(self)
        self.arduinoCom = arduinoCom
        self.name = 'procuraArduino'
        self.threadViva = True
        self.start()

    def run (self):
        achou = False
        while self.threadViva is True and self.arduinoCom.threadViva is True:
            print('Procurando arduino...')
            while achou is False:
                #portList é uma lista de listas, 
                portList = list(serial.tools.list_ports.comports())
                
                #Abaixo, port é uma lista aux 
                for port in portList:
                    if "VID:PID=2341:0043" in port[0] or "VID:PID=2341:0043" in port[1] or "VID:PID=2341:0043" in port[2]:
                        print('port: ',port)
                        print('port type: ', type(port))
                        print('port[0]: ', port[0])
                        print('port[1]: ', port[1])
                        print('port[2]: ', port[2])
                        #please note: it is not sure [0]
                        #returned port[] is no particular order
                        #so, may be [1], [2]
                        print("\nArduino Encontrado! ")
                        achou = True
                        break
            
            portTuple = (port[0], port[1], port[2])
            self.arduinoCom.connectArduino(portTuple)
            
            print('Thread: ', self.name, ' terminou!')
            self.threadViva = False
            sys.exit()
            
        
    def terminate(self):
        print('Thread: ', self.name, ' terminou!')
        self.threadViva = False
                    



class vigiaConexao (threading.Thread):
    def __init__(self, arduinoCom):
        threading.Thread.__init__(self)
        self.arduinoCom = arduinoCom
        self.name = 'vigiaConexao'
        self.threadViva = True
        self.start()

    def run (self):
        con = True
        while self.threadViva is True and self.arduinoCom.threadViva is True:
            while con is True:
                try:
                    test = self.arduinoCom.inWaiting()
                except:
                    print('Arduino desconectado!')
                    self.arduinoCom.conStatus = False
                    self.arduinoCom.clearCon()
                    self.arduinoCom.findArduinoUnoPort()
                    self.threadViva = False
                    con = False
        
        print('Thread: ', self.name, ' terminou!')
        self.threadViva = False
        sys.exit()
    
    def terminate(self):
        self.threadViva = False



class comArduino:
    def __init__(self):
        self.threadViva = True
        self.ser = serial.Serial()
        self.conStatus = False
        self.findArduinoUnoPort()        

    def clearCon(self):
        print(self.ser.isOpen())
        self.conStatus = False
        self.close()
        print(self.ser.isOpen())

    def close(self):
        self.ser.close()

    def list_ports(self):
        ports = serial.tools.list_ports.comports()
        return(ports)
 
    def inWaiting(self):
        return self.ser.inWaiting()

    def connectArduino(self, portTuple):
        if self.conStatus is False and self.threadViva is True:
            time.sleep(2)
            try:
                self.ser = serial.Serial(portTuple[0], baudrate = 9600)
                self.conStatus = True
                print('Arduino conectado!')
                self.watchCon()
            except:
                try:
                    self.ser = serial.Serial(portTuple[1], baudrate = 9600)
                    self.conStatus = True
                    print('Arduino conectado!')
                    self.watchCon()
                except:
                    try:
                        self.ser = serial.Serial(portTuple[2], baudrate = 9600)
                        self.conStatus = True
                        print('Arduino conectado!')
                        self.watchCon()
                    except:
                        print('Não foi possível estabelecer uma conexão com a porta: ', portTuple,'\n Provalmente a porta está ocupada, ou o Arduino está desconectado.')
        else:
            print('Arduino já conectado!')

    def findArduinoUnoPort(self):
        self.procura = procuraArduino(self)

    def watchCon(self):
        self.vigia = vigiaConexao(self)

    def enviaFreq(self, freq):
        try:
            #Frequencia recebida em string é convertida em float:
            freq = float(freq)
            #Frequencia(float) é enpacotada (IEEE)
            freq_ser = struct.pack('f', freq )
            #Frequência é printada:
            print('Frequencia a ser enviada para o Arduino:', freq_ser)
            self.ser.write(freq_ser)
            print('frequencia enviada!')
        
        except Exception as Expt:
            print('Erro ocorreu: ', Expt,type(Expt), '\nTentando enviar dado novamente. . . ')
            time.sleep(1.2)
            try:
                print('tentando novamente:')
                self.ser.write(freq_ser)
                print('frequencia enviada!')
            #LEMBRAR DO permissionError
            except:
                print('Erro ocorreu novamente!\nVerifique a conexão com o arduino.')
                pass

    def terminate(self):
        self.threadViva = False
        try:
            self.vigia.terminate()
            self.procura.terminate()
            self.close()
        except Exception as Expt:
            print(Expt)
            self.procura.terminate()
            self.close()
            pass