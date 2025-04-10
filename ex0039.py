from datetime import date
ano = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - ano
sexo = str(input('Sexo[M/F]:'))
if sexo in 'Ff':
    print('O alistamento militar para mulheres começara a ser efetivo em 2026.')
else:
    if sexo in 'Mm':
        print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
    if idade > 18:
        print(f'Seu alistamento foi em {ano+18}, já se passaram {idade-18} anos.')
    if idade < 18:
        print(f'Seu alistamento será em {ano+18}, ainda faltam {18-idade} anos. ')
    if idade == 18:
        print(f'Seu alistamento é agora em {ano+idade}, procure uma junta de serviço militar.')