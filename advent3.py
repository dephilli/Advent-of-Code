
#%%
with open("rucksacks.txt") as file:
    rucks=[line.rstrip() for line in file]

#%%
import string

lower=[i for i in string.ascii_lowercase]
upper=[i for i in string.ascii_uppercase]

letters=lower+upper

priority=[i for i in range(1,53)]

letter_priority=dict(zip(letters, priority))

def depacker(item):
    slicer=int(len(item)/2)
    first=item[0:slicer]
    last=item[slicer:]
    common=[]
    for i in first:
        for j in last:
            if i==j and i not in common:
                common.append(i)
    the_common = common[0]
    priority=letter_priority[the_common]
    return priority


sum([depacker(i) for i in rucks ])
#%%

def common(itera):

    commoner=[]
    for i in rucks[itera]:
        for j in rucks[itera+1]:
            if i==j and i not in commoner:
                commoner.append(i)
    for k in commoner:
        for l in rucks[itera+2]:
            if k==l:
                return letter_priority[l]        
    
common(0)
#%%

id_priority=[]

id_start=0

while id_start<300:
    id_priority.append(common(id_start))
    id_start+=3

sum(id_priority)