# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:17:05 2018

@author: Emanuel
"""

#Hausaufgabe 3.2 (1 Punkt)

#Gegeben ist ein String Zahl, z.B. mit dem Wert 'abf573'. Überprüfen Sie, ob es sich bei Zahl 
#um eine Zahl im Hexadecimal-System handelt, d.h. ob Zahl nur die Zahlen 0-9 und Buchstaben a-f enthält.

Zahl = "abf573"

#Definieren Sie dazu einen String mit dem Wert '0123456789abcdefABCDEF' und überprüfen Sie, 
#ob alle Zeichen in Zahl auch in diesem String enthalten sind.

String = "0123456789abcdefABCDEF"
Test = 0

print "String: ", Zahl
for x in Zahl:
    if  x in String:
        Test += 0
    else:
        Test += 1

print "Es befinden sich ", Test, " unpassende Zeichen im String." 
#Falls es sich um eine Zahl im Hexadecimal-System handelt, können Sie diese mit 
#dem Befehl int(Zahl, 16) in eine Decimal-Zahl umwandeln. Geben Sie die Decimal-Zahl aus.

if Test == 0:
    hexa= int(Zahl,16)
    print "Zahl: " , hexa
else:
    print "Zahl ist keine Hexadezimalzahl"
    
#Falls Zahl keine Hexadecimal-Zahl ist, soll False ausgegeben werden.
#Testen Sie Ihr Programm mit einigen Werten für Zahl.


#TEST1
print 
print "TEST1"
Zahl = "8347wwi4z87tz5w348975f"

String = "0123456789abcdefABCDEF"
Test = 0

print "String: ", Zahl
for x in Zahl:
    if  x in String:
        Test += 0
    else:
        Test += 1

print "Es befinden sich ", Test, " unpassende Zeichen im String." 

if Test == 0:
    hexa= int(Zahl,16)
    print "Zahl: " , hexa
else:
    print "Zahl ist keine Hexadezimalzahl"

#Test2
print 
print "TEST2"
Zahl = "343afde234cbb"

String = "0123456789abcdefABCDEF"
Test = 0

print "String: ", Zahl
for x in Zahl:
    if  x in String:
        Test += 0
    else:
        Test += 1

print "Es befinden sich ", Test, " unpassende Zeichen im String." 

if Test == 0:
    hexa= int(Zahl,16)
    print "Zahl: " , hexa
else:
    print "Zahl ist keine Hexadezimalzahl"