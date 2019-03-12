# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:36:02 2018

@author: Emanuel
"""

"""
ANGABE:
    
    Gegeben ist folgende Berechnungsvorschrift für x:

     x = a*((1-(y/b)**2)**0.5)
     
       1 Erzeugen Sie ein Python Skript mit beliebigem Namen mittels Spyder.
       2 Definieren Sie zwei Variablen a und b mit den Werten 2 und 3
       3 Definieren Sie eine Variable y mit dem Wert 3
       4 Berechnen Sie den Wert von x für y = 3
       5 Geben Sie das Ergebnis aus 4) in der folgenden Form aus: x = ..., y = .... 
           Setzen Sie dabei für die Punkte Ihr Ergebnis aus 4) und den Wert für y ein.
       6 Wiederholen Sie die Punkte 3), 4) und 5) für y = 1 und y = 1. 
          (Beachten Sie den Punkt hinter 1!).
       7 Beantworten Sie die folgenden Fragen als Kommentar in Ihrem Skript: 
           Wieso unterscheiden sich die Ergebnisse für x für y = 1 und y = 1.? 
           Welches Ergebnis ist mathematisch richtig?

"""

"""PROGRAMM"""

a = 2
b = 3

#für y=3
y = 3

x = a*((1-(y/b)**2)**0.5)

print "x =", x, ",", "y =", y

#für y=1
y = 1

x = a*((1-(y/b)**2)**0.5)

print "x =", x, ",", "y =", y

#für y=1.
y = 1.

x = a*((1-(y/b)**2)**0.5)

print "x =", x, ",", "y =", y

"""Fragen beantworten"""

print "Die Ergebnisse unterscheiden sich, weil y=1 ganzzahlig (Integer) rechnet und y=1. mit Gleit-Komma-Darstellung (Float). Mathematisch richtig ist natürlich das Ergebnis mit Nach-Komma-Stellen (Float)"

