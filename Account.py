import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Jpetstoredemo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
    
    #If error, possibly from the web

    def test_1_creating_account(self):
        web = self.browser
        web.get("https://petstore.octoperf.com/actions/Catalog.action")
        web.maximize_window()
        time.sleep(3)

        #homepage
        web.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/a[2]").click()
        time.sleep(3)
        web.find_element(By.XPATH,"/html/body/div[2]/div/a").click()
        time.sleep(3)

        #account information

        #User ID
        #different user each run
        web.find_element(By.NAME,'username').send_keys("Coconut20")
        time.sleep(3)
        #New password
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[1]/tbody/tr[2]/td[2]/input').send_keys("123")
        time.sleep(3)
        #Repeat password
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[1]/tbody/tr[3]/td[2]/input').send_keys("123")
        time.sleep(3)
        #First name
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[1]/td[2]/input').send_keys("test")
        time.sleep(3)
        #Last name
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input').send_keys("test")
        time.sleep(3)
        #Email
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[3]/td[2]/input').send_keys("test@gmail.com")
        time.sleep(3)
        #Phone
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[4]/td[2]/input').send_keys("123")
        time.sleep(3)
        #Address 1
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[5]/td[2]/input').send_keys("test")
        time.sleep(3)
        #City
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[7]/td[2]/input').send_keys("test")
        time.sleep(3)
        #State
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[8]/td[2]/input').send_keys("test")
        time.sleep(3)
        #Zip
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[9]/td[2]/input').send_keys("123")
        time.sleep(3)
        #Country
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[10]/td[2]/input').send_keys("test")
        time.sleep(3)

        #Favourite Category
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/select/option[2]').click()
        time.sleep(3)

        #Save
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/input').click()

        #Validation
        assert web.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/a/img")

    def test_2_fail_login(self):
        #Pre-condition
        web = self.browser
        web.get("https://petstore.octoperf.com/actions/Catalog.action")
        web.maximize_window()
        time.sleep(3)

        #Login page
        web.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/a[2]").click()
        time.sleep(3)

        #username
        web.find_element(By.NAME,"username").send_keys("Coconut20")
        #password
        web.find_element(By.NAME,"password").send_keys("Coconut20")
        #login
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/input").click()

        #Validation
        assert web.find_element(By.XPATH,"/html/body/div[2]/ul/li")


    def test_3_success_login(self):
        #Pre-condition
        web = self.browser
        web.get("https://petstore.octoperf.com/actions/Catalog.action")
        web.maximize_window()
        time.sleep(3)

        #Login page
        web.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/a[2]").click()
        time.sleep(3)

        #username
        web.find_element(By.NAME,"username").send_keys("Coconut20")
        #password
        web.find_element(By.NAME,"password").send_keys("123")
        #login
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/input").click()

        #Validation
        assert web.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/a/img")
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
