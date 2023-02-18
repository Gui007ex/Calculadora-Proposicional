import Utility, Boolean_Calculator as Calculator
Utility.ChangeColor("Azul")

Equations_Bank: list = [["~","P","v","Q","^","P"]]
Comands = '''Calculadora Proposicional

A - Adicionar equação
R - Resolver equação
-------------------------
B - Mostrar banco
E - Sair do código

Comando:'''

while True:
    Utility.Clear()
    action = input(Comands).upper()

    match action: 
        case "A":
            Calculator.Add(Calculator.Create(), Equations_Bank)
            input("Equação adicionada\n\nEnter para continuar")
        case "R":
            ambient = "Resolver equação"
            Utility.SetTitle(ambient)
            Index = Utility.GetBankEquation(Equations_Bank, ambient)
            if type(Index) == int:
                equation = Equations_Bank[Index]
                result = Calculator.Execute(Calculator.Read(equation), True, [])
                input(f"Resultado da proposição: {str(result)}\n\nEnter para continuar")
        case "B":
            Utility.SetTitle("Banco de proposições")
            if len(Equations_Bank):
                Utility.ShowBank(Equations_Bank)
                input("Enter para voltar")
            else:
                input("Banco vazio, pressione enter para continuar...")        
        case "E":
            break
        case _:
            Utility.ChangeColor(action)