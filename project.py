import selenium
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

email='youremail'
password='yourpassword'

path = "C:/Users/ADMIN/Desktop/subjects/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://twitter.com/i/flow/login")
driver.maximize_window()

def login():
    user = driver.find_element_by_xpath('//input[@name="username"]')
    user.send_keys(email)

login()
driver.find_element_by_xpath('//div[@class="css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]').click()
def passw():
    
    passw = driver.find_element_by_xpath('//input[@type="password"]')
    time.sleep(3)
    passw.send_keys(password)
passw()

driver.find_element_by_xpath('//div[@class="css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]').click()

sea = 'Whatyouwanttosearch'

def search():
    
    box = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-14lw9ot.r-gtdqiz.r-1gn8etr.r-1g40b8q > div.css-1dbjc4n.r-136ojw6 > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1777fci > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-16y2uox.r-1wbh5a2.r-4amgru.r-itp27i > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > input")
    box.send_keys(sea)
    box.send_keys(Keys.RETURN)

search()
for i in range(1,3):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
likes = driver.find_elements_by_xpath('//div[@data-testid="like"]')
for like in likes:
    like.click()
    time.sleep(15)
    
    
    

    
