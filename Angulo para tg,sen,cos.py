from math import radians, tan, sin, cos
a = float(input('Digite o ângulo: '))
t = tan(radians(a))
s = sin(radians(a))
c = cos(radians(a))
print('O angulo de {} tem a tangente de {:.2f}'.format(a, t))
print('O angulo de {} tem o seno de {:.2f}'.format(a, s))
print('O angulo de {} tem o cosseno de {:.2f}'.format(a, c))

