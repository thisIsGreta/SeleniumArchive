# Learnt to create interaction with webpage using Selenuim today.
# The project is called cookie clicker.
# Tips for myself: 
  # 1) Run func every 5 seconds by using threading module; 
  # 2) End the loop after 5 minutes by using time module; 
  # 3) threading should not be included inside the while loop.


import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/username/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


game_is_on = True


# -------Click the cookie div -------#
def click_cookie():
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

    
#---------Get the price of different items on the pane on the right--------#
def get_price():
    store_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
    prices = [item.text.split("-")[1].split(" ")[1] for item in store_items if item.text != ""]
    new = [item.replace(",000", "000") for item in prices]
    newer = [item.replace("123,456,789", "123456789") for item in new]
    prices = [int(num) for num in newer]
    return prices

  
# ----------Interaction----------------also-using-threading-to-define-the-function--------#
def buy_product():
    threading.Timer(5.0, buy_product).start()
    prices = get_price()
    for n in range(0, len(prices)):
        money = driver.find_element(By.ID, "money")
        money = int(money.text)
        store_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
        if prices[n] < money < prices[n+1]:
            product = store_items[n]
            print(f"Can afford {product.text}")
            product.click()

            
# ------------------call-the-fuction-outside-the-while-loop---------#
buy_product()

# -----------------run-and-end-the-game-in-5-minutes------------------------#
timeout = time.time() + 60*5
while game_is_on:
    click_cookie()
    if time.time() > timeout:
        # cookie_per_second = driver.find_element(By.ID, "cps")
        # print(cookie_per_second.text)
        break
