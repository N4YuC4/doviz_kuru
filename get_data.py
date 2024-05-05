import requests
from bs4 import BeautifulSoup

url_base="https://www.google.com/finance/quote/"

def kur_al(birim):
    response= requests.get(url_base+birim)
    site_icerik = response.content

    soup= BeautifulSoup(site_icerik,"html.parser")

    return (soup.find("div",class_="YMlKec fxKbKc").get_text(),soup.find("div",class_="JwB6zf").get_text())

