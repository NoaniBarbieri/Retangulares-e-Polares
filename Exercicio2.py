#Aluna: Noani Barbieri
#Materia: Eletromagnetismo 2

#Definindo a biblioteca
import math

#Pede o usuario e imprime o numero complexo
real=int(input('Entre com o valor real: '))
imag=int(input('Entre com o valor imaginario ( contem j): '))
comp=complex(real,imag)
print('complexo =', comp)

#Auxiliares para o calculo
aux1=pow(real,2)
aux2=pow(imag,2)

#Calculo para obter o modulo de Z e a fase, para realizar a transformação
modulo=round((math.sqrt(aux1+aux2)),2)
tet=math.atan2(imag,real) #realiza arctang
aux3=math.degrees(tet) #transforma em graus 
if(aux3>0): 
    print("Z = {:.2f} |{:.2f}°".format(modulo,aux3))
else:
    aux3+=360
    print("Z = {:.2f} |{:.2f}°".format(modulo,aux3))
    
#fim
