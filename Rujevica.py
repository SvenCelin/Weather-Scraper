import requests
from bs4 import BeautifulSoup

# otvaranje stranice i parsiranje
page = requests.get('https://pljusak.com/meteo.php?stanica=rujevica')
soup = BeautifulSoup(page.text, 'html.parser')

#trazenje taga od div-a i ispis vrijednosti
TablicaRijekaTemp = soup.find_all(class_ = 'broj_met')

try:
    TemperaturaRujevica = TablicaRijekaTemp[0].get_text()
except ValueError:
    TemperaturaRujevica = 0

try:
    TlakMeh = TablicaRijekaTemp[2].get_text()
    TlakRujevica = TlakMeh[1:5]
except ValueError:
    TlakRujevica = 0





#ispis za test
#print(TemperaturaRujevica)
#print(TlakRujevica)
