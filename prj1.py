import networkx as nx
import numpy as ny
import matplotlib.pyplot as plt
import random
import pdb
pdb.set_trace()
z = []
d = []
c = []
trials=100
vert=[5,10,15,20,25,30,35,40,45,50]
for v in vert:#number of edges
    d.append(v)
    print "Now running -->", v
    for b in range(trials):
        X=nx.Graph()
        for i in range(v):
            X.add_node(i)

        for j in range(25000):
            X.add_edge(random.randint(0,v),random.randint(0,v))
            if nx.is_connected(X):
                break

        z.append(X.size())
    c.append(ny.mean(z))
print(c)
plt.plot(d,c)
plt.show()
