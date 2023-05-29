# Aula_19_pt-III
def soma(a, b):
    s = a + b
    print(s)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


def dobra(list):
    pos = 0
    
    while pos < len(list):
        list[pos] *= 2
        pos += 1


soma(4,5)
soma(8,9)
soma(2,1)
soma(b=4, a=5)

contador(2, 1, 7)
contador(8,0)
contador(4, 4, 7, 6, 2)

valores = [6 , 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
