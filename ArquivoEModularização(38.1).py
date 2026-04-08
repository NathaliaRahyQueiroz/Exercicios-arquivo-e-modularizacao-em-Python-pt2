import os


numero: float = 0.0
dir: str = ''
arq: str = ''
cont: int = 0



def grava(n, max, min):
    global dir 
    global arq
    global cont
    dir = '/home/nathi/exercicios/'
    arq = 'ex38.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(n) + '\n'
    if cont == 100:
        linha = 'O maior valor é ' + str(max) + ' e o menor valor é ' + str(min) + '\n'
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
    
    cont+=1
    

       

def valores(ma,me, num):
    contador: int = 0
    while contador < 99:
        num = float(input("Digite um número positivo:"))
        while num<0:
            num = float(input("Por favor, digite um valor POSITIVO:"))
        if num >= ma:
            ma = num
        if num <= me:
            me = num
        contador +=1
        grava(num, ma, me)
    grava(num, ma, me)
        
    print ("Maior valor:", ma, "Menor valor:", me)
    
    
    
   


def main():
    global numero
    maior: float = 0.0
    menor: float = 0.0
    numero = float(input("Digite um número positivo:"))
    while numero <0:
        numero = float(input("Digite um valor (apenas positivo):"))
    maior = numero
    menor = numero
    grava(numero, maior, menor)
    valores(maior, menor, numero)
    

    


if (__name__ == '__main__'):
    main()