
def menu():
    menu = """#################################################
        Sistema Bancário

    - Digite (1) para realizar o depósito
    
    - Digite (2) para realizar o saque.

    - Digite (3) para ver o extrato da conta.

    - Digite (4) para cadastrar usuario.

    - Digite (5) para cadastrar conta.

    - Digite (6) para listar contas.

    - Digite (7) para sair.

#################################################
> """
    return menu

def depositar(saldo, extrato, /):
    print('Digite o valor: ')
    deposito = float(input('> '))

    if deposito > 0:
        saldo += deposito
        print('\n###   Depósito realizado com sucesso!   ###')
        extrato += f'Deposito no valor de R$ {deposito:.2f}\n'
    else:
        print('\n###   Por favor, digite o valor corretamente.   ###')

    return saldo, extrato

def sacar(*, saldo, saques, limite, extrato):
    if saques > 0:
        print('Você tem direito a três saques diários com valores menores a R$ 500')
        print('Digite o valor do saque: ')
        saque = float(input('> '))

        if saque < limite and saque < saldo and saque > 0:
            saldo -= saque
            print('\n###   Saque realizado com sucesso!   ###')
            extrato += f'Saque no valor de R$ {saque:.2f}\n'
            saques -= 1
        elif saque > limite:
            print('Digite um valor menor à 500!')
        elif saque > saldo:
            print('Você não possui essa quantia no seu saldo!')
        elif saque <= 0:
            print('Digite um número válido!')
    else:
        print('\n###    Você já sacou três vezes hoje, tente outro dia!    ')
    
    return saldo, extrato

def vizualizar_extrato(saldo, /, *,extrato):
    print("######EXTRATO######\n")
    if extrato:
        print(extrato,'\n',f'Saldo: R$ {saldo:.2f}.')

    else:
        print("Não foram realizadas movimentações.")
    print('###################')

def cadastrar_usuario(usuarios):
    cpf = input("Informe o cpf (somente numeros): ")
    ususario = filtrar_usuario(cpf, usuarios)

    if ususario:
        print("\n###   Já existe um usuario com esse cpf.    ###")
        return
    
    nome = input("informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco(logradouro, nmr - bairro - cidade-sigla/estado): ")

    usuarios.append({'nome':nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print("\n###   Usuario cadastrado com sucesso!   ###")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n###   Conta criada com sucesso!    ###")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print("\n###    Usuario não encontrado, fluxo de criação de conta encerrado!    ###")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("#" * 100)
        print(linha)


def main():
    AGENCIA = '0001'

    saldo = 0
    saques = 3
    extrato = ''
    limite = 500

    usuarios = []
    contas = []
    
    while True:
        
        resposta = input(menu())

        if resposta == '1': 
            saldo, extrato = depositar(saldo, extrato)

        elif resposta == '2':
            saldo, extrato = sacar(saldo=saldo, limite=limite, saques=saques, extrato=extrato)
            
        elif resposta == '3':
            vizualizar_extrato(saldo, extrato=extrato)
            
        elif resposta == '4':
            cadastrar_usuario(usuarios)

        elif resposta == '5':
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif resposta == '6':
            listar_contas(contas)
            
        elif resposta == '7':
            print('Obrigado por usar o nosso sistema.')
            break

        else: 
            print('Por favor, digite um número válido')

main()