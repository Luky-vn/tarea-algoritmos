print("Ingresa las notas, una vez ingresadas todas escribe -1 para saber el promedio.")
nota = int(input())
a = 1
suma = nota
while nota != -1:
    nota = int(input())
    if nota != -1:
        suma += nota
        a+=1
promedio = suma/a
print(f"la suma es {suma}")
print(f"a es {a}")
print(f"El promedio de las notas es: {promedio}")
