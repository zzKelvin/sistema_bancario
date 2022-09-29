menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            add = f"+{valor}"
            extrato.append(add)
            print("Depósito Efetuado Sucesso")
        else:
            print("Valor de deposito incorreto")
    
    elif opcao == "s":
        if LIMITE_SAQUES > 0:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque <= 500:
                if (saldo - saque) >= 0:
                    saldo -= saque
                    adds = f"-{saque}"
                    extrato.append(adds)
                    LIMITE_SAQUES -= 1
                    print("Saque efetuado com sucesso!.")
                else:
                    print("Saldo indisponivel para saque.")
            else:
                print("Limite maximo por saque de 500$.")
        else:
            print("Limite diario de saques atingidos.")

    elif opcao =="e":
        print("Extrato:", list(extrato))
        print(f"Seu saldo atual é: {saldo}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
