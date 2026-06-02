# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 20:32:00 2025

@author: simone soares de oliveira

"""

import pandas as pd

# carregando base de dados

df = pd.read_excel (r"C:\Caminho do usuário\Princ_Insig_Julgados.xlsx")

print(df.shape)
 
# tamanho da amostra
  
n=400
  
# gerar amostra aleatoria simples
  
amostra= df.sample(n=n,random_state=42)
  
# salvar a amostra
  
amostra.to_excel(r"C:\\Caminho do usuário\amostra_400.xlsx",index=False)
 