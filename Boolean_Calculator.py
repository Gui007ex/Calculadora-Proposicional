import os

Global_Alf = ["P", "Q"]

#Funções de utilidade
def Clear():
    os.system("cls")

def SetTitle(string: str):
    Clear()
    print(string+"\n")

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

#Função pra resolver uma equação válida
def Execute(array: list):
    Op_Symbols: list = ["~","^","v","->","<>"]
    #Procurar parênteses para encontrar as prioridades
    while "(" in array:
        print(' '.join(map(str,array)))
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
        #Remover elementos restantes dos parênteses
        Total_Deletes = len(PriorArray)+1
        array[Delete_Flag] = Execute(PriorArray)
        del array[Delete_Flag+1:Delete_Flag+1+Total_Deletes]
        
    #Passar pelos valores da lista até encontrar uma operação (enquanto seu tamanho for maior que 1)
    while len(array) > 1:
        #Navegar pelos símbolos em ordem de precedência
        for symbol in Op_Symbols:
            #Manter aquele símbolo até efetuar todos
            while symbol in array:
                print(" ".join(map(str, array)))
                #Encontrar próxima operação com sinal de inversão de valor
                operation_index = array.index(symbol)
                if symbol == Op_Symbols[0]:
                    a = array.pop(operation_index+1)
                    array[operation_index] = not a
                else:
                    a, b = array.pop(operation_index-1), array.pop(operation_index)
                    array[operation_index-1] = Operate(symbol, a, b)
        
                
    print(array[0])
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
        SetTitle("Adicionar equação")
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
            SetTitle("Adicionar equação\n\n" + " ".join(new_equation))
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

#Função para mostrar uma equação na tela
def Show(equation: list):
    pass