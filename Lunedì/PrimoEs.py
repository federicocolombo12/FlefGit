# Existing code
for riga in infinitoRighe:
    parole += riga.split(" ")

for parola in parole:
    parolaNew = parola.lower()
    parolaNew = parolaNew.replace(",", "")
    parole[parole.index(parola)] = parolaNew

dizionarioParole = {}
for parola in parole:
    if parola in dizionarioParole:
        dizionarioParole[parola] += 1
    else:
        dizionarioParole[parola] = 1

# Exclude articles, prepositions, and conjunctions
exclude_words = {'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'about', 'as', 'of', 'from', 'that', 'which', 'or', 'but', 'if', 'when', 'than', 'because', 'while', 'where', 'after', 'so', 'though', 'since', 'until', 'whether', 'before', 'although', 'nor', 'like', 'once', 'unless', 'now', 'except'}

filtered_dizionarioParole = {k: v for k, v in dizionarioParole.items() if k not in exclude_words}

# Get the 5 most frequent words
most_frequent_words = sorted(filtered_dizionarioParole.items(), key=lambda item: item[1], reverse=True)[:5]

print(most_frequent_words)

infinitoFile.close()