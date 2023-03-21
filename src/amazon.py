import log4p
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

logger = log4p.GetLogger(__name__, config="log4p.json").logger

PRICE_XPATH = '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
serv = Service(r"C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=serv, options=chrome_options)


def get_price(code):
    driver.get("https://www.amazon.ca/dp/"+code)
    current_price = driver.find_element(By.XPATH, PRICE_XPATH).get_attribute('innerHTML').replace('$', '')
    logger.info(f'Current price: {current_price}')
    return current_price


# Timer starts
# start = timeit.default_timer()
# print(get_price("B09Q5KPFXM"))
# print('Time: ', timeit.default_timer() - start)
