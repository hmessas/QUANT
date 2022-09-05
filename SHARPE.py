import pandas as pd
import numpy as np
import pandas_datareader as pdr

#Coleta de dados do Yahoo e importa dados de planilha
df_selic = pd.read_excel('taxa_selic_apurada.xlsx')
df_petr4=pdr.DataReader('PETR4.SA',data_source='yahoo', start='2021-9-4', end='2022-9-4')['Close']

#Cria df de retornos diarios da PETR4
df_ret=df_petr4/df_petr4.shift(1)-1

#Calcula std, média da taxa Selic e retorno, todos usando 1 ano como base
std=df_ret.std()
sel_mean=(df_selic['Taxa (% a.a.)']/100).mean()
ret=df_petr4[-1]/df_petr4[0]-1

#Calcula o Sharpe Ratio
sharpe=(ret-sel_mean)/std


print(sharpe)