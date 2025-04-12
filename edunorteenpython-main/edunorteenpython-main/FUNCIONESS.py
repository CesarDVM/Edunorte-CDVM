#Reglas generales de las funciones:
#1- no se ejecuta la funcion a menos que la llames
#2- no la pueedo llamar las veces que quiera 
#3- primero hay que definir la funcion, y despues llamarla 

#FUNCIONES SIN PARAMETROS

#def miFuncion():
    #conjunto de instrucciones

def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la igualdad ante la ley")
    print("Derecho a la libertad")

derechos_humanos()

def derechos_mayorDeEdad():
    print("Derecho a votar")
    print("Derecho al trabajo")

def mayoria_de_edad(nombre,edad):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()
     
     
def sss(num1,num2):
    return num1+num2


def mayoria_de_edad2(edad,nombre='DESCONOCIDO'):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()

MM = int(input("digite su edad"))
SS = input("ESCRIBA SU NFFFFOMBRE")
mayoria_de_edad2(MM)
#selecciona el importe 

if __name__ == "__main__":
    mayoria_de_edad()
    mayoria_de_edad2()
    sss()
