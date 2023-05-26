import pandas as pd
import numpy as np


datos =  pd.read_excel('Libro1.xlsx')  #En el excel se encuentra la secuencia dada la cual a cada letra se le ha asigando un numero equivalente a la posicion dentro un vector 
#                                        # teniendo en cuenta el cuadro del pdf visto en clase: A = 0, C = 1, G = 2, T = 3
Pos_secu = datos['identificador'].values
print(Pos_secu)