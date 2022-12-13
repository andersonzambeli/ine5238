from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import json

from Crawler import CrawlerGalapagos, CrawlerPlayEasy

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
                'preco': j.preco

            }
            dicts_json.append(dict)
        json_ = json.dumps(dicts_json , indent= 2, ensure_ascii=False)
        print(json_)
        return dicts_json


def encontrarJogos(titulo):

    urls =[ Url('Galapagos', 'https://www.mundogalapagos.com.br/'), Url('Play Easy', 'https://www.playeasy.com.br/')]

    jogos = []



    crawler_galapagos = CrawlerGalapagos(titulo, urls[0], jogos)
    crawler_playeasy = CrawlerPlayEasy(titulo, urls[1], jogos)

    if  not jogos:
        raise Exception("Jogo não encontrado")


    json_ = writeJogosJson(jogos)
    with open("result.json", "w") as outfile:
        json.dump(json_, outfile, indent= 2, ensure_ascii=False)


print("Digite o titulo do jogo:")
tituloJogo = input()

encontrarJogos(tituloJogo)
