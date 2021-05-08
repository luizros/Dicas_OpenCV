x = int(input("Digite um número: "))
n = [2,4,5,6,5,7,9] # sua lista
novalista = [] 
cont = 0
for numero in n: 
    if numero == x:
        novalista.append(cont)
    cont +=1
    
print(novalista)
        
        
    