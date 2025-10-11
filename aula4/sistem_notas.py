lista_alunos = []

nome1 = input('nome 1: ')
nome2 = input('nome 2: ')
nome3 = input('nome 3: ')

lista_alunos.append(nome1)
lista_alunos.append(nome1)
lista_alunos.append(nome1)

notas_alunos1 = [float(input(f'nota1: {nome1}: ')),float(input(f'nota2: {nome1}: '))]
notas_alunos2 = [float(input(f'nota1: {nome2}: ')),float(input(f'nota2: {nome2}: '))]
notas_alunos3 = [float(input(f'nota1: {nome3}: ')),float(input(f'nota2: {nome3}: '))]

media_aluno1 = sum(notas_alunos1)/len(notas_alunos1)
media_aluno2 = sum(notas_alunos2)/len(notas_alunos2)
media_aluno3 = sum(notas_alunos3)/len(notas_alunos3)

print('media alunos')
print(f'''
medias:
aluno{nome1} - {media_aluno1} 
aluno{nome2} - {media_aluno2}
aluno{nome3} - {media_aluno3}
''')

aprovado_1 = media_aluno1 >= 7
aprovado_2 = media_aluno2 >= 7
aprovado_3 = media_aluno3 >= 7

print(f'''

{nome1} - Aprovado - {media_aluno1}
{nome2} - Aprovado - {media_aluno2}
{nome3} - Aprovado - {media_aluno3}

''')