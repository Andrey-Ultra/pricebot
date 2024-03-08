from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def parse_ozon_product(url):
    chrome_options = Options()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)
    
    wait = WebDriverWait(driver, 10)
    title_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layoutPage"]/div[1]/div[4]/div[3]/div[1]/div[1]/div[2]/div/div[1]/h1')))
    price_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layoutPage"]/div[1]/div[4]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/span/div/div[1]/div/div/span')))
    

    title = title_element.text.strip()
    price = price_element.text.strip()
    

    driver.quit()
    
    return {'title': title, 'price': price}


url = "https://www.ozon.ru/product/vlazhnyy-korm-pro-plan-sterilised-maintenance-dlya-vzroslyh-sterilizovannyh-koshek-i-kastrirovannyh-230756179/?avtc=1&avte=1&avts=1709914638"
product_info = parse_ozon_product(url)

if product_info:
    print("Название:", product_info['title'])
    print("Цена:", product_info['price'])
