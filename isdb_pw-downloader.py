from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import urllib.request

# Scraping Isdb.pw with Selenium

driver = webdriver.Chrome('/your_path_to/chromedriver')
driver.get("https://isdb.pw/user/profile")

username = driver.find_element_by_id("login")
username.clear()
username.send_keys("your_email")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("your_password")


driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

user_stories = driver.find_element_by_id("search_story_name")
user_stories.clear()
user_stories.send_keys("your_target")

driver.find_element_by_id("search_story").click()

while True:
    try:
        loadMoreButton = driver.find_element_by_id("load_more_button")
        time.sleep(0.5)
        loadMoreButton.click()
        time.sleep(1.5)
    except Exception as e:
        print(e)
        break
    
element = driver.find_element_by_xpath("/html/body/header/div/div[2]/div/div[2]/div")
hrefs = [x.get_attribute('href') for x in element.find_elements_by_css_selector('a')]


# Getting the images and videos of each URL

def dummy(url):
    driver.set_page_load_timeout(15)
    driver.get(url)
    try:
        element = driver.find_element_by_xpath("/html/body/header/div/div/div/div[2]/div/div")
        video = driver.find_element_by_tag_name('source').get_attribute('src')
        return video
    except NoSuchElementException: # If it's not a video then it's an image
        element = driver.find_element_by_xpath("/html/body/header/div/div/div/div[2]/div/div")
        products = driver.find_elements_by_css_selector("img[itemprop='image']")
        for product in products:
            return (product.get_attribute("src"))
    
listeV = []
for i in hrefs:
    listeV.append(dummy(i))


# Save JPG and MP4

def download_image_solo(url):
    t= datetime.now()
    img_name = str(t.day) + "." + str(t.month) + "." + str(t.year) + " - " + str(t.hour) + "." + str(t.minute) + "." + str(t.second)
    path = 'the_folder_you_want'
    full_name = img_name + ".jpg"
    urllib.request.urlretrieve(url, path+full_name)
def download_video(url):
    t= datetime.now()
    vid_name = str(t.day) + "." + str(t.month) + "." + str(t.year) + " - " + str(t.hour) + "." + str(t.minute) + "." + str(t.second)
    path = 'the_folder_you_want'
    full_name = vid_name + ".mp4"
    urllib.request.urlretrieve(url, path+full_name)

for i in listeV:
    if i[-3:] == 'mp4':
        download_video(i)
    elif i[-3:] == 'jpg':
        download_image_solo(i)

 