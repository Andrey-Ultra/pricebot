import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def print_text_within_length(html, min_length=1, max_length=100):
    
    soup = BeautifulSoup(html, 'html.parser')
    
    all_text = soup.get_text()

    words = all_text.split()
    for word in words:
        if min_length <= len(word) <= max_length:
            print(word)

def extract_text_by_class(html, class_list):
    soup = BeautifulSoup(html, 'html.parser')

    responses = []


    for class_name in class_list:

        elements = soup.find_all(class_=class_name)

        for element in elements:
            responses.append(element.get_text())

    return responses


def smart_waiter(driver, interval=0.5, max_attempts=20, by=By.TAG_NAME, value='body'):
    time.sleep(10)

    #todo более умное ожидание не 10 сек
    '''
    for _ in range(max_attempts):
        try:
            element = driver.find_element(by, value)
            return
        except NoSuchElementException:
            pass
        sleep(interval)
    print("Время ожидания превышено. Страница не загружена.")
    '''
    
def get_page_html(url):
    driver = uc.Chrome()
    try:
        driver.get(url)
        smart_waiter(driver)
        html = driver.page_source
        
        return html

    finally:
        driver.quit()






if __name__ == "__main__":
    url = 'https://www.ozon.ru/product/programmirovanie-na-c-v-primerah-i-zadachah-vasilev-aleksey-nikolaevich-249173686/?avtc=1&avte=2&avts=1710437273'

    page_num = get_page_html(url)

    ans1 = extract_text_by_class(page_num, ["lp0", "l1p tsHeadline550Medium"])

    ans2 = extract_text_by_class(page_num, ["l5o ol5 o9l"])

    print('Название:')
    print(ans1)
    print('Цена:')
    print(ans2)
    





    
