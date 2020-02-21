import json
import requests
import time
import urllib.request
import webbrowser
from datetime import datetime
from selenium import webdriver

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

driver = webdriver.Chrome(PATH)
driver.get('https://instagram.com/username/')

scroll_pause = 1.5
user_url_link = []
user_url_post = []
counter = 1

for i in range(number):
  
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
  time.sleep(scroll_pause)
  
  print(counter)
  counter += 1
  
  article = driver.find_element_by_tag_name('article')
  list_cards = article.find_elements_by_tag_name('a')
  
  for item in list_cards:
  
    url_link = item.get_attribute('href')
    user_url_link.append(url_link)
    
    temp_list = url_link.rsplit('/', 2)
    user_url_post.append(temp_list[1])
    
# the loop makes duplicate so we do this :
new_list = user_url_post
new_list = list(dict.fromkeys(new_list))
add_before = 'https://www.instagram.com/p/'
add_after = '?__a=1'

time.sleep(1)

empty_list = []
for i in new_list:
  empty_list.append(add_before+i+add_after)

data_empty = []
data_empty2 = []
data_empty3 = []

for i in empty_list:
  r = requests.get(i)
  data = r.json()
  
  data_test = data['graphql']['shortcode_media']['__typename']
  if data_test == 'GraphImage':
     data_empty2.append(data['graphql']['shortcode_media']['display_resources'][2])
     
     data_test3 = data_empty2
     dico = {}
     container1 = []
     for i in data_test3:
      for k, v in i.items():
        if k == 'src':
          dico[k] = v
      container1.append(dico.get('src'))
  
  elif data_test == 'GraphSidecar':
    data_test = data['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
    
    for i in range(len(data_test)):
      if data_test[i]['node']['is_video'] == True:
        data_empty3.append(data_test[i]['node']['video_url']
      elif data_[i]['node']['is_video'] == False:
        data_empty.append(data_test[i]['node']['display_resources'][2])
        
    data_test2 = data_empty
    dico = {}
    container2 = []
    for i in data_test2:
      for k, v in i.items():
        if k == 'src':
          dico[k] = v
      container2.append(dico.get('src'))
      
fcontainer1 = container1
fcontainer2 = container2
fcontainer3 = data_empty3

# functions to save images and videos
def download_image(url):
  t = datetime.now(
  img_name = str(t.day) + '.' + str(t.month) + '.' + str(t.year) + '-' + str(t.hour) + '.' + str(t.minute) + '.' + str(t.second)
  path = 'yourpath'
  full_name = img_name + '.jpg'
  urllib.request.urlretrieve(url, path+full_name)

def download_video(url):
  t = datetime.now(
  img_name = str(t.day) + '.' + str(t.month) + '.' + str(t.year) + '-' + str(t.hour) + '.' + str(t.minute) + '.' + str(t.second)
  path = 'yourpath'
  full_name = img_name + '.mp4'
  urllib.request.urlretrieve(url, path+full_name)
  
for i in fcontainer1:
  download_image(i)
  time.sleep(2)
  
for i in fcontainer2:
  download_image(i)
  time.sleep(2)
  
for i in fcontainer3:
  download_image(i)
  time.sleep(2)