print('='*30)
print(f'{'10º PRIMEIROS TERMOS DE UMA PA:^30'}')
print('='*30)
primeirotermo = int(input('Primeiro termo:'))
razãodapa = int(input('Razão da pa:'))
deisprimeiros = primeirotermo + (10 - 1) * razãodapa
for c in range(primeirotermo,deisprimeiros + razãodapa,razãodapa):
    print(c,end='->')
print('Acabou')