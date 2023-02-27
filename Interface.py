import Fan, Mines, UI, Boolean_Calculator as Calculator
UI.ChangeColor("Azul")

Equations_Bank: list = [["P","v","Q","^","P","->","Q"]]
Comands = '''Calculadora Proposicional

A - Adicionar equação
R - Resolver equação
T - Gerar tabela verdade
-------------------------
B - Mostrar banco
E - Sair do código

Comando:'''

while True:
    UI.Clear()
    action = input(Comands).upper()

    match action: 
        case "A":
            Calculator.Add(Calculator.Create(), Equations_Bank)
            input("Equação adicionada\n\nEnter para continuar")
        case "R":
            ambient = "Resolver equação"
            UI.SetTitle(ambient)
            Index = UI.GetBankEquation(Equations_Bank, ambient)
            if type(Index) == int:
                equation = Equations_Bank[Index]
                result = Calculator.Execute(Calculator.Read(equation), True, [])
                result = {True: "Verdadeiro", False: "Falso"}[result]
                input(f"Resultado da proposição: {result}\n\nEnter para continuar")
        case "T":
            ambient = "Tabela verdade"
            UI.SetTitle(ambient)
            Index = UI.GetBankEquation(Equations_Bank, ambient)
            if type(Index) == int:
                equation = Equations_Bank[Index]
                UI.SetTitle(ambient)
                Calculator.GenerateTable(equation)
                input("Enter para continuar")
        case "B":
            UI.SetTitle("Banco de proposições")
            if len(Equations_Bank):
                UI.ShowBank(Equations_Bank)
                input("Enter para voltar")
            else:
                input("Banco vazio, pressione enter para continuar...")        
        case "E":
            break
        case "WILLIAM":
            Mines.Play()
        case "GPU":
            Fan.Start()
        case _:
            UI.ChangeColor(action)