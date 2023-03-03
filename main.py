from tkinter import *
import tkinter
from PIL import Image, ImageDraw, ImageFont, ImageFilter

cor1 = "#A020F0" 
cor2 = "#000000" 
cor3 = "#6EE612" 
cor4 = "#D8BFD8" 
cor5 = "#A4B3BF" 
cor6 = "#0A0CE5" 

#Define Windowns
janela = Tk()
janela.title("Projeto - Cássio Estevão")
janela.geometry("300x180")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

#Define Var Global
global tempo
global radar
global contador
global limitador

limitador = 59
tempo = "00:00:00"
rodar = False
contador = -5

def iniciar():
  
  global tempo
  global contador
  global limitador
  
  if rodar:
    if contador <=-1:
      inicio="Começando em "+str(contador)
      label_tempo["text"] = inicio
      label_tempo["font"] = "Arial 10"
      
    else:
      label_tempo["font"] = "Times 50 bold"
      
      temporario = str(tempo)
      h,m,s = map(int,temporario.split(":"))
      
      h = int(h)
      m = int(m)
      s = int(contador)
      
      if (s>=limitador):
        contador = 0
        m+=1
        
      s = str(0)+str(s)
      m = str(0)+str(m)
      h = str(0)+str(h)
      
      #Release Valor
      temporario = str(h[-2:])+":" + str(m[-2:])+":" + str(s[-2:])
      label_tempo["text"] = temporario
      tempo = temporario
        
    label_tempo.after(1000,iniciar)
    contador +=1

def start():
  global rodar
  rodar = True
  iniciar()
  
def pausar():
  global rodar
  rodar = False
  
def reiniciar():
  global contador
  global tempo
#restart contador
  contador = 0
#reecrono
  tempo = "00:00:00"
  label_tempo["text"] = tempo

  
  
  
  
#windowns
label_app=Label(janela,text="CRONÔMETRO PYTHON",font=("Arial 10"),bg=cor1,fg=cor4)
label_app.place(x=20,y=5)

label_tempo=Label(janela,text=tempo,font=("Times 50 bold"),bg=cor1,fg=cor4)
label_tempo.place(x=20,y=30)

botao_iniciar=Button(janela,command=start,text="Iniciar",font=("Ivy 8 bold"),width=10, height=2, bg=cor4, fg=cor1, relief="raised", overrelief="ridge")
botao_iniciar.place(x=20,y=130)

botao_pausar=Button(janela,command=pausar,text="Pausar",font=("Ivy 8 bold"),width=10, height=2, bg=cor4, fg=cor1, relief="raised", overrelief="ridge")
botao_pausar.place(x=105,y=130)

botao_reiniciar=Button(janela,command=reiniciar,text="Reiniciar",font=("Ivy 8 bold"),width=10, height=2, bg=cor4, fg=cor1, relief="raised", overrelief="ridge")
botao_reiniciar.place(x=190,y=130)

iniciar()

janela.mainloop()