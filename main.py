from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

import Crawler


class Url():

    def __init__(self, nomeSite, endereco) -> None:
        self.nomeSite = nomeSite
        self.endereco = endereco
        
        
        
def writeJogosJson(jogos):
        dicts_json = []
        for j in jogos:
            dict = {
                
                'titulo': j.titulo,
                'disponibilidade': j.disponibilidade,
                'numJogadores': j.numJogadores,
                'idade': j.idade,
                'tempoJogo': j.tempoJogo,
                'editora': j.editora,
                'siteFonte': j.siteFonte,
                'preco': float(j.preco.removeprefix('R$ ').replace(',', '.'))

            }
            dicts_json.append(dict)
        json_ = json.dumps(dicts_json , indent= 2, ensure_ascii=False)
        print(json_)
        return dicts_json



urls =[ Url('Galapagos', 'https://www.mundogalapagos.com.br/'), Url('Play Easy', 'https://www.playeasy.com.br/')]


print("Digite o titulo do jogo:")
tituloJogo = input()
jogos = []
for url in urls:
    crawler = Crawler.Crawler(tituloJogo, url)
    if url.nomeSite == 'Galapagos':
        Crawler.CrawlerGalapagos(crawler.titulo, crawler.url, jogos)
    elif url.nomeSite == 'Play Easy':
        Crawler.CrawlerPlayEasy(crawler.titulo, crawler.url, jogos)
print(jogos)
