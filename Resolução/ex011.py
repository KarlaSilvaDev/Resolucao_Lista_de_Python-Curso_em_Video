largura = float(input('Insira a largura da parede em metros: '))
altura = float(input('Insira a altura da parede em metros:'))
area = largura * altura
tinta = area/2
print('Sua parede de {}x{}m tem área igual a {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
