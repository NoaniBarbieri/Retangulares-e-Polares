#Aluna: Noani Barbieri
#Materia: Eletromagnetismo 2

#Definindo as bibliotecas necessarias
import math
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

#inicio da função
def main():

    #definindo as variaveis necessárias para o programa
    beta=1/3
    compOnda=(2*(3.14/beta)) #utilizando pi como 3.14, para facilitar os calculos
    Tam = 1/(100*compOnda) #formmula pelo livro do tamanho

    #Algumas das funções base foram retiradas  dos programas postados pelo professor
    aux= compOnda*3
    x = np.arange(-aux,aux,Tam) #define um intervalo para o grafico
    E = 50*np.cos(beta*x)  
    E1 = -50*np.sin(beta*x)
    E2 = -50*np.cos(beta*x)

    fig, ax1 = plt.subplots(3,1) #função que irá ajudar a gerar os graficos.
    x = x/compOnda
    #funções retiradas da base infomadas pelo professor
    #referente ao primeiro grafico
    ax1[0].plot(x, E, 'r-', linewidth=2, label="E(s,x)")   
    ax1[0].set_xlabel("x=lambda")     #escrita na horizontal
    ax1[0].set_ylabel("Amplitude")    #escrita na vertical
    ax1[0].grid(True)
    ax1[0].set_title('E = 50cos(βx)')  #titulo do grafico

    #referente ao segundo grafico
    ax1[1].plot(x, E1, 'g-', linewidth=2, label="E1(s,x)")
    ax1[1].set_xlabel("x=lambda")
    ax1[1].set_ylabel("Amplitude")
    ax1[1].grid(True)
    ax1[1].set_title('E = -50sin(βx)')

    #referente ao terceiro grafico
    ax1[2].plot(x, E2, 'b-', linewidth=2, label="E2(s,x)")
    ax1[2].set_xlabel("x=lambda")
    ax1[2].set_ylabel("Amplitude")
    ax1[2].grid(True)
    ax1[2].set_title('E = -50cos(βx)')

    #função que separa os graficos
    fig.tight_layout()  

    plt.show()

main() 
#fim do programa