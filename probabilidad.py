import pandas as pd
import numpy as np



class Viterbi:
    def __init__(self, secuencia):
        self.estados = {"H": {"A":0.2 ,"C": 0.3,"G": 0.3 ,"T": 0.2},
                        "L": {"A":0.3,"C": 0.2, "G": 0.2,"T": 0.3}} #Estados modelo aculto de Markov
        self.inicial =  0.5 # Estados Iniciales
        self.paso_estado = {"LL":0.6, "LH":0.4, "HH":0.5,"HL":0.5} #Paso entre estados
        self.secuencia = secuencia
        self.probabilidad = {}
        self.longitud_secuencia = len(secuencia)
    def forward(self):
        ph = self.inicial+self.estados["H"][self.secuencia[0]]
        pl = self.inicial+self.estados["L"][self.secuencia[0]]
        self.probabilidad[]
        # self.probabilidad.append(self.inicial+self.estados[0])
        # for i in self.longitud_secuencia:
        #     pass


if "__main__" == __name__:
    secuencia =  "GGCA"
    forward = Viterbi(secuencia)
    forward.forward()
    print(secuencia[0])
    


        
