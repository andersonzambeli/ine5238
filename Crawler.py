import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from Jogo import *
import time

class Crawler():

    def __init__(self, titulo, url) -> None:
        self.titulo = titulo
        self.url = url
        

    def accessPage(self):
        driver = webdriver.Firefox()
        driver.get(self.url)


class CrawlerGalapagos(Crawler):

    def __init__(self, titulo, url, jogos) -> None:
        Crawler.__init__(self, titulo, url)
        self.extractGalapagos(jogos)


    

    def extractGalapagos(self, jogos):
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
            


            href =[]
            for i in range(0,len(ts)):
                h = ts[i].find_element(By.TAG_NAME, 'a')
                href.append(h.get_attribute("href"))
                #print(href)
            
            if (len(ts) == 0):
                return -1
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
                    print(tn[0].text, disp, te[0].text, te[1].text, te[2].text, "Mundo Galapagos", self.url.nomeSite, preco)

                    jogos.append(Jogo(tn[0].text, disp, te[0].text, te[1].text, te[2].text, "Mundo Galapagos", self.url.nomeSite, preco))
            driver.close()


class CrawlerPlayEasy(Crawler):

    def __init__(self, titulo, url, jogos) -> None:
        Crawler.__init__(self, titulo, url)
        self.extractPlayEasy(jogos)


    

    def extractPlayEasy(self, jogos):
        
        titulo = self.titulo
        titulo = titulo.replace(':', '')
        jogo = Jogo('', False, '', 0, '', '', 'PlayEasy', 0.0)
            

        driver = webdriver.Firefox()
        driver.get('https://www.playeasy.com.br/')

        time.sleep(3)
        elem = driver.find_element(By.XPATH, '//*[@id="search"]')
        elem.clear()
        elem.send_keys(titulo)
        elem.send_keys(Keys.RETURN)

        time.sleep(5)

        lis = driver.find_elements(By.TAG_NAME, 'li')

        i = []
        for li in lis:
            if titulo in li.text:
                i.append(li)

        #print(len(driver.find_element(By.XPATH, f'/html/body/main/div[6]/section/div[4]/section/ul/li')))
        assert 'No results found.' not in driver.page_source
        for i in range(1, len(i)):
            driver.find_element(By.XPATH, f'/html/body/main/div[6]/section/div[4]/section/ul/li[{i}]').click()
            jogo.titulo = driver.find_element(By.XPATH,'/html/body/main/div[6]/section/div[2]/article/div[1]/div[2]/div/form/div[2]/h2').text
            try:
            #if titulo in driver.find_element(By.XPATH, f'/html/body/main/div[6]/section/div[4]/section/ul/li[{i}]').text.split('\n')[0]:
                jogo.disponibilidade = True if 'Em estoque' in driver.find_element(By.XPATH, '//*[@id="info-secundaria"]').text else False
                preco = None if jogo.disponibilidade == False else driver.find_element(By.XPATH, '/html/body/main/div[6]/section/div[2]/article/div[1]/div[2]/div/form/div[6]/div[1]/div[1]/div/span/span[1]').text
                jogo.preco = float(preco.removeprefix('R$ ').replace(',', '.'))

                num = 4
                if jogo.titulo == "Rory's Story Cubes: Harry Potter":
                    num = 3

                # O TR MUDA PORQUE AS ESPECIFICACOES TECNICAS SAO MUITO BUGADAS, TEM QUE RESOLVER

                jogo.numJogadores = driver.find_element(By.XPATH, f'/html/body/main/div[6]/section/div[2]/article/div[{num}]/div/div/table/tbody/tr[5]/td').text #/html/body/main/div[6]/section/div[2]/article/div[3]/div/div/table/tbody/tr[5]/td
                jogo.idade = int(driver.find_element(By.XPATH, f'/html/body/main/div[6]/section/div[2]/article/div[{num}]/div/div/table/tbody/tr[3]/td').text.removesuffix('+'))
                jogo.tempoJogo = driver.find_element(By.XPATH, f'/html/body/main/div[6]/section/div[2]/article/div[{num}]/div/div/table/tbody/tr[6]/td').text
                jogo.editora = driver.find_element(By.XPATH, f'/html/body/main/div[6]/section/div[2]/article/div[{num}]/div/div/table/tbody/tr[1]/td').text
                print(jogo.titulo, jogo.disponibilidade, jogo.numJogadores, jogo.numJogadores, jogo.idade, jogo.tempoJogo, jogo.editora, jogo.preco)
                jogos.append(jogo)
                driver.back()
                time.sleep(2)
            except:
                print("algo deu errado com " + jogo.titulo)

                driver.back()


        print(jogos)

        driver.close()
