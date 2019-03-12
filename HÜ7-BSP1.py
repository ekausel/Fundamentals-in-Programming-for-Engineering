# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 14:35:24 2018

@author: Emanuel
"""

#Hausaufgabe 7.1 (1 Punkt)
#
#Ziel ist es die Funktion Read_BMI (aus Hausaufgabe 5.1, siehe Kapitel 7) mit der 
#Klasse Person (aus Hausaufgabe 6.1) zu kombinieren.
#
#Als ersten Schritt importieren Sie hierfuer die Loesungen fuer Hausaufgaben 5.1 und 6.1 von TUWEL 
#in Ihr Skript (siehe Kapitel 6). Anschließend soll eine Datei (Format wie aus Hausaufgabe 5.1), 
#die Informationen zu Personen enthält eingelesen werden. Die Informationen aller Personen sollen 
#als Instanzen der Klasse Person in einer Liste Personen_Liste gespeichert werden. D.h. als Datenstruktur 
#wird hier eine Liste von Klassen-Objekten gewählt.
#
#Ermitteln Sie das Minimum von Personen_Liste, das heißt die Person mit dem niedrigsten BMI, 
#und geben Sie die Person per print Befehl aus. Verwenden Sie zum Testen des Codes die Datei BMI.csv aus TUWEL.

#HÜ6.1
    
class Person:

   def __init__(self, Vorname, Gewicht, Groesse, BMI):
      self.vorname = Vorname
      self.__gewicht = Gewicht
      self.__groesse = Groesse
      self.__bmi = BMI

   def get_Gewicht(self):
      return self.__gewicht
   
   def get_BMI(self):
       return self.__bmi
      
   def set_Gewicht(self, neues_Gewicht):
      self.__gewicht = neues_Gewicht   
      self.__BMI = float(self.__gewicht / (self.__groesse * 0.01)**2)
      
   def __str__(self): 
       return "%s %3.2f %i %3.2f" % (self.vorname, self.__gewicht, self.__groesse, self.__bmi) 
      
   def __lt__(self, other):
       return self.__bmi < other.__bmi
           

def Read_BMI(filename):
        
    infile = open(filename, 'r')
    Personen_Liste = []
    
    for line in infile:
        liste = line.split(';')
        Vorname = liste[0].strip()
        Gewicht = float(liste[3])
        Groesse = float(liste[4])
        BMI = float((Gewicht/((Groesse/100.)**2.)))
        Objekt =  Person(Vorname, Gewicht, Groesse, BMI)
        Personen_Liste.append(Objekt)
            
    infile.close()
    return Personen_Liste



if __name__ == "__main__":
    
    Personen_Liste=Read_BMI("BMI.csv")
    print "Liste aus Instanzen der Klasse <Person> :\n"
    print Personen_Liste
    print
    print "Objekte in der Liste:\n"
    for x in Personen_Liste:
        print x
    print
    
    Minimum = Personen_Liste[0].get_BMI
    a=0
    for i in range(len(Personen_Liste)):
        
        if (Personen_Liste[i].get_BMI<Minimum):
            Minimum = Personen_Liste[i].get_BMI
            a=i
    print "Minimum (BMI): ", Personen_Liste[a]
        
        
