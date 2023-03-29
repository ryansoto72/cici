num = int(input('Digite a quantidade de valores: '))

valores = []

for i in range(num):
    i =  i + 1
    valor = float(input(f'informe o {i}º valor: '))
    valores.append(valor)


print(f'A media aritmedica dos valores sera: {sum(valores) / num:.2f}')