import pandas as pd
import numpy as np


datos =  pd.read_excel('Libro1.xlsx')  #En el excel se encuentra la secuencia dada la cual a cada letra se le ha asigando un numero equivalente a la posicion dentro un vector 
                                       # teniendo en cuenta el cuadro del pdf visto en clase: A = 0, C = 1, G = 2, T = 3
Pos_secu = datos['identificador'].values

#Denota las probabilidades (Sin sacar el log en base 2)

# Probabilidades de transición
transi = np.array(((0.5, 0.5), (0.4, 0.6)))


# Probabilidades de emisión
emisi = np.array(((0.2, 0.3, 0.3, 0.2), (0.3, 0.2, 0.2, 0.3)))  #Cada fila denota la probabilidad que se de A C G T para cada estado H y L


# Probabilidades iniciales
inicial = np.array((0.5, 0.5))


SS = Pos_secu.shape[0] #Numero de filas de la secuencia dada 
T = transi.shape[0] #Numero de filas de la matriz de transición
  

matriz = np.zeros((SS, T)) #Construyo inicialmente una matriz de cero que voy a ir llenando
matriz[0, :] = np.log2(inicial * emisi[:, Pos_secu[0]])  # Caso base

ubi = np.zeros((SS - 1, T))


for i in range(1, SS):
    for j in range(T):
        probabilidad = matriz[i-1] + np.log2(transi[:, j]) + np.log2(emisi[j, Pos_secu[i]]) #Para no perderme, saco todas las probabilidades con todos los caminos
        ubi[i-1, j] = np.argmax(probabilidad) #Ubicacion de los estados más probable dado el estado anterior 
        
        matriz[i, j] = np.max(probabilidad) #El camino más probable que termina en el estado j con la observación "i"
    

E = np.zeros(SS)  #Creo un vector de ceros que voy a ir llenando con las ubicaciones de los estados mas probables

#Una vez calculada las probabilidades mas probables, calculamos el camino mas probable

ubi_estados = np.argmax(matriz[SS - 1, :]) #Ubicacion del ultimo estado mas probable 

E[0] = ubi_estados

m = 1 

for i in range(SS - 2, -1, -1): #Arranco el contador de atras haci adelante, desde el penultimo estado i.e. SS - 2
    E[m] = ubi[i, int(ubi_estados)]  #Ubicacion de los estados mas probables
    
    m += 1
    
print('La matriz que contiene los valores de probabilidad mas probables: ', '\n', np.transpose(matriz),'\n')   
# Invierto la matriz que contiene la ubicacion del camino de los estados mas probable (Como arranque del último al primero)
E = np.flip(E, axis=0)

estados = [] #Lista vacia que va a contener los estados 
for s in E:
    if s == 0:  #Como ya conozco la posicion de los estados mas probables les asigno la letra que denota los estados y los agrego a la lista
        estados.append("H")
    else:
        estados.append("L")
        
print('El camino más probable es: ', estados,'\n') 


#La probabilidad de que la secuencia S haya sido generada por el modelo HMM

P = 2**(matriz[SS-1, 0] + matriz[SS-1, 1])

print('La probabilidad de que la secuencia S haya sido generada por el modelo HMM es : ', P)