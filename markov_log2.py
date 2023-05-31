import pandas as pd
import numpy as np





class Markov_log2:
    def __init__(self, secuencia):
        self.estados = {"H": {"A":-2.322 ,"C": -1.737,"G": -1.737 ,"T": -2.322},
                        "L": {"A":-1.737,"C": -2.322, "G": -2.322,"T": -1.737}} #Estados modelo oculto de Markov
        self.columns = ['G','G','C','A','C','T','G','A','A']
        self.row = ['H','L']
        self.inicial =  -1 # Estados Iniciales
        self.paso_estado = {"LL":-0.737, "LH":-1.322, "HH":-1,"HL":-1} #Paso entre estados
        self.secuencia = secuencia
        self.probabilidad = []
        self.longitud_secuencia = len(secuencia)
        self.P = []
        self.probabilidad_secuencia = 0
        self.probabilidad_maxima = []
    
    def forward(self):
        ph = self.inicial+self.estados["H"][self.secuencia[0]]
        pl = self.inicial+self.estados["L"][self.secuencia[0]]
        self.probabilidad.append([ph , pl])
        self.observaciones(ph,pl)
        self.probabilidad_maxima.append(max(ph,pl))
        for i in range(1,self.longitud_secuencia):
            ph, pl = self.viterbi(i)
            self.probabilidad.append([ph,pl])
            self.observaciones(ph,pl)
        self.format()

    def viterbi(self,i):
        ph = self.estados["H"][self.secuencia[i]]+max(self.probabilidad[i-1][0]+self.paso_estado["HH"],self.probabilidad[i-1][1]+self.paso_estado["LH"])
        pl = self.estados["L"][self.secuencia[i]]+max(self.probabilidad[i-1][0]+self.paso_estado["HL"],self.probabilidad[i-1][1]+self.paso_estado["LL"])
        return ph,pl
    
    def observaciones(self,ph,pl):
        if ph > pl:
            self.P.append("H")
            
        else:
            self.P.append("L")               

    def format(self):
        transpuesta = list(zip(*self.probabilidad))
        trans = []
        for fila in transpuesta:
            trans.append(fila)
        df = pd.DataFrame(trans)
        df.columns = self.columns
        df.index = self.row
        print(df, "\n", "\n", self.P, "\n")
        
        self.probabilidad_secuencia = max(self.probabilidad[self.longitud_secuencia-1])
        print("La probabilidad de la secuencia es: ", 2**self.probabilidad_secuencia)

if "__main__" == __name__:
    secuencia =  "GGCACTGAA"
    forward = Markov_log2(secuencia)
    forward.forward()

    


        
