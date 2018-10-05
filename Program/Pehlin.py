import requests
from bs4 import BeautifulSoup

# otvaranje stranice i parsiranje
page = requests.get('https://pljusak.com/meteo.php?stanica=pehlin')
soup = BeautifulSoup(page.text, 'html.parser')

#trazenje taga od div-a i ispis vrijednosti
TablicaRijekaTemp = soup.find_all(class_ = 'broj_met')

TemperaturaPehlin = TablicaRijekaTemp[0].get_text()

TlakMeh = TablicaRijekaTemp[2].get_text()
TlakPehlin = TlakMeh[1:5]



try:
    TemperaturaPehlin = TablicaRijekaTemp[0].get_text()
except ValueError:
    TemperaturaPehlin = 0

try:
    TlakMeh = TablicaRijekaTemp[2].get_text()
    TlakPehlin = TlakMeh[1:5]
except ValueError:
    TlakPehlin = 0




#ispis za test
#print(TemperaturaPehlin)
#print(TlakPehlin)
