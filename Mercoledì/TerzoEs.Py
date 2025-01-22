''' Scrivere un programma che legga un file di testo (maze.txt) contenente
l’immagine di un labirinto, come il seguente, in cui gli asterischi ('*') rappresentano muri invalicabili
e gli spazi (' ') rappresentano corridoi percorribili.

Creare un dizionario corridors le cui chiavi sono tuple (riga,
colonna) di posizioni corrispondenti a un corridoio e i cui valori sono
insiemi di posizioni anch’esse corrispondenti a un corridoio, e adiacenti
alla posizione specificata dalla rispettiva chiave. Nell'esempio sopra, la
chiave corrispondente alla tupla (1, 1), evidenziata in blu, ha come
posizioni adiacenti {(1, 2), (0, 1), (2, 1)}. Visualizzare il
dizionario. [P8.20]'''
file=open(r"FlefGit\Lab11-file-input (1) (33846610)\Lab11-file-input\11.2.3 Labirinto\maze.txt", "r")
listaRaw=[]
for line in file:
    listaRaw.append(line.strip())

dizionarioCorridoio={}
for i in range(len(listaRaw)):
    for j in range(len(listaRaw[i])):
        if listaRaw[i][j]==" ":
            dizionarioCorridoio[(i,j)]=set()

            
print(dizionarioCorridoio)






file.close()