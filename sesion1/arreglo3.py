array_str = ["uno", "dos", "tres", "cuatro", 'cinco']
print("Array de cadena", array_str)

#insertar un elemento  al inicio:
array_str.insert(3, "cero")
print("Array de cadenas despues de inserter cero al inicio:", array_str)

#Contar cuantos elementos hay en el arreglo
cantidad = len(array_str)
print("Cantidad de elementos en el arreglo: ", cantidad)

#Eliminar un elemento en el arreglo
array_str.remove("tres")
print("Array de cadenas despues de eliminar 'tres':", array_str)

#otra forma de eliminar
array_str.pop(2)
print("Array de cadenas despues de eliminar el elemento en posicion 2:", array_str)

