import os

def Clear():
    os.system("cls")

def SetTitle(string: str):
    Clear()
    print(string+"\n")

def ShowBank(bank: list):
    for i in range(len(bank)):
        show =  " ".join(map(str, bank[i]))
        print(f"{i+1} --> {show}")
    print()

def GetBankEquation(bank: list, ambient: str):
    if len(bank) == 0:
        input("Banco vazio, pressione enter para continuar...")
        return "Empty"
    selecting = True
    while selecting:
        ShowBank(bank)
        try:
            select = input("Selecione uma equação:")
            if 0 < int(select) <= len(bank):
                selecting = False
            else:
                input("\nEquação não existe")
        except:
            if select.upper() == "E":
                return "Exit"
        if selecting:
            SetTitle(ambient)
    return int(select)-1

def GetValidInput(title: str, string: str, entry: list):
    SetTitle(title)
    while True:
        _input = input(string)
        if _input in entry or _input.upper() in entry:
            return _input
        SetTitle(title)

def ChangeColor(string: str):
    colors = ["AZUL", "VERDE", "AMARELO", "VERMELHO"]
    codes = ["color 1", "color 2", "color 6", "color 4"]
    if string in colors:
        os.system(codes[colors.index(string)])