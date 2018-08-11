# -*- coding: cp1252 -*-
from time import *
from Tkinter import *
import tkFont
import sqlite3
import datetime as dt
##import RPi.GPIO as GPIO
##import sqlite3

##GPIO.setmode(GPIO.BOARD)
##GPIO.setup(12,GPIO.OUT) ## Saida 1
##GPIO.setup(16,GPIO.OUT) ## Saida 2
##GPIO.setup(15,GPIO.OUT) ## Saida 3
##GPIO.setup(13,GPIO.OUT) ## Saida 4
##
##GPIO.setwarnings(False)

win = Tk()

months = dict(Jan=1, Feb=2, Mar=3, Apr=4, May=5, Jun=6, Jul=6, Aug=8, Sep=9, Oct=10, Nov=11, Dec=12)

myFont = tkFont.Font(family = 'courier', size = 20, weight = 'bold')

##con = sqlite3.connect('TomadaPrism.db')

TomadaX = 0
PotenciaX = 0
Tx = [0,0,0,0]
Px = [00, 0, 0, 0]
tempo1 = 0
tempo2 = 0
tempo3 = 0
tempo4 = 0
hra = ""
Matrix = [[0 for x in range(7)] for y in range(24)]
currentevent = [0,0,0,0]

BD = sqlite3.connect('Rpi.db')
curso = BD.cursor()

##curso.execute('ALTER TABLE agendado ADD COLUMN fulN string')

#curso.execute('CREATE TABLE agendado ( idAg INTEGER PRIMARY KEY AUTOINCREMENT, hAg int, dAg string)') 

##curso.execute("DROP TABLE agendado")

#print curso.fetchall()
##curso.execute("INSERT INTO agendado (hAg , dAg) VALUES (09 , 'Do')")

#t = '9'
#curso.execute('SELECT * FROM A')
##curso.execute("DELETE FROM agendado ")

#BD.text_factory = str
#curso.execute("SELECT last_insert_rowid()")

#isso = curso.fetchall()
##assert type(isso[0]) is str

##curso.execute("ALTER TABLE evento ADD COLUMN sigmaPot")
##print isso
#urso.execute('ALTER TABLE agendado MODIFY hAg FLOAT')
##print curso.fetchall()

BD.commit()

akilo = ' '
for isso in curso.execute('SELECT fulN FROM agendado'):
        akilo = akilo+str(isso[0])
        akilo = akilo+" ] [ "

diaSem = Label(win, text=("Horarios agendados: [ "+akilo))
diaSem.place(x=10, y=300)

def T1d():
        print("1 button pressed")
        curso.execute('SELECT estado FROM A WHERE tomadaA = 1')
        isso = curso.fetchone()
        curso.execute('SELECT potInst FROM A ')
        akilo = curso.fetchall()
        if ( isso[0][0] == "I"):

                T1.config( bg = "red")
                T1["text"] = "T1 Off"
                curso.execute("UPDATE A SET estado = 'O',operando=0 WHERE tomadaA = 1")
                curso.execute('SELECT curSt FROM A WHERE tomadaA = 1')
                isso = curso.fetchone()
                curso.execute('''UPDATE evento SET df = ? , tf = ? WHERE idEv = ?''',(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),int(isso[0])))
                curso.execute('''SELECT pot FROM evento WHERE idEv = ?''',isso)                      
                akilo = curso.fetchone()   
                curso.execute('''SELECT d0, t0 FROM evento WHERE idEv = ?''',isso)
                isso2 = curso.fetchone()
                issod = str(isso2[0])
                issoh = str(isso2[1])               
                a = dt.datetime(int(issod[8:]),int(months[issod[4:-6]]),int(issod[1:-10]),int(issoh[0:-6]),int(issoh[3:-3]),int(issoh[6:]))
                b = dt.datetime(int(strftime('%Y')),int(strftime('%m')),int(strftime('%d')),int(strftime('%H')),int(strftime('%M')),int(strftime('%S')),)
                
                curso.execute('''UPDATE evento SET sigmaPot = ? WHERE idEv = ?''',( ((b-a).total_seconds())*(int(akilo[0])),int(isso[0])))
                #GPIO.output(12,1)
                
        else:
                T1.config( bg = "green") 
                T1["text"] = "T1 On (" + str(akilo[0][0])+" W )"
                curso.execute("UPDATE A SET estado = 'I',operando=1 WHERE tomadaA = 1")
                curso.execute("INSERT INTO evento (d0, t0, tomada , pot) VALUES (?,?,?,?)",(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),'1',akilo[0][0]))
                curso.execute("SELECT last_insert_rowid()")
                isso = curso.fetchall()
                curso.execute('''UPDATE pointer SET point = ? ''', isso[0])
                curso.execute('''UPDATE A SET curSt = ? WHERE tomadaA = 1''', isso[0])
                #GPIO.output(12,0)
                

        BD.commit()

