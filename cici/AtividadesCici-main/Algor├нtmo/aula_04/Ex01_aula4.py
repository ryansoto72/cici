num1 = float(input('Digite a nota da PRIMEIRA prova: '))
num2 = float(input('Digite a nota da SEGUNDA prova: '))
if num1 < 0 or num2 < 0:
    print ('N pode ser numero negativo')
elif num1 > 10 or num2 > 10:
    print('Numero dve ser menor que 10')
else: 
    print(f'A media do aluno sera: {(num1+num2)/2}')
    