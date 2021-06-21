from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('https://curso-python-selenium.netlify.app/exercicio_02.html')
sleep(1)


p_list = browser.find_elements_by_tag_name('p')
num_esperado = p_list[-1].text.split(' ')[-1]

anchor = browser.find_element_by_id('ancora')

while True:
    anchor.click()
    p_list = browser.find_elements_by_tag_name('p')
    if num_esperado in p_list[-1].text:
        break
