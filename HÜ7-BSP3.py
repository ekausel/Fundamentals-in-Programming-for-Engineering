# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:28:37 2018

@author: Emanuel
"""

#Hausaufgabe 7.3 (1 Punkt)
#
#Verwenden Sie das Modul doctest um Ihre Klasse Person (aus Hausaufgabe 6.1) zu testen. 
#Schreiben Sie für alle Methoden (also Konstruktor, print-Operator, set_Gewicht und 
#get_Gewicht und größer-Operator) jeweils mindestens einen Test. Rufen Sie die Tests 
#im Hauptprogramm auf. Beachten Sie hierbei das es nicht einfach möglich ist die 
#privaten Anteile des Konstruktors zu testen. Beschränken Sie sich also daher auf den Vornamen.

class Person:

   def __init__(self, Vorname, Gewicht, Groesse, BMI):
      """
      >>> Emanuel=Person("Emanuel",88,190,24)
      
      """
      self.vorname = Vorname
      self.__gewicht = Gewicht
      self.__groesse = Groesse
      self.__bmi = BMI

   def get_Gewicht(self):
      """
      >>> Franz.get_Gewicht()
      85.33
      """
      return self.__gewicht
      
   def set_Gewicht(self, neues_Gewicht):
      """
      >>> Helmut.set_Gewicht(105)
      
      """
      self.__gewicht = neues_Gewicht   
      self.__bmi = int(self.__gewicht / (self.__groesse * 0.01)**2)
      
       
   def __str__(self): 
       """
       >>> Franz.__str__()
       'Franz 85.33 187 24'
       """
       return "%s %3.2f %i %i" % (self.vorname, self.__gewicht, self.__groesse, self.__bmi) 
      
   def __lt__(self, other):
       """
       >>> Franz.__lt__(Herbert)
       True
       """
       return self.__bmi < other.__bmi

if __name__ == '__main__':
   Franz = Person("Franz",85.33,187,24)
   Herbert = Person("Herbert",102,195,27)
   Helmut = Person("Helmut",67.8,171,23)
   import doctest 
   doctest.testmod(verbose=True)
    
