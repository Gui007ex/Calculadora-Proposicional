import Fan, Mines, UI, Boolean_Calculator as Calculator, Options
UI.ChangeColor("AZUL")

Equations_Bank: list = []
Comands = '''Calculadora Proposicional

A - Adicionar equação
R - Resolver equação
T - Tabela verdade
C - Comparação de tabelas
-------------------------
B - Mostrar banco
O - Opções
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
                Calculator.GenerateTable([equation])
                input("\nEnter para continuar")
        case "C":
            ambient = "Comparação de tabelas"
            UI.SetTitle(ambient)
            equations = UI.GetEquationsArray(Equations_Bank, ambient)
            UI.SetTitle(ambient)
            Calculator.GenerateTable(equations)
            input("\nEnter para continuar")
        case "B":
            UI.SetTitle("Banco de proposições")
            if len(Equations_Bank):
                UI.ShowBank(Equations_Bank)
                input("Enter para voltar")
            else:
                input("Banco vazio, pressione enter para continuar...")    
        case "O":
            Options.Configure(Equations_Bank)
        case "E":
            break
        case "WILLIAM":
            Mines.Play()
        case "GPU":
            Fan.Start()
        case _:
            UI.ChangeColor(action)