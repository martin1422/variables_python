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

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
Ma

Cualquier duda con estos métodos pueden consultarla por el campus
'''
newstring ='' 
count1 = 0
pos_espacio = 0

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio
print('Ingrese su nombre completo: ')
string = str(input())
print(string.lower())
print(string.upper())

#calculo numero de letras y espacios
for a in string: 
    count1 += 1                   #Numero de caracteres
    if(a.isspace()) == True:      #Detecto espacio y tomo posicion
        pos_espacio = count1      #posicion espacio

#print('Numeros de caracteres: ' + str(count1))        
#print('Posicion espacio: ' + str(pos_espacio))

#Armo nombre
print(string[0:1].upper() + string[1:(pos_espacio)].lower() + string[pos_espacio:(pos_espacio+1)].upper() + string[(pos_espacio + 1):].lower())
