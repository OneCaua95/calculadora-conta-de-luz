consumo = float(input("Informe o valor consumido kw/h:"))

tipo = input("Informe o tipo do setor: R - residencial, C - comercial, I - industrial").upper()

tarifas = {
    'R': {'limite':500, 'baixa':0.40, 'alta':0.65},
    'C': {'limite':1000, 'baixa':0.55, 'alta':0.60},
    'I': {'limite':5000, 'baixa':0.55, 'alta':0.60}
}

if tipo not in tarifas:
    print("Setor invalido.")
    exit()

cliente = {
    'R': {'A sua residência'},
    'C': {'O seu comércio'},
    'I': {'A sua indústria'}
}[tipo]

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