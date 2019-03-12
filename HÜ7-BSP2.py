# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:50:02 2018

@author: Emanuel
"""
#Hausaufgabe 7.2 (1 Punkt)
#
#Schreiben Sie basierend auf der Funktion Read_BMI (aus Hausaufgabe 5.1) eine neue Funktion Read_BMI_check. 
#Diese Methode soll das selbe machen wie die Methode Read_BMI, aber zusätzlich überprüfen ob die Information 
#in der übergebenen Datei das richtige Format hat. Es sollen nur Personen gespeichert werden, die Angaben im 
#korrekten Format gemacht haben.
#
#Fangen Sie dazu die folgenden typischen Fehler mit Hilfe von try-except-else Blöcken ab:
#
#    Das File könnte z.B. nicht existieren.
#    Das File könnte in einer Zeile falsche Trennzeichen, z.B. Beistriche (,) statt Strichpunkten (;) enthalten 
#bzw. eine falsche Anzahl an Angaben enthalten. Siehe z.B. die Testdatei BMI_fehlerhaft_v1.csv auf TUWEL.
#    Das File könnte als Groesse etwas enthalten, das sich nicht zu einem Integer oder Float konvertieren lässt. 
#Siehe z.B. die Testdatei BMI_fehlerhaft_v2.csv auf TUWEL.
#
#Geben Sie eine hilfreiche Fehlermeldung aus, wenn ein Fehler aufgetreten ist!




def Read_BMI_check(filename):
       
    try:
        infile = open(filename, 'r')
    except IOError:
        print "file: >",filename,"< wurde nicht gefunden!"
    else:
        
            Personen = {}
            for line in infile:
                try:
                    liste = line.split(';')    
                    Vorname = liste[0].strip()
                    Gewicht = float(liste[3])
                    Groesse = float(liste[4])
                except IndexError:
                    print line,"Bitte verwenden Sie ausschließlich Strichpunkte als Trennzeichen!\n"
                except ValueError:
                    print line,"Konversion zu float nicht moeglich!\n"
                else:
                    Personen[Vorname] = [Gewicht, Groesse]
            
            infile.close()     
            return Personen



if __name__ == '__main__':
    P1 = Read_BMI_check('nichtvorhanden.csv')
    print
    #P2 = Read_BMI_check('BMI_fehlerhaft_v1.csv')
    print
    #P3 = Read_BMI_check('BMI_fehlerhaft_v2.csv')
    print
    P4 = Read_BMI_check('BMI_fehlerhaft.csv')
    print P4