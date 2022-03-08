"""funcion que imprime cuenta regresiva a partir de un numero"""
# def crearListaRegresiva(numero=1):
#     list = []
#     for i in range(numero, -1, -1):
#         list.append(i)
#     return list
# list_numbers = crearListaRegresiva(4)
# print(list_numbers)
"""Funcion de imprimir primer valor y devolver segundo valor"""
# def imprimir_devolver(list):
#     for i in range(len(list)):
#         if(i==0):
#             print(list[i])
#         else:
#             return list[i]
# numbers = [7, 14]
# print("Devuelvo el segundo valor: ",imprimir_devolver(numbers))
"""Funcion que devuelve la suma del primer valor de la lista mas la longitud de la misma"""
# def sumar_primero_longitud(lista):
#     sum=0
#     sum = lista[0]+len(lista)
#     return sum
# array = [2, 4, 6, 8, 10, 12]
# resultado = sumar_primero_longitud(array)
# print(resultado)
"""Funcion que devuelve valores mayores que el segundo item de la lista de entrada e imprime el valor"""
# def devuelve_lista_nueva(lista2):
#     new_list=[]
#     # print('La longitud de lista es', len(lista2))
#     if(len(lista2)>2):
#         for index in range(len(lista2)):
#             print('El index es', index)
#             if(lista2[index]<=lista2[1]):
#                 print('Dentro de continue',lista2[index], lista2[1])
#                 continue
#             else:
#                 print('Dentro del else',lista2[index])
#                 new_list.append(lista2[index])
#         return new_list
#     else:
#         return False
# listaNum=[1, 2, 3, 4, 5, 2, 7, 1]
# print(devuelve_lista_nueva(listaNum))
"""Funcion que devuelve lista con longitud acorde a la longitud dada, y valores acorde al valor dado"""
def retorna_longitud_valor(longitud, valor):
    nueva_lista=[]
    for index in range(longitud):
        # print(index)
        nueva_lista.append(valor)
    return nueva_lista
long=7
val=14
print(retorna_longitud_valor(long, val))