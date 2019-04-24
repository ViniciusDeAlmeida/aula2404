#detetive

print('detetive')
print('responda as perguntas abaixo com s(sim) ou n(não): ')

perguntas = ('voce telefonou parra a vitima?',
             'voce esteve no local do crime?',
             'voce era vizinha da vitima?',
             'voce tinha crush na vitima?',
             'voce devia dinheiro para vitima?')

respostas = []

for pergunta in perguntas:
    respostas.append(input(pergunta).upper())

quantidade = 0 
for resposta in respostas:
    if resposta == 'S':
        quantidade += 1

if quantidade < 2:
    print('inocente')
elif quantidade == 2:
    print('acho que voce matou')
elif quantidade <= 4:
    print('voce deve ter participado do assassinato')
else:
    print('voce e o mordomo entao voce matou')