s = float(input('Digite o salário do funcionário: R$ '))
if s <= 1250:
    aum = s * 0.15
else:
    aum = s * 0.10
sal = s + aum
print('O aumento será de R$ {:.2f} e o novo salário é R$ {:.2f}'.format(aum, sal))
