l = float(input('Largura da parede: '))
a = float(input('Altura da sua parede: '))
area = l * a
print('Sua parede tem a dimensão de {} x {} e a sua área é {}m².'.format(l, a, area))
tinta = area / 2
print('Para pintar sua parede, é necessario {} L de tinta.'.format(tinta))