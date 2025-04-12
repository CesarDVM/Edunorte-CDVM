# Clase de contacto
class Contacto:

    def __init__(self,
        nombre, apellido,
        celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    def mostrar_contacto(self):
        print(f'''Contacto:
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Celular: {self.celular}
            Email: {self.email}
        ''')

# Codigo Principal
print('*** Clases y Objetos en Python')
# Crear un primer objeto
contacto1 = Contacto()
contacto1.inicializar_contacto('Layla', 'Acosta',
                               '55667788', 'layla@mail.com')
contacto1.mostrar_contacto()
# Crear un segundo objeto
contacto2 = Contacto()
contacto2.inicializar_contacto('Carlos', 'Gomez',
                               '55789898', 'cgomez@mail.com')
contacto2.mostrar_contacto()
print(f'Dir. Memoria: {id(contacto2)}')
print(f'Dir. Memoria Hex: {hex(id(contacto2))}')



class Persona:
    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: nombre = {self.nombre}, apellido = {self.apellido}')

# Codigo Principal
persona1 = Persona('Esteban', 'Quiroz')
persona1.mostrar_persona()


