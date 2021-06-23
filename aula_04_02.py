from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')


def find_by_text(browser, tag, text):
    '''criando nosso próprio método que encontra o elemento com o texto 'text'

    browser - instancia do browser
    text - texto que deve estar na tag
    tag - tag onde o texto será procurado

    '''
    elementos = browser.find_elements_by_tag_name(tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento


#elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')


def find_by_href(browser, link):
    '''criando nosso próprio método que encontra o elemento a com o link 'link'

    browser - instancia do browser
    link - link que será procurado dentro dos a
    '''
    ancoras = browser.find_elements_by_tag_name('a')

    for ancora in ancoras:
        if link in ancora.get_attribute('href'):
            return ancora


elemento_ddg_2 = find_by_href(browser, 'ddg')