#elaborar una funcion que reciba tres numeros enteros y nos retome el valor promedio de los mismos

def promedio_tres_numeros(num1, num2, num3):
    suma = num1 + num2 + num3
    promedio = suma / 3
    return promedio

# Ejemplo de uso:
numero1 = 158787
numero2 = 692541
numero3 = 665255

resultado = promedio_tres_numeros(numero1, numero2, numero3)
print("El promedio de los tres números es:", resultado)
