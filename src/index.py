# Librerias
import sys
import subprocess

try:
    from tkinter import *
    from tkinter import ttk
    import tkinter as tk
    import pyfirmata2
    from pyfirmata2 import Arduino

except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyfirmata2'])
    import pyfirmata2
    from pyfirmata2 import Arduino

class Arduino:

    def __init__(self, app):
        
        self.ventana = app
        self.ventana.title("Arduino Control")
        self.ventana.iconbitmap("./ico/icono.ico")
        self.ventana.resizable(False, False)

        contenido = LabelFrame(self.ventana, text="Control - LED")
        contenido.grid(row=0, column=0, padx=5, pady=5)

        self.off = PhotoImage(file='./img/off.png')
        self.on = PhotoImage(file='./img/on.png')

        self.imagen = Label(contenido, image=self.off)
        self.imagen.grid(row=0, column=0, columnspan=2)

        self.mensaje = Label(contenido, text="", fg="red")
        self.mensaje.grid(row=1, column=0, columnspan=2)

        on = ttk.Button(contenido, text="Encender", command=self.encender)
        on.grid(row=2, column=0, padx=5, pady=5)

        off = ttk.Button(contenido, text="Apagar", command=self.apagar)
        off.grid(row=2, column=1, padx=5, pady=5)

        self.validar()

    def validar(self):
       
        try:
            puerto = pyfirmata2.Arduino.AUTODETECT
            self.arduino = pyfirmata2.Arduino(puerto)
            self.mensaje['text'] = ("Estado: Conectado")
            self.mensaje['fg'] = ("green")
        
        except:
            self.mensaje['text'] = ("Estado: Desconectado")
            self.mensaje['fg'] = ("red")
            pass

    def encender(self):
        
        try: # El numero 9 hace regerente al pin 9 del arduino.
            self.arduino.digital[9].write(1)
            self.imagen['image'] = self.on
        
        except:
            self.validar()
            return
        

    def apagar(self):
        
        try: # El numero 9 hace regerente al pin 9 del arduino.
            self.imagen['image'] = self.off
            self.arduino.digital[9].write(0)
        
        except:
            self.validar()
            return

if __name__ == "__main__":
    app = Tk()
    aplicacion = Arduino(app)
    app.mainloop()
