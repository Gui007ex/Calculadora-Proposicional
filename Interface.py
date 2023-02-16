import Boolean_Calculator as Calculator

Equations_Bank: list = [["~","P","v","Q","^","P"]]
Comands = '''Calculadora Proposicional

A - Adicionar equação
R - Resolver equação
-------------------------
B - Mostrar banco
E - Sair do código

Comando:'''

while True:
    Calculator.Clear()
    action = input(Comands).upper()

    match action: 
        case "A":
            Calculator.Add(Calculator.Create(), Equations_Bank)
            input("Equação adicionada\n\nEnter para continuar")
        case "R":
            Calculator.SetTitle("Resolver equação")
            if len(Equations_Bank):
                Index = Calculator.GetBankEquation(Equations_Bank)
                if type(Index) == int:
                    result = Calculator.Execute(Calculator.Read(Equations_Bank[Index]), True)
                    input(f"Resultado da proposição: {str(result)}\n\nEnter para continuar")

            else:
                input("Banco vazio, pressione enter para continuar...")
        case "B":
            Calculator.SetTitle("Banco de equações")
            if len(Equations_Bank):
                Calculator.ShowBank(Equations_Bank)
            else:
                input("Banco vazio, pressione enter para continuar...")
        case "E":
            break