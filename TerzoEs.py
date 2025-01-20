'''
. Un vettore sparso è una sequenza di numeri, la maggior parte dei quali è 0.
Un modo efficiente per memorizzare un vettore sparso è un dizionario, nel quale le chiavi sono le
posizioni in cui sono presenti i soli valori diversi da zero, e i valori sono i corrispondenti valori nella
sequenza. Per esempio, la sequenza 0 0 0 0 0 4 0 0 0 2 9 sarebbe rappresentata dal
dizionario {5:4, 9:2, 10:9}. Scrivere una funzione, sparse_array_sum(a, b), i cui
argomenti sono due dizionari di questo tipo, a e b. La funzione, senza modificare i dizionari passati
come argomenti, deve restituire il loro vettore somma come un vettore sparso, dove un valore nella
posizione i è la somma dei valori di a e b nelle rispettive posizioni i. [P8.22]
'''
a={5:4, 9:2, 10:9}
b={2:3, 5:1, 9:5}
def sparse_array_sum(a, b):
    c=[]
    maxKey = max(max(a.keys()), max(b.keys()))
    for i in range(maxKey+1):
        c.append(0)
    for key in a.keys():
        c[key] = a[key]
    for key in b.keys():
        c[key] += b[key]


    return c
print(sparse_array_sum(a, b))