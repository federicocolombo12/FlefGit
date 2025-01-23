import random
Valori_Carte = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
Semi_Carte = ['P', 'Q', 'F', 'C']

Mazzo = []
for valore in Valori_Carte:
    for seme in Semi_Carte:
        Mazzo.append((valore, seme))

for i in range (len(Mazzo)):
    index=random.randint(0, 31)
    Valore_Random = Mazzo[index]
    Mazzo[index] = Mazzo[i]
    Mazzo[i] = Valore_Random


MazzoGruppi = []
counter = 0
for i in range(0, 6):
    MazzoGruppi.append([])
    for j in range(0, 5):
    
        MazzoGruppi[i].append(Mazzo[counter])
        counter += 1


def CheckPoint(Gruppo):
    counterCoppie=CheckCoppia(Gruppo)
    return counterCoppie



def CheckCoppia(Gruppo):
    coppia=0
    listaValori=[]
    ValoriCoppia=[]
    for i in range(0, 5):
        listaValori.append(Gruppo[i][0])
    counter=0
    for i in range(0, 5):
        for j in range(counter, 5):
            counter+=1
            if i!=j:
                if listaValori[i]==listaValori[j] and listaValori[i]:
                    coppia+=1

                    
    return coppia
print(MazzoGruppi)
for i in range(0, 6):
    print(CheckPoint(MazzoGruppi[i]))