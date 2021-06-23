from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_b.html')


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


nome_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nome_das_caixas:
    find_by_text(browser, 'div', nome).click()

# a gente pode ir voltando também:
for volta_caixa in range(len(nome_das_caixas)):
    sleep(0.3)
    browser.back()

# e podemos ir pra frente:
for frente_caixa in range(len(nome_das_caixas)):
    sleep(0.3)
    browser.forward()

