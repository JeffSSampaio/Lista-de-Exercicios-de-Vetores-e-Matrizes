code =  [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
iSecreta = [2,15,13,0,4,9,1]

def traduzir(codigo):   
    mensagem = ''
    for i in iSecreta:
        mensagem += code[i]
    print(mensagem)                 
         
traduzir(iSecreta)      
    
    