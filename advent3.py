
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
