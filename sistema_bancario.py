from termcolor import colored as cld

LIMITE_SAQUE = 3
saldo = 0
lista_de_operacoes = []
menu = {
    1: "Deposito",
    2: "Saque",
    3: "Extrato",
    4: "Sair",
}
while True:
    for i in menu:
        print(cld(f"[{i}] - {menu.get(i)}", "cyan"))
    operacao = int(input("Digite a operação desejada: "))
    if operacao == 1:
        print(cld(f"Operação {menu[1]} selecionada\n", "cyan"))
        deposito = float(input(f"Digite o valor que você quer Depositar: "))
        if deposito <= 0:
            print(cld("Valor invalido", "red"))
            print("Operação finalizada voltando ao menu principal")
            continue
        else:
            print(cld("Deposito autorizado", "green"))
            lista_de_operacoes.append(f"Deposito: +R${deposito:.2f}")
            saldo += deposito
    if operacao == 2:
        print(cld(f"Operação {menu[2]} selecionada\n", "cyan"))
        saque = float(input("Digite o valor que deseja sacar: "))
        if saque <= 0:
            print("Operção Falhou, Valor invalido")
        elif saque > 500:
            print(cld("Saque negado, pois ultrapassa o valor maximo por saque", "red"))
        elif LIMITE_SAQUE == 0 and saque <= saldo:
            print(
                cld(
                    "Você exedeu o limeite de 3 saques diarios tente novamente mais tarde!!!",
                    "red",
                )
            )
            LIMITE_SAQUE = 3
        elif saque <= 500 and saque <= saldo:
            LIMITE_SAQUE -= 1
            print(f"Saque de R${saque} autoriazado")
            lista_de_operacoes.append(f"Saque: -R${saque:.2f}")
            saldo -= saque
        else:
            print("Saldo Insuficiente")
    msg = " EXTRATO DA CONTA ".center(50, "=")
    if operacao == 3:
        print(cld(f"Operação {menu[3]} selecionada\n", "cyan"))
        print(cld(msg, "cyan"))
        if len(lista_de_operacoes) == 0:
            print(cld("Não á transações á serem exibidas", "yellow"))
        for i in lista_de_operacoes:
            if i[:8] == menu[1]:
                print(cld(f"{i}", "green"))
            if i[:5] == menu[2]:
                print(cld(f"{i}", "red"))
        print(cld("Saldo Atual", "cyan"))
        if saldo == 0:
            print(cld(f"R${saldo:.2f}", "red"))
            print(cld("=" * len(msg), "cyan"))
        else:
            print(cld(f"R${saldo:.2f}", "green"))
            print(cld("=" * len(msg), "cyan"))
    if operacao == 4:
        print("Fim da operação")
        break
