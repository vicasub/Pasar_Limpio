import pandas as pd

listAss=['Algebra','Calcul1','MecFon','Quim1','Info1',
     'Geom','Calcul2','TermoFon','Quim2','Expre']

Ass={'Algebra':240011,'Calcul1':240012,'MecFon':240013,'Quim1':240014,'Info1':240015,
     'Geom':240021,'Calcul2':240022,'TermoFon':240023,'Quim2':240024,'Expre':240025}

fnotas = pd.read_csv('notas.csv') #31126 notas
fpers = pd.read_csv('personassinrep.csv') #2580 people

lCODEX=[]
for c in fpers.CODEX:
    lCODEX.append(c)

def dameconv(ass,curs,quatri): #ass name of the subject, curs is a number ej:2015, quatri is either 1 or 2
    fnotas = pd.read_csv('notas.csv')
    fpers  = pd.read_csv('personassinrep.csv')
    df=fnotas[(fnotas.CODASS==Ass[ass]) & (fnotas.CURS==curs) & (fnotas.Q==quatri)]
    return df

def nsus(c): #returns the number of fails
    df=fnotas[fnotas.CODEX==c]
    s=0
    for i in range(len(df)):
        if list(df[i:i+1].APR)[0]=='N':s+=1
    return s

def grupos(): #return dr, dr[n=number of fails]=DataFrame of people who fail n times
    d={}
    m=0
    for c in lCODEX:
        n=nsus(c)
        if n>m:
            m=n
        if n not in d:
            d[n]=[c]
        else:
            d[n]+=[c]
    dr={}
    for n in d:
        dr[n]=fpers[fpers.CODEX==int(d[n][0])]
        for i in range(1,len(d[n])):
            dr[n]=dr[n].append(fpers[fpers.CODEX==int(d[n][i])],ignore_index=True) #this takes A LOT OF time
    return dr

def comp(c): #for a given expedient returns list of subjects where compensation was applied 
    df=fnotas[fnotas.CODEX==c]
    lista=[]
    for i in range(len(df)):
        if list(df[i:i+1].NF)[0]!=list(df[i:i+1].NC)[0]:
            lista.append(int(df[i:i+1].CODASS))
    return lista
        
def todoscomp(): #returns a dict
    dcomp={}
    for c in lCODEX:
        dcomp[c]=comp(c)
    return dcomp

