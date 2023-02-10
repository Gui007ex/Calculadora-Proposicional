#Versão Beta 0.7 (Agora com ViniShows!)
from os import system as sys

def Clear():
    sys("cls")
Clear()

Equations_Bank: list = []
A, B, C, D = True, False, False, False
Op_Symbols: list = ["~","^","v","<>","->"]
TestArray: list = ["~",A,"v","(","(",B,"<>",D,"^",B,")","->","~",C,")"]

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

def Execute(array: list):
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

Execute(TestArray)
