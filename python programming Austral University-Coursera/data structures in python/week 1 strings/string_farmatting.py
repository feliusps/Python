import string

#how to generate the next string  'El saldo de la cuenta 32673 es $100.25'

#variable declaration
nro_cuenta = '32673'
saldo = 100.2543
#output value
print('El saldo de la cuenta {} es ${:.2f}'.format(nro_cuenta, saldo))
# or using {:s} for string
print('El saldo de la cuenta {:s} es ${:.2f}'.format(nro_cuenta, saldo))