def T2d():
        print("2 button pressed")
        curso.execute('SELECT estado FROM A WHERE tomadaA = 2')
        isso = curso.fetchone()

        curso.execute('SELECT potInst FROM A ')
        akilo = curso.fetchall()
        if ( isso[0][0] == "I"):
                T2.config( bg = "red")
                T2["text"] = "T2 Off"
                curso.execute("UPDATE A SET estado = 'O',operando=0 WHERE tomadaA = 2")
                curso.execute('SELECT curSt FROM A WHERE tomadaA = 2')
                isso = curso.fetchone()
                curso.execute('''UPDATE evento SET df = ? , tf = ? WHERE idEv = ?''',(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),int(isso[0])))
                curso.execute('''SELECT pot FROM evento WHERE idEv = ?''',isso)                      
                akilo = curso.fetchone()   
                curso.execute('''SELECT d0, t0 FROM evento WHERE idEv = ?''',isso)
                isso2 = curso.fetchone()
                issod = str(isso2[0])
                issoh = str(isso2[1])               
                a = dt.datetime(int(issod[8:]),int(months[issod[4:-6]]),int(issod[1:-10]),int(issoh[0:-6]),int(issoh[3:-3]),int(issoh[6:]))
                b = dt.datetime(int(strftime('%Y')),int(strftime('%m')),int(strftime('%d')),int(strftime('%H')),int(strftime('%M')),int(strftime('%S')),)
                curso.execute('''UPDATE evento SET sigmaPot = ? WHERE idEv = ?''',( ((b-a).total_seconds())*(int(akilo[0])),int(isso[0])))              
                #GPIO.output(16,1)

        else:
                T2.config( bg = "green")
                T2["text"] = "T2 On (" + str(akilo[1][0])+" W )"
                curso.execute("UPDATE A SET estado = 'I',operando=1 WHERE tomadaA = 2")
                curso.execute("INSERT INTO evento (d0, t0, tomada , pot) VALUES (?,?,?,?)",(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),'2',akilo[1][0]))
                curso.execute("SELECT last_insert_rowid()")
                isso = curso.fetchall()
                curso.execute('''UPDATE pointer SET point = ? ''', isso[0])
                curso.execute('''UPDATE A SET curSt = ? WHERE tomadaA = 2''', isso[0])
                #GPIO.output(16,0)

        BD.commit()
               
