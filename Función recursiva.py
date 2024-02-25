def convertir_a_binario(numero):
    if numero > 1:
        convertir_a_binario(numero // 2)
    print(numero % 2, end='')


def contar_digitos(numero):
    if numero == 0:
        return 0
    return 1 + contar_digitos(numero // 10)


def calcular_raiz_cuadrada(numero, candidato):
    if candidato * candidato <= numero < (candidato + 1) * (candidato + 1):
        return candidato
    else:
        return calcular_raiz_cuadrada(numero, candidato + 1)


def raiz_cuadrada_entera(numero):
    if numero < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo."
    else:
        return calcular_raiz_cuadrada(numero, 0)


def convertir_a_decimal(romano):
    romano_numeros = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return romano_numeros[romano[0]]

    if romano_numeros[romano[0]] < romano_numeros[romano[1]]:
        return romano_numeros[romano[1]] - romano_numeros[romano[0]] + convertir_a_decimal(romano[2:])
    else:
        return romano_numeros[romano[0]] + convertir_a_decimal(romano[1:])


def suma_numeros_enteros(n):
    if n <= 1:
        return n
    return n + suma_numeros_enteros(n - 1)

def menu_interactivo():
    while True:
        print("\nMenú:")
        print("1. Convertir a binario")
        print("2. Contar dígitos")
        print("3. Raíz cuadrada entera")
        print("4. Convertir a decimal desde Romano")
        print("5. Suma de números enteros")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            numero = int(input("Ingrese un número entero para convertir a binario: "))
            print("El número", numero, "en binario es:", end=' ')
            convertir_a_binario(numero)
        elif opcion == '2':
            numero = int(input("Ingrese un número entero para contar sus dígitos: "))
            print("El número", numero, "tiene", contar_digitos(numero), "dígitos.")
        elif opcion == '3':
            numero = int(input("Ingrese un número entero para calcular su raíz cuadrada entera: "))
            print("La raíz cuadrada entera de", numero, "es:", raiz_cuadrada_entera(numero))
        elif opcion == '4':
            romano = input("Ingrese un número romano para convertir a decimal: ")
            print("El número romano", romano, "en decimal es:", convertir_a_decimal(romano))
        elif opcion == '5':
            numero = int(input("Ingrese un número entero para calcular la suma de números enteros hasta ese número: "))
            print("La suma de números enteros hasta", numero, "es:", suma_numeros_enteros(numero))
        elif opcion == '6':
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu_interactivo()
