opcao = 0
saldo = 100.00
valor = 0.00
valor_depositado = 0.00
valor_sacado = 0.00
qtd_saque = 0

LIMITE_SAQUE = 500.00
QTD_SAQUES = 3

print("\n[SESSÃO INICIADA]")

while True:
    print("\n[1] Depositar", "[2] Sacar", "[3] Extrato", "[4] Sair\n", sep = "    ")
    
    opcao = int(input("Digite o número correspondente a opção desejada: "))

    if opcao == 1:
        print()
        valor += float(input("Digite o valor a ser depositado: R$ "))
        saldo += valor
        valor_depositado += valor
        valor = 0.00
        print("Depósito realizado com sucesso!")
    elif opcao == 2:
        print()
        if qtd_saque < QTD_SAQUES:
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if saldo >= valor:
                if valor <= LIMITE_SAQUE:
                    saldo -= valor
                    valor_sacado += valor
                    valor = 0.00
                    qtd_saque += 1
                    print("Saque realizado com sucesso. Aguarde a impressão das notas.")
                else:
                    print("\nOperação não autorizada!\nO limite máximo é de R$ 500,00 por saque.")
                    continue
            else:
                print("\nOperação não autorizada!\nSaldo em conta insuficiente para realizar a operação de saque no valor desejado.")
                continue
        else:
            print("\nOperação não autorizada!\nO limite máximo de saque diário foi atingido.")
            continue
    elif opcao == 3:
        if valor_depositado == 0.00 and valor_sacado == 0.00:
            print()
            print("Não foram realizadas movimentações.")
            print()
            print(f'Saldo atual ............. R$ {saldo:.2f}')
            continue
        else:
            print()
            print(f'Valor depositado .... R$ {valor_depositado:.2f}')
            print(f'Valor sacado ........ R$ {valor_sacado:.2f}')
            print()
            print(f'Saldo atual ......... R$ {saldo:.2f}')
    elif opcao == 4:
        print("\nEncerrando sessão...")
        break
    else:
        print()
        print("O número digitado não corresponde a nenhuma das opções. Tente novamente.")

print("\n[SESSÃO ENCERRADA]\n")
