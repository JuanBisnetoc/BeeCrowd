A, B, C = map(float, input().split())
pi= float(3.14159)

areatriangulo=float(A*C/2)
areacirculo= float(pi*C**2)
areatrapezio= float(((A+B)*C/2))
areaquadrado= float(B**2)
arearetangulo= float(A*B)

print(f'TRIANGULO: {areatriangulo:.3f}')
print(f'CIRCULO: {areacirculo:.3f}')
print(f'TRAPEZIO: {areatrapezio:.3f}')
print(f'QUADRADO: {areaquadrado:.3f}')
print(f'RETANGULO: {arearetangulo:.3f}')