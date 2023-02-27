import UI

Global_Alf = ["P","Q","R","S"]

#Função pra realizar operação
def Operate(symbol: str, a: bool, b: bool):
    #Navegar pelos símbolos e escolher a operação
    match symbol: 
        case "^":
            return a and b
        case "v":
            return a or b
        case "->":
            if a and not b:
                return False
            else:
                return True
        case "<>":
            if a == b:
                return True
            else:
                return False

#Função para ler equação
def Read(equation: list):
    sub_equation = [i for i in equation]
    this_title = f"Resolver equação\n\n" + UI.ShowEq(sub_equation)
    for Letter in Global_Alf:
        if Letter in sub_equation:
            value = UI.GetValidInput(this_title, f"Valor de {Letter} (V ou F):", ["V","F"])
            value = value.upper() == "V"
            while Letter in sub_equation:
                next_change = sub_equation.index(Letter)
                sub_equation[next_change] = value
                this_title = f"Resolver equação\n\n" + UI.ShowEq(sub_equation)
    UI.SetTitle(this_title)
    input("Equação pronta, enter para resolver")
    UI.SetTitle("Resolver equação")
    return sub_equation

#Função pra resolver uma equação válida
def Execute(array: list, steps: bool, mask: list):
    title = "Resolver Equação"
    Op_Symbols = ["~","^","v","->","<>"]
    #Procurar parênteses para encontrar as prioridades
    while "(" in array:
        mask = [i for i in array]
        if steps:
            UI.SetTitle(title)
            print(UI.ShowEq(array))
        building = False
        #Construir o interior dos elementos dentro dos parênteses
        for i in range(len(array)):
            if array[i] == "(":
                PriorArray = []
                building = True
                Delete_Flag = i
            elif array[i] == ")":
                break
            elif building:
                PriorArray.append(array[i])
        #Remover elementos restantes dos parênteses e criar máscara para interface
        #mask = [[antes], [meio], [depois]]
        Total_Deletes = len(PriorArray)+1
        mask = [array[:Delete_Flag+1], array[Delete_Flag+Total_Deletes:]]
        array[Delete_Flag] = Execute(PriorArray, True, mask)
        del array[Delete_Flag+1:Delete_Flag+1+Total_Deletes]
        mask = []
        
    #Passar pelos valores da lista até encontrar uma operação (enquanto seu tamanho for maior que 1)
    while len(array) > 1:
        #Navegar pelos símbolos em ordem de precedência
        for symbol in Op_Symbols:
            #Manter aquele símbolo até efetuar todos
            while symbol in array:
                if steps:
                    UI.SetTitle(title)
                    if len(mask):
                        print(UI.ShowEq(mask[0]),UI.ShowEq(array),UI.ShowEq(mask[1]))
                    else:
                        print(UI.ShowEq(array))
                    input()
                #Encontrar próxima operação com sinal de inversão de valor
                operation_index = array.index(symbol)
                if symbol == Op_Symbols[0]:
                    a = array.pop(operation_index+1)
                    array[operation_index] = not a
                else:
                    a, b = array.pop(operation_index-1), array.pop(operation_index)
                    array[operation_index-1] = Operate(symbol, a, b)
    if steps:
        UI.SetTitle(title)
        print(UI.ShowEq(array) + "\n")
    return array[0]

#Função para adicionar símbolos possíveis
def Add_Symbol(possible: list, equation: list, closes: int, ready: bool):
    comands = [i for i in possible]
    limit = len(possible)
    for i in range(len(comands)):
        if comands[i] == "Variáveis:":
            sufix = "(" + ",".join(Global_Alf) + ")"
            limit = len(possible)-1
        else:
            sufix = f" ({i+1})"
        comands[i] += sufix
    comands = "\n".join(map(str, comands))
    while True:
        UI.SetTitle("Adicionar equação")
        if len(equation):
            print(f"{' '.join(equation)}\n")
        if closes == 0 and ready:
            print("Digite (Pronto) para salvar equação no banco")
        select = input(f"{comands}\nInput:")

        #Verificar possibilidade da saída
        if closes == 0 and ready and select.upper() == "PRONTO":
            return "Exit"

        #Verificar o tipo da entrada
        try:
            select = int(select)
            if 1 <= select <= limit:
                return select
        except:
            if select.upper() in Global_Alf and limit == len(possible)-1:
                return select.upper()
            
#Função pra criar equação
def Create():
    new_equation: list = []
    #Valores iniciais possíveis = "~", "VAR", "("
    avaiable = ["~","(","Variáveis:"]
    closes_needed, can_finish = 0, False

    while True:
        #Iniciar a pedida de símbolos possíveis
        next_command = Add_Symbol(avaiable, new_equation, closes_needed, can_finish)
        if next_command == "Exit":
            UI.SetTitle("Adicionar equação\n\n" + " ".join(new_equation))
            break
        elif type(next_command) == str:
            new_equation.append(next_command)
        else:
            new_equation.append(avaiable[next_command-1])
        
        #Filtrar próximas possibilidades e suas consequências
        last = new_equation[-1]
        can_finish = last in Global_Alf or last == ")"
        if last in Global_Alf:
            avaiable = ["^","v","->","<>"]
        else:
            match new_equation[-1]:
                case "~":
                    avaiable = ["(", "Variáveis:"]
                case "^" | "v" | "->" | "<>":
                    avaiable = ["~", "(", "Variáveis:"]
                case "(":
                    closes_needed += 1
                    avaiable = ["~", "(", "Variáveis:"]
                case ")":
                    closes_needed -= 1
                    avaiable = ["^","v","->","<>"]
        if closes_needed > 0 and (last in Global_Alf or last == ")"):
            avaiable.insert(0, ")")
    
    return new_equation

#Função pra adicionar equação ao banco
def Add(equation: list, bank: list):
    bank.append(equation)

#Função para criar uma tabela verdade
def GenerateTable(equation: list):
    sub_equation = [i for i in equation]
    #Saber quantas variáveis eu tenho
    order = []
    for letter in Global_Alf:
        if letter in sub_equation:
            order.append(letter)
            while letter in sub_equation:
                sub_equation[sub_equation.index(letter)] = order.index(letter)
    #Gerar variações com N variáveis
    total_variations = GetVariations(len(order))
    #Executar para cada variação
    results = []
    for variation in total_variations:
        test_equation = [i for i in sub_equation]
        for i in range(len(test_equation)):
            item = test_equation[i]
            if type(item) == int:
                test_equation[i] = variation[item]
        results.append(Execute(test_equation, False, []))
    #Adicionar resultado ao array de variações
    print(results)
    #Mostrar na tela os resultados
    pass

def GetVariations(num):
    arr = [[0 for i in range(num)] for j in range(2**num)]
    for i in range(num):
        value = False
        for j in range(2**num):
            if j % (2**num/(2**(i+1))) == 0:
                value = not value
            arr[j][i] = value
    return arr

UI.Clear()
arr_ex = ["P","v","Q","^","R","->","S"]
GenerateTable(arr_ex)