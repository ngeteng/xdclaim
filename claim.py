import undetected_chromedriver as uc
uc.install()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re

opts = webdriver.ChromeOptions()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_argument("disable-infobars")
opts.add_argument("--disable-extensions")
prefs = {'profile.default_content_setting_values': {'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
opts.add_experimental_option("prefs", prefs)


def open_browser():
    
    global browser

    random_angka = random.randint(100,999)
    random_angka_dua = random.randint(10,99)
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka}.{random_angka_dua} Safari/537.36")
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc)
    browser.get("https://mail.ledgermail.io/auth/login")
    print('\033[93m[*] Trying to Login')
    loggok()

def loggok():

    input_email = wait(browser,32).until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-17']")))
    input_email.send_keys(email)
    input_pw = wait(browser,32).until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-20']")))
    input_pw.send_keys(password)
    input_memon = wait(browser,32).until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-24']")))
    input_memon.send_keys(memonicid)
    loggen = wait(browser,32).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Sign In')]"))).click()
    Claim()

def Claim():
    print("\033[93m[*] \033[32mTrying to Claim!")
    sleep(5)
    trying = 0
    while True:
        if trying == 30:
            print("\033[93m[*] Please Run Again!")
            break
        try:
            try:
                wait(browser,32).until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Claim 10XDC')]"))).click()
                sleep(2)
                print("\033[93m[*] \033[32mCoba Claim !")
            except:
                try:
                    wait(browser,32).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Sign In')]"))).click()
                    sleep(2)
                    print("\033[93m[*] \033[31mLogin lagi dong!!")
                except:
                    try:
                        wait(browser,32).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Email is required')]")))
                        sleep(2)
                        print("\033[93m[*] \033[31mlogin lagi asu !")
                        loggok()
                    except:
                        pass
        except:
            print("\033[93m[*] Trying Again to Verify!")
        trying = trying + 1

if __name__ == '__main__':
    global email
    global password
    global memonicid
    
    print('\033[93m[*] \033[32mAutomation Claim Xdc')
    print('\033[93m[*] \033[32mTelegram: @bangkit')
    print('\033[93m[*] \033[32mGithub: https://github.com/ngeteng')
    print('\033[93m[*] \033[32mWebsite: https://www.sans.eu.org')
    email = input(str("\033[93m[*] \033[32mEmail:"))
    password = input(str("\033[93m[*] \033[32mPassword: "))
    memonicid = input(str("\033[93m[*] \033[32mMemo: "))
    open_browser()