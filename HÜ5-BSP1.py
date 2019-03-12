#Hausaufgabe 5.1 (1 Punkt)
#
#Auf TUWEL finden Sie die Beispieldatei BMI.csv. Diese Datei enthält mehrere Zeilen. 
#Jede Zeile enthält den Vornamen, Geschlecht, Alter, Gewicht in kg und die Größe einer Person in cm. 
#Die einzelnen Einträge sind durch Semikolon (;) voneinander getrennt. Z.B.: Alexander;M;27;80.31;190
#
#1.) Schreiben Sie eine Funktion Read_BMI(filename), die einen Dateinamen filename übergeben bekommt. 
#Hierbei soll die Datei BMI.csv eingelesen werden. Speichern Sie den Inhalt der Datei als Dictionary, 
#welches aus Listen besteht. Verwenden Sie als Keys für das Dictionary die in der Datei enthaltenen 
#Vornamen der Personen. Als Value speichern Sie das Gewicht sowie die Größe der jeweiligen Person in 
#Form einer Liste in das Dictionary. Geschlecht und Alter sind hierbei irrelevant. 
#Wählen Sie einen jeweils sinnvollen Datentypen.
#

def Read_BMI(filename):
    fobj = open(filename, "r")
    name=[]
    weight=[]
    height=[]
    liste=[]
    dictionary = {}

    for line in fobj:

        line = line.strip()
        zuordnung = line.split(";")
        
        name.append(zuordnung[0])
        weight.append(float(zuordnung[3]))
        height.append(float(zuordnung[4]))
        
    for i in range(len(name)):
        tupel=[weight[i],height[i]]
        liste.append(tupel)
        dictionary[name[i]] = liste[i]
    print "Namen = ", name
    print "Gewicht [kg] = ", weight
    print "Groesse [cm] = ", height 
    print
    fobj.close()
    return dictionary


#Weiterhin soll eine Funktion Write_BMI geschrieben werden, welche eine Datei Ausgabe.csv erstellt. 
#In dieser sollen die Daten Vorname, Gewicht in kg, Größe in cm sowie der BMI ausgegeben werden. 
#Achten Sie hierbei darauf, dass es sich um eine .csv Datei handelt, welche als Trenner einen 
#Beistrich (,) verwendet. Eine Zeile der Ausgabedatei sollte wie folgt aussehen: Alexander,80.31,190,22.
    
def Write_BMI(dict,filename):
    fobj = open(filename, "w")                   
    for x in dict:
        fobj.write(x + ";" + str(dict[x][0])+ ";" +str(dict[x][1])+ ";"+str(dict[x][2]) + "\n")  
    fobj.close()
        
    
    

#2.) Schreiben Sie einen Code, welcher den Body Mass Index (BMI) der Personen aus 1.) berechnet.
# Der BMI berechnet sich zu: BMI = (Masse [kg]) / (Körpergröße [m])^2
#
#mit der Masse m in Kilogramm und der Körpergröße h in Metern. Der BMI ist ganzzahlig (integer). 
#Anschließend soll der berechnete BMI an das Ende der jeweiligen Liste jeder Person hinzugefügt werden.

    
if __name__ is "__main__":

    Dict = Read_BMI("BMI.csv")
    print "Dictionary:"
    print Dict
    print
    
    for x in Dict:
        Tupel=Dict[x]
        print x,": ", Tupel
        m=Tupel[0]
        h=Tupel[1]
        BMI = (m / (h/100)**2)
        print "BMI = ", BMI, "          ","BMI (auf integer gerundet) = ",int(round(BMI))
        Dict[x].append(int(round(BMI)))
        
    print
    print "Neues Dictionary mit BMI: "
    print Dict
    
    
    Write_BMI(Dict,"Ausgabe.csv")
    
    

    
    
    
    
    
    