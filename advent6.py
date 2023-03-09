#%%

testrun="bvwbjplbgvbhsrlpgdmjqwftvncz"



first=testrun[0:3]

check=[]
for i in first:
    for j in first:
        if i==j:
            check.append(i)




#%%
with open("cypher.txt") as file:
    cypher=file.read()

#cypher='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

for i in range(0,4096):
    end=i+4
    test=[]
    spot=cypher[i:end]
    for i in spot:
        for j in spot:
            if i==j:
                test.append(i)
    if len(test)==4:
        print(spot,end)
        break

#%%
h=[i for i in range(0,3)]

cypher[1815]
#%%
for i in range(0,4096):
    end=i+14
    test=[]
    spot=cypher[i:end]
    for i in spot:
        for j in spot:
            if i==j:
                test.append(i)
    if len(test)==14:
        print(spot,end)
        break
#%%
cypher[2926:]