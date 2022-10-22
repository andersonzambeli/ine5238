from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


driver.get('https://www.mundogalapagos.com.br/mais-vendidos/categoria/B2C-Mais-Vendidos')

time.sleep(5)

ts = driver.find_elements(By.TAG_NAME , 'h2')
print(len(ts))
print(ts[1].text)