import requests
from bs4 import BeautifulSoup

#Script 1
def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def imagenes_14():
    soup = get_soup('https://www.google.com/search?q=real+de+catorce&tbm=isch&ved=2ahUKEwjH-5rx9NjsAhUP66wKHXf9BDUQ2-cCegQIABAA&oq=real+de+&gs_lcp=CgNpbWcQARgBMgQIIxAnMgUIABCxAzIECAAQQzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgjEOoCECc6BwgAELEDEENQixlYnDpgq0NoAXAAeACAAc8DiAHvCpIBBzEuNy40LTGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=Gj6aX8eGOo_WswX3-pOoAw&bih=873&biw=1600')
    images = soup.find_all('img')
    real = [{ 'src': image.get('src'), 'alt': image.get('alt')}  for image in images]
    print(f"{real}", file=open("RealdeCatorce.txt", "a"))

if __name__ == '__main__':
    imagenes_14()

#Script 2
def clima():
    soup = get_soup("https://www.meteored.mx/clima_Escobedo-America+Norte-Mexico-Coahuila--1-69848.html")
    tr= soup.table.find_all('tr')
    for row in tr:
        cols = row.find_all('td')
        cale = [ele.text.strip() for ele in cols]
        print(f"{cale}", file=open("Clima_en_Escobedo.txt", "a"))
if __name__ == '__main__':
    clima()
