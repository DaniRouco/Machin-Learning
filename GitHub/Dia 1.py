# -*- coding: utf-8 -*-
"""Ejercicicos1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rM-amr_eqJXlMkMByOtyU7DGuY9EpsBm
"""

lista = [1,2,3,4,5,6,7]
#print(lista[0])
#print(lista[1])
#print(lista[2])

# MANERA FACIR: FOR
#for numero in lista : #número = variable reiterativa
  #print(numero) #nunca se imprime la variable que se recorre

# MANERA DIFICIL: WHILE
posicion = 0
while posicion < len(lista) :# posicion menor q longitud de lista
  numero = lista[posicion] #variable iteradora numero
  posicion = posicion + 1
  print(numero)

#cuantas vocales hay
texto = 'holaestoesunapurebaenpython'
cont = 0
cont2 = 0

for cuenta in texto:
  if cuenta == "a" or cuenta =="e" or cuenta =="i" or cuenta =="o" or cuenta =="u":
    cont = cont + 1
print(cont)
for cuenta in texto:
  cont2 = len(texto) - cont
print(cont2)

cont

#Input:
#Ella te da detalle

texto = str(input('Introduce la frase: '))
texto = texto.lower()
texto = list(texto.replace(' ',''))

print(texto)

texto_reves = list(reversed(texto))
print(texto_reves)

if texto == texto_reves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

# Escriba aquí su solución

anyo = int(input('Introduce el año: '))
if (anyo % 4 == 0 and not anyo % 100 == 0) or anyo % 400 == 0:
  print('Es un año bisisesto')
else:
  print('No es un año bisiesto')

# Escriba aquí su solución
#Si introducimos:
can_fly = True
is_human = False
has_mask = False
#Debe devolver: "Vision"
if can_fly == True:
  if is_human == True:
    if has_mask == True:
      print('Ironman')
    if has_mask == False:
      print('Capitan Marvel')
  if is_human == False:
    if has_mask == True:
      print('Ronnan Acuser')
    if has_mask == False:
      print('Vision')
if can_fly == False:
  if is_human == True:
    if has_mask == True:
      print('Spiderman')
    if has_mask == False:
      print('Hulk')
  if is_human == False:
    if has_mask == True:
      print('Black Bolk')
    if has_mask == False:
      print('Thanos')