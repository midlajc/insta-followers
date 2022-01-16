from selenium import webdriver
from time import sleep
from secrets import pw
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        self.username = username
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element(By.XPATH,'//input[@name="username"]').send_keys(
            username
        )
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys(pw)
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element(By.XPATH,
            "/html/body/div[1]/section/main/div/div/div/div/button"
        ).click()
        sleep(4)
        self.driver.find_element(By.XPATH,
            "//button[contains(text(), 'Not Now')]"
        ).click()
        sleep(2)

    def get_unfollowers(self):
        # self.driver.find_element(By.XPATH,
        #     "//a[contains(@href,'/{}')]".format(self.username)
        # ).click()
        self.driver.get("https://www.instagram.com/_midlaj_c/")
        sleep(3)
        self.driver.find_element(By.XPATH,"//a[contains(@href,'/following')]").click()
        print("no of following:")
        following = self._get_following_names()
        self.driver.find_element(By.XPATH,"//a[contains(@href,'/followers')]").click()
        print("no of followers:")
        followers = self._get_followers_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_followers_names(self):
        sleep(2)
        scroll_box = self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[3]")
        last_ht,ht=0,1
        while last_ht!=ht:
            last_ht=ht
            sleep(2)
            ht=self.driver.execute_script("""
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
        # sleep(20)
        links = scroll_box.find_elements_by_tag_name('a')
        # print(links)
        names = {name.text for name in links if name.text != ""}
        x = len(names)
        print(x)
        # close button
        self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[1]/div/div[2]/button"
        ).click()
        return names

    def _get_following_names(self):
        sleep(2)
        #/html/body/div[6]/div/div/div[2]/ul
        #/html/body/div[6]/div/div/div[3]
        #/html/body/div[6]/div/div/div[2]/ul/div
        #/html/body/div[6]/div/div/div[2]
        #/html/body/div[6]/div/div/div[2]/ul/div
        #/html/body/div[6]/div/div/div[2]
        scroll_box = self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[3]")
        last_ht,ht=0,1
        while last_ht!=ht:
            last_ht=ht
            sleep(2)
            ht=self.driver.execute_script("""
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
            #/html/body/div[6]/div/div/div[3]
        scroll_box = self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[2]")
        #sleep(20)
        print(scroll_box)
        links = scroll_box.find_element_by_tag_name('a')
        # print(links)
        names = {name.text for name in links if name.text != ""}
        x = len(names)
        print(x)
        # close button
        self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[1]/div/div[2]/button"
        ).click()
        return names


my_bot = InstaBot("_midlaj_c", pw)
my_bot.get_unfollowers()
