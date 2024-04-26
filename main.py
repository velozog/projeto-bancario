import pyautogui as pg
import time
from termcolor import colored
import os


def print_menu(menu: dict):
    for i in menu:
        print(colored(f"[{i}] - {menu.get(i)}", "cyan"))


def tray(mod: str, ban: int, op: int):
    return f"{mod} {ban} / OP {op}"


def detectar_imagem():
    procurando = True
    while procurando:
        try:
            pg.locateCenterOnScreen("imagem (1).png")
            procurando = False
            print("Executanto resto do codigo")
        except:
            print("Procurando")


def config_impressora():

    pg.hotkey("ctrl", "p")  # Acessa a tela de impressão
    pg.press("tab")
    pg.press("tab")
    pg.press("2")  # Define a velocidade de impressão
    pg.press("tab")
    pg.press("1")  # Define o primeiro digito de obscuridade de impressão
    pg.press("8")  # Define o segundo digito de obscuridade de impressão
    pg.press("enter")
    pg.hotkey("alt", "f4")
    pg.press("x")


def modificar_txt(itens):
    caminho_arquivo = r"C:\CSV\Etiquetas.csv - colar aqui.csv (1).csv"

    with open(caminho_arquivo, "w") as arquivo:
        for item in itens:
            arquivo.write(f"{item}\n")
    print(colored(f"Lista de itens foi salva em: {caminho_arquivo}", "green"))


def main():
    i = True
    while i:
        try:
            menu = {1: "AMO", 2: "RES", 3: "DVI", 4: "RET"}
            itens = []
            print_menu(menu)
            mod = int(input("Digite um das opções Acima: "))
            if mod > len(menu) or mod <= 0:
                print(colored("Opção inexistente\n", "red"))
                continue
            mod = menu[mod]
        except ValueError:
            print(colored("Erro de digitação\n", "red"))
            continue

        while True:
            try:
                num_tray = int(
                    input(
                        "Digite o Numero da Bandeja, Para mudar o modelo digite 666 ou 555 para imprimir: "
                    )
                )
                if num_tray == 666:
                    print_menu(menu)
                    mod = int(input("Digite um das opções Acima: "))
                    mod = menu[mod]
                    continue
                elif num_tray == 555:
                    i = False
                    break
                num_op = int(input("Digite o Numero da OP: "))
                linha = tray(mod, num_tray, num_op)
                itens.append(linha)
                print(itens)
            except ValueError:
                print(colored("Erro de digitação", "red"))
                continue
    modificar_txt(itens)

    caminho_arquivo = r"C:\Etiquetas\Bandeja QR code\RETs e RES e AMO csv.nlbl"

    os.startfile(caminho_arquivo)

    detectar_imagem()
    config_impressora()

    pg.alert("Concluído com sucesso!!")


if __name__ == "__main__":
    main()
