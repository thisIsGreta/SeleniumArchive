from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

research_sheet_url = "https://docs.google.com/forms/d/e/1FAIpQLSeP6PA7SiNWrPNmO2NXo36-" \
                     "j_InqLz_0J1W2U8V8rkBdpOzdA/viewform?usp=sf_link"
zillow_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%' \
             '22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.90711440039063%2C%22east%22%3A-' \
             '121.95954359960938%2C%22south%22%3A37.47182402929133%2C%22north%22%3A38.07751831986319%' \
             '7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A8' \
             '72627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%' \
             '22mp%22%3A%7B%22max%22%3A3000%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%' \
             '22value%22%3Atrue%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%' \
             '22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
headers = {
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/'
                 '537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}
response = requests.get(zillow_url, headers=headers)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

links_r = soup.find_all("a", {"class": "list-card-link list-card-link-top-margin"})
links = [link.get("href") for link in links_r]
addresses_r = soup.find_all("address", class_="list-card-addr")
addresses= [address.getText() for address in addresses_r]
prices_r = soup.find_all(class_="list-card-price")
prices_too = [price.getText().split("/")[0] for price in prices_r]
prices = [price.split("+")[0] for price in prices_too]
# print(links)
# print(addresses)
# print(prices)
chrome_driver_path = "/Users/username/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(research_sheet_url)

for n in range(0, len(prices)):
    q1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                                                                   'div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')))
    q2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/'
                                                  'div/div[1]/div/div[1]/input')))
    q3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                                  'div/div[1]/div/div[1]/input')))

    q1.send_keys(addresses[n])
    sleep(3)
    q2.send_keys(prices[n])
    sleep(3)
    q3.send_keys(links[n])
    sleep(3)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    sleep(3)
    get_back = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    get_back.click()
    sleep(3)
