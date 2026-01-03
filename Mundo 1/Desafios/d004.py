#Ler algo pelo teclado e mostrar o tipo primitivo e todas as informações possíveis sobre ele.
t = input('Digite algo: ')
print(type(t))
print('É númerico?',(t.isnumeric()))
print('É alfabético?',(t.isalpha()))
print('É alfanumérico?',(t.isalnum()))
print('É em maiúsculo?',(t.isupper()))

