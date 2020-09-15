from tkinter import Tk, Button, Entry, StringVar
from Practica1 import Equipo, Inventario


#TODO agregar un boton para salirse
#TODO button modificar tag
#TODO button modificar nombre


class Inve:
    def __init__(self, parent):
        self.parent =  parent
        self.inven = Inventario()
        self.va = ' '

    def butones(self):
        '''Declaracion de wisgets para la interfaz de programcio'''
        self.va = StringVar()
        self.va.set('Pon el dispositivo')
        Button(self.parent, text = 'Añadir', command = lambda : self.agregar()).place(x = 10, y = 100)
        Button(self.parent, text='Mostrar', command=lambda: self.mostrar()).place(x = 230, y = 100)
        Entry(self.parent, textvariable = self.va).place(x= 80, y = 100)


    def mostrar(self, equipos= None):
        '''Mostrar equipo a la lista de dispositivos'''
        if not equipos:
            equipos = self.inven.dispositivos
        for x in equipos:
            print('{0} {1} {2}'.format(x.id, x.nombre, x.tag))


    def agregar(self):
        '''Agregar el dispositivo medico madiante sintaxis (nombre, tag)'''
        r = self.va.get()
        p = r.split(',')
        self.inven.agregar(p[0], p[1])
        print('Ya estuvo padre!!!!!!!!!!!!!!!!!!!!!!!!!!')

def main():
    root = Tk()
    root.title('Inventario')
    root.geometry('400x400')
    gui = Inve(root)
    gui.butones()
    root.mainloop()

if __name__ == '__main__':
    main()