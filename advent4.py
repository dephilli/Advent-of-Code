#%%
with open("elf_sectors.txt") as file:
    elf_sectors=(file.read().split("\n"))


#%%
example=elf_sectors[0]


#%%

#basic outline here, turn into a function 
example.split(",")

reformat=[]
for i in example.split(","):
    for a in i.split("-"):
        reformat.append(int(a))


range1="".join([str(i) for i in range(reformat[0],reformat[1]+1)])
range2="".join([str(i) for i in range(reformat[2],reformat[3]+1)])

if range1 in range2 or range2 in range1:
    print("overlap")

#%%
def getranger(ranges):
    ranges.split(",")

    reformat=[]
    for i in ranges.split(","):
        for a in i.split("-"):
            if a !="":
                reformat.append(int(a))


    range1=[i for i in range(reformat[0],reformat[1]+1)]
    range2=[i for i in range(reformat[2],reformat[3]+1)]

    lengthts=[len(range1), len(range2)]

    match=[]
    for i in range1:
        for j in range2:
            if i==j:
                match.append(i)
    
    if len(match)==min(lengthts):
        return 1
    
    return 0

getranger(elf_sectors[4])



z=sum([getranger(i) for i in elf_sectors if i !=""])

#%%

#overlap at all 

def overlap(ranges):
    ranges.split(",")

    reformat=[]
    for i in ranges.split(","):
        for a in i.split("-"):
            if a !="":
                reformat.append(int(a))


    range1=[i for i in range(reformat[0],reformat[1]+1)]
    range2=[i for i in range(reformat[2],reformat[3]+1)]

    

    match=[]
    for i in range1:
        for j in range2:
            if i==j:
                match.append(i)
    
    if len(match)>0:
        return 1,ranges
    
    return 0,ranges

[overlap(i) for i in elf_sectors if i !=""]