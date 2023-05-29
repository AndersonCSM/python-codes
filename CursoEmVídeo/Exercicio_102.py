# Exercicio_102
def fatorial(i, show=False):
    """
    Função fatorial:
    i = número fatorial
    Show = False - não mostra o cálculo
    Show = True - mostra o cálculo
    """

    f = 1
    
    for c in range(i, 0, -1):
        f *= c
   
    if show == False:
        return print(f'{f}')
    
    else:          
        for c in range(i,0,-1):
            print(f'{c}', end='')
            
            if c != 1:
                print(' x ', end='')
            
            else:
                print(f' = {f}')      

                
fatorial(5, show=True)

# Solução do professor
def fatorial(n, show=False):
   """
   Função fatorial:
   n = número fatorial
   Show = False - não mostra o cálculo
   Show = True - mostra o cálculo
   """   
   
    f = 1
    
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
        
        if c > 1:
            print(' x ', end='')
        
        else:
            print(' = ', end='')
        f *= c
    
    return f

print(fatorial(5, show=True))
