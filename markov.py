import pandas as pd
import numpy as np


class Markov:
    def __init__(self, secuencia):
        self.estados = {"H": {"A":0.2 ,"C": 0.3,"G": 0.3 ,"T": 0.2},
                        "L": {"A":0.3,"C": 0.2, "G": 0.2,"T": 0.3}} #Estados modelo oculto de Markov
        self.inicial =  0.5 # Estados Iniciales
        self.paso_estado = {"LL":0.6, "LH":0.4, "HH":0.5,"HL":0.5} #Paso entre estados
        self.secuencia = secuencia
        self.probabilidad = []
        self.longitud_secuencia = len(secuencia)
        self.P = []
        self.probabilidad_secuencia = 0
        self.probabilidad_maxima = []
    
    def forward(self):
        ph = self.inicial*self.estados["H"][self.secuencia[0]]
        pl = self.inicial*self.estados["L"][self.secuencia[0]]
        self.probabilidad.append([ph , pl])
        self.observaciones(ph,pl)
        self.probabilidad_maxima.append(max(ph,pl))
        for i in range(1,self.longitud_secuencia):
            ph, pl = self.viterbi(i)
            self.probabilidad.append([ph,pl])
            self.observaciones(ph,pl)
        print(self.probabilidad)
        print(self.P)
        self.probabilidad_secuencia = sum(self.probabilidad[self.longitud_secuencia-1][j] for j in range(len(self.estados)))
        print("La probabilidad de la secuencia es: ", self.probabilidad_secuencia)
        
    def viterbi(self,i):
        ph = self.probabilidad[i-1][0]*self.paso_estado["HH"]*self.estados["H"][self.secuencia[i]] \
                +self.probabilidad[i-1][1]*self.paso_estado["LH"]*self.estados["H"][self.secuencia[i]]
        pl = self.probabilidad[i-1][0]*self.paso_estado["HL"]*self.estados["L"][self.secuencia[i]] \
                +self.probabilidad[i-1][1]*self.paso_estado["LL"]*self.estados["L"][self.secuencia[i]]
        return ph ,pl
    
    def observaciones(self,ph,pl):
        if ph > pl:
            self.P.append("H")
            
        else:
            self.P.append("L")
 

if "__main__" == __name__:
    secuencia =  "GGCA"
    forward = Markov(secuencia)
    forward.forward()
