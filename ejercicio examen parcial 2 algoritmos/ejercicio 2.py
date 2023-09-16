#confeccionar una funcion que calcule la superficie de un rectangulo y la retorne,
#la funcion recibe como parametros los valores de dos de sus lados;
#en el bloque principal del programa cargar los lados de dos rectangulos y luego mostar cual de los dos tiene mayor superficie
# Definir la función para calcular la superficie de un rectángulo
def calcular_superficie_rectangulo(base, altura):
    return base * altura

# Entrada de datos para el primer rectángulo
base1 = float(input("Ingrese la base del primer rectángulo: "))
altura1 = float(input("Ingrese la altura del primer rectángulo: "))

# Entrada de datos para el segundo rectángulo
base2 = float(input("Ingrese la base del segundo rectángulo: "))
altura2 = float(input("Ingrese la altura del segundo rectángulo: "))

# Calcular las superficies de los rectángulos
superficie1 = calcular_superficie_rectangulo(base1, altura1)
superficie2 = calcular_superficie_rectangulo(base2, altura2)

# Determinar cuál de los dos rectángulos tiene mayor superficie
if superficie1 > superficie2:
    print("El primer rectángulo tiene una superficie mayor.")
elif superficie2 > superficie1:
    print("El segundo rectángulo tiene una superficie mayor.")
else:
    print("Ambos rectángulos tienen la misma superficie.")
