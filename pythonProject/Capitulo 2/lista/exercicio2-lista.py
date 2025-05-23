numero = int(input("Digite um número de 5 digitos: "))

numero1 = (numero // 10000) % 10
numero2 = (numero //1000) % 10
numero3 = (numero // 100) % 10
numero4 = (numero //10) % 10
numero5 = numero % 10

# // é usado para realizarmos a divisao inteira, ignorando a parte decimal
# % é usado para o resto da divisao

print("   ", numero1)
print("   ", numero2)
print("   ", numero3)
print("   ", numero4)
print("   ", numero5)

