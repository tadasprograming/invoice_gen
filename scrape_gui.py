import sys
sys.path.append(r'C:\Users\tadas\anaconda3\Lib\site-packages')
import requests
from bs4 import BeautifulSoup

# Prašom nuorodos ir tikrinam ar nuoroda atiduoda HTML failą

def scrape_gui(url):
    try:
        res = requests.get(url)
        soup_in = ''
        soup_in = BeautifulSoup(res.text)
    except:
        soup_in = ''

    return soup_in

'''Jeigu nuoroda atiduoda HTML, tikrinam ar programa randa įmonės informaciją. Jeigu neranda nei vieno
duomens, gali būti jog nuoroda su klaida. Klausiame ar norima bandyti pateikti nuorodą dar kartą
'''
def get_data_gui(url):
    soup = scrape_gui(url)
    try:
        company_name = soup.select('.fn')
        company_name = company_name[0].text
    except:
        company_name = ''

    try:
        company_code_tag = soup.find('td', text='Įmonės kodas')
        company_code = company_code_tag.find_next_sibling('td')
        company_code = company_code.text.strip()
    except:
        company_code = ''

    try:
        company_address_elem = soup.find('td', {'itemprop': 'address'})
        company_address = company_address_elem.get_text(strip=True)
    except:
        company_address = ''

    try:
        company_boss_tag = soup.find('td', text='Vadovas')
        company_boss = company_boss_tag.find_next_sibling('td')
        company_boss = company_boss.text.strip()
    except:
        company_boss = ''

    return (company_name,company_code,company_address,company_boss)

'''
TEST
url = 'https://rekvizitai.vz.lt/imone/lindyhop_lt_klubas/'
data = get_data_gui(url)
print(data)'''







