# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:52:07 2018

@author: Emanuel
"""

"""
Hausaufgabe 2.2 (1 Punkt)
"""
#Volumen eines Ellipsoids:

#   1) Definieren Sie eine Liste, die 3 strings enthält: "a = 4.12", "b = 13.2" und "c=4.25". 
#   a, b und c sind die Halbachsen eines Ellipsoids.
#   2) Extrahieren Sie die Werte für die Halbachsen aus den Strings. 
#    Verwenden Sie dazu die erstellte Liste. 
#   Achtung: Die Strings können beliebig viele zusätzliche Leerzeichen enthalten!
#   3) Berechnen Sie das Volumen des Ellipsoids. (Verwenden Sie für {\pi} den Wert 3.1415.)
#   4) Erstellen Sie ein Dictionary Ellipsoid, dass die Hauptachsen des Ellipsoids enthält. 
#    Dabei soll als Schlüssel der Name als string (z.B. a) und als Wert der Wert als 
#    Gleitkommazahl verwendet werden.
#   5) Testen Sie Ihr Programm mit verschiedenen Anfangslisten (die verschiedene Werte 
#    für die Halbachsen und verschieden viele Leerzeichen an beliebiger Stelle enthalten). 
#    Definieren Sie dazu Strings mit integer-Zahlen bzw. float-Zahlen verschiedener Längen. 
#    Geben Sie in Ihrem Skript an, welche Anfangslisten Sie getestet haben!


#1 Liste erstellen
str1="a = 4.12"
str2="b = 13.2"
str3="c=4.25"
Liste=[str1,str2,str3]
print "Liste: " , Liste

#2 Werte exrahieren
str_a=Liste[0]
str_b=Liste[1]
str_c=Liste[2]

Liste_a=str_a.split("=")
Liste_b=str_b.split("=")
Liste_c=str_c.split("=")

Wert_a=Liste_a[1]
Wert_b=Liste_b[1]
Wert_c=Liste_c[1]

a=float(Wert_a)
b=float(Wert_b)
c=float(Wert_c)

print "Halbachsen (a,b,c) des Ellipsoids: "
print "a = ", a , ",    Typ = ", type(a)
print "b = ", b , ",    Typ = ", type(b)
print "c = ", c , ",    Typ = ", type(c)

#3 Volumen berechnen
pi=3.1415
Volumen=(4/3)*pi*a*b*c
print "Volumen vom Ellipsoid mit den Halbachsen a,b,c:"
print "Volumen = ",Volumen

#4 Dictionary erstellen
Ellipsoid={"a": a, "b": b, "c": c}
print Ellipsoid








#5 Testen1
print "TEST1"
str1="a =   33"
str2="b =3.32"
str3="c  =4.99"
Liste=[str1,str2,str3]
print "Liste: " , Liste

str_a=Liste[0]
str_b=Liste[1]
str_c=Liste[2]

Liste_a=str_a.split("=")
Liste_b=str_b.split("=")
Liste_c=str_c.split("=")

Wert_a=Liste_a[1]
Wert_b=Liste_b[1]
Wert_c=Liste_c[1]

a=float(Wert_a)
b=float(Wert_b)
c=float(Wert_c)

print "Halbachsen (a,b,c) des Ellipsoids: "
print "a = ", a , ",    Typ = ", type(a)
print "b = ", b , ",    Typ = ", type(b)
print "c = ", c , ",    Typ = ", type(c)

pi=3.1415
Volumen=(4/3)*pi*a*b*c
print "Volumen vom Ellipsoid mit den Halbachsen a,b,c:"
print "Volumen = ",Volumen

Ellipsoid={"a": a, "b": b, "c": c}
print Ellipsoid

#5 Testen2
print "TEST2"
str1="a    =  9"
str2="b =  23.68"
str3="c  =77.431"
Liste=[str1,str2,str3]
print "Liste: " , Liste

str_a=Liste[0]
str_b=Liste[1]
str_c=Liste[2]

Liste_a=str_a.split("=")
Liste_b=str_b.split("=")
Liste_c=str_c.split("=")

Wert_a=Liste_a[1]
Wert_b=Liste_b[1]
Wert_c=Liste_c[1]

a=float(Wert_a)
b=float(Wert_b)
c=float(Wert_c)

print "Halbachsen (a,b,c) des Ellipsoids: "
print "a = ", a , ",    Typ = ", type(a)
print "b = ", b , ",    Typ = ", type(b)
print "c = ", c , ",    Typ = ", type(c)

pi=3.1415
Volumen=(4/3)*pi*a*b*c
print "Volumen vom Ellipsoid mit den Halbachsen a,b,c:"
print "Volumen = ",Volumen

Ellipsoid={"a": a, "b": b, "c": c}
print Ellipsoid
