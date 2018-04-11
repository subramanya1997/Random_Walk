import networkx as nx
import numpy as ny
import matplotlib.pyplot as plt
import random
import pdb
pdb.set_trace()
n =[]
m =[]
k =[]
#read the file to graph
g = nx.read_adjlist("reco.txt",nodetype=int,create_using=nx.DiGraph())

#random init point
s = random.randint(1,g.order()-1)
#init the list to 0
for i in range(g.order()):
    n.append(0)
    m.append(0)

j = 0

while(100000):
    #print "S ---->", s
    p = random.randint(0,100)
    if(p<5):#90% of the time
        while(1):
            if(g.out_degree(s)==0):#if no out degree
                n[s]+=1
                s = random.randint(1,g.order()-1)
                break
            a = random.randint(1,g.order()-1)
            if((s,a) in g.edges()):
                n[s]+=1
                s=a
                break
    else:#10%of the time
        s = random.randint(1,g.order()-1)
    #print "Running --->", j
    j+=1
    if (j%5000) == 0:
        k = n
        k = sorted(range(len(k)), key=lambda i:k[i],reverse=True)
        if m == k:
            break
        else:
            m = k

#print n
for i in range(0,40):
    print i,"----->",m[i]
