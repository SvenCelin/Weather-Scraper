import time
from Rujevica import TemperaturaRujevica
from Rujevica import TlakRujevica
from Kozala import TemperaturaKozala
from Kozala import TlakKozala
from Drenova import TemperaturaDrenova
from Drenova import TlakDrenova
from Pravni import TemperaturaPravni
from Pravni import TlakPravni
from Pehlin import TemperaturaPehlin
from Pehlin import TlakPehlin

TemperaturaSrednja = (float(TemperaturaDrenova) + float(TemperaturaKozala) + float(TemperaturaPehlin) + float(TemperaturaPravni) + float(TemperaturaRujevica))/5
TlakSrednji = (float(TlakDrenova) + float(TlakKozala) + float(TlakPehlin) + float(TlakPravni) + float(TlakRujevica))/5
#print(TemperaturaSrednja)
#print(TlakSrednji)


Vrijeme = time.ctime()


#radenje enumeracije za dane 
CitamDatoteku = open("Vrijeme.txt", "r")
count = len(open("Vrijeme.txt").readlines(  ))
#print(count+1)
CitamDatoteku.close()


#otvaranje i upis vrijednosti u datoteku --SAV DATA--
Datoteka = open("Vrijeme.txt", "a+")
Datoteka.write("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n" %((count+1), TemperaturaSrednja, TlakSrednji,TemperaturaPehlin, TemperaturaRujevica, TemperaturaKozala, TemperaturaDrenova, TemperaturaPravni, TlakPehlin, TlakRujevica, TlakKozala, TlakDrenova, TlakPravni, Vrijeme))
Datoteka.close()

#otvaranje i upis vrijednosti u datoteku --ZA GRAF--
Graf = open("Graf.txt", "a+")
Graf.write("%s, %s, %s\n" %((count+1), TemperaturaSrednja, TlakSrednji))
Graf.close()

#ispis iz datoteke - provjera -
CitamDatoteku = open("Vrijeme.txt", "r")
Datoteka2 = CitamDatoteku.read()
print(Datoteka2)
CitamDatoteku.close()
