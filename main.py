from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


class Url():

    def __init__(self, nomeSite, endereco) -> None:
        self.nomeSite = nomeSite
        self.endereco = endereco


urls =[ Url('Galapagos', 'https://www.mundogalapagos.com.br/'), Url('Play Easy', 'https://www.playeasy.com.br/')]


print("Digite o titulo do jogo:")
tituloJogo = input()

