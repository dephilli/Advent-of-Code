#omg this code is a mess
#TODO make it make more sense 

#%%
with open("cargo.txt")as file:
    cargo=file.read().split("\n\n")

top=cargo[0].split("\n")
bottom=cargo[1].split("\n")

top[0]

locations =[1,5,9,13,17,21,25,29,33]

cols=[]
for i in top:
    if i[1]!="":
        cols.append(i[1])
cols=",".join(cols)

def rows(location):
    cols=[]
    for i in top:
        if i[location]!=' ':
            cols.append(i[location])
    cols.reverse()
    return cols
    return ",".join(cols)

collection=[rows(i) for i in locations]

#%%
collection

#%%

move=[collection[7].pop() for i in range(0,3)]

[collection[1].append(i) for i in move]
#%%
instruct=bottom[0]

inputs=[int(instruct.split(" ")[i]) for i in range(1,6,2)]

boxes=inputs[0]
froms=inputs[1]-1
tos=inputs[2]-1

move=[collection[froms].pop() for i in range(0,boxes)]
[collection[tos].append(i) for i in move]
boxes=[]
#%%
def move_boxes(inputter):
    inputs=[int(inputter.split(" ")[i]) for i in range(1,6,2)]
    boxes=inputs[0]
    froms=inputs[1]-1
    tos=inputs[2]-1

    move=[collection[froms].pop() for i in range(0,boxes)]
    [collection[tos].append(i) for i in move]
    boxes=[]

h=0
for i in bottom:
    if i!="":
        move_boxes(i)
        h+=1

collection

#%%
colll=collection

answer=[colll[i].pop() for i in range(0,len(colll)) ]

#%%
"".join(answer)

#%%
def move_boxes_improved(inputter):
    inputs=[int(inputter.split(" ")[i]) for i in range(1,6,2)]
    boxes=inputs[0]
    froms=inputs[1]-1
    tos=inputs[2]-1

    move=[collection[froms].pop() for i in range(0,boxes)]
    move.reverse()
    [collection[tos].append(i) for i in move]
    boxes=[]

h=0
for i in bottom:
    if i!="":
        move_boxes_improved(i)
        h+=1

collection
#%%
colll=collection

answer=[colll[i].pop() for i in range(0,len(colll)) ]


"".join(answer)