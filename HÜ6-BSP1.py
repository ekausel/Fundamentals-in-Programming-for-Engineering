# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:12:23 2018

@author: Emanuel
"""

#Erstellen Sie eine Klasse Person mit den Attributen Vorname (string), Gewicht (float) 
#Groesse (integer) und BMI (integer). Die Attribute sollen über den Konstruktor gesetzt werden. 
#Gewicht, Groesse und BMI sollen dabei privat, waehrend der Vorname NICHT privat ist. z.B.:
#Alexander = Person("Alexander", 80.31, 190, 22)
#Schreiben Sie eine Get-Methode, über die das Gewicht der Person abgerufen werden kann. 
#Schreiben Sie eine Methode zum Setzen des Gewichts der Person. Berücksichtigen Sie das durch 
#die änderung des Gewichtes sich auch der BMI ändert. Überprüfen Sie über einen print-Befehl ob 
#sich der Wert für Gewicht auch wirklich geändert hat. z.B. für die oben definierte Person Alexander:
#Überladen Sie den print-Operator, sodass mittels print Klasseninstanz, Vorname, Gewicht, Größe und 
#BMI einer Person ausgegeben werden können, z.B.:
#Überladen Sie den größer-Operator, sodass das der BMI von 2 Personen, z.B. Alexander und Maria, 
#mittels Alexander > Maria verglichen werden kann.

class Person:
    def __init__(self,Vorname,Gewicht,Groesse,BMI):
        self.Vorname=Vorname
        self.__Gewicht=Gewicht
        self.__Groesse=Groesse
        self.__BMI=BMI
        
    def Get_Gewicht(self):
        """Schreiben Sie eine Get-Methode, über die das Gewicht 
        der Person abgerufen werden kann."""
        return self.__Gewicht
    
    def Set_Gewicht(self,Gewicht_neu):
        """Schreiben Sie eine Methode zum Setzen des Gewichts der Person."""
        self.__Gewicht=Gewicht_neu
        
    def __str__(self):
        """Überprüfen Sie über einen print-Befehl ob sich der Wert für Gewicht auch wirklich geändert hat."""
        return "%s %.2f %i %i" %(self.Vorname, self.__Gewicht, self.__Groesse, self.__BMI)
    
    def __get__(self,other):
        """Überladen Sie den größer-Operator, sodass das der BMI von 2 Personen."""

Alexander = Person("Alexander", 80.31, 190, 22)
Maria = Person("Maria", 42.1, 152, 18)

print "\nGewicht: ", Alexander.Get_Gewicht()

Alexander.Set_Gewicht(50.2)

print "Neues Gewicht: ", Alexander.Get_Gewicht(),"\n"


          
print Alexander
print Alexander > Maria