salario = float(input('Digite o salário do funcionário: R$ '))
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
novosalario = salario + aumento
print('O aumento será de R$ {:.2f} e o novo salário é R$ {:.2f}'.format(aumento, novosalario))
