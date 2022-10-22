from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


driver.get('https://www.mundogalapagos.com.br/jogo-de-cartas-dobble/produto/DOB001')

time.sleep(5)

ts = driver.find_elements(By.TAG_NAME , 'span')
print(len(ts))
for i in range(0, len(ts)):
    print(ts[i].text + " (" + str(i) + ")/n")