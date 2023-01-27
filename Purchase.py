import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Jpetstoredemo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_1_add_cart_item(self):
        #Pre-condition
        web = self.browser
        web.get("https://petstore.octoperf.com/actions/Catalog.action")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/a[2]").click()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Coconut20")
        web.find_element(By.NAME,"password").send_keys(Keys.CONTROL,"a")
        web.find_element(By.NAME,"password").send_keys(Keys.DELETE)
        web.find_element(By.NAME,"password").send_keys("123")
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/input").click()

        #Dogs catalog
        web.find_element(By.XPATH,"//div[@id='QuickLinks']//img[@src='../images/sm_dogs.gif']").click()
        time.sleep(3)
        #golden retriver
        web.find_element(By.XPATH,"/html/body/div[2]/div[2]/table/tbody/tr[5]/td[1]/a").click()
        time.sleep(3)
        #add
        web.find_element(By.XPATH,"/html/body/div[2]/div[2]/table/tbody/tr[2]/td[5]/a").click()
        time.sleep(3)
       
        #Validation
        assert web.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[2]/td[3]")


    def test_2_purchase_item(self):
        #Pre-condition
        web = self.browser
        web.get("https://petstore.octoperf.com/actions/Catalog.action")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/a[2]").click()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Coconut20")
        web.find_element(By.NAME,"password").send_keys(Keys.CONTROL,"a")
        web.find_element(By.NAME,"password").send_keys(Keys.DELETE)
        web.find_element(By.NAME,"password").send_keys("123")
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/input").click()
        web.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/a[2]').click()
        web.find_element(By.XPATH,"/html/body/div[2]/div[2]/table/tbody/tr[5]/td[1]/a").click()
        web.find_element(By.XPATH,"/html/body/div[2]/div[2]/table/tbody/tr[2]/td[5]/a").click()
        time.sleep(3)

        #checkout
        web.find_element(By.XPATH,'//*[@id="Cart"]/a').click()
        time.sleep(3)

        #Payment Detail

        #Card
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/table/tbody/tr[2]/td[2]/select/option[1]").click()
        time.sleep(3)
        #Card Number
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/table/tbody/tr[3]/td[2]/input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/table/tbody/tr[3]/td[2]/input").send_keys(Keys.DELETE)
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/table/tbody/tr[3]/td[2]/input").send_keys("999 9999 9999 9999")
        time.sleep(3)
        #Expiry date
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/table/tbody/tr[4]/td[2]/input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/table/tbody/tr[4]/td[2]/input").send_keys(Keys.DELETE)
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/table/tbody/tr[4]/td[2]/input").send_keys("05/23")
        time.sleep(3)

        #First name
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[6]/td[2]/input').send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[6]/td[2]/input').send_keys(Keys.DELETE)
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[6]/td[2]/input').send_keys("test")
        time.sleep(3)
        #Last name
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[7]/td[2]/input').send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[7]/td[2]/input').send_keys(Keys.DELETE)
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[7]/td[2]/input').send_keys("test")
        time.sleep(3)
        #Address 1
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[8]/td[2]/input').send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[8]/td[2]/input').send_keys(Keys.DELETE)
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[8]/td[2]/input').send_keys("test")
        time.sleep(3)
        #City
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[10]/td[2]/input').send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[10]/td[2]/input').send_keys(Keys.DELETE)
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[10]/td[2]/input').send_keys("test")
        time.sleep(3)
        #State
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[11]/td[2]/input').send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[11]/td[2]/input').send_keys(Keys.DELETE)
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[11]/td[2]/input').send_keys("test")
        time.sleep(3)
        #Zip
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[12]/td[2]/input').send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[12]/td[2]/input').send_keys(Keys.DELETE)
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[12]/td[2]/input').send_keys("123")
        time.sleep(3)
        #Country
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[13]/td[2]/input').send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[13]/td[2]/input').send_keys(Keys.DELETE)
        web.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tbody/tr[13]/td[2]/input').send_keys("test")
        time.sleep(3)

        #Submit
        web.find_element(By.XPATH,"/html/body/div[2]/div/form/input").click()
        time.sleep(3)

        #Confirm purchase
        web.find_element(By.XPATH,"/html/body/div[2]/div[2]/a").click()
        time.sleep(3)

        #Validation
        assert web.find_element(By.XPATH,"/html/body/div[2]/ul/li")

    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
