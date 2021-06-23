from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')


#como posso pegar os itens que estão dentro da lista?

#encontramos a nossa lista
lista_nao_ordenada = browser.find_element_by_tag_name('ul')

#e dentro dela procuramos o nossos elementos
itens = lista_nao_ordenada.find_elements_by_tag_name('li')
