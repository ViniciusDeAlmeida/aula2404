def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    dinheiro = float(valor_hora)
    if horas <= 40:
        salario = horas * dinheiro
    else:
        print('voce nao trabalhou suficiente')
    return salario

salario = calcular_pagamento(40, 43.6)
print(salario)