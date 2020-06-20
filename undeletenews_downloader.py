from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import urllib.request

# Phase 1

# Options for ChromeDriver
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

driver = webdriver.Chrome('your_path', chrome_options=opt)
driver.get("https://undelete.news/#/")
           
# Step 1
driver.find_element_by_xpath("//*[@id='header']/nav/div/div[3]/div/div[1]/form").click()
driver.find_element_by_xpath("//*[@id='header']/nav/div/div[3]/div/div[1]/form/div[2]").click()

# Step 2
driver.find_element_by_xpath("//*[@id='easySearch']").clear()
driver.find_element_by_xpath("//*[@id='easySearch']").send_keys("type_something")

# Step 3
time.sleep(3)
driver.find_element_by_xpath("//*[@id='eac-container-easySearch']/ul/li[1]/div/div/a/div[2]/div[1]/span[1]").click()

# Step 4
new_tab = driver.window_handles
driver.switch_to.window(new_tab[1])

# Step 5
link = driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[2]/div[2]/div[1]/a")
open_link = (link.get_attribute('href'))




# Phase 2

driver = webdriver.Chrome('your_path', chrome_options=opt)
driver.get(open_link)
          
scroll_pause = 1.5

for i in range(5):
  
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(scroll_pause)
    
path_of_link = driver.find_element_by_xpath("//*[@id='v-app']/div")
hrefs = [x.get_attribute('href') for x in path_of_link.find_elements_by_css_selector('a')]
print(hrefs)




# Phase 3

opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'DuckDuckBot')

def download_video(url):
    t = datetime.now()
    img_name = str(t.day) + '.' + str(t.month) + '.' + str(t.year) + '-' + str(t.hour) + '.' + str(t.minute) + '.' + str(t.second)
    path = 'name_path'
    full_name = img_name + '.mp4'
    filename, headers = opener.retrieve(url, path+full_name)

driver = webdriver.Chrome('your_path', chrome_options=opt)
driver.get(hrefs[0])
counter = 0

def dummy(url):
    
    # The idea is to find the xpath of the video 
    # So you have to inspect the page to find it
    # I've put an example here of what it looks like
    try:
        element = driver.find_element_by_xpath("//*[@id='stories-container']/div[3]/div/video")
        video = element.get_attribute('src')
        return download_video(man)
    except NoSuchElementException:
        return None
        
for i in range(len(hrefs)):
    
    dummy(hrefs[i])
           
    driver.find_element_by_xpath("//*[@id='stories-container']/div[3]/div/div[2]/div[3]").click()
    counter += 1
    time.sleep(2)
    
    if counter == 12:
        counter = 0
        driver = webdriver.Chrome('your_path', chrome_options=opt)
        driver.get(hrefs[i])
        
        dummy(hrefs[i])
           
        driver.find_element_by_xpath("//*[@id='stories-container']/div[3]/div/div[2]/div[3]").click()
        time.sleep(3)
