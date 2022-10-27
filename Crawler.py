from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


class Crawler():

    def __init__(self, titulo, url) -> None:
        self.titulo = titulo
        self.url = url

    

    def accessPage(self):
        if( self.url.nomeSite == 'Galapagos'):

            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

            driver.get('https://www.mundogalapagos.com.br/')
            time.sleep(5)

        if( self.url.nomeSite == 'Play Easy'):

            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

            driver.get('https://www.playeasy.com.br/')
            
            time.sleep(5)

        
