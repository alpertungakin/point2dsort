# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import geopandas as gpd
import numpy as np
from matplotlib import pyplot as plt
from tkinter.filedialog import askopenfilename as ask

def setPoints():
    girdi = []
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    girdi.append(plt.ginput(0,0))
    plt.show()
    girdi = np.array(girdi)
    girdi = girdi.reshape((len(girdi[0]), 2))
    return girdi

def defineQuadrants(x):
    c1 = np.array([np.min(x[:,0]),np.min(x[:,1])])
    c2 = np.array([np.min(x[:,0]),np.max(x[:,1])])
    c12 = np.array([(c1[0]+c2[0])/2,(c1[1]+c2[1])/2])
    c3 = np.array([np.max(x[:,0]),np.max(x[:,1])])
    c23 = np.array([(c2[0]+c3[0])/2,(c2[1]+c3[1])/2])
    c4 = np.array([np.max(x[:,0]),np.min(x[:,1])])
    c34 = np.array([(c3[0]+c4[0])/2,(c3[1]+c4[1])/2])
    c41 = np.array([(c4[0]+c1[0])/2,(c4[1]+c1[1])/2])
    cM = np.array([np.min(x[:,0])+(np.max(x[:,0])-np.min(x[:,0]))/2,np.min(x[:,1])+(np.max(x[:,1])-np.min(x[:,1]))/2])
    box1 = np.array([c1,c12,cM,c41])
    box2 = np.array([c12,c2,c23,cM])
    box3 = np.array([cM,c23,c3,c34])
    box4 = np.array([c41,cM,c34,c4])
    return [box1,box2,box3,box4]

def pinBox(x, box):
    limXMax = np.max(box[:,0])
    limXMin = np.min(box[:,0])
    limYMax = np.max(box[:,1])
    limYMin = np.min(box[:,1])
    if (x[0]<=limXMax and x[0]>=limXMin and x[1]<=limYMax and x[1]>=limYMin):
        return True
    else:
        return False
    
def pointsDivider(x):
    temp = {}
    Quads = defineQuadrants(x)
    for i in range(len(Quads)):
        temp["{}".format(i)] = []
        for point in x:
            if pinBox(point, Quads[i])==True:
                temp["{}".format(i)].append(point)
            else:   
                continue
        temp["{}".format(i)] = np.array(temp["{}".format(i)])
    return temp

def subDivider(t):
    keylist = list(t.keys())
    for i in range(len(t)):
        temp_input = np.copy(t["{}".format(keylist[i])])
        Quad = initQuads[i]
        ####
        subQuad = defineQuadrants(Quad)
        if len(t["{}".format(i)])>1:
            for j in range(len(subQuad)):
                t["{}{}".format(keylist[i], j)] = []
                for q in subQuad:
                    plt.scatter(q[:,0], q[:,1], color = "blue")
                for tinput in temp_input:
                    if pinBox(tinput, subQuad[j])==True:
                        t["{}{}".format(i, j)].append(tinput)
                    else:
                        continue
        else:
            continue
    return t

def sortByKeys(x):
    keysToRem = []
    for element in x:
        if len(x["{}".format(element)])>1 or len(x["{}".format(element)])==0:
            keysToRem.append("{}".format(element))
    for key in keysToRem:
        x.pop(key)
    
def saveShape(x):
    return True    

if __name__ ==  "__main__":
    # points = np.array([[0,0],[0.5,1],[2,0],[2,3],[3,2.75],[2.75,0]])    
    points = setPoints()
    plt.scatter(points[:,0],points[:,1], color = "green")
    initQuads = defineQuadrants(points)
    t = pointsDivider(points)
    t = subDivider(t)
    sortByKeys(t)


    
