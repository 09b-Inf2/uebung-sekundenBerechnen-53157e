# Berechne die Gesamtanzahl von Sekunden anhand gegebener Stunden, Minuten und Sekunden.

# Die nächste Zeile nicht verändern!
def sekundenBerechnen():
    
###################################################
# Frage hier die Stunden, die Minuten sowie die Sekunden ab und wandle den string in einen integer um. Weise den Wert jeweils einer Variable zu. Zwei Variablen fehlen noch!!
    stunden = int(input("Stunden?"))
    



###################################################
# Formel zur Umwandlung con Stunden, Minuten, Sekunden in Sekunden
# Du sollttest deinen code unter dieser Zeile einfügen. Das Ergebnis der Rechnung wird der Variable total_sekunden zugewiesen. ACHTE AUF DIE INDENTIERUNG!

    

####################################################
# output
# Hier wird das Ergebnis in der gewünschten Form ausgegeben.
    print(stunden, "Stunden,", minuten, "Minuten und", sekunden, "Sekunden sind insgesamt", total_sekunden, "Sekunden.") 
    

###################################################

# Die nächste Zeile nicht verändern
    return str(stunden) + " Stunden, " + str(minuten) + " Minuten und " + str(sekunden) + " Sekunden sind insgesamt " + str(total_sekunden) + " Sekunden"

# Erwarterter output (Beispiel)
# Für 7 Stunden, 21 Minuten und 37 Sekunden sollte dein output folgendermaßen aussehen:

#7 Stunden, 21 Minuten und 37 Sekunden sind insgesamt 26497 Sekunden.

# Die nächsten zwei Zeilen nicht verändern
if __name__ == "__main__":
    sekundenBerechnen()
