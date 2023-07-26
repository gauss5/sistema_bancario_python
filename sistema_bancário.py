menu = """#################################################
        Sistema Bancário

    - Digite (1) para realizar o depósito
    
    - Digite (2) para realizar o saque.

    - Digite (3) para ver o extrato da conta.

    - Digite (4) para sair.

#################################################
"""
saldo = 0
saques = 3
extrato = ''
limite = 500

while True:
    print(menu)
    resposta = input('> ')

    if resposta == '1': 
        print('Digite o valor: ')
        deposito = float(input('> '))

        if deposito > 0:
            saldo += deposito
            print('Depósito realizado com sucesso!')
            extrato += f'Deposito no valor de R$ {deposito:.2f}\n'
        else:
            print('Por favor, digite o valor corretamente.')
        voltar = input('Aperte (q) para voltar: ')
        if voltar == 'q':
            continue

    elif resposta == '2':
        if saques > 0:
            print('Você tem direito a três saques diários com valores menores a R$ 500')
            print('Digite o valor do saque: ')
            saque = float(input('> '))

            if saque < limite and saque < saldo and saque > 0:
                saldo -= saque
                print('Saque realizado com sucesso!')
                extrato += f'Saque no valor de R$ {saque:.2f}\n'
                saques -= 1
            elif saque > limite:
                print('Digite um valor menor à 500!')
            elif saque > saldo:
                print('Você não possui essa quantia no seu saldo!')
            elif saque <= 0:
                print('Digite um número válido!')
        else:
            print('Você já sacou três vezes hoje, tente outro dia!')
        voltar = input('Aperte (q) para voltar: ')
        if voltar == 'q':
            continue

    elif resposta == '3':
        print("######EXTRATO######\n")
        if extrato:
            print(extrato,'\n',f'Saldo: R$ {saldo:.2f}.')

        else:
            print("Não foram realizadas movimentações.")
        print('###################')
        voltar = input('Aperte (q) para voltar: ')
        if voltar == 'q':
            continue

    elif resposta == '4':
        print('Obrigado por usar o nosso sistema.')
        break

    else: 
        print('Por favor, digite um número válido')