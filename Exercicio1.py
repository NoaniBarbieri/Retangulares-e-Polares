#Aluna: Noani Barbieri
#Materia: Eletromagnetismo 2

#Definindo a biblioteca
import math

fat=int(input('digite o valor fatorial '))
ang=int(input('digite o valor angular '))

#auxiliar para o calculo
aux= ang*(3.14/180)

#utilizando round para arredondar o valor em 2 casas decimais
x = round(fat *(math.cos(aux)),2)
y = round(fat *(math.sin(aux)),2)

#função do python que imprime o numero complexo
comp= (complex(x,y))

print(comp)
#fim