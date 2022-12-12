from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

import Crawler


class Url():

    def __init__(self, nomeSite, endereco) -> None:
        self.nomeSite = nomeSite
        self.endereco = endereco


urls =[ Url('Galapagos', 'https://www.mundogalapagos.com.br/'), Url('Play Easy', 'https://www.playeasy.com.br/')]


print("Digite o titulo do jogo:")
tituloJogo = input()
jogos = []
for url in urls:
    crawler = Crawler.Crawler(tituloJogo, url)
    if url.nomeSite == 'Galapagos':
        Crawler.CrawlerGalapagos(crawler.titulo, crawler.url, jogos).extractGalapagos(jogos)
    elif url.nomeSite == 'Play Easy':
        Crawler.CrawlerPlayEasy(crawler.titulo, crawler.url, jogos).extractPlayEasy(jogos)
print(jogos)
