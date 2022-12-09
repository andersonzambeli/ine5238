import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from Jogo import *
import time


class CrawlerGalapagos():

    def __init__(self, titulo, url, jogos) -> None:
        self.titulo = titulo
        self.url = url
        self.extract_Galapagos(jogos)


    

    def extract_Galapagos(self, jogos):
        if( self.url.nomeSite == 'Galapagos'):

            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

            driver.get('https://www.mundogalapagos.com.br/')
            time.sleep(10)

            elem = driver.find_element(By.XPATH, '//*[@id="CC-headerWidget-Search"]')
            elem.clear()
            elem.send_keys(self.titulo)
            elem.send_keys(Keys.RETURN)
            time.sleep(5)


            ts = driver.find_elements(By.XPATH , "//article/div[contains(@class,'product-cover')]")
            print(len(ts))
            if (len(ts) == 0):
                return 0


            href =[]
            for i in range(0,len(ts)):
                h = ts[i].find_element(By.TAG_NAME, 'a')
                href.append(h.get_attribute("href"))
                #print(href)
            
            if (len(ts) == 0):
                return 1
            else:
                for page in href:
                    driver.get(page)
                    time.sleep(5)
                    tn = driver.find_elements(By.CLASS_NAME , 'product-title')
                    #print(ts[0].text)
                    te = driver.find_elements(By.CLASS_NAME , 'info-item-text')
                    tp = driver.find_elements(By.CLASS_NAME , 'best-price')
                    disp=''
                    preco =''
                    if(len(tp) == 0):
                        disp = False
                        preco = None
                    else:
                        disp = True
                        preco = tp[0].text
                    #print(ts[0].text)
                    jogos.append(Jogo(tn[0].text, disp, te[0].text, te[1].text, te[2].text, "Mundo Galapagos", self.url.nomeSite, preco))

    def jogo_para_json(self, jogos):
        dicts_json = []
        for j in jogos:
            dict = {
                
                'titulo': j.titulo,
                'disponibilidade': j.disponibilidade,
                'numJogadores': j.numJogadores,
                'idade': int(j.idade.removesuffix('+')),
                'tempoJogo': j.tempoJogo,
                'editora': j.editora,
                'siteFonte': j.siteFonte,
                'preco': float(j.preco.removeprefix('R$ ').replace(',', '.'))

            }
            dicts_json.append(dict)
        json_ = json.dumps(dicts_json , indent= 2)
        print(json_)
        return dicts_json
            

        
