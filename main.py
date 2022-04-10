from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/username/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")))

number_of_articles = articles.get_attribute("textContent")
print(number_of_articles)

# driver.quit()

fname = driver.find_element(By.NAME, "fName")
fname.click()
fname.send_keys("Greta")

sign_up = driver.find_element(By.CLASS_NAME, "btn")
sign_up.send_keys(Keys.ENTER)
