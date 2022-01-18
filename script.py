from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
  
def main():
    while(True):
        # use appropriate driver for your browser
        driver = webdriver.Chrome(r'.\driver\chromedriver.exe')

        link = "http://localhost:15000/docs/index.html"
        driver.get(link)
        
        driver.maximize_window()
        
        try:
            post = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "operations-Mining-post_api_Mining_generate"))
            )
        except:
            driver.quit()
        post.click()


        try_it_out = driver.find_element(By.XPATH, "//button[@class='btn try-out__btn']")
        try_it_out.click()

        parameter = driver.find_element(By.XPATH, "//textarea[@class='body-param__text']")
        parameter.clear()
        
        # use your prefered block count
        parameter.send_keys('{\n  "blockCount": 10000}\n}')

        execute = driver.find_element(By.XPATH, "//div[@class='execute-wrapper']/button")
        execute.click()
        time.sleep(3)
        
        # close browser
        driver.quit()
        
        # set the interval to trigger mine command with your prefered time
        # e.g it waits for 30 minutes and trigger again
        time.sleep(300)
        
        
        
        
if __name__ == "__main__":
    main()
    
    

input()