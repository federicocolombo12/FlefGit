'''Scrivere un programma che legga i dati dal file di testo
rawdata_2004.txt e li inserisca in un dizionario le cui chiavi sono nomi di nazioni e i cui valori
sono redditi annui pro capite. Si noti che nel file i campi sono separati da un carattere di tabulazione
'\t'. Poi, il programma deve chiedere all’utente di fornire in input nomi di nazioni, per visualizzare i
valori corrispondenti di reddito annuo pro capite. Il programma deve terminare quando l’utente
inserisce in input la stringa 'quit'. È possibile leggere dati analoghi, aggiornati al 2021, in formato
.csv, dal file rawdata_2021.csv. Provare a risolvere lo stesso esercizio lavorando su questo file
.csv.'''
file= open(r"FlefGit\Lab11-file-input (1) (33846610)\Lab11-file-input\11.2.1 Redditi pro capite\rawdata_2004.txt", "r")
listaRaw=[]
dizionario={}
for line in file:
    listaRaw.append(line.split("\t"))
    
for i in range(len(listaRaw)):
    dizionario[listaRaw[i][1]]=listaRaw[i][2].replace("$","").strip()

inputText=""
while inputText!="quit":
    
    inputText=input("dimmi una nazione o quit per uscire: ").lower()
    for key in dizionario:
        if key.lower()==inputText:
            print(dizionario[key]+"$")

file.close()