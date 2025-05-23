#matriz con nombres
matriz = [['Roger', 'Alfredo', 'Roberto'], ['Bowler', 'Jose', 'Steven'], ['Marvin', 'Reynaldo', 'Keneth']]
cantidad_letras = []

print("_" * 37)

for fila in matriz:
    for columna in fila:
        print(f"|{columna:>10}", end=" ")
    print("|")
    print("_" * 37)

for fila in matriz:
    new_row = []
    for columna in fila:
        new_row.append(len(columna))  
    cantidad_letras.append(new_row)

print("-" * 26)


for fila in cantidad_letras:
    for columna in fila:
        print(f"|{columna:>5}", end=" ")
    print("|")
    print("-" * 26)