import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import get_attributes
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(0)

'''

driver.get("https://skelbiu.lt")
butinu_mygtukai = driver.find_element(By.ID,"onetrust-reject-all-handler")
butinu_mygtukai.click()

keyword = driver.find_element(By.ID,"searchKeyword")
keyword.send_keys("kadagys")
driver.find_element(By.ID,"searchKeyword").send_keys(Keys.ENTER)
time.sleep(3)

count = 0
aruodas = 0
while True:
    # list_aurodas = driver.find_elements(By.CLASS_NAME, "aruodas")
    # for xa in list_aurodas:
    #     aruodas += 1
    #     print(xa.text)
    items = driver.find_elements(By.CLASS_NAME, "standard-list-item")
    for item in items:
        print(item.get_attribute("href"))
        count += 1
    time.sleep(1)
    pages = driver.find_elements(By.CLASS_NAME, "pagination_link")
    next_page_found = False
    for page in pages:
        if page.text == "»":
            page.click()
            next_page_found = True
            break
    if not next_page_found:
        print("Nera daugiau puslapiu")
        break

# print(count)
text = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/ul/li/span").text
number = int(text[1:-1])
if count == number:
    print(f"All fine {number}/{count}")
else:
    print("Ah S***, Here We Go Again")
# print(f'{driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/ul/li/span").text}')
time.sleep(3000)

'''

'''
driver.get("https://skelbiu.lt")
butinu_mygtukai = driver.find_element(By.ID,"onetrust-reject-all-handler")
butinu_mygtukai.click()

keyword = driver.find_element(By.ID,"searchKeyword")
keyword.send_keys("žibalas")
driver.find_element(By.ID,"searchKeyword").send_keys(Keys.ENTER)
time.sleep(3)

count = 0
while True:
    items = driver.find_elements(By.CLASS_NAME, "standard-list-item")
    for item in items:
        print(item.get_attribute("href"))
        count += 1
    time.sleep(1)
    pages = driver.find_elements(By.CLASS_NAME, "pagination_link")
    next_page_found = False
    for page in pages:
        if page.text == "»":
            page.click()
            next_page_found = True
            break
    if not next_page_found:
        print("Nera daugiau puslapiu")
        break

print(count)
'''

''
driver.get("https://skelbiu.lt")
butinu_mygtukai = driver.find_element(By.ID,"onetrust-reject-all-handler")
butinu_mygtukai.click()

keyword = driver.find_element(By.ID,"searchKeyword")
keyword.send_keys("telefonas")
driver.find_element(By.ID,"searchKeyword").send_keys(Keys.ENTER)
time.sleep(3)

count = 0
while True:
    items = driver.find_elements(By.CLASS_NAME, "standard-list-item")
    for item in items:
        print(item.get_attribute("href"))
        count += 1
    if count == 0:
        print('Nera tokiu prekiu')
    time.sleep(1)
    pages = driver.find_elements(By.CLASS_NAME, "pagination_link")
    next_page_found = False
    for page in pages:
        if page.text == "»":
            page.click()
            next_page_found = True
            break
    if not next_page_found:
        print("Nera daugiau puslapiu")
        break

print(count)

text = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/ul/li/span").text
number = int(text[1:-1])
if count == number:
    print(f"All fine {number}/{count}")
else:
    print("Ah S***, Here We Go Again")
# print(f'{driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/ul/li/span").text}')
time.sleep(3000)
''

# skelbiu.lt
# pagal atitinkamus raktažodžius:
# nurinkti visus url (<a href""></a>) nuorodas ir išspausdinti konsolėje
# patikrinti ar rodomų skelbiu.lt skelbimų kiekis atitinka viršuje rodomą skelbimų sumą (kainos.lt skelbimus ignoruojame)
# kaip skelbimų kiekį įtakoja aruodas.lt duomenys? t.y ar iš aruodo įkelti skelbimai į skelbiu.lt patenka į bendrą skelbimų sumą?
#
# paieškos žodžiai:
#
# kadagys
# žibalas
# asdfgsdf
# telefonas