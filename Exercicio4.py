#Aluna: Noani Barbieri
#Materia: Eletromagnetismo 2

#Definindo as bibliotecas necessarias
import math
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

#Começando a função base
#valores foram arredondados com 2 casas decimais, para facilitar as execuções 
def main():
    
    #definição de funções base para o programa
    i=2/3
    compOnda= 9.42 
    t = 3.93*pow(10,-9)
    vAngular = 2*pow(10,8)

    #formmula pelo livro do tamanho
    tam = 1/(100*compOnda)

    #auxiliar para facilitar os calculos
    aux=compOnda*2

    ##define um intervalo para o grafico
    x = np.arange(-aux,aux,tam) 

    #funções com base nas informações retiradas do livro
    H = 0.1*np.cos(vAngular*t - i*x)

    fig, ax1 = plt.subplots()
    x = x/compOnda

    #referente ao segundo grafico, funções base retiradas dos slides do professor
    ax1.plot(x, H, 'c-', linewidth=2, label="H(s,x)")
    ax1.set_xlabel("x=lambda")  #escrita na horizontal
    ax1.set_ylabel("Amplitude") #escrita na vertical
    ax1.grid(True)
    ax1.set_title('H = 0,1*cos((2*10^8)*t - i*x)')  #titulo do grafico

    fig.tight_layout()

    plt.show()

main()
#fim do programa