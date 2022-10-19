def teste_01():
    tupla = (
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: '))
    )
    cont_9 = 0
    pos_3 = 0
    qtd_par = 0
    for c in range (0, 4):
        if tupla[c] == 9 :
            cont_9 += 1
        if tupla[c] == 3:
            pos_3 = tupla.index(3) + 1
        else:
            pos_3 = str('(Inexistente!)')
        if tupla[c] % 2 == 0:
            qtd_par += 1
    return f'O número nove apareceu {cont_9} vezes.'

teste_01()