from selenium import webdriver
from time import sleep
import json

from dotmap import DotMap


def require( arquivo: str ):
  resultado = None
  with open( arquivo, 'r', encoding='utf-8' ) as p:
    resultado = DotMap( json.load( p ) )
  
  return resultado


params = None

with open( './desenvolvimento.json', 'r' ) as p:
    params = json.loads( p.read() )

navegador = webdriver.Chrome()

navegador.get( params["url"] )

#sleep(5)
#02-botao-start
navegador.find_element('xpath', '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
#sleep(5)

#03-realizar-download-excel
navegador.find_element('xpath', '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a').click()
sleep(5)