aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip()
aluno['media'] = float(input('Media do aluno: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO!!'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÂO!!'
else:
    aluno['situação'] = 'REPROVADO!!'
print(f'O nome do aluno é {aluno["nome"]}.')
print(f'A media de {aluno["nome"]} é {aluno["media"]}.')
print(f'A situação de {aluno["nome"]} é:\n >> {aluno["situação"]} <<')