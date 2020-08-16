from selenium import webdriver
import time
from datetime import datetime
import urllib.request

driver = webdriver.Chrome(path)
driver.get('dummy_scrape')

element = driver.find_element_by_xpath('//*[@id="collection-module-1532039018217"]/div')
links = [elem.get_attribute("href") for elem in element.find_elements_by_tag_name('a')]


links = list(dict.fromkeys(links))

def dummy(url):
    driver.get(url)
    element = driver.find_element_by_xpath('//*[@id="shopify-section-product-template"]/div/section/div/div[2]/div[1]/div[1]/div')
    hrefs = [elem.get_attribute("href") for elem in element.find_elements_by_tag_name('a')]
    return hrefs

listeV = []
for i in links:
    if i == links[-1]:
        break
    else:
        listeV.append(dummy(i))
        
def download_image(url):
    t= datetime.now()
    img_name = str(t.day) + "." + str(t.month) + "." + str(t.year) + " - " + str(t.hour) + "." + str(t.minute) + "." + str(t.second)
    path = 'path'
    full_name = img_name + ".jpg"
    urllib.request.urlretrieve(url, path+full_name)

merge_list = [item for sublist in listeV for item in sublist]

for i in merge_list:
    download_image(i)
    time.sleep(1.5)

