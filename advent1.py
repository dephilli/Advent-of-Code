#%%


#%%
with open("input.txt") as file:
    lines=[line.rstrip() for line in file]

#%%
lines[4]==""

# %%
h=1
i=0
for j in lines:
    if j=='':
        lines[i]="elf " + str(h)
        h+=1
    i+=1

#%%

elf_index=[]

elf_names=["elf "+str(i) for i in range(1,251)]

for i in range(1,251):
    look="elf " + str(i)
    elf_index.append(lines.index(look))

import pandas as pd

#%%

import numpy as np

elf_index=pd.Series(elf_index)
elf_names=pd.Series(elf_names)

elf_table={'names': elf_names, 'locations': elf_index}

elfs=pd.DataFrame(elf_table)

elfs["start"]=elfs.locations.shift()

elfs["start"]=np.where(elfs.start.isna(),0,elfs.start)

elfs["end"]=elfs.locations-1


# %%

calories=pd.Series(lines)

#%%
cals=0
for i in range(0,5):
    
    cals+=int(calories[calories.index==i])


def caloric_total(start,end):
    cals=0
    for i in range(start,end):
        cals+=int(calories[calories.index==i])
    return cals

caloric_total(0,5)


elfs["start"]=elfs.start.astype(int)

elfs.dtypes
#%%

caloric_total(6,20)

#%%

elfs["start"]=np.where(elfs.start>0,elfs.start+1,0)

#%%

indexer=elfs[["start","end"]]

#indexer=dict(indexer)


#%%
for index, row in indexer.iterrows():
    print(row['start'],row['end'])

#%%


#%%
caltotals=[]

for index, row in indexer.iterrows():
    caltotals.append(caloric_total(row['start'],row['end']))
    

#%%
caltotals.sort()

caltotals.reverse()

top_three=0
sum(caltotals[0:3])

#%%
t=0
x=open("input.txt", "r").read().split("\n")

for i in x:
    t=max(t,sum([int(r) for r in i.splitlines()]))

print(t)