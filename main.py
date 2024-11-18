import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://skelbiu.lt")
butinu_mygtukai = driver.find_element(By.ID,"onetrust-reject-all-handler")
butinu_mygtukai.click()

keyword = driver.find_element(By.ID,"searchKeyword")
keyword.send_keys("kadagys")
driver.find_element(By.ID,"searchKeyword").send_keys(Keys.ENTER)
time.sleep(3)

# container = driver.find_element(By.ID, ("container"))
count = 0
while True:
    items = driver.find_elements(By.CLASS_NAME, "standard-list-item")
    # print(len(items))
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
        print("No more pages. Exiting loop.")
        break

print(count)
# time.sleep(1)
# toliau = driver.find_element(By.CLASS_NAME, "pagination_link")
# toliau.click()

time.sleep(3000)

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