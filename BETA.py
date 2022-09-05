import pandas as pd
import pandas_datareader as pdr


#Coleta dados do Yahoo Finance
ativos=['^BVSP','PETR4.SA']
df=pd.DataFrame()
for i in ativos:
    df[i]=pdr.DataReader(i,data_source='yahoo', start='2017-9-4', end='2022-9-4')['Close']

#Cria dataframe dos retornos diários
df_ret = df/df.shift(1)-1

#Calculo dos valores necessários, todos com base em 5 anos de dados
cov=df_ret.cov()
var=df_ret.var()
beta=cov.iat[0,1]/var['^BVSP']

print(round(beta,2))
