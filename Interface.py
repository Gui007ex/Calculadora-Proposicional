import Boolean_Calculator

A, B, C, D = True, False, False, False
TestArray: list = ["~",A,"v","(","(",B,"<>",D,"^",B,")","->","~",C,")"]
Equations_Bank: list = [TestArray]

#Execute(TestArray)

while True:

    action = input('''Calculadora Booleana
A - Adicionar Equação
R - Resolver Equação
E - Sair do Código
''').upper()

    if action == "A":
        print("\n~Adicionar Equação~\n")
        Boolean_Calculator.Add()
    elif action == "R":
        print("\n~Resolver Equação~\n")
        if len(Equations_Bank) == 0:
            input("Função Vazia Pressione Enter para continuar...")
        else:
            Boolean_Calculator.Execute(TestArray)
    elif action == "E":
        print("\n~Sair do Código~\n")
        break
    else:
        print("Operação Inválida")
        pass