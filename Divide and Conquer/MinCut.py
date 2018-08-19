#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:42:17 2018

@author: Das
"""

import random
import copy

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}
        
    def addNeighbor(self, neighbor, weight=0):
        self.connections[neighbor] = weight
        
    def getConnections(self):
        return list(self.connections.keys())
    
    def getId(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.connections[neighbor]

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0
        self.edgesList = []
        
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex
    
    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertexList
    
    def addEdge(self, source, dest, weight=0):
        if source not in self.vertexList:
            self.addVertex(source)
        if dest not in self.vertexList:
            self.addVertex(dest)
        #self.vertexList[source].addNeighbor(self.vertexList[dest], weight)
        if (source, dest) not in self.edgesList and (dest, source) not in self.edgesList:
            self.edgesList.append((source, dest))
        
    def getEdges(self):
        return self.edgesList
        
    def getVertices(self):
        return self.vertexList
    
def contract(g):
    v = g.numVertices
    while v > 2:
        edgeIndex = random.choice(range(0, len(g.edgesList)-1))
        head, foot = g.getEdges()[edgeIndex]
        del g.vertexList[foot]
        v -= 1
        g.edgesList.remove((head, foot))
        for i in range(0, len(g.edgesList)-1):
            (h, f) = g.edgesList[i]
            if f == foot:
                g.edgesList[i] = (h, head)
            elif h == foot:
                g.edgesList[i] = (head, f)
        selfEdges = []
        for i in range(0, len(g.edgesList)):
            (h, f) = g.edgesList[i]
            if (h == f):
                selfEdges.append((h, f))
        for i in range(0, len(selfEdges)):
            if selfEdges[i] in g.edgesList:
                g.edgesList.remove(selfEdges[i])
    return len(g.edgesList)
    
graph = Graph()
with open('kargerMinCut.txt', 'r') as f:
    for i in range(1, 201):
        graph.addVertex(i)
    for line in f:
        r = (list(map(int, line.split())))
        for i in range(1, len(r)):
            graph.addEdge(r[0], r[i])
            
edges = graph.getEdges()
n = graph.numVertices
minCuts = []
for repeats in range(n):
    g = copy.deepcopy(graph)
    minCuts.append(contract(g))
print(min(minCuts))