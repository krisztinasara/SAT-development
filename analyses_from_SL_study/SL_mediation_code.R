library(tidyverse)
library(lavaan)
library(psych)

df = read_csv("SL_df.csv")

df = df |>
  mutate(
    PS_vis_RT = -PS_vis_RT,
    PS_ac_RT = -PS_ac_RT,
    PS_vis_dec_RT = -PS_vis_dec_RT,
    PS_ac_dec_RT = -PS_ac_dec_RT,
    age_2 = age_years^2,
    log_age = log(age_years),
    log_age_2 = log(age_years)^2,
  ) |>
  select(
    age_years, age_2, log_age, log_age_2,
    PS_vis_RT, PS_ac_RT, PS_vis_dec_RT, PS_ac_dec_RT,
    DS_forward, DS_backward, nback,
    SEGM_VN_RT, SEGM_VN_offline
  )|>
  mutate(
    across(
      c(age_years, age_2,
        PS_vis_RT, PS_ac_RT, PS_vis_dec_RT, PS_ac_dec_RT,
        DS_forward, DS_backward, nback,
        SEGM_VN_RT, SEGM_VN_offline),
      ~ scale(.x)
    )
  ) |>
  rename(
    "age" = age_years
  )

# EFA

# Bartlett test
cortest.bartlett(
  df |> select(
    PS_vis_RT, PS_vis_dec_RT,
    DS_forward, DS_backward, nback
  ) |> cor(use = "pairwise.complete.obs"),
  n = 450
)

# okay

# KMO test
KMO(
  df |> select(
    PS_vis_RT, PS_vis_dec_RT,
    DS_forward, DS_backward, nback
  ) |> cor(use = "pairwise.complete.obs")
)

# okayish

# scree plot

scree(
  df |> select(
    PS_vis_RT, PS_vis_dec_RT,
    DS_forward, DS_backward
  ) |> cor(use = "pairwise.complete.obs")
)

efa = df |>
  select(
    PS_vis_RT, PS_vis_dec_RT,
    DS_forward, DS_backward
  ) |>
  psych::fa(
    nfactors = 2,
    rotate = "oblimin",
    fm = "minres"
  )

# EFA results
efa

cfa_model = '
  PS_vis =~ PS_vis_RT + PS_vis_dec_RT
  DS =~ DS_forward + DS_backward
'

fit_CFA = cfa(cfa_model, df)

summary(fit_CFA, fit.measures = TRUE, standardized = TRUE, rsquare = TRUE)

# mediation analyses

med_OFF = '
  # measurement model
  PS =~ PS_vis_RT + PS_vis_dec_RT
  DS =~ DS_forward + DS_backward
  # covariances
  PS ~~ DS
  PS ~~ nback
  DS ~~ nback
  
  # regression paths
  # a
  PS ~ a1*age + a2*age_2
  DS ~ a3*age + a4*age_2
  nback ~ a5*age + a6*age_2
  # b
  SEGM_VN_offline ~ b1*PS
  SEGM_VN_offline ~ b2*DS
  SEGM_VN_offline ~ b3*nback
  # c
  SEGM_VN_offline ~ c1*age + c2*age_2
  
  # a
  PS_age := a1 + a2
  DS_age := a3 + a4
  nback_age := a5 + a6
  # c
  c := c1 + c2
  # indirect effect
  abPS := (a1 + a2) * b1
  abDS := (a3 + a4) * b2
  abnback := (a5 + a6) * b3
  ab := (a1 + a2) * b1 + (a3 + a4) * b2 + (a5 + a6) * b3
  # total effect
  total := ((a1 + a2) * b1) + ((a3 + a4) * b2) + ((a5 + a6) * b3) + (c1 + c2)
'


fit_OFF = sem(med_OFF, df, std.lv = TRUE, missing = "FIML", estimator = "MLR")

summary(fit_OFF, fit.measures = TRUE, standardized = TRUE, rsquare = TRUE)
