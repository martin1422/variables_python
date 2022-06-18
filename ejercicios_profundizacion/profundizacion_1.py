# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!\n Eliga una opcion:')
# Empezar aquí la resolución del ejercicio
opcion = ''
while(opcion != 'F'):
  print("A) Suma\nB) Resta\nC) Multiplicacion\D) Division\nE) Exponente/Potencia\nF) Salir")
  opcion = str(input())
  if(opcion == 'A'):
    print('Ingrese numero 1: ')
    numero_1 = int(input())
    print('\nIngrese numero 2: ')
    numero_2 = int(input())
    suma = numero_1 + numero_2
    print('La suma entre ' + str(numero_1) + ' y ' + str(numero_2) + ' es = ' + str(suma))

  if(opcion == 'B'):
    print('Ingrese numero 1: ')
    numero_1 = int(input())
    print('\nIngrese numero 2: ')
    numero_2 = int(input())
    resta = numero_1 -  numero_2
    print('La resta entre ' + str(numero_1) + ' y ' + str(numero_2) + ' es = ' + str(resta))

  if(opcion == 'C'):
    print('Ingrese numero 1: ')
    numero_1 = int(input())
    print('\nIngrese numero 2: ')
    numero_2 = int(input())
    mul = numero_1 * numero_2
    print('La multiplicacion entre ' + str(numero_1) + ' y ' + str(numero_2) + ' es = ' + str(mul))

  if(opcion == 'D'):
    print('Ingrese numero 1: ')
    numero_1 = int(input())
    print('\nIngrese numero 2: ')
    numero_2 = int(input())
    div = numero_1 / numero_2
    print('La Divicion entre ' + str(numero_1) + ' y ' + str(numero_2) + ' es = ' + str(div)) 

  if(opcion == 'E'):
    print('Ingrese la base: ')
    numero_1 = int(input())
    print('\nIngrese el exponente: ')
    numero_2 = int(input())
    exp = numero_1 ** numero_2
    print('La potenciacion entre ' + str(numero_1) + ' y ' + str(numero_2) + ' es = ' + str(exp))

