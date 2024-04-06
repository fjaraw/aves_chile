import requests
import json
from html_maker import make_cards, make_full_html

#Funcion que transforma a lista un JSON obtenido desde una URL
def request_get(url):
    return json.loads(requests.get(url).text)

#Solicita imagenes desde API y genera listado
url = 'https://aves.ninjas.cl/api/birds'
fotos = request_get(url)

#Arma tarjetas con información de las aves
info_aves = make_cards(fotos)

#Genera plantilla de pagina html
html_template = make_full_html(info_aves)

#Escribe archivo html
with open('index.html', 'w', encoding='utf-8') as archivo:
    archivo.write(html_template)