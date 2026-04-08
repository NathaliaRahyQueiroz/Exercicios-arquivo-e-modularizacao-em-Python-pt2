import os

numero: int = 0
dir: str = ''
arq: str = ''
soma: float = 0.0

def grava(resultado):
    global dir
    global arq
    dir = '/home/nathi/exercicios/'
    arq = 'ex36.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(resultado) + '\n'
    os.makedirs(dir, exist_ok = True)
    os.chmod(dir, 0o744)
    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        if (os.path.exists(file)):
            tipo = 'a'

        with open (file, tipo, encoding=enc) as file:
            file.write(linha)


def f_fatorial(cont):
    fatorial: int = 0
    c: int = 0
    fatorial = 1
    c=1
    while c <= cont:
        fatorial = fatorial *c
        c+=1
    return fatorial

   
    
    




def f_divisao(num_fat): 
    divisão: float = 0.0
    divisão = 1/num_fat
    print(divisão)
    grava(divisão)
    return divisão

def f_soma(dv):
    global soma 
    soma = float(soma + dv)
    return soma 

def main():
    global numero 
    contador: int = 1
    fat: int = 0 
    div: float =0.0
    soma_final: float = 0.0
    numero = int(input("Digite um número:"))
    if contador ==1:
        grava(contador)
        print(1)
    while contador <= numero:    
        fat = f_fatorial(contador)
        div= f_divisao(fat)
        soma_final= f_soma(div)
        contador+=1
    soma_final+=1
    print (soma_final)
    grava(soma_final)
    
    
    

if (__name__ == '__main__'):
    main()