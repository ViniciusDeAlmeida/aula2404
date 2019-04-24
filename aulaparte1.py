print('ola mundo')

nota1 = float(input('me informe sua primeira nota: '))
nota2 = float(input('me informe sua segunda nota: '))
nota3 = float(input('me informe sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3.0 

print('a sua media foi {}' .format(media))

if media == 10:
    print('aprovado ta de parabens')
elif media >= 6:
    print('passou raspando')
else:
    print('pode choraR PEGOU DP')