# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:16:07 2018

@author: Emanuel
"""

#Erstellen Sie eine von Person abgeleitete Klasse Patient, welche neben den Attributen Vorname, 
#Gewicht, Groesse und BMI noch das zusaetzliche Attribut Patientnummer (= string) hat.
# Die Patientennummer soll NICHT als private Variable gespeichert werden! Die Attribute sollen
# in einem Konstruktor gesetzt werden. Verwenden Sie zum Initialisieren der Attribute Vorname, 
#Gewicht, Grösse und BMI den Konstruktor der Basisklasse Person! z.B.:
#Patient_Alexander = Patient("Alexander", 80.31, 190, 22, "56483L512")
#Überladen Sie für die Klasse Patient den print-Operator, so dass Vorname, Gewicht und 
#Patientennummer des Patienten ausgegeben werden. z.B.:
#print Patient_Alexander
#Alexander 80.31 56483L512

#aus 6.1

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



#6.2


class Patient(Person):
    def __init__(self,Vorname, Gewicht, Groesse,BMI,Patientennummer):
        self.Patientennummer=Patientennummer
        Person.__init__(self, Vorname, Gewicht, Groesse, BMI)
        
    def __str__(self):
        """ueberladene Print Funktion"""
        return"%s %.2f %s" %(self.Vorname, Person.Get_Gewicht(self),self.Patientennummer)
        
Patient_Alexander = Patient("Alexander", 80.31, 190, 22, "56483L512")


print Patient_Alexander



















