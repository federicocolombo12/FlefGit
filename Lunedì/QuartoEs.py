def Crivello(n):
    '''Restituisce la lista dei numeri primi minori o uguali a n'''
    numeri=list(range(2,n+1))
    for i in numeri:
        if i!=0:
            for j in range(2*i,n+1, i):
                numeri[j-2]=0
    numeri=[x for x in numeri if x!=0]
    return numeri
print(Crivello(100))