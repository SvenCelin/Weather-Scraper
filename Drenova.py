import requests
from bs4 import BeautifulSoup

# otvaranje stranice i parsiranje
page = requests.get('https://pljusak.com/meteo.php?stanica=drenova')
soup = BeautifulSoup(page.text, 'html.parser')

#trazenje taga od div-a i ispis vrijednosti
TablicaRijekaTemp = soup.find_all(class_ = 'broj_met')

TemperaturaDrenova = TablicaRijekaTemp[0].get_text()

TlakMeh = TablicaRijekaTemp[2].get_text()
TlakDrenova = TlakMeh[1:5]


try:
    TemperaturaDrenova = TablicaRijekaTemp[0].get_text()
except ValueError:
    TemperaturaDrenova = 0

try:
    TlakMeh = TablicaRijekaTemp[2].get_text()
    TlakDrenova = TlakMeh[1:5]
except ValueError:
    TlakDrenova = 0



#ispis za test
#print(TemperaturaDrenova)
#print(TlakDrenova)
