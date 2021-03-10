from math import sin, cos, tan, radians
a = float(input('Ângulo em graus: '))
print(f'Ângulo {a}')
seno = sin(radians(a))
cosse = cos(radians(a))
tang = tan(radians(a))
print(f'Seno {seno:.2f} - Cosseno {cosse:.2f} - Tangente {tang:.2f}')