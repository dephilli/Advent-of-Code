#%%
#maybe i'll find an easier one and come back to this one
test='''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

#%%
current_directory=""

input1=test.split("\n")[0]

for i in test.split("\n"):
    if i[0:4]=="$ cd":
        action=i.split(" ")[2]
        print (action)
        if action !=".." or action !="/":
            current_directory+="/"+action
        if action =="..":
            current_directory.replace("/"+a)

