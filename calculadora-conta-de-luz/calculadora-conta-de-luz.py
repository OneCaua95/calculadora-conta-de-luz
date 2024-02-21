consumo = float(input("Informe o valor consumido kw/h:"))

tipo = input("Informe o tipo do setor: R - residencial, C - comercial, I - industrial").upper()

tarifas = {
    'R': {'limite':500, 'baixa':0.40, 'alta':0.65, 'client':'A sua residência'},
    'C': {'limite':1000, 'baixa':0.55, 'alta':0.60, 'client': 'O seu comércio'},
    'I': {'limite':5000, 'baixa':0.55, 'alta':0.60, 'client': 'A sua indústria'}
}

if tipo not in tarifas:
    print("Setor invalido.")
    exit()

cliente = tarifas[tipo]['client']

if consumo <= tarifas[tipo]['limite']:
    tarifa =  tarifas[tipo]['baixa']
else:
    tarifa = tarifas[tipo]['alta']

valor = consumo * tarifa

print(f'''
{cliente} teve um consumo de {consumo} kWh de energia neste mês.
A tarifa para essa faixa de consumo é de R$ {tarifa:.2f}.
Dessa forma, a sua conta foi de R$ {valor:.2f}
''')
