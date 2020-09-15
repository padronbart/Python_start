last_id = 0

class Equipo:
    def __init__(self, nombre, tag):
        '''Contructor de inventario'''
        self.nombre = nombre
        self.tag = tag
        global last_id
        last_id +=1
        self.id = last_id

    def match(self, filtro):
        '''Determianr la existencia de algun disp medico'''
        return filtro in self.nombre or filtro in self.tag

class Inventario:
    def __init__(self):
        self.dispositivos = []


    def agregar(self, nombre, tag):
        '''Agregar equipos medicos'''
        self.dispositivos.append(Equipo(nombre, tag))

    def modificar_nombre(self, id, nombre):
        '''Modificar el nombre de equipo medico'''
        for equipo in self.dispositivos:
            if equipo.id == id:
                equipo.nombre = nombre
                break

    def modificar_tag(self, id, tag):
        '''Modificar el eituqeta de equipo medico'''
        for equipo in self.dispositivos:
            if equipo.id == id:
                equipo.tag = tag
                break

    def buscar(self, filtro):
        '''Para buscar el equipo encomendado'''
        return [equipo for equipo in self.dispositivos if equipo.match(filtro)]

