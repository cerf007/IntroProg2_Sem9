#MATRIZ
matriz = [[10,2], [300,4]]
print("_"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end= " ")
    print("|")
    print("_"*17)