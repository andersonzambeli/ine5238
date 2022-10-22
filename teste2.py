from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


driver.get('https://www.mundogalapagos.com.br/mais-vendidos/categoria/B2C-Mais-Vendidos')

time.sleep(5)

ts = driver.find_elements(By.CSS_SELECTOR , 'div.items4:nth-child(2) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > a:nth-child(2)')
print(len(ts))
href = ts[0].get_attribute('href')
print(href)