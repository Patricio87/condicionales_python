# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas

from xml.dom.expatbuilder import ElementInfo


texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:

    print("{} es mayor que {}". format (texto_1, texto_2))

else:

    print(texto_2, "es mayor que" ,texto_1)

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):

    print ("{} tiene mas o por lo menos las mismas letras que {}" .format(texto_1,texto_2))

else:
     
     print("{} tiene mas letras que {}" .format(texto_2,texto_1))



# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:

    print ("Primer letra de", texto_1, "es mayor a primer letra de",  texto_2)
else: 
    print("No es mayor")

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda


if texto_1 == texto_2:
    print(texto_1,"es igual a", texto_2)


# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if texto_1 != texto_2:
    print('{} es distinto a {}'.format (texto_1, texto_2))