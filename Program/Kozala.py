import requests
from bs4 import BeautifulSoup

# otvaranje stranice i parsiranje
page = requests.get('https://pljusak.com/meteo.php?stanica=dhmz_rijeka')
soup = BeautifulSoup(page.text, 'html.parser')

#trazenje taga od div-a i ispis vrijednosti
TablicaRijekaTemp = soup.find_all(class_ = 'broj_met')

try:
    TemperaturaKozala = TablicaRijekaTemp[0].get_text()
except ValueError:
    TlakKozala = 0

try:
    TlakMeh = float(TablicaRijekaTemp[2].get_text())
    TlakKozala = TlakMeh[1:5]
except ValueError:
    TlakKozala = 0


#ispis za test
#print(TemperaturaKozala)
#print(TlakKozala)
