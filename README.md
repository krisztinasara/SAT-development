# file structure

- data: data files, df.csv contains merged data, files starting with "SAT" and "trog" contain SAT and pragmatic comprehension task data
- script: merging script and scripts for calculating SAT and pragmatic comprehension scores

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
PS_ac_RT	|	perceptual speed acoustic reaction time	|	general cognitive	|	predictor	|	lower values mean better processing, likely negatively correlates with other indices
PS_vis_dec_RT	|	processing speed visual decision reaction time	|	general cognitive	|	predictor	|	lower values mean better processing, likely negatively correlates with other indices
PS_ac_dec_RT	|	processing speed acoustic decision reaction time	|	general cognitive	|	predictor	|	lower values mean better processing, likely negatively correlates with other indices
DS_forward	|	digit span forward score	|	general cognitive	|	predictor	
DS_backward	|	digit span backward score	|	general cognitive	|	predictor	
n_back_1_dprime	|	nback task score aggregated from block 1back	|	general cognitive	|	predictor	
n_back_2_dprime	|	nback task score aggregated from block 2back	|	general cognitive	|	predictor	
n_back_3_dprime	|	nback task score aggregated from block 3back	|	general cognitive	|	predictor	
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
Indicates which version of the Social Attribution Task – Multiple Choice (SAT‑MC) was used (original / child friendly with spoken trial questions and choices).

## SAT_accuracy
Participants watch the silent “Heider & Simmel” animation twice, then answer multiple-choice questions probing their social attribution interpretations.
Scores on the SAT‑MC is calculated as the ratio of correctly answered multiple-choice items.

## PS_vis_RT
In the task, participants were instructed to look at a blank screen, and focus on the appearance of the image of a ball in the middle of the screen, and to press the spacebar as fast as they could each time when the ball appeared.
32 trials were presented.
We calculated PS_vis_RT_med as the median of RTs in the task.

## PS_ac_RT
In the task, participants had to focus on a tone presented via headphones, and had to press the spacebar as fast as they could each time when the sound was presented.
32 trials were presented.
We calculated PS_ac_RT_med as the median of RTs in the task.

## PS_vis_dec_RT
In this speeded visual decision task, two Gabor patches were presented and participants had to decide if their orientations matched.  
They completed as many trials as possible in 60 seconds.  
This index is the median RT for correct responses.

## PS_ac_dec_RT
In this speeded auditory decision task, two pure tones were presented and participants had to decide if their pitches matched.  
They completed as many trials as possible in 60 seconds.  
This index is the median RT for correct responses.

## DS_forward
In the task, sequences of digits were presented, and participants were instructed to reproduce them by typing them in in the same order.
Tasks started with the presentation of 3 digits long sequences and the length of sequences increased as the task proceeded.
Participants were presented with four trials within each length, and the task was terminated after three incorrect responses within the same length.
The last sequence length with at least two correct responses were considered as the value of digit_span_forward.

## DS_backward
In the task, sequences of digits were presented, and participants were instructed to reproduce them by typing them in in reversed order.
Tasks started with the presentation of 3 digits long sequences and the length of sequences increased as the task proceeded.
Participants were presented with four trials within each length, and the task was terminated after three incorrect responses within the same length.
The last sequence length with at least two correct responses were considered as the value of digi_span_backward.

## n_back_1_dprime
Participants performed a 1-back task: pressing spacebar when the current letter matched the previous one.  
One block of 60 trials were presented.  
The index is calculated as:  
(hit rate / 10) - (false alarms / 50) * 100

## n_back_2_dprime
Participants performed a 2-back task: pressing spacebar when the current letter matched the one two items earlier.  
Two blocks of 60 trials were presented.  
The d-prime score was calculated similarly to 1-back in each block, and averaged across both blocks.

## n_back_3_dprime
Participants performed a 2-back task: pressing spacebar when the current letter matched the one two items earlier.  
One block of 60 trials were presented.  
The d-prime score was calculated similarly to 1-back.

## simon_RT
In the Simon task, participants responded to the left/right/center direction of arrows presented left/right/center.  
This RT index is calculated as:  
median RT (incongruent trials) - median RT (congruent trials), sign-reversed so higher values indicate better interference control.

## stroop_RT
In the Stroop task, participants named the color of font ignoring incongruent word meaning.  
This RT index is calculated as:  
median RT (incongruent trials) - median RT (congruent trials), sign-reversed to reflect better inhibitory control with higher scores.

## pragm_compr_test_version
The version of the computerized test.
Can be an old version with an error (error trials omitted in analysis), and a corrected new version.

## pragm_compr_accuracy
The pragmatic comprehension subtest of the KOBAK test, including metaphor, irony, and implicature items.
Accuracy in a four-alternative forced-choice picture selection task designed to assess comprehension of pragmatic content.  
Higher values reflect better comprehension.
