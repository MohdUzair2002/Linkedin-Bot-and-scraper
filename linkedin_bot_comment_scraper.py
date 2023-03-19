from selenium import webdriver
import time
import requests
import csv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

links=[]
comments_name_l=[]
commenter_occupation_l=[]
comment_text_l=[]
no_of_likes_l=[]
no_of_replies_l=[]
main_data=[]

chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)

driver.get("https://www.linkedin.com/in/norman-heurtematte-15ba158a/recent-activity/shares/")
time.sleep(10)
i=0
while(i<5):
    
    menu_button= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class,'feed-shared-control-menu__trigger artdeco-button artdeco-button--tertiary artdeco-button--muted artdeco-button--1 artdeco-button--circle artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view')]")))
    menu_button=driver.find_elements(By.XPATH,"//button[contains(@class,'feed-shared-control-menu__trigger artdeco-button artdeco-button--tertiary artdeco-button--muted artdeco-button--1 artdeco-button--circle artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view')]")[i]
    driver.execute_script("arguments[0].click();", menu_button)

    copy_link=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[contains(@class,'feed-shared-control-menu__item')]")))
    copy_link=driver.find_elements(By.XPATH,"//li[contains(@class,'feed-shared-control-menu__item')]")[1].click()
    # driver.execute_script("arguments[0].click();", copy_link)
    
    link=pyperclip.paste()
    links.append(link) 
    print(i+1)   
    print(pyperclip.paste())
    time.sleep(3)
    i+=1
j=0
while(j<5):
    i=0
    driver.get(links[j])
    data=[]
    while(i<5):

        
        try:
            
            comments_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'comments-comment-item__post') and contains(@class,'comments-comment-item')]//span[@class='comments-post-meta__name-text hoverable-link-text']")))
            comments_name=driver.find_elements(By.XPATH,"//div[contains(@class,'comments-comment-item__post') and contains(@class,'comments-comment-item')]//span[@class='comments-post-meta__name-text hoverable-link-text']")[i]
            comments_name_l.append(comments_name.text)
        

            commenter_occupation=driver.find_elements(By.XPATH,"//div[contains(@class,'comments-comment-item__post') and contains(@class,'comments-comment-item')]//span[contains(@class,'comments-post-meta__headline t-12 t-normal')]")[i]
            commenter_occupation_l.append(commenter_occupation.text)
            

            comment_text=driver.find_elements(By.XPATH,"//div[contains(@class,'comments-comment-item-content-body break-words')]//div[contains(@class,'update-components-text relative')]")[i]
            comment_text_l.append(comment_text.text)
            
            no_of_likes=driver.find_elements(By.XPATH,"//div[contains(@class,'comments-comment-item__social-actions') and not(contains(@class, 'reply'))]//span[contains(@class,'v-align-middle pl1')]")[i]
            no_of_likes_l.append(no_of_likes.text)

            no_of_replies=driver.find_elements(By.XPATH,"//div[contains(@class,'comments-comment-item__social-actions') and not(contains(@class, 'reply'))]//span[contains(@class,'comments-comment-social-bar__replies-count')]")[i]
            no_of_replies_l.append(no_of_likes.text)
          
            
            i+=1
        except:
            if(i==0):
                i=i+5
            comments_name_l.append("-")
            commenter_occupation_l.append("-")
            comment_text_l.append("-")
            no_of_likes_l.append("-")
            no_of_replies_l.append("-")

            
            i+=1
    data.append(comments_name_l)
    data.append(commenter_occupation_l)
    data.append(comment_text_l)
    data.append(no_of_likes_l)
    data.append(no_of_replies_l)
    
    main_data.append(data)
    data=[]
        
    comments_name_l=[]
    commenter_occupation_l=[]
    comment_text_l=[]
    no_of_likes_l=[]
    no_of_replies_l=[]
    j+=1
print(links)
header = ['Commenter Name','Commenter Details','Comment Text','No of Likes','No of Replies']
with open('comment_data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(main_data) 
