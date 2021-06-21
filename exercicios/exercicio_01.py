from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('https://curso-python-selenium.netlify.app/exercicio_01.html')
sleep(1)

my_dict = {}
my_dict_2 = {}

list_p = browser.find_elements_by_tag_name('p')

for p in (list_p):
    my_dict_2[p.get_attribute("atributo")] = p.text

my_dict['H1'] = my_dict_2
print(my_dict)

browser.quit()