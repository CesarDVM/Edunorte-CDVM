def sumar_numeros(num1, num2):
    return num1 + num2

if __name__ == '__main__':
    while True:
        # Solicitar los números al usuario
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Calcular la suma
        resultado = sumar_numeros(num1, num2)

        # Mostrar el resultado
        print(f'La suma de {num1} y {num2} es: {resultado}')
        
        # Preguntar si desea realizar otra operación
        repetir = input("¿Quieres hacer otra suma? (si/no): ").strip().lower()
        if repetir != 'si':
            print("¡Hasta luego!")
            break  # Sale del bucle si la respuesta no es "sí"