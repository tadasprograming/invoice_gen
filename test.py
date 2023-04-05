import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Set up the Selenium driver
driver = webdriver.Chrome()
driver.get('https://www.google.lt/search?q=rekvizitai.vz.lt+fotovis')

# Find the button element and click it
button = driver.find_element_by_id('button-id')
button.click()

# Wait for the page to load
time.sleep(5)

# Get the HTML source of the page
html_source = driver.page_source

# Parse the HTML into a BeautifulSoup object
soup = BeautifulSoup(html_source, 'html.parser')

# Close the browser window
driver.quit()

# Write the soup to a file
with open('soup.txt', 'w') as f:
    f.write(str(soup))


