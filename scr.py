import sys
sys.path.append(r'C:\Users\tadas\anaconda3\Lib\site-packages')
import requests
from bs4 import BeautifulSoup

# Prašom nuorodos ir tikrinam ar nuoroda atiduoda HTML failą

def scrape():
    while True:
        url = input('Nukopijuokite rekvizitai.vz.lt nuorodą su įmonės informacija: ')
        #url = "https://rekvizitai.vz.lt/imone/maxima_lt_uab/"
        try:
            res = requests.get(url)
            soup_in = ''
            soup_in = BeautifulSoup(res.text,'lxml')
            break
        except:
            print('Neteisingai įvesta nuoroda (nerastas HTML failas)! Bandykite dar kartą.')
    return soup_in

'''Jeigu nuoroda atiduoda HTML, tikrinam ar programa randa įmonės informaciją. Jeigu neranda nei vieno
duomens, gali būti jog nuoroda su klaida. Klausiame ar norima bandyti pateikti nuorodą dar kartą
'''
def get_data():
    data_empty = True
    while data_empty:
        soup = scrape()
        try:
            company_name = soup.select('.fn')
            company_name = company_name[0].text
        except:
            print('Įmonės pavadinimas nerastas')
            company_name = ''

        try:
            company_code_tag = soup.find('td', text='Įmonės kodas')
            company_code = company_code_tag.find_next_sibling('td')
            company_code = company_code.text.strip()
        except:
            print('Įmonės kodas nerastas')
            company_code = ''

        try:
            company_address_elem = soup.find('td', {'itemprop': 'address'})
            company_address = company_address_elem.get_text(strip=True)
        except:
            print('Įmonės adresas nerastas')
            company_address = ''

        try:
            company_boss_tag = soup.find('td', text='Vadovas')
            company_boss = company_boss_tag.find_next_sibling('td')
            company_boss = company_boss.text.strip()
        except:
            print('Informacija apie vadovą nerasta')
            company_boss = ''

        if company_name == '' and company_code == '' and company_address == '' and company_boss =='':
            print('Nepavyko nuskaityti įmonės duomenų.')
            try_again = ''
            while try_again != 't' and try_again != 'n':
                try_again = input('Ar norite pateikti nuorodą dar kartą? ("t" arba "n"):  ')
            if try_again == 'n':
                print('Duomenys nenuskaityti!')
                break
        else:
            print('Duomenys nuskaityti!')
            data_empty = False

    return (company_name,company_code,company_address,company_boss)






