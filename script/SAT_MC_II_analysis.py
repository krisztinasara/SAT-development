# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:38:45 2023

@author: Kriszti
"""

import pandas as pd
from glob import glob
from datetime import datetime

files = input("Path of output files (e.g., C:/outputs/*.csv): ")

long = pd.DataFrame()
long_cols = ['expName', 'Azonosító' ,'sorszam',
             'kerdes', 'valasz1', 'valasz2', 'valasz3', 'valasz4',
             'helyes', 'fizikai', 'mozgas', 'kontextus',
             'helyes_valasz.keys', 'helyes_valasz.rt']

for file in glob(files):
    df = pd.read_csv(file)
    long = pd.concat(
        [
            long,
            df[long_cols]
         ],
        ignore_index = False
        )
long.insert(loc = 12, column = 'response_type', value = float('nan'))
long.rename(columns = {
    "expName" : "experiment" ,"Azonosító" : "ID", "sorszam" : "trial", "kerdes" : "question",
    "valasz1" : "choice_1", "valasz2" : "choice_2",
    "valasz3" : "choice_3", "valasz4" : "choice_4",
    "helyes" : "mentalization", "fizikai" : "physical", "mozgas" : "movement", "kontextus" : "context",
    "helyes_valasz.keys" : "response", "helyes_valasz.rt" : "RT"
    }, inplace = True)

long['response_type'] = long.apply(lambda row : row[['mentalization', 'physical', 'movement', 'context']][row == row['response']].index.values[0], axis = 1)
long['ACC'] = long.apply(lambda row : 1 if row['response_type'] == 'mentalization' else 0, axis = 1)

# filter unused items
include = [3, 4, 5, 6, 9, 13]
long['trial'] = long['trial'].astype(int)
long = long[long['trial'].isin(include)]

#wide = pd.DataFrame(
#    long.groupby(['experiment', 'ID'])['response_type'].value_counts(normalize = True)
#    ).rename(columns = {"response_type" : "proportion"}).reset_index(drop = False)
#wide = pd.pivot_table(data = wide,
#                      values = 'proportion',
#                      index = ['experiment', 'ID'],
#                      columns = 'response_type').fillna(0).reset_index(drop = False)
wide = long.groupby(['experiment', 'ID']).agg({'ACC' : "mean"}).reset_index(drop = False)

path = input("Path of results files (e.g. C:/experiment/data): ")
long.to_csv(path + "/SAT_MC_II_long_" + datetime.today().strftime("%Y%m%d") + ".csv",
            index = False)
wide.to_csv(path + "/SAT_MC_II_wide_" + datetime.today().strftime("%Y%m%d") + ".csv",
            index = False)
