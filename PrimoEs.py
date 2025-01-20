infinitoFile = open(r"C:\Users\chicc\Documents\Creatività\StudioPythonFede\FlefGit\Infinito.txt", "r")
infinitoString = infinitoFile.read()
infinitoRighe=infinitoString.split("\n")
parole=[]
for riga in infinitoRighe:
    parole+=riga.split(" ")

for parola in parole:
    parolaNew=parola.lower()
    parolaNew=parolaNew.replace(",","")
    parole[parole.index(parola)]=parolaNew

dizionarioParole={}
for parola in parole:
    if parola in dizionarioParole:
        dizionarioParole[parola]+=1
    else:
        dizionarioParole[parola]=1
print(dizionarioParole)
infinitoFile.close()