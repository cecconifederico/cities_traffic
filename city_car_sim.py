# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:55:08 2022

@author: Federico
"""
import pandas as pd
import numpy as np
import random

class CityCar():
    # car_id=""
    # gasoline = 0
    # visited = []
    
    def __init__(self,gasoline,car_id):
        self.car_id=str(car_id)+"id"
        self.gasoline = gasoline
        self.visited = []
        
    def __str__(self):
        # quando mostro una city car scrivo
        # l id, la quantità di benzina e il numero di città visitate
        return(self.car_id+"_"+str(self.gasoline)+"_"+str(len(self.visited)))

cars_list = []   
 
def init_simulation(n):
    for i in range(n):
        # crea n car con un valore per la benzina che va da 100 a 1000
        cars_list.append(CityCar(np.random.randint(100,1000),i))

def calcola_arrivo(percorsi,start):
    appoggio = []
    for percorso in percorsi:
        if percorso[0]==start:
            appoggio.append(percorso)
    if len(appoggio)==0:
        return(['none',-1])
    else:
        x=random.choice(appoggio)
        return([x[1],x[2]])        



        
init_simulation(100)        
df=pd.read_csv('citta.csv',delimiter=',')  
df_list=df.values.tolist()

t = 0
durata = 1

l = df['partenza'].tolist()
m = list(set(l))

for j in cars_list:
    x=random.choice(m)
    j.visited.append(x)
    
while t < durata:
    random.shuffle(cars_list)
    for a in cars_list:
        print(calcola_arrivo(df_list,a.visited[0]))
    t+=1    
      