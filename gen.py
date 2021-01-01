import numpy as np
from numpy.random import randint as rndi
from numpy.random import random as rnd

nodelen=0.4
nodeoverlay=0.1
nodevelocity=100
minpitch=50
maxpitch=70
nodenum=10
setsize=4#8
setnum=3
setrep=5
set2size=4#8
set2num=3
set2rep=5
set3size=4#8
set3num=3
set3rep=8

lens=[0.2,0.3,0.4,0.5]



posn=["q","w","e","r","t","y","u","i","o","p","z","x","c","v","b","n","m",",",".","/"]
minpitch=0
maxpitch=len(posn)-1
nodenum=maxpitch



nodes=[int(x) for x in np.arange(minpitch,maxpitch*1.001,(maxpitch-minpitch)/nodenum)]

nnodes=[]

for zw in [[[node,le] for le in lens] for node in nodes]:
  for zx in zw:
    nnodes.append(zx)
nodes=nnodes

# print(nodes)
# exit()

nodes=[{"inn":x,"out":x,"q":x,"multi":False,"p":1} for x in nodes]

# print(nodes)
# exit()

def diff(a,b):
  return [aa-bb for aa,bb in zip(a,b)]

def probabl(inn,out):
  # print("calcing",inn,out)
  # exit()
  if inn["inn"]==out["out"]:return 1
  if inn["q"][0]==out["q"][0]:return 1
  return 100.0/np.sqrt(np.sum(np.abs(diff(inn["inn"],out["out"]))))

def setprobs(nodes,before):
  for i in range(len(nodes)):
    nodes[i]["p"]=probabl(before,nodes[i])
  return nodes

def dice(nodes):
  # return nodes[rndi(len(nodes))]#enable pure random
  # print("dicing",nodes)
  # exit()
  cou=np.sum([x["p"] for x in nodes])
  roll=rnd()*cou
  for n in nodes:
    if roll<n["p"]:
      return n
      # print("resulting in",n)
      # exit()
    roll-=n["p"]
  return nodes[rndi(len(nodes))]

def flatten(q):
  ret=[]
  for ac in q:
    if ac["multi"]:
      for sq in ac["q"]:ret.append(sq)
    else:
      ret.append(ac["q"])
  return ret

def daddy(q):
  return {"inn":q[0],"out":q[-1],"q":q,"multi":True,"p":1}

def genset(nodes,n=8):
  rel=[]
  ac=nodes[rndi(len(nodes))]
  rel.append(ac)
  for i in range(n-1):
    nodes=setprobs(nodes,ac)
    ac=dice(nodes)
    rel.append(ac)
  return daddy(flatten(rel))
  


sets=[genset(nodes,n=setsize) for i in range(setnum)]
sets2=[genset(sets,n=setrep) for i in range(set2num)]
sets3=[genset(sets,n=set2rep) for i in range(set3num)]


# print(np.array(sets).shape)
# print(np.array(sets2).shape)
# print(np.array(sets3).shape)

# print(sets2)

# exit()


q=[]
# for n in nodes:q.append(n)
q=genset(sets2,n=set3rep)["q"]
# q=genset(sets3,n=set3rep)["q"]





print("generated",q)