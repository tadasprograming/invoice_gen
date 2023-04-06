import sys
sys.path.append(r'C:\Users\tadas\anaconda3\Lib\site-packages')
import requests
from bs4 import BeautifulSoup


url = 'https://rekvizitai.vz.lt/imone/lindyhop_lt_klubas/'
res = requests.get(url)
soup_in = ''
soup_in = BeautifulSoup(res.text,)
print(soup_in)



