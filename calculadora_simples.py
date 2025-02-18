import os
import time

while True:
    print('Calculadora Simples')
    escolha = input('Escolha qual operação ')
    while True:
        try:
            Num1 = int(input('Digite um numero: '))
            Num2 = int(input('Digite outro numero: '))
            break
        except ValueError:
            print('Você não digitou um valor numérico')

    soma = Num1 + Num2
    sub = Num1 - Num2
    try:
        div = Num1 / Num2
    except ZeroDivisionError:
        print('É impossível dividir por zero')
        time.sleep(1.5)
        break
    multi = Num1 * Num2

    if escolha == '+':
        print('Resultado: ',soma)
    elif escolha == '-':
        print('Resultado: ',sub)
    elif escolha == '/':
        print('Resultado: ',div)
    elif escolha == '*':
        print('Resultado: ',multi)
    else:
        print('Essa operação não existe')

    continuar = input('Deseja continuar? (s/n): ')
    if continuar.lower() != 's':
        print('Saindo...')
        time.sleep(1.5)
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')