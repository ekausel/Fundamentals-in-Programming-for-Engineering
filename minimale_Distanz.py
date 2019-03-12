# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:10:46 2018

@author: Emanuel
"""



def berechne_distanz(A,B):
    distanz = ( (A[0]-B[0])**2+(A[1]-B[1])**2+(A[2]-B[2])**2 )**0.5
    return distanz
    

A = [1,2,3]
B = [2,3,4]
C = [5,2,3]
D = [1,2,4]

Punkte = [A,B,C,D]
#         0 1 2 3
Namen = ["A","B","C","D"]
"""
AB, AC, AD
    BC, BD
        CD
        
"""

def minimale_Distanz(Punkte):

    min_Distanz = berechne_distanz(Punkte[0],Punkte[1])
    min_Punkt1 = 0
    min_Punkt2 = 1
    
    Anzahl = len(Punkte)
    for index1 in range(0, Anzahl - 1):
        for index2 in range(index1 + 1, Anzahl):
            print index1, index2
            Punkt1 = Punkte[index1]
            Punkt2 = Punkte[index2]
            Distanz = berechne_distanz(Punkt1,Punkt2)
            print "Distanz= ", Distanz
            if Distanz < min_Distanz:
                min_Distanz = Distanz
                min_Punkt1 = index1
                min_Punkt2 = index2
                print "neue Distanz = ",min_Distanz
    return min_Distanz,min_Punkt1,min_Punkt2

min_Distanz,min_Punkt1,min_Punkt2 = minimale_Distanz(Punkte)
print "minimale Distanz: ",min_Distanz
print "zwischen dem Punkt ", Namen[min_Punkt1], " und ", Namen[min_Punkt2]


