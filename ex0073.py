times = ('Corinthians','Palmeiras','Santos','Grêmeo',
         'Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atlético','Botafogo','Atlético-PR','Bahia',
         'São Paulo','Fluminense','Sport Recife',
         'EC Vitória','Coritiba','Avaí','Ponte Preta',
         'Atlético-GO')
print('-=-'*15)
print(f'Lista de times  do Brasileirão {times}')
print('-=-'*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=-'*15)
print(f'Os ultimos quartos são {times[-4:]}') # ASSIM TAMBÉM FUNCIONA {times[16:]}
print('-=-'*15)
print(f'Os times em ordem alfábetica {sorted(times)}')
print('-=-'*15)
print(f'0 Chapecoense está na {times.index('Chapecoense')+1}ª posição')