from tkinter import *
import base64

ventana = Tk()
ventana.geometry('500x300')
ventana.resizable(0,0)
ventana.configure(background = 'light salmon')
ventana.title('Base64')

Label(ventana, text ='Codificando y Decodificando con python', font = 'Garamond 20 bold').pack()
Texto = StringVar()
opcion = StringVar()
Resultado = StringVar()

def Reset():
    Texto.set("")
    opcion.set("")
    Resultado.set("")

def Opcion():
    if(opcion.get() == 'c'):
        Resultado.set(Cod(Texto.get()))
    elif(opcion.get() == 'd'):
        Resultado.set(Dec(Texto.get()))
    else:
        Resultado.set('Opcion invalida')

def Cod(message):
    a = message.encode("UTF-8")
    cod = base64.b64encode(a)
    return cod

def Dec(message):
    dec = base64.b64decode(message)
    return dec
        
def Exit():
    ventana.destroy()

Label(ventana, font= 'Garamond 16 bold', text='Texto').place(x= 60,y=60)
Entry(ventana, font = 'Garamond 15', textvariable = Texto, bg = 'white').place(x=310, y = 60)
Label(ventana, font = 'Garamond 14 bold', text ='Opcion(c-codifi/d-decodi)').place(x=60, y = 120)
Entry(ventana, font = 'Garamond 15', textvariable = opcion , bg= 'white').place(x=310, y = 120)
Entry(ventana, font = 'Garamond 15 bold', textvariable = Resultado, bg ='white').place(x=310, y = 150)
Button(ventana, font = 'Garamond 15 bold', text = 'Resultado'  ,padx =2,bg ='light pink' ,command = Opcion).place(x=60, y = 150)
Button(ventana, font = 'Garamond 15 bold' ,text ='Nuevo' ,width =6, command = Reset,bg = 'coral', padx=2).place(x=80, y = 190)
Button(ventana, font = 'Garamond 15 bold',text= 'Salir' , width = 6, command = Exit,bg = 'orange', padx=2, pady=2).place(x=180, y = 190)

ventana.mainloop()










