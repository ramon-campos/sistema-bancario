opcao = 0
saldo = 100.00
valor = 0.00
valor_depositado = 0.00
valor_sacado = 0.00
qtd_saque = 0

LIMITE_SAQUE = 500.00
QTD_SAQUES = 3

print("\n")
print("|" * 54)
print(" SESSÃO INICIADA ".center(50))
print("|" * 54)
print()

while True:
    print("-" * 54)
    print("[1] Depositar", "[2] Sacar", "[3] Extrato", "[4] Sair", sep = "    ")
    print("-" * 54)
    
    opcao = int(input("\nDigite o número correspondente a opção desejada: "))

    if opcao == 1: # DEPOSITAR
        print()
        print(".\n" * 4)
        valor += float(input("Digite o valor a ser depositado: R$ "))
        saldo += valor
        valor_depositado += valor
        valor = 0.00
        print("Depósito realizado com sucesso!")
        print()
        print(".\n" * 4)
    elif opcao == 2: # SACAR
        print()
        print(".\n" * 4)
        if qtd_saque < QTD_SAQUES:
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if saldo >= valor:
                if valor <= LIMITE_SAQUE:
                    saldo -= valor
                    valor_sacado += valor
                    valor = 0.00
                    qtd_saque += 1
                    print("Saque autorizado com sucesso. Aguarde a impressão das notas.")
                    print()
                    print(".\n" * 4)
                else:
                    print("\nOperação não autorizada!\nO limite máximo é de R$ 500,00 por saque.")
                    print()
                    print(".\n" * 4)
                    continue
            else:
                print("\nOperação não autorizada!\nSaldo em conta insuficiente para realizar a operação de saque no valor desejado.")
                print()
                print(".\n" * 4)
                continue
        else:
            print("\nOperação não autorizada!\nO limite máximo de saque diário foi atingido.")
            print()
            print(".\n" * 4)
            continue
    elif opcao == 3: # EXTRATO
        if valor_depositado == 0.00 and valor_sacado == 0.00:
            print()
            print(".\n" * 4)
            print("Obs: Nenhuma operação depósito/saque foi realizada.")
            print()
            print(f'Saldo atual ............. R$ {saldo:.2f}')
            print()
            print(".\n" * 4)
            continue
        else:
            print()
            print(".\n" * 4)
            print(f'Valor depositado .... R$ {valor_depositado:.2f}')
            print(f'Valor sacado ........ R$ {valor_sacado:.2f}')
            print()
            print(f'Saldo atual ......... R$ {saldo:.2f}')
            print()
            print(".\n" * 4)
    elif opcao == 4: # SAIR
        print()
        print(".\n" * 4)
        print("\nEncerrando sessão...")
        print()
        print(".\n" * 4)
        break
    else:
        print()
        print(".\n" * 4)
        print("O número digitado não corresponde a nenhuma das opções. Tente novamente.")
        print()
        print(".\n" * 4)

print("\n")
print("|" * 54)
print(" SESSÃO ENCERRADA ".center(50))
print("|" * 54)
print()
