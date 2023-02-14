import Boolean_Calculator as Calculator

A, B, C, D = True, False, False, False
TestArray: list = ["~",A,"v","(","(",B,"<>",D,"^",B,")","->","~",C,")"]
Equations_Bank: list = []
Comands = '''Calculadora Proposicional

A - Adicionar Equação
R - Resolver Equação
E - Sair do Código

Comando:'''

#Execute(TestArray)

while True:
    Calculator.Clear()
    action = input(Comands).upper()

    match action: 
        case "A":
            Calculator.Add(Calculator.Create(), Equations_Bank)
            print(Equations_Bank)
            input()
        case "R":
            print("\n~Resolver equação~\n")
            if len(Equations_Bank) == 0:
                input("Banco vazio, pressione enter para continuar...")
            else:
                Calculator.Execute(TestArray)
                input()
        case "E":
            break