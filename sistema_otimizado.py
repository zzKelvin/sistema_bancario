import textwrap

def menu():
    menu = """\n
    ========MENU========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [un]\tNovo Usuario
    [lc]\tListar Contas
    [cc]\tCriar Conta Corrente
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar_valor (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito Efetuado Sucesso")
    else:
        print("Valor de deposito incorreto!")
    return saldo, extrato

def sacar_valor (*, saldo, saque, extrato, numero_saques, limite_saques):

    excedeu_saldo = saque > saldo
    excedeu_limite = saque > 500
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Valor solicitado indisponivel em conta!")

    elif excedeu_limite:
        print("O Valor solicitado está acima do suportado (500$)")

    elif excedeu_saques:
        print("Seu numero de saques diarios estão esgotados!")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque:\t\tR$ {saque:.2f}\n"
        numero_saques += 1
        print(f"Saque no valor de: {saque}, efetuado com sucesso!")

    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_user(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print("\nCPF já consta cadastro.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_user(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, cadastre-se primeiro!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))  
            saldo, extrato = depositar_valor(saldo, valor, extrato)

        elif opcao == "s":
            saque = float(input("Digite o valor que deseja sacar: "))
            
            saldo, extrato = sacar_valor(
            saldo=saldo,
            saque = saque,
            extrato=extrato,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
            )

        elif opcao =="e":
            ver_extrato(saldo,extrato=extrato)

        elif opcao == "un":
            criar_user(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
