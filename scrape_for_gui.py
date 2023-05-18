import requests
from bs4 import BeautifulSoup


def scrape(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, features="lxml")
    except:
        soup = ''

    return soup


def get_data(url):
    soup = scrape(url)
    try:
        company_name = soup.select('.fn')
        company_name = company_name[0].text
    except AttributeError:
        company_name = ''

    try:
        company_code_tag = soup.find('td', text='Įmonės kodas')
        company_code = company_code_tag.find_next_sibling('td')
        company_code = company_code.text.strip()
    except AttributeError:
        company_code = ''

    try:
        company_address_elem = soup.find('td', {'itemprop': 'address'})
        company_address = company_address_elem.get_text(strip=True)
    except AttributeError:
        company_address = ''

    try:
        company_boss_tag = soup.find('td', text='Vadovas')
        company_boss = company_boss_tag.find_next_sibling('td')
        company_boss = company_boss.text.strip()
    except AttributeError:
        company_boss = ''

    extra_info = ''

    return [company_name, company_code, company_address, company_boss,
            extra_info]
