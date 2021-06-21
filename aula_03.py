from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('https://curso-python-selenium.netlify.app/aula_03.html')
sleep(1)


a = browser.find_element_by_tag_name('a')

for clique in range(1, 11):
    a.click()

list_p = browser.find_elements_by_tag_name('p')
print(f'O último parágrafo encontrado foi o de número {list_p[-1].text}')


browser.quit()