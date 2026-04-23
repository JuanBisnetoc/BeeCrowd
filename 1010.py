codigopeca1, quantidadepeca1, valorpeca1 = input().split()
codigopeca2, quantidadepeca2, valorpeca2 = input().split()

quantidadepeca1 = int(quantidadepeca1)
valorpeca1 = float(valorpeca1)

quantidadepeca2 = int(quantidadepeca2)
valorpeca2 = float(valorpeca2)

total= (quantidadepeca1 * valorpeca1) + (quantidadepeca2 * valorpeca2)
print(f'VALOR A PAGAR: R$ {total:.2f}')