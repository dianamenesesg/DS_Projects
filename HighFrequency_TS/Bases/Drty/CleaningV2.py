import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

# Data manipulation
import numpy as np
import pandas as pd
#import datetime

# Plotting
import matplotlib.pyplot as plt
#import seaborn
import matplotlib.mlab as mlab

# Statistical manipulation
#from scipy.stats import norm

# Tabulate data
#from tabulate import tabulate

df_cpa = pd.read_csv("C:\\Users\\vipac\\Desktop\\ITAU\\ValueAtRisk\\Bases\\Drty\\OFER_CPA_20181116.txt", 
                     sep=";",low_memory=False,header=1)


df_cpa.columns = ['Data_Sessão',
'Símbolo_do_Instrumento',
'Sentido_Of_Compra',
'Sequência',
'GenerationID_Of_Compra',
'Cód_do_Evento_da_Of_Compra',
'Hora_Prioridade',
'Ind_de_Prioridade_Of_Compra',
'Preço_Of_Compra',
'Qtd_Total_Of_Compra',
'Qtd_Negociada_Of_Compra',
'Data_Oferta_Compra',
'Data_de_Entrada_Of_Compra',
'Estado_Of_Compra',
'Condição_Oferta',
'Corretora']

list = ['SUZB3                                             ',
'MGLU3                                             ',
'FIBR3                                             ',
'BTOW3                                             ',
'VALE3                                             ',
'BRKM5                                             ',
'EMBR3                                             ',
'PETR4                                             ',
'CPFE3                                             ',
'KLBN4                                             ',
'BRFS3                                             ',
'KROT3                                             ',
'ELET6                                             ',
'QUAL3                                             ',
'UGPA3                                             ',
'ECOR3                                             ',
'ELET3                                             ',
'CCRO3                                             ',
'SBSP3                                             ',
'GOLL4                                             ']

df_cpa = df_cpa[df_cpa["Símbolo_do_Instrumento"].isin(list)] # elimina assets no estudiados

df_cpa.drop(['Data_Sessão',

'Sentido_Of_Compra',
'Sequência',
'GenerationID_Of_Compra',
'Cód_do_Evento_da_Of_Compra',

'Ind_de_Prioridade_Of_Compra',

'Qtd_Total_Of_Compra',
'Qtd_Negociada_Of_Compra',
'Data_Oferta_Compra',
'Data_de_Entrada_Of_Compra',
'Estado_Of_Compra',
'Condição_Oferta',
'Corretora'],inplace = True, axis = 1)

df_cpa.to_csv("C:\\Users\\vipac\\Desktop\\ITAU\\ValueAtRisk\\Bases\\CPA\\OFER_CPA_20181005.csv", 
#              index=False)
#df_cpa.to_csv("C:\\Users\\vipac\\Desktop\\ITAU\\ValueAtRisk\\Bases\\VDA\\OFER_VDA_20181122.csv", 
              index=False)