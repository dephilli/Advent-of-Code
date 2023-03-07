#%%
import pandas as pd

import numpy as np
# %%
with open("strategy.txt") as file:
    games=[line.rstrip() for line in file]

#%%
games2=pd.read_csv("strategy.txt", delimiter=" ", header=None)

#%%
games2.rename(columns={0:"Opponent", 1:"Me"}, inplace=True)

#%%
## A for Rock, B for Paper, and C for Scissors. 
# The second column--" Suddenly, the Elf is called away to help 
# with someone's tent.

##The second column, you reason, must be what you should play 
# in response: X for Rock, Y for Paper, and Z for Scissors. 
# Winning every time would be suspicious, so the responses must 
# have been carefully chosen

##shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

def score(hand):
    opponent=hand.split(" ")[0]
    me=hand.split(" ")[1]
    score=0
    if opponent=="A" and me=="X":
        score+=3
    if opponent=='B' and me=='Y':
        score+=3
    if opponent=='C' and me=="Z":
        score+=3
    if opponent=="A" and me=="Y":
        score+=6
    if opponent=="B" and me=="Z":
        score+=6
    if opponent=="C" and me=="X":
        score+=6
    if me=="X":
        score+=1
    if me=="Y":
        score+=2
    if me=="Z":
        score+=3            
    return score

score(games[0])

scores=[]

for i in games:
    scores.append(score(i))

sum(scores)

#%%
h=games[0]

h=h.split(" ")[0]
#%%
def gamer(value):
    v1=value.split(" ")[0]
    v2=value.split(" ")[1]
    return v1,v2

gamer(games[0])

#%%
#X means you need to lose, 
#Y means you need to end the round in a draw, 
# and Z means you need to win
#A for Rock, B for Paper, and C for Scissors.
#(1 for Rock, 2 for Paper, and 3 for Scissors) 

def the_game(hand):
    opponent=hand.split(" ")[0]
    outcome=hand.split(" ")[1]
    score=0
    if outcome=='Y':
        score +=3
    if outcome=='Z':
        score +=6
    if outcome=='X':
        if opponent=="A":
            shape="C"
        if opponent=="B":
            shape="A"
        if opponent=='C':
            shape='B'
    if outcome=="Z":
        if opponent=="A":
            shape="B"
        if opponent=="B":
            shape="C"
        if opponent=="C":
            shape="A"
    if outcome=="Y":
        shape=opponent
    if shape=="A":
        score +=1
    if shape=="B":
        score +=2
    if shape=="C":
        score +=3
    return score

the_game(games[3])   

games[3]

full_games=sum([the_game(i) for i in games])

