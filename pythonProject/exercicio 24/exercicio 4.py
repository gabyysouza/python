maior = None
menor = None

for i in range(10):
    num = int(input(f"Digite o {i + 1} número positivo: "))

    if num <= 0:
        print("Por favor, digite apenas números inteiros positivos.")
        continue

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")