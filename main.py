import json
from outscraper import ApiClient
from selenium import webdriver
from time import sleep

api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMTAxNDk2MDA0Mjg2MDE1ODYzOTJ8ZjAxNDBhOTUyZQ')
maps_result = api_client.google_maps_search('')

with open('maps_results.json','w') as file: 
    json.dump(maps_result, file, indent=5)

driver=webdriver.Chrome("C:/Users/taysi/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.google.com/maps/@43.7321301,-79.2563908,15z")
sleep(2)

def search():
    place=driver.find_element("name","q")
    place.send_keys("")
    submit=driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()
search()
sleep(100)
