class Contacto:
    def __init__(self, nombre, apellido, celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    def mostrar_info(self):
        return f"{self.nombre} {self.apellido} - 📱 {self.celular} - ✉️ {self.email}"

# Lista global para almacenar todas las listas de contactos
todas_las_listas = []
contador_listas = 1  # Número de la lista actual

def crear_lista():
    global contador_listas
    print(f"\n📌 Creando Lista {contador_listas} de Contactos:")
    contactos = []  # Lista temporal para esta sesión

    while True:
        print("\n📝 Agregar un nuevo contacto:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        celular = input("Celular: ")
        email = input("Email: ")

        # Crear y agregar contacto
        contacto = Contacto(nombre, apellido, celular, email)
        contactos.append(contacto)

        # Preguntar si desea agregar otro contacto
        continuar = input("\n🔄 ¿Agregar otro contacto? (s/n): ").strip().lower()
        if continuar != 's':
            break

    # Guardar la lista y actualizar contador
    todas_las_listas.append(contactos)
    print(f"\n✅ Lista {contador_listas} guardada exitosamente.\n")
    contador_listas += 1

def ver_listas():
    if not todas_las_listas:
        print("\n⚠️ No hay listas guardadas todavía.")
        return
    
    print("\n📑 Historial de Listas de Contactos:")
    for i, lista in enumerate(todas_las_listas, start=1):
        print(f"\n📌 Lista {i}:")
        for c in lista:
            print(c.mostrar_info())

def menu_principal():
    while True:
        print("\n📌 **Menú Principal**")
        print("1️⃣ Ver listas guardadas")
        print("2️⃣ Crear una nueva lista de contactos")
        print("3️⃣ Salir")

        opcion = input("\n👉 Selecciona una opción (1/2/3): ").strip()

        if opcion == '1':
            ver_listas()
        elif opcion == '2':
            crear_lista()
        elif opcion == '3':
            print("\n👋 ¡Gracias por usar el gestor de contactos! Hasta pronto.")
            break
        else:
            print("\n⚠️ Opción no válida. Intenta de nuevo.")

# Iniciar el menú principal
menu_principal()