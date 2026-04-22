nome= input()
salariofixo= float(input())
totalvendas= float(input())
comissao= totalvendas *0.15
TOTAL= salariofixo+comissao
print(f'TOTAL = R$ {TOTAL:.2f}')