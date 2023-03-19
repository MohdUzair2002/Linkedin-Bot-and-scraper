from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)

driver.get("https://www.linkedin.com/in/norman-heurtematte-15ba158a/recent-activity/shares/")
name_person= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='update-components-actor__title']")))
i=0
main_data=[]
while(i<5):
    data=[]
    name_person=driver.find_elements(By.XPATH,"//span[@class='update-components-actor__title']")[i].text
    print(name_person)
    paragraph=driver.find_elements(By.XPATH,"//span[@class='break-words']")[i].text
    print(paragraph)
    occupation=driver.find_elements(By.XPATH,"//*[contains(@class, 'update-components-actor__description t-12 t-normal')]")[i].text
    print(occupation)
    time_=driver.find_elements(By.XPATH,"//*[contains(@class, 'update-components-text-view white-space-pre-wrap break-words')]//span[@aria-hidden='true']")[i].text
    print(time)
    like_button=driver.find_elements(By.XPATH,"//span[@class='reactions-react-button feed-shared-social-action-bar__action-button']//span[contains(@class,'artdeco-button__text react-button__text')]")[i]
    driver.execute_script("arguments[0].click();", like_button)
    data.append(name_person)
    data.append(paragraph)
    data.append(occupation)
    data.append(time_)
    main_data.append(data)
    i+=1
header = ['Name','Paragraph','Occupation','Time']
with open('data1.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(main_data)  

time.sleep(1000)