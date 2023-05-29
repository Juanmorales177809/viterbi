import pandas as pd
import numpy as np



class Viterbi:
    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.transicion= np.array(((0.5, 0.5), (0.4, 0.6)))# Probabilidades de transición # Probabilidades de emisión
        self.emision = np.array(((0.2, 0.3, 0.3, 0.2), (0.3, 0.2, 0.2, 0.3))) #cada fila denota la probabilidad que se de A C G T para cada estado H y L
        self.probabilidad_inicial = np.array((0.5, 0.5)) #Probabilidades iniciales
        self.observaciones = []
        self.filas = len(secuencia) #Filas de la secuencia dada
        self.filas_transicion = self.transicion.shape[0] #Filas de la matriz de transición
        self.probabilidades = np.zeros((self.filas, self.filas_transicion)) #Construyo inicialmente una matriz de cero que voy a ir llenando
        self.probabilidades[0, :] = np.log2(self.probabilidad_inicial * self.emision[:, self.observaciones[0]])  # Caso base
        self.matriz = np.zeros((self.filas - 1, self.filas_transicion))
        self.estados_probables = np.zeros(self.filas)
        self.estados = [] #Lista vacia que va a contener los estados 
        
    def values(self):
        for i in range(1,self.filas):
            if self.secuencia[i] == "G":
                self.observaciones.append(2)
            if self.secuencia[i] == "C":
                self.observaciones.append(1)
            if self.secuencia[i] == "A":
                self.observaciones.append(0)
            if self.secuencia[i] == "T":
                self.observaciones.append(3)
    
    
    def probabilidades_mod(self):
        for i in range(1, self.filas):
            for j in range(self.filas_transicion):
                probabilidad = self.probabilidades[i-1] + np.log2(self.transicion[:, j]) + np.log2(self.emision[j, self.observaciones[i]]) #Para no perderme, saco todas las probabilidades con todos los caminos
                self.matriz[i-1, j] = np.argmax(probabilidad) #Ubicacion de los estados más probable dado el estado anterior 
                
                self.matriz[i, j] = np.max(probabilidad) #El camino más probable que termina en el estado j con la observación "i"

    def camino_mas_probable(self):
        ubi_estados = np.argmax(self.probabilidades[self.filas - 1, :]) #Ubicacion del ultimo estado mas probable 
        self.estados_probables[0] = ubi_estados
        m = 1   
        for i in range(self.filas - 2, -1, -1): #Arranco el contador de atras haci adelante, desde el penultimo estado i.e. SS - 2
            self.estados_probables[m] = self.matriz[i, int(ubi_estados)]  #Ubicacion de los estados mas probables
            m += 1
        print('La matriz que contiene los valores de probabilidad mas probables: ', '\n', np.transpose(self.probabilidades),'\n')   
# Invierto la matriz que contiene la ubicacion del camino de los estados mas probable (Como arranque del último al primero)
        E = np.flip(E, axis=0)
        for s in E:
            if s == 0:  #Como ya conozco la posicion de los estados mas probables les asigno la letra que denota los estados y los agrego a la lista
                self.estados.append("H")
            else:
                self.estados.append("L")
        
        print('El camino más probable es: ', self.estados,'\n') 


#La probabilidad de que la secuencia S haya sido generada por el modelo HMM

        probabilidad = 2**(self.probabilidades[self.filas-1, 0] + self.probabilidades[self.filas-1, 1])

        print('La probabilidad de que la secuencia S haya sido generada por el modelo HMM es : ', probabilidad)
   

if "__main__" == __name__:
    secuencia = "GGCACTGAA"
    lo = Viterbi(secuencia)
    lo.values()
    lo.probabilidades_mod()
    lo.camino_mas_probable()
    
    


