import os



def grava(vlr):
    dir = '/home/nathi/exercicios/'
    arq = 'multiplosDe5.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(vlr) + '\n'
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


def ler_conteudo(dir, arq):
    valor: float = 0.0
    arquivo: str = ''
    arquivo = dir + arq
    if (os.path.exists(dir) and os.path.isdir(dir)):
        with open (arquivo) as file:
            for linha in file:
                valor = float(linha)
                if valor % 5 ==0:
                    print(valor)
                    grava(valor)
                    



def main():
    dir1: str = ''
    arq1: str = ''
    dir1 = '/home/nathi/exercicios/'
    arq1= 'ex38.txt'
    
    ler_conteudo(dir1, arq1)

    
            
               

if __name__ == '__main__':
    main()