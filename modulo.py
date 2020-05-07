
def modulo(numero,modulo):
    risultato = numero % modulo
    return risultato
    
while 1:
    
    num=input("dammi il numero :")
    num=int(num)
    
    mod=input("dammi il modulo :")
    mod=int(mod)
    
    ris=modulo(num,mod)
    
    print("viene "+str(ris))
