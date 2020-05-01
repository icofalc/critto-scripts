import array
#caesar cipher
def cifra(lettera):
    let=ord(lettera)
    return let


def decifra(numero):
    lit=chr(numero)
    return lit

def main():
    stringa = input('Inserisci la frase: ')
    frase_in_numero=[]
    for i in stringa:
        numero=cifra(i)
        frase_in_numero.append(numero)
        
    
    chiave = input('dimmi la chiave: ')
    chiave=int(chiave)
    
    cifratura=[]
    #inizio parte decifratura
    
    for i in frase_in_numero:
        numero=i
        ris=numero + chiave
        finale=ris % 5000
        cifratura.append(finale)
        
    print("la cifratura viene "+str(cifratura))
    
    decifratura=[]
    
    for i in cifratura:
        numero=i
        ris=numero - chiave
        finale=ris % 5000
        decifratura.append(finale)
    
    #print(frase_in_numero)
    #print(decifratura)
    
    frase_final=[]
    for i in decifratura:
        frase_final.append(decifra(int(i)))
        
    print("la decifratura viene "+str(frase_final))
        
    
main()
