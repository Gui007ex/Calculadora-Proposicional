import Boolean_Calculator as Calculator

A, B, C, D = True, False, False, False
TestArray: list = ["~",A,"v","(","(",B,"<>",D,"^",B,")","->","~",C,")"]
Equations_Bank: list = [1]
Comands = '''Calculadora Proposicional

A - Adicionar equação
R - Resolver equação
-------------------------
B - Mostrar banco
E - Sair do código

Comando:'''

#Execute(TestArray)

while True:
    Calculator.Clear()
    action = input(Comands).upper()

    match action: 
        case "A":
            Calculator.Add(Calculator.Create(), Equations_Bank)
            input("Equação adicionada\n\nEnter para continuar")
        case "R":
            print("\n~Resolver equação~\n")
            if len(Equations_Bank) == 0:
                input("Banco vazio, pressione enter para continuar...")
            else:
                Calculator.Execute(TestArray)
                input()
        case "B":
            pass
        case "E":
            break