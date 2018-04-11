import networkx as nx
import numpy as ny
import matplotlib.pyplot as plt
import random
import pdb
pdb.set_trace()

for j in range(2,10):
    t=0
    #print "Now running -->", j
    for l in range(0,100):
        X = nx.Graph()
        m=[]
        #print "Now running -->", l
        for i in range(1000):
            X.add_node(i)
            m.append(0)
            #print "Now running -->", i
        for q in range(1000):

            while(m[q]<j):
                a=random.randint(0,1000)
                if((q,a) in X.edges() or (a,q) in X.edges()):
                    print 1
                    pass
                else:
                    X.add_edge(q,a)
                    m[q]+=1
                    m[a]+=1
                    
                print m[q]
            if nx.is_connected(X):
                t+=1
                break
        print j
    print(j,t)
