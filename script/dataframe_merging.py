# -*- coding: utf-8 -*-
"""
This code merges dataframes for the SAT development project.
author: krisztinasara
date: 2025-07-02
"""

import pandas as pd

path = "C:/Users/krisztinasara/github/SAT-development/data/"

dem = pd.read_csv(path + "demography.csv")
dem = dem[dem['inclusion'] == 1]
sat = pd.concat(
    [pd.read_csv(path + "SAT_MC_II_sound_wide_20230428_FINAL_SAMPLE.csv"),
     pd.read_csv(path + "SAT_MC_II_nosound_wide_20250423_FINAL_SAMPLE.csv")]
    )
ps = pd.concat(
    [pd.read_csv(path + "PROC_SPEED_YA_20231026_FINAL_SAMPLE.csv"),
     pd.read_csv(path + "PROC_SPEED_v2_20250423_FINAL_SAMPLE.csv")]
    )
ds = pd.read_csv(path + "DigitSpan_20250423_FINAL_SAMPLE.csv")
nback = pd.read_csv(path + "Verbal_n_back_wide_20250423_FINAL_SAMPLE.csv")
simon = pd.read_csv(path + "Simon_nyilas_wide_20250423_FINAL_SAMPLE.csv")
stroop = pd.read_csv(path + "stroop_wide_20250423_FINAL_SAMPLE.csv")
trog = pd.concat(
    [pd.read_csv(path + "trog_old_wide_20230425.csv"),
     pd.read_csv(path + "trog_new_wide_20250425_FINAL_SAMPLE.csv")]
    )

df = pd.merge(
    dem, sat, how = "inner", on = "ID"
    )
df = pd.merge(
    df, ps[['ID', 'vis_RT_med', 'ac_RT_med', 'vis_dec_RT_med', 'ac_dec_RT_med']], how = "left", on = "ID"
    )
df = pd.merge(
    df, ds[['ID', 'forward_span', 'backward_span']], how = "left", on = "ID"
    )
df = pd.merge(
    df, nback[['ID', 'nback_1_dprime', 'nback_2_dprime', 'nback_3_dprime']], how = "left", on = "ID"
    )
df = pd.merge(
    df, simon[['ID', 'RT_score']].rename(columns = {'RT_score' : "simon_RT"}), how = "left", on = "ID"
    )
df = pd.merge(
    df, stroop[['ID', 'RT_score']].rename(columns = {'RT_score' : "stroop_RT"}), how = "left", on = "ID"
    )
df = pd.merge(
    df, trog[['ID', 'experiment_version', 'pragm_ACC_mean']], how = "left", on = "ID"
    )

df = df.rename(
    columns = {
        'experiment' : "SAT_test_version",
        'ACC' : "SAT_accuracy",
        'vis_RT_med' : "PS_vis_RT",
        'ac_RT_med' : "PS_ac_RT",
        'vis_dec_RT_med' : "PS_vis_dec_RT",
        'ac_dec_RT_med' : "PS_ac_dec_RT",
        'forward_span' : "DS_forward",
        'backward_span' : "DS_backward",
        'experiment_version' : "pragm_compr_test_version",
        'pragm_ACC_mean' : "pragm_compr_accuracy"
        }
    )
df = df.drop(
    ['incorrect_ID', 'right_handedness', 'dich_handedness', 'native', 'cognitive_impairment', 'books_read_per_year', 'MoCA', 'inclusion', 'reason_for_exclusion', 'duplicated', 'backup_date'],
    axis = 1
    )

df.to_csv(path + "df.csv", index = False)
