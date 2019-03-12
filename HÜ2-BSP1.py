# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:09:35 2018

@author: Emanuel
"""

""" 
Hausaufgabe 2.1 (1 Punkt)

Gegeben ist eine Liste Preise mit den Einträgen 1.50, 0.99, 12.40, 0.99, 15.25

Schreiben Sie Code, der die folgenden Punkte löst und lassen Sie sich zu jedem 
Punkt eine kurze Ausgabe mit erklärendem Text ausgeben.

1 Finden Sie heraus ob sich die Zahl 0.99 in der Liste befindet.
2 Wenn ja, wie oft ist die Zahl 0.99 in der Liste enthalten?
3  Finden Sie alle Positionen, an denen sich 0.99 in der Liste befindet.
Kontrollieren Sie, dass Sie die richtigen Stellen gefunden haben, 
indem Sie die Liste an diesen Positionen auslesen.
4  Entfernen Sie alle Vorkommen von 0.99 aus der Liste.
5 Hängen Sie die Zeichenkette leer an die Liste an.
6 Bestimmen Sie die aktuelle Länge der Liste.
7 Multiplizieren Sie die Liste mit 2 und überprüfen Sie das Ergebnis mittels print.
8 Multiplizieren Sie jedes Element der Liste mit 2.
9 Erstellen Sie eine neue Liste Produkte mit beliebigen Einträgen. 
Addieren Sie die Listen Preise und Produkte.
10 Erstellen Sie eine neue Liste Lager, die die Liste Preise als 0. Element und 
die Liste Produkte als 1. Element enthält. D.h. Lager ist eine Liste, die Listen enthält.
11 Erstellen Sie eine explizite Kopie von Lager.
12 Schreiben Sie mindestens 2 Tests um zu überprüfen, dass eine Veränderung 
an der Kopie die ursprüngliche Liste Lager tatsächlich nicht verändert.
"""

Preise = [1.50, 0.99, 12.40, 0.99, 15.25]

print ("Unsere Liste:")
print (Preise)

print ("Befindet sich 0.99 in der Liste?")
print (0.99 in Preise)         #Punkt1

print ("Wie oft?")
print (Preise.count(0.99))     #Punkt2

print ("An welchen Stellen?")  #punkt3
print (Preise.index(0.99,0,5))
print (Preise.index(0.99,2,5))
print ("Was befindet sich an diesen Stellen? (Probe)")
print (Preise[1])
print (Preise[3])

print ("Entferne alle Vorkommen von 0.99")
Preise.pop(1)                                      #punkt4
Preise.remove(0.99)

print ("\"leer\" an die Liste hängen")       #punkt5
Preise.append("leer")
print ("Neue Liste:")
print (Preise)

print("Wie lang ist die Liste jetzt?")          #punkt6
print(len(Preise))

print("Liste mal 2:")
print (2*Preise)                               #punkt7

print ("Elemente der Liste mal 2:")  
Preise_doppelt=[2*Preise[0],2*Preise[1],2*Preise[2], 2*Preise[3]]    #punkt8
print (Preise_doppelt)

print("Neue Liste:" )
Produkte=["Nudeln", "Reis", "Kartoffeln"]   
print(Produkte)                                #punkt9
print("Neue plus alte Liste")
print(Preise+Produkte)

print("beide listen in einer Liste")        #punkt10
Lager =[Preise,Produkte]
print (Lager)

Explizite_Kopie = Lager [:]              #punkt11
print("Explizite Kopie davon:")
print(Explizite_Kopie)

print("Änderungen an der ursprünglichen Liste ändern nix an der expliziten Kopie") #punkt12
Lager.append("Test")
print(Lager)
print(Explizite_Kopie)
Lager.pop(1)
print(Lager)
print(Explizite_Kopie)



