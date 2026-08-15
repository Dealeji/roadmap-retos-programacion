# estos son mi operadores y estructuras de control
print("Operadores Aritméticos:")
print(f"Suma: 2 + 2 = {2 + 2}")
print(f"Resta: 2 - 2 = {2 - 2}")
print(f"Multiplicación: 2 * 2 = {2 * 2}")
print(f"División: 2 / 2 = {2 / 2}")
print(f"División entera: 2 // 2 = {2 // 2}")
print(f"Módulo: 2 % 2 = {2 % 2}")
print(f"Potencia: 2 ** 2 = {2 ** 2}")

#ahora mis operadores de comparación
print("Operadores de Comparación:")
print(f"Igualdad: 2 == 2 es {2 == 2}")
print(f"Desigualdad: 2 != 2 es {2 != 2}")
print(f"Mayor que: 2 > 2 es {2 > 2}")
print(f"Menor que: 2 < 2 es {2 < 2}")
print(f"Mayor o igual que: 2 >= 2 es {2 >= 2}")
print(f"Menor o igual que: 2 <= 2 es {2 <= 2}")

#ahora mis operadores de asignación
print("Operadores de Asignación:")
a = 2
print(f"Asignación: a = 2, a = {a}")
a += 2
print(f"Suma y asignación: a += 2, a = {a}")
a -= 2
print(f"Resta y asignación: a -= 2, a = {a}")
a *= 2
print(f"Multiplicación y asignación: a *= 2, a = {a}")
a /= 2
print(f"División y asignación: a /= 2, a = {a}")
a //= 2
print(f"División entera y asignación: a //= 2, a = {a}")
a %= 2
print(f"Módulo y asignación: a %= 2, a = {a}")
a **= 2
print(f"Potencia y asignación: a **= 2, a = {a}")

#ahora mis operadores de identidad
print("Operadores de Identidad:")
b = 2
print(f"b is a: {b is a}")
print(f"b is not a: {b is not a}")

#ahora mis operadores de pertenencia
print("Operadores de Pertenencia:")
print(f"'a' in 'Python' = {'a' in 'Python'}")
print(f"'b' not in 'Python' = {'b' not in 'Python'}")

#ahora mis operadores de bit
print("Operadores de Bit:")
c = 5
d = 3
print(f"AND: {c} & {d} = {c & d}")
print(f"OR: {c} | {d} = {c | d}")
print(f"XOR: {c} ^ {d} = {c ^ d}")
print(f"NOT: ~{c} = {~c}")
print(f"Desplazamiento a la izquierda: {c} << 1 = {c << 1}")
print(f"Desplazamiento a la derecha: {c} >> 1 = {c >> 1}")

#ahora mis estructuras de control
print("Estructuras de control:")
my_variable = 10
if my_variable > 5:
    print(f"{my_variable} es mayor que 5")
elif my_variable == 5:
    print(f"{my_variable} es igual a 5")
else:
    print(f"{my_variable} es menor que 5")

#ahora mis bucles
print("Bucles:")
for i in range(5):
    print(f"Iteración {i}")

a = 0
while a < 5:
    print(f"Iteración {a}")
    a += 1

#ahora mis excepciones
print("Excepciones:")
try:
    result = 2 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Fin del bloque try-except")

# esto es la solucion de ejercicio de iteracion de numeros pares del 10 al 50, excluyendo el 16 y los multiplos de 3
print("Iteración de números pares del 10 al 50:")
for i in range(10, 55):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)