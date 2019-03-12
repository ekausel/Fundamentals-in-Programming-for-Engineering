# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:08:54 2018

@author: Emanuel
"""

"""
ANGABE:
Erstellen Sie eine Variable Bytes und weisen Sie ihr eine beliebige positive Integer-Zahl zu.
Bytes gibt die Anzahl an verfügbaren Bytes an. Was ist die größte Integerzahl,
die in dieser Anzahl an Bytes abgespeichert werden kann? (Gehen Sie davon aus,
dass kein Vorzeichen mitgespeichert wird, d.h. es handelt sich um einen unsigned integer!).

Bestimmen Sie mittels eines kurzen Python-Skripts die größte Integerzahl in Abhängigkeit
von der Variable Bytes und geben Sie diese auf der Konsole aus. Testen Sie Ihr Skript mit
verschieden Werten für Bytes.
"""

Bytes = 1

# 1 Byte besteht aus 8 Bit, welche jeweils den Zustand 0 oder 1 haben können.
# 1 Byte hat also 2^8=256 verschiedene Möglichkeiten aus Nullen und Einsern zusammengesetzt zu sein
# Die größte Integerzahl die in 1 Byte abgespeichert werden kann, ist daher 255!
# Da man die Null nicht vergessen darf.

"""PROGRAMM"""

Bytes = input("Wie viele Bytes haben Sie zur Verfuegung..? ")

Ergebnis = 2**(8*int(Bytes))-1

print ("Mit der gewaehlten Anzahl an Bytes, ist die groeßtmoegliche Integer-Zahl: ")
print (Ergebnis)