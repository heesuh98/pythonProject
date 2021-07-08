GC_count = 0
G_count = 0
C_count = 0
d_DNA = dict()
head = list()
value = list()
with open("Computing_GC_Content.txt","r") as DNA:
    lines = DNA.readlines()
    for line in lines:
        if line.startswith('>'):
            line = line.strip('\n')
            line = line.strip('>')
            head.append(line)
        else:
            line = line.strip('\n')
            value.append(line)

DNA_DIC = dict(zip(head,value))

for i in value:
    GC_count= (DNA_DIC[i].count("C") + DNA_DIC)

'''
for i in range(len(head)):
    if i == 0:
        G_count0 = (DNA_DIC[head[i]]).count('G')
        C_count0 = (DNA_DIC[head[i]]).count('C')
        GC_count0 = G_count0 + C_count0
        ATGC0 = len(value[i])
        per0 = (GC_count0)/(ATGC0)

    elif i ==1:
        G_count1 = (DNA_DIC[head[i]]).count('G')
        C_count1 = (DNA_DIC[head[i]]).count('C')
        GC_count1 = G_count1 + C_count1
        ATGC1 = len(value[i])
        per1 = (GC_count1) / (ATGC1)

    elif i == 2:
        G_count2 = (DNA_DIC[head[i]]).count('G')
        C_count2 = (DNA_DIC[head[i]]).count('C')
        GC_count2 = G_count2 + C_count2
        ATGC2 = len(value[i])
        per2 = (GC_count2) / (ATGC2)
'''





