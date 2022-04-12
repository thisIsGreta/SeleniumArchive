from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InternetSpeedTwitterBot:
    def __init__(self, driver, down, up):
        self.driver = driver
        self.down = down
        self.up = up

    def twitter_login(self, driver, email, password):
        login_page = "https://twitter.com/i/flow/login"
        driver.get(login_page)
        sleep(5)
        input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 "
                                                       "r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l "
                                                       "r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"))
        )
        input.click()
        input.send_keys(email)

        next = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/'
                                             'div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next.click()
        
        sleep(5)
        password = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/'
                                                 'div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[1]')
        password.click()
        password.send_keys(password)

        login = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/'
                                              'div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div')
        login.click()

    def get_internet_speed(self, driver):
        hit_go = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/'
                                               'div/div[2]/div[3]/div[1]/a/span[4]')
        hit_go.click()
        sleep(70)
        speed_down = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                           'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))
        )
        speed_up = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                           'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'))
        )
        return speed_down, speed_up

    def tweet_at_provider(self, driver, down, up):
        write_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/'
                                                  'header/div/div/div/div[1]/div[3]/a/div'))
        )
        write_button.click()

        type = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
                (By.XPATH,         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/'
                                   'div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/'
                                   'div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div'))
        )
        type.send_keys(f"down: {down}; up: {up} #100DaysofCode #Day51 #InternetSpeedTestBot")

        post = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/'
                           'div/div/div[2]/div/div/div/div/div[3]/div'))
        )
        post.click()

        
