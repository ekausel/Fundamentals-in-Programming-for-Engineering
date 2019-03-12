# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:22:37 2018

@author: Emanuel
"""

#Hausaufgabe 3.1 (1 Punkt)
#
#Gegeben ist ein Dictionary Briefe mit z.B. folgendem Inhalt: 
#    '163' : 4.2, '175' : 20.01, '214' : 15.5, '159' : 21.2. 
#Die Schlüssel sind Strings und geben den Identifikationscode jeweils eines Briefes an. 
#Der entsprechende Wert ist das Gewicht des Briefes in Gramm. 
#Ab einem Gewicht von 20 g wird ein höherer Betrag für die Zustellung verlangt.

Briefe = {'163' : 4.2, '175' : 20.01, '214' : 15.5, '159' : 21.2}

#Erstellen Sie zwei Listen, schwerer und leichter, die jeweils die Identifikationsnummern 
#der Briefe enthalten, die schwerer bzw. leichter als 20 g sind.

schwerer = []
leichter = []

for x in Briefe:
    if Briefe[x] > 20 :
        schwerer.append(x)
    else:
        leichter.append(x)

print "leichter als 20 Gramm = ",leichter
print "schwerer als 20 Gramm = ",schwerer
            
    





#Testen Sie Ihren Code an Dictionaries mit unterschiedlichem Inhalt und Länge.

#TEST1
print "TEST1"
Briefe = {'163' : 4.42, '234' : 33.7, '175' : 2.01, '898' : 23.7, '214' : 15.5, '159' : 21.2}


schwerer = []
leichter = []

for x in Briefe:
    if Briefe[x] > 20 :
        schwerer.append(x)
    else:
        leichter.append(x)

print "leichter als 20 Gramm = ",leichter
print "schwerer als 20 Gramm = ",schwerer


