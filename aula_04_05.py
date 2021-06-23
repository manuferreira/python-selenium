"""
1. Pegar todos os links de aulas
    dicionario = {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""

from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04.html')
sleep(2)



def get_links(browser, tag):

    """
    Pega todos os links dentro de um elemento
    browser - instância do navegador
    tag - elemento onde iremos procurar os links
    retorna um dicionário de links

    """
    dicionario_links = {}
    elemento = browser.find_element_by_tag_name(tag)
    links = elemento.find_elements_by_tag_name('a')

    for link in links:
        dicionario_links[link.text] = link.get_attribute('href')

    return dicionario_links


# exercício 1:
print(get_links(browser, 'aside'))

# exercício 2:
url = get_links(browser, 'main')
browser.get(url['Exercício 3'])


