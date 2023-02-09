
#Versão Beta 0.5
from os import system as sys

def Clear():
    sys("cls")

Symbols = ["~","^","v","<>","->"]
A, B, C, D = True, False, False, False
TestArray = [A,"v","~","(","(",B,"<>",D,"^","~",B,")","->",C,")"]

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
        for i in range(Total_Deletes):
            array.pop(Delete_Flag+1)
        
    #Passar pelos valores da lista até encontrar uma operação (enquanto seu tamanho for maior que 1)
    while len(array) > 1:
        for i in range(len(array)):
            #Operação encontrada
            if array[i] in Symbols:
                print("(" + ' '.join(map(str,array)) + ")")
                #Verificar se é um símbolo de negação
                if array[i] == Symbols[-1]:
                    a = array.pop(i+1)
                    array[i] = not a
                    break
                #Caso não seja, verificar qual operação
                elif array[i+1] != "~":
                    #Armazenar e remover valor sucessor e anterior para cálculo
                    a, b = array.pop(i-1), array.pop(i)
                    #Retornar o resultado da operação no lugar do símbolo
                    array[i-1] = Operate(array[i-1], a, b)
                    break
    print(array[0])
    return array[0]

Execute(TestArray)