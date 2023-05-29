# Aula_23
try:
    a = int(input('A: '))
    b = int(input('B: '))
    r = a / b

except (ValueError, TypeError):
    print(f'O problema ocorreu devido aos tipos de dados que você digitou')

except ZeroDivisionError:
    print('Não é possível dividir por zero')

except KeyboardInterrupt:
    print('O usuário prefiiriu não informar os dados')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado foi {r:.2f}')

finally:
    print('Programa concluido')
