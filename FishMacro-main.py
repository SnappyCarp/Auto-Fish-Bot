from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeOptions
from selenium import webdriver
from math import inf
import json, time
from playsound import playsound as Sound

'''
Thanks For Downloading This Program :)

if you hear a 'ding' that means you need to solve a captcha
'''




options=EdgeOptions()
options.use_chromium = True
options.add_argument('log-level=3')
#options.add_argument("headless")
options.add_argument("disable-gpu")
ServerId = 'Enter Server Id'
ChannelId = 'Enter Channel Id'


def verf(mId):
    addStr = f'chat-messages-{ChannelId}-{mId}'
    items = driver.find_elements_by_tag_name("li")
    for item in items:
        inHtml = str(item.get_attribute("innerHTML"))
        AntiB = '''role="button"><img alt="Anti-bot
/verify <result>"'''
        if addStr and AntiB in inHtml:
            Sound('ding.mp3')
    

def fish():
    ActionChains(driver).move_to_element(driver.find_element_by_css_selector('.textArea-2CLwUE')).click().perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys('/fish').perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1.2)
    LatestXPATH=str("""//ol[@data-list-id="chat-messages"]/li[last()]//div[contains(@class,'messageContent')]""")
    LatestMsg=str(driver.find_element(By.XPATH,LatestXPATH).get_attribute('id').replace('message-content-',''))
    verf(LatestMsg)


try:
    #Logging In
    with open('creds.json','r') as f:data=json.load(f)
    global driver
    driver = webdriver.Chrome("Path To Microsoft Edge Driver.exe", options=options)
    driver.get(f'https://discord.com/login?redirect_to=%2Fchannels%2F{ServerId}%2F{ChannelId}')
    LogBtn='//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]'
    WebDriverWait(driver, inf).until(EC.presence_of_element_located((By.XPATH,LogBtn)))
    #Fill The Password And Username Forms
    driver.find_element_by_name('email').send_keys(data['Username'])
    driver.find_element_by_name('password').send_keys(data['Password'])
    #Click The Login Button
    driver.find_element_by_xpath(LogBtn).click()
    WebDriverWait(driver, inf).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.textArea-2CLwUE')))
    fish()
except NoSuchWindowException: exit(1)
except Exception as e: print(e)
