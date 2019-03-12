# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:39:42 2018

@author: Emanuel
"""

#Hausaufgabe 4.1 (1 Punkt)
#
# call-by-value vs. call-by-reference:
#
"""Schreiben Sie eine Funktion Bearbeitung(Dict, String) mit den Argumenten Dict (ein Dictionary)
 und String (eine Zeichenkette).
Verdoppeln Sie String in der Funktion und fügen Sie den so veränderten String mit dem 
Schlüssel doppelt in das Dictionary ein.
Geben Sie das veränderte Dictionary und den veränderten String zurück."""

def Bearbeitung(Dict,String):
    String*=2
    Dict['doppelt'] = String
    print "In der Funktion: ", Dict, String
    
    return Dict, String

"""Rufen Sie Ihre Funktion im Hauptprogramm auf, z.B. mit den folgenden Werten:
Dict_main = {"Buch" : 0.2, "Kekse" : 0.3}
string_main = "Buch"
Überprüfen Sie mittels Ausgaben im Hauptprogramm und der Funktion, ob sich Dict 
bzw. String im Hauptprogramm bzw. der Funktion verändert haben."""

if __name__ == '__main__':
    Dict_main = {"Buch" : 0.2, "Kekse" : 0.3}
    string_main = "Buch"
    print "Vor dem Aufruf: ",Dict_main,string_main
    Dict_return, string_return = Bearbeitung(Dict_main, string_main)
    print "Zurueck gegeben: ", Dict_return, string_return
    # 4)
    print "Nach Aufruf in main: ", Dict_main, string_main
    
    
""""Beantworten Sie die folgenden Fragen als Kommentar in Ihrem Skript: 
Sind Dictionaries bzw. Strings daher veränderlich oder unveränderliche Datentypen? 
In welchem Fall wird einer Funktion daher nur der Wert (also call-by-value) und 
wann das ganze Objekt (also call-by-reference) übergeben?"""
#Antwort:
'''
String des Hauptprogramms bleibt gleich (strings sind unveraenderlich)
strings werden ueber call-by-value an Funktion uebergeben

Dict des Hauptprogramms hat sich geändert,(Dictionaries sind veraenderlich) 
Dictionaries werden ueber call-by-reference an Funktion uebergeben
'''


"""Verwenden Sie Ihre bisherige Funktion um eine neue Funktion Bearbeitung_Kopie zu schreiben.
 Diese neue Funktion soll das selbe tun wie die Funktion Bearbeitung, aber dabei 
 das Dictionary und den String nicht verändern!
Hinweis Legen Sie, bevor Sie Punkt (1) ausführen eine Kopie des Dictionaries an.
 Das geht z.B. mit der Dictionary-Methode copy. 
Überprüfen Sie, dass Ihre Funktion das Dictionary des Hauptprogramms nicht verändert."""


print "\n"

def Bearbeitung_Kopie(Dict, String): 
    neues_Dict = Dict.copy()
    neues_Dict['doppelt'] = String
    print "In der Funktion: ", neues_Dict, String
    return neues_Dict, String


if __name__ == '__main__':
    Dict_main = {"Buch" : 0.2, "Kekse" : 0.3}
    string_main = "Buch"
    print "Vor dem Aufruf: ", Dict_main, string_main
    (Dict_return, string_return) = Bearbeitung_Kopie(Dict_main, string_main)
    print "Zurueck gegeben: ", Dict_return, string_return
    print "Nach Aufruf in main: ", Dict_main, string_main