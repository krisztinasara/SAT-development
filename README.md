# file structure

- data: data files, df.csv contains merged data
- script: preprocess and combine data, xgboost

# summary of indices

variable |	explanation	|	variable group	|	variable type	|	note
--- |	--- |	--- |	--- |	---
ID	|	participant's ID code	|	demography	|	n.a.	
sex	|	participant's ID code	|	demography	|	control	
age_years	|	age in years	|	demography	|	predictor	
years_in_education	|	years in education	|	demography	|	control	
highest_education_level	|	highest education level	|	demography	|	control	
current_education_level	|	current education level (if indicated)	|	demography	|	control	
SAT_test_version	|	test version of the SAT test ("with sound": child friendly version)	|	ToM	|	n.a.	
SAT_accuracy	|	SAT accuracy score	|	ToM	|	outcome	
PS_vis_RT	|	perceptual speed visual reaction time	|	general cognitive	|	predictor	|	lower values mean better processing, likely negatively correlates with other indices
PS_ac_RT	|	perceptual speed acoustic reaction time	|	general cognitive	|	predictor	|	lower values mean better processing, likely negatively 
PS_vis_dec_RT	|	processing speed visual decision reaction time	|	general cognitive	|	predictor	|	lower values mean better processing, likely negatively correlates with other indices
PS_ac_dec_RT	|	processing speed acoustic decision reaction time	|	general cognitive	|	predictor	|	lower values mean better processing, likely negatively correlates with other indices
DS_forward	|	digit span forward score	|	general cognitive	|	predictor	
DS_backward	|	digit span backward score	|	general cognitive	|	predictor	
n_back_1_mean_score	|	nback task score aggregated from block 1back	|	general cognitive	|	predictor	
n_back_2_mean_score	|	nback task score aggregated from block 2back	|	general cognitive	|	predictor	
n_back_3_mean_score	|	nback task score aggregated from block 3back	|	general cognitive	|	predictor	
simon_RT	|	reaction time index from the Simon task	|	general cognitive	|	predictor	
stroop_RT	|	reaction time index from the Stroop task	|	general cognitive	|	predictor	
pragm_compr_test_version	|	test version of the TROG task including the "pragmatic comprehension" subtest which is included here	|	language	|	n.a.	
pragm_compr_accuracy	|	pragmatic comprehension accuracy score	|	language	|	predictor	

# description of indices

## ID

## sex

## age_years
We calculated age_years by substracting the date of birth from the date of the first test session.

## years_in_education

## highest_education_level

## current_education_level

## SAT_test_version

## SAT_accuracy

## PS_vis_RT_med
In the task, participants were instructed to look at a blank screen, and focus on the appearance of the image of a ball in the middle of the screen, and to press the spacebar as fast as they could each time when the ball appeared.
32 trials were presented.
We calculated PS_vis_RT_med as the median of RTs in the task.

## PS_ac_RT_med
In the task, participants had to focus on a tone presented via headphones, and had to press the spacebar as fast as they could each time when the sound was presented.
32 trials were presented.
We calculated PS_ac_RT_med as the median of RTs in the task.

## digit_span_forward
In the task, sequences of digits were presented, and participants were instructed to reproduce them by typing them in in the same order.
Tasks started with the presentation of 3 digits long sequences and the length of sequences increased as the task proceeded.
Participants were presented with four trials within each length, and the task was terminated after three incorrect responses within the same length.
The last sequence length with at least two correct responses were considered as the value of digit_span_forward.

## digit_span_backward
In the task, sequences of digits were presented, and participants were instructed to reproduce them by typing them in in reversed order.
Tasks started with the presentation of 3 digits long sequences and the length of sequences increased as the task proceeded.
Participants were presented with four trials within each length, and the task was terminated after three incorrect responses within the same length.
The last sequence length with at least two correct responses were considered as the value of digi_span_backward.

## n_back_2_mean_score
In the task, letters were presented individually in the middle of the screen, and participants were instructed to press the spacebar for every item that is identical to the one presented two steps earlier, and button ‘A’ for every other trial.
The task consisted of two blocks, and each block consisted of 60 trials: 10 targets, 10 lures and 40 foils, and participants were instructed to give responses for each trial.
We calculated an n-back task score for each participant by subtracting the rate of false alarms from the rate of hits for both experimental blocks (x = (hit/10) - (FA/50) * 100), and we considered the mean of block scores as an individual n-back task score (x = (score2-back(A) + score2-back(B) / 2).

## simon_RT

## stroop_RT

## pragm_compr_test_version

## pragm_compr_accuracy