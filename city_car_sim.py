# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:55:08 2022

@author: Federico
"""
import pandas as pd
import numpy as np

class CityCar():
    car_id=""
    gasoline = 0
    visited = []
    
    def __init__(self,gasoline,car_id):
        self.car_id=str(car_id)+"id"
        self.gasoline = gasoline
        
    def __str__(self):
        # quando mostro una city car scrivo
        # l id, la quantità di benzina e il numero di città visitate
        return(self.car_id+"_"+str(self.gasoline)+"_"+str(len(self.visited)))

cars_list = []   
 
def init_simulation(n):
    for i in range(n):
        # crea n car con un valore per la benzina che va da 100 a 1000
        cars_list.append(CityCar(np.random.randint(100,1000),i))
        
init_simulation(100)        
        