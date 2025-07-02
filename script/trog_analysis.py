# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:46:34 2022

@author: Kriszti
"""

import pandas as pd
from glob import glob
from datetime import datetime

o_path = input('Path of output files (e.g., C:/Experiment/Outputs/*.csv): ')

by_trial = pd.DataFrame()

for file in glob(o_path):
    df = pd.read_csv(file)
    df = df[df['blokk'] != 'practice']
    df['trial'] = df['Trials.thisIndex'].fillna(0) + df['pragm_trials.thisIndex'].fillna(0)
    df = df[
        ['expName', 'Azonosító', 'trial', 'blokk', 'mondat',
         'test_resp.keys', 'test_resp.corr', 'test_resp.rt']
        ].rename(
            {'expName' : 'experiment_version',
             'Azonosító' : 'ID',
             'blokk' : 'condition',
             'mondat' : 'sentence',
             'test_resp.keys' : 'response',
             'test_resp.corr' : 'ACC',
             'test_resp.rt' : 'RT'},
            axis = 1
            )
    by_trial = pd.concat([by_trial, df], ignore_index = True)

# Filter participants below chance level (below 0.4 here)    
cor = by_trial.groupby(['ID']).agg({'ACC' : 'mean'}).reset_index(drop = False)
IDs = list(cor[cor['ACC'] >= 0.4]['ID'])
by_trial = by_trial[by_trial['ID'].isin(IDs)]

wide = pd.DataFrame()

for name, group in by_trial.groupby(['ID']):
    ID = group['ID'].unique()[0]
    wide.loc[ID, 'experiment_version'] = group['experiment_version'].unique()[0]
    wide.loc[ID, 'gram_ACC_mean'] = group[group['condition'] == "gramm"]['ACC'].mean()
    wide.loc[ID, 'gram_RT_median'] = group[group['condition'] == "gramm"]['RT'].median()
    wide.loc[ID, 'pragm_ACC_mean'] = group[group['condition'] == "pragm"]['ACC'].mean()
    wide.loc[ID, 'pragm_RT_median'] = group[group['condition'] == "pragm"]['RT'].median()
wide = wide.reset_index(drop = False).rename(columns = {'index' : 'ID'})

today = datetime.today().strftime('%Y%m%d')
r_path = input("Path of data file: ")
by_trial.to_csv(r_path + "/trog_by_trial_" + today + ".csv", index = False)
wide.to_csv(r_path + "/trog_wide_" + today + ".csv", index = False)
