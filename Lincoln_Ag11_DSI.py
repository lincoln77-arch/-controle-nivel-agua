# -*- coding: utf-8 -*-

from colorama import Fore, Style, init

init(autoreset=True)

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def cor_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

def barra(nivel):
    return "[" + "#" * nivel + " " * (5 - nivel) + "]"

def alerta(nivel):
    if nivel == 1:
        return ">>> ALERTA CRÍTICO: nível muito baixo!"
    elif nivel == 5:
        return ">>> ATENÇÃO: reservatório muito cheio!"
    else:
        return ""

print("\n=== Controle de Nível de Água ===\n")

for i in range(5):
    nivel = i + 1
    cor = cor_nivel(nivel)

    print(cor + f"Nível {nivel}: {niveis[i]}")
    print(cor + f"Indicador: {barra(nivel)}")

    msg_alerta = alerta(nivel)
    if msg_alerta:
        print(cor + msg_alerta)

    print()

print(Style.RESET_ALL)

