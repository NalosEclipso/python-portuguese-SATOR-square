#Note that both h1 and h2 will be from Dic/h and p from Dic/p in the final runtest
def SATOR(h1, h2, p):
    """Verify if those words can be a sator square"""
    sq = [h1, h2, p, h2[::-1], h1[::-1]]
    n=0
    L=''
    U=''
    for word in sq:
        L=L+word
    while n<5:
        for word in sq:
            U=U+word[n]
        n+=1
    return L == U == L[::-1] == U[::-1]

    
#Examples:

print(SATOR('SATOR', 'AREPO', 'TENET')) #Should be True
print(SATOR('SATOR', 'BUNDA', 'TENET')) #Should be False
print(SATOR('ENALD', 'INHOS', 'LOUCO')) #Should be False
