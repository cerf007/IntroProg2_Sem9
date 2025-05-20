#Arrwglod de enteros
#Arreglo de mayor a menor
array_int = [5, 4, 9, 2, 1]
array_int.sort()
print("Arrsy de enteros", array_int)

#ordenar de menor a mayor
array_int.sort(reverse=True)
print(f"Array de enteros de mayor a menor: {array_int}")

#buscar elemento 
elemento = 4
if elemento in array_int:
    print(f"El elemento {elemento}, se encunetra en el array")
else:
    print(f"El elemento {elemento}, no se encuentra en el arreglo")
    