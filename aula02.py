# criar uma função de soma
#sera que a nossa turma é jovem? pergunte a idade mental dos colegas qual a quantidade dos colegas e veja se a turma é jovem

#se for igual ou menos de 25 sao jovens 
##se for mais de 60 voce é bem velho

def soma (valor1, valor2):
    return valor1 + valor2

valor1 = int(input('informe o valor: '))
valor2 = int(input('informe o valor: '))

print(f'a soma dos valores e {soma(valor1, valor2)}')