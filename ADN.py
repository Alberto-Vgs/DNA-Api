""" Cadenas de ADN """
def entrada(string):
    """ 
        string = "['ATGCGAT','CAGTGCT','TTAAAAT','AGAAGGT','CCCCTTT','TCACTGT']"
        string = "['ATGCGA','CAGTGC','TTATTT','AGACGG','GCGTCA','TCACTG']" 
    """
    """string = input("ingresa la matris: ")"""
    string = string.upper()
    str = ""
    val="false"
    print(string)
    for item in string:
        if item == " " or item == "{" or item == '"' or item == "}" or item == "]" or item == "[" or item == "'":
            continue
        else:
            str += item
    str = str.split(",")
    number =[]
    for s in str:
       number.append(len(s))
    for num in number:
        if number[0] != num:
            print("cadena no valida c")
            exit()
    for s in str:
        for ss in s:
            if ss != "A":
                if ss != "C":
                    if ss != "G":
                        if ss != "T":
                            print("cadena no valida")
                            exit()
    print(str)
    return str 

def matrix(string):
    matriz = []
    a = []
    for item in string:
        for i in item:
            a += [i]
        matriz.append(a)
        a = []
    return matriz

def mutacionesFilas(dna):
    mutacion = 0
    for item in dna:
        if len(item) <= 3:
            exit()
        counter = 0
        cnt = 0
        for i in item:
            letter = item[cnt]
            if letter == i:
                counter += 1
                if counter == 4:
                    mutacion += 1
            else:
                cnt += counter
                counter = 1
        counter = 0
    return mutacion

def mutacionesColumnas(dna):
    mutacion = 0
    letter=""
    if len(dna[0]) <= 3:
            exit()
    else:
        for tem in range(len(dna[0])):
            counter = 0
            for item in range(len(dna)):
                if item > 0:
                    if letter == dna[item][tem]:
                        counter += 1
                        if counter == 4:
                            mutacion += 1
                    else:
                        counter = 1
                else:
                    letter = dna[item][tem]
    return mutacion

def mutacionesDiagonal(dna):
    mutacion = 0
    counter = 0
    letter =""
    dct = dict()
    for i in range(len(dna)-1,-len(dna[0]),-1):
        dct[i] = []
    for i in range(len(dna)):
        for j in range(len(dna[0])):
            dct[i-j].append(dna[i][j])
    """print(dct)"""
    for d in dct:
        if len(dct[d]) <= 3:
            continue
        else:
            """print(dct[d])"""
            for item in range(len(dct[d])):
                if item > 0:
                    if letter == dct[d][item]:
                        counter += 1
                        if counter == 4:
                            mutacion += 1
                    else:
                        counter = 1
                else:
                    letter = dct[d][item]
    return mutacion

def printMatrix(matriz):
    print("-"*20+"La matriz es :"+"-"*20)
    for item in matriz:
        print(item)
    print("-"*26+"-"*26)

def comprovation(string):
    matriz = entrada(string)
    printMatrix(matriz)
    matriz = matrix(matriz)
    dnaMutado = mutacionesFilas(matriz) + mutacionesColumnas(matriz) + mutacionesDiagonal(matriz)
    if dnaMutado == 0:
        print("FALSE")
        return False
    else:
        print("TRUE")
        return True

if __name__ == "__main__":
    string = entrada(string)
    matriz = matrix(string)
    printMatrix(matriz)
    comprovation(matriz)
    