def T3d():
        print("3 button pressed")
        curso.execute('SELECT estado FROM A WHERE tomadaA = 3')
        isso = curso.fetchone()
        curso.execute('SELECT potInst FROM A ')
        akilo = curso.fetchall()
        if ( isso[0][0] == "I"):
                T3.config( bg = "red")
                T3["text"] = "T3 Off"
                curso.execute("UPDATE A SET estado = 'O',operando=0 WHERE tomadaA = 3")
                curso.execute('SELECT curSt FROM A WHERE tomadaA = 3')
                isso = curso.fetchone()
                curso.execute('''UPDATE evento SET df = ? , tf = ? WHERE idEv = ?''',(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),int(isso[0])))
                curso.execute('''SELECT pot FROM evento WHERE idEv = ?''',isso)                      
                akilo = curso.fetchone()   
                curso.execute('''SELECT d0, t0 FROM evento WHERE idEv = ?''',isso)
                isso2 = curso.fetchone()
                issod = str(isso2[0])
                issoh = str(isso2[1])               
                a = dt.datetime(int(issod[8:]),int(months[issod[4:-6]]),int(issod[1:-10]),int(issoh[0:-6]),int(issoh[3:-3]),int(issoh[6:]))
                b = dt.datetime(int(strftime('%Y')),int(strftime('%m')),int(strftime('%d')),int(strftime('%H')),int(strftime('%M')),int(strftime('%S')),)
                curso.execute('''UPDATE evento SET sigmaPot = ? WHERE idEv = ?''',( ((b-a).total_seconds())*(int(akilo[0])),int(isso[0])))
                #GPIO.output(15,1)
                
        else:
                T3.config( bg = "green")
                T3["text"] = "T3 On (" + str(akilo[2][0])+" W )"
                curso.execute("UPDATE A SET estado = 'I',operando=1 WHERE tomadaA = 3")
                curso.execute("INSERT INTO evento (d0, t0, tomada , pot) VALUES (?,?,?,?)",(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),'3',akilo[2][0]))
                curso.execute("SELECT last_insert_rowid()")
                isso = curso.fetchall()
                curso.execute('''UPDATE pointer SET point = ? ''', isso[0])
                curso.execute('''UPDATE A SET curSt = ? WHERE tomadaA = 3''', isso[0])
               # GPIO.output(15,0)

        BD.commit()

def T4d():
        print("4 button pressed")
        curso.execute('SELECT estado FROM A WHERE tomadaA = 4')
        isso = curso.fetchone()
        curso.execute('SELECT potInst FROM A ')
        akilo = curso.fetchall()
        if ( isso[0][0] == "I"):
                T4.config( bg = "red")
                T4["text"] = "T4 Off"
                curso.execute("UPDATE A SET estado = 'O',operando=0 WHERE tomadaA = 4")
                curso.execute('SELECT curSt FROM A WHERE tomadaA = 4')
                isso = curso.fetchone()
                curso.execute('''UPDATE evento SET df = ? , tf = ? WHERE idEv = ?''',(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),int(isso[0])))
                curso.execute('''SELECT pot FROM evento WHERE idEv = ?''',isso)                      
                akilo = curso.fetchone()   
                curso.execute('''SELECT d0, t0 FROM evento WHERE idEv = ?''',isso)
                isso2 = curso.fetchone()
                issod = str(isso2[0])
                issoh = str(isso2[1])               
                a = dt.datetime(int(issod[8:]),int(months[issod[4:-6]]),int(issod[1:-10]),int(issoh[0:-6]),int(issoh[3:-3]),int(issoh[6:]))
                b = dt.datetime(int(strftime('%Y')),int(strftime('%m')),int(strftime('%d')),int(strftime('%H')),int(strftime('%M')),int(strftime('%S')),)
                curso.execute('''UPDATE evento SET sigmaPot = ? WHERE idEv = ?''',(((b-a).total_seconds())*(int(akilo[0])),int(isso[0])))
                #GPIO.output(13,1)
        else:
                T4.config( bg = "green")
                T4["text"] = "T4 On (" + str(akilo[3][0])+" W )"
                curso.execute("UPDATE A SET estado = 'I',operando=1 WHERE tomadaA = 4")
                curso.execute("INSERT INTO evento (d0, t0, tomada , pot) VALUES (?,?,?,?)",(strftime(' %d/%b/%Y '),strftime('%H:%M:%S'),'4',akilo[3][0]))
                curso.execute("SELECT last_insert_rowid()")
                isso = curso.fetchall()
                curso.execute('''UPDATE pointer SET point = ? ''', isso[0])
                curso.execute('''UPDATE A SET curSt = ? WHERE tomadaA = 4''', isso[0])
                #GPIO.output(13,0)

        BD.commit()
               
def exitProgram():
	print("Exit Button pressed")
	win.quit()	


class Texto:
        def __init__(self, master=None):
          self.fontePadrao = ("Arial", "10")
          self.primeiroContainer = Frame(master)
          self.primeiroContainer["pady"] = 10
          self.primeiroContainer.pack()
   
          self.segundoContainer = Frame(master)
          self.segundoContainer["padx"] = 20
          self.segundoContainer.pack()
   
          self.terceiroContainer = Frame(master)
          self.terceiroContainer["padx"] = 20
          self.terceiroContainer.pack()
   
          self.quartoContainer = Frame(master)
          self.quartoContainer["pady"] = 20
          self.quartoContainer.pack()

          self.quintoContainer = Frame(master)
          self.quintoContainer["pady"] = 20
          self.quintoContainer.pack()

          self.sextoContainer = Frame(master)
          self.sextoContainer["pady"] = 20
          self.sextoContainer.pack()

          
          self.titulo = Label(self.primeiroContainer, text="Infome a tomada e respectiva potencia")
          self.titulo["font"] = ("Arial", "10", "bold")
          self.titulo.pack()
   
          self.nomeLabel = Label(self.segundoContainer,text="Tomada:", font=self.fontePadrao)
          self.nomeLabel.pack(side=LEFT)
   
          self.nome = Entry(self.segundoContainer)
          self.nome["width"] = 3
          self.nome["font"] = self.fontePadrao
          self.nome.pack(side=LEFT)
   
          self.senhaLabel = Label(self.terceiroContainer, text="Potencia:", font=self.fontePadrao)
          self.senhaLabel.pack(side=LEFT)
   
          self.senha = Entry(self.terceiroContainer)
          self.senha["width"] = 30
          self.senha["font"] = self.fontePadrao
          self.senha.pack(side=LEFT)

          self.hrLabel = Label(self.quintoContainer,text="Horarios (sT1Mo13On) (rT4Sa00Of):", font=self.fontePadrao)
          self.hrLabel.pack(side=LEFT)

          self.hrr = Entry(self.quintoContainer)
          self.hrr["width"] = 50
          self.hrr["font"] = self.fontePadrao
          self.hrr.pack()

          self.autenticar = Button(self.sextoContainer)
          self.autenticar["text"] = "Salva"
          self.autenticar["font"] = ("Calibri", "9")
          self.autenticar["width"] = 12
          self.autenticar["command"] = self.setPT
          self.autenticar.pack(side=BOTTOM)

          self.setar = Button(self.sextoContainer)
          self.setar["text"] = "Agendar"
          self.setar["font"] = ("Calibri", "9")
          self.setar["width"] = 12
          self.setar["command"] = self.agnd
          self.setar.pack(side=BOTTOM)
   
          self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
          self.mensagem.pack(side=TOP)

        def agnd(self):

                taski = self.hrr.get()                
                
                if(taski[0] == 's'):
                        print("setando")
                        isso  = int(taski[5]+taski[6])
                        akilo = str(taski[3]+taski[4])
                        aisso = int(taski[2])
                        if (taski[8]=='n'):
                                akilola = 'on'
                        elif(taski[8]=='f'):
                                akilola = 'off'
                        else:
                                print("problema leitura on/off")
                                self.mensagem["text"] = "Valor invalido para DATA"
                        
                        curso.execute("INSERT INTO agendado (hAg, dAg, tomAg, fo, fulN) VALUES (?,?,?,?,?)",((isso),(akilo),(aisso),(akilola),(taski)))
                        self.mensagem["text"] = "SALVO"                     
                        

                elif(taski[0] == 'r'):
                        print("resetando")
                        
                        isso  = int(taski[5]+taski[6])
                        akilo = str(taski[3]+taski[4])
                        aisso = int(taski[2])
                        curso.execute('''DELETE FROM agendado WHERE hAg = ? AND dAg = ? AND tomAg = ?''', ((isso),(akilo),(aisso)))
                        self.mensagem["text"] = "APAGADO"
                        
                        
                else:
                        print ("nao ta lendo s ou r")
                        self.mensagem["text"] = "Valor invalido para DATA"
                        
                akiloO = ' '                
                for isso in curso.execute('SELECT fulN FROM agendado'):
                        akiloO = akiloO+str(isso[0])
                        akiloO = akiloO+" ] [ "                
        
                diaSem.config(text=("Horarios agendados: [ "+akiloO))                            
                                        
                BD.commit()

                
        def setPT(self):
            
          global TomadaX
          global PotenciaX
          global Tx
          global Px
          global hra

          TomadaX = int(self.nome.get())
          PotenciaX = float(self.senha.get())
          hra = self.hrr.get()

          if ((TomadaX > 4) or (TomadaX < 1)):
                  self.mensagem["text"] = "Tomada invalida "
          elif (PotenciaX <= 0 or PotenciaX > 10000):
                  self.mensagem["text"] = "Valor invalido para Potencia"
          else:        
                        
                  TomadaX2 = (TomadaX - 1)                  
                  Px[TomadaX2] = str(PotenciaX)                  
                  curso.execute('''UPDATE A SET potInst = ? WHERE tomadaA = ?''', (Px[TomadaX2],TomadaX))
                  curso.execute('SELECT potInst FROM A ')
                  akilo = curso.fetchall()
                  
                  print (TomadaX)
                  print (Px)
                  
                  if ( T1["bg"] == "green"):
                          T1["text"] = "T1 On (" + str(akilo[0][0])+" W)"
                  if ( T2["bg"] == "green"):
                          T2["text"] = "T2 On (" + str(akilo[1][0]) +" W)"
                  if ( T3["bg"] == "green"):
                          T3["text"] = "T3 On (" + str(akilo[2][0]) +" W)"
                  if ( T4["bg"] == "green"):
                          T4["text"] = "T4 On (" + str(akilo[3][0]) +" W)"
                          
                  self.mensagem["text"] = "Salvo"
                  BD.commit()       
          
              
   
Texto(win)

time1 = ''
clock = Label(win, font=('courier', 15, 'bold'))
clock.place(x=10, y=10)

def tick():
    global time1
  
    time2 = strftime('%H:%M:%S - %d %b %Y (%a)')
 
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
   
    clock.after(200, tick)
    akiloO = ''

    for isso in curso.execute('SELECT fulN FROM agendado'):
        akiloO = akiloO+str(isso[0])
        akiloO = akiloO+" ] [ "
        diaSem.config(text=("Horarios agendados: [ "+akiloO))    

    if(strftime('%d,%H,%M,%S')=='17,00,00,00'): # Todo Dia 17 fecha os eventos (ligando e desligando)
        
        T1d()
        T2d()
        T3d()
        T4d()

        T1d()
        T2d()
        T3d()
        T4d()

    if(strftime('%S')=='00' and strftime('%M')=='00'):
       
        isso = strftime('%w')
        akilo = 0
        
        if(isso == '0'):#
            akilo = 'Su'#
        elif(isso=='1'):#
            akilo = 'Mo'#        
        elif(isso=='2'):#
            akilo = 'Tu'#
        elif(isso=='3'):#   Substituir tudo isso por:
            akilo = 'We'#       semanas = dict(0=Su, 1=Mo...)
        elif(isso=='4'):#
            akilo = 'Th'#
        elif(isso=='5'):#
            akilo = 'Fr'#
        elif(isso=='6'):#
            akilo = 'Sa'#
        else:
            print("eRRO NA DATA ")
            
        isso = strftime('%H')
        
        curso.execute("SELECT tomAg, idAg, fo FROM agendado WHERE ?=?",('hAg',int(isso)))
        akilo = curso.fetchall()
        numL = len(akilo)        
        
        if(akilo!=[]):
            for i in range(0, numL):
                if(akilo[i][2]=='On'):
                    if ( akilo[i][0]=='1' and T1["bg"] != "green"):
                        T1d()                        
                    elif ( akilo[i][0]=='2' and T2["bg"] != "green"):
                        T2d()                        
                    elif ( akilo[i][0]=='3' and T3["bg"] != "green"):
                        T3d()                        
                    elif ( akilo[i][0]=='4' and T4["bg"] != "green"):
                        T4d()
                    else:
                        print ("Sem tomada ligada por agendamento")
                        
                    
                elif(akilo[i][2]=='Off'):
                    if ( akilo[i][0]=='1' and T1["bg"] == "green"):
                        T1d()                        
                    elif ( akilo[i][0]=='2' and T2["bg"] == "green"):
                        T2d()                        
                    elif ( akilo[i][0]=='3' and T3["bg"] == "green"):
                        T3d()                        
                    elif ( akilo[i][0]=='4' and T4["bg"] == "green"):
                        T4d()
                    else:
                        print ("Sem tomada ligada por agendamento")     
    
tick()


##HrSem = Label(win, text="  00\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23")    ##################################################
##HrSem.place(x=50, y=185)

win.title("Tomadas PRISM")
win.geometry('1080x720')

curso.execute('SELECT potInst FROM A ')
akilo = curso.fetchall()

T1  = Button(win, text = "T1 On (" + str(akilo[0][0])+" W )", font = myFont, command = T1d, height =1 , width = 5) 
T1.config( bg = "green")

T2  = Button(win, text = "T2 On (" + str(akilo[1][0])+" W )", font = myFont, command = T2d, height =1 , width = 5) 
T2.config( bg = "green")

T3  = Button(win, text = "T3 On (" + str(akilo[2][0])+" W )", font = myFont, command = T3d, height =1 , width = 5) 
T3.config( bg = "green")

T4  = Button(win, text = "T4 On (" + str(akilo[3][0])+" W )", font = myFont, command = T4d, height =1 , width = 5) 
T4.config( bg = "green")

T4.pack(fill=X,side=BOTTOM)
T3.pack(fill=X,side=BOTTOM)
T2.pack(fill=X,side=BOTTOM)
T1.pack(fill=X,side=BOTTOM)


exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6,bg = "blue") 
exitButton.place(x=1000, y=25)

curso.execute('SELECT estado FROM A ')
isso = curso.fetchall()

curso.execute('SELECT potInst FROM A ')
akilo = curso.fetchall()

## PARA printar os valors do BD nos bots

if(isso[0][0] == 'O'):
        T1.config( bg = "red")
        T1["text"] = "T1 Off"
        #GPIO.output(12,1)
else:
        T1.config( bg = "green")
        T1["text"] = "T1 On (" + str(akilo[0][0])+" W )"
        #GPIO.output(12,0)
        
if(isso[1][0] == 'O'):
        
        T2.config( bg = "red")
        T2["text"] = "T2 Off"
        #GPIO.output(16,1)
else:
        
        T2.config( bg = "green")
        T2["text"] = "T2 On (" + str(akilo[1][0])+" W )"
        #GPIO.output(16,0)
        
if(isso[2][0] == 'O'):
        T3.config( bg = "red")
        T3["text"] = "T3 Off"
        #GPIO.output(15,1)
else:
        
        T3.config( bg = "green")
        T3["text"] = "T3 On (" + str(akilo[2][0])+" W )"
        #GPIO.output(15,0)
        
if(isso[3][0] == 'O'):
        T4.config( bg = "red")
        T4["text"] = "T4 Off"
        #GPIO.output(13,1)
else:
        
        T4.config( bg = "green")
        T4["text"] = "T4 On (" + str(akilo[3][0])+" W )"
        #GPIO.output(13,0)
        
##curso.execute("PRAGMA table_info(agendado)")
##curso.execute('SELECT * FROM agendado')
##akilo = curso.fetchall()
##print (akilo)
##
##curso.execute("PRAGMA table_info(agendado)")
##print (curso.fetchall())


mainloop()




        
