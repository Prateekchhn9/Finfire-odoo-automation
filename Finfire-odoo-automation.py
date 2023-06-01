
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver")

options= webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "c:\\Users\\Noran\\Desktop", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})




# FinFire credentials
Benutzername = "80034"
passwort = "Erfolgbergers0401#"
# initialize the Chrome driver
# put your chromdrive version in the directory of the file
driver.maximize_window()


# head to Finfire login page
import time


driver.get("https://finfire.de/app/docs/overview/all")
time.sleep(5)
# find username/email field and send the username itself to the input field
driver.find_element("id", "input-11").send_keys(Benutzername)
time.sleep(5)

# find password input field and insert password as well
driver.find_element("id", "input-12").send_keys(passwort)
time.sleep(5)

# click login buttoncontent
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
time.sleep(10)


all_a_tags= driver.find_elements(By.XPATH,"//a")
for a in all_a_tags:
            if a.get_attribute('href') and '/services/filestore/api/dokument/v2/binary/inline' in a.get_attribute('href'):
                a.click()
time.sleep(15)

while True:
    try:
        number_of_pages=driver.find_element(By.XPATH,"//button[@aria-label='Nächste Seite']")
        number_of_pages.click()
        time.sleep(20)
        all_a_tags= driver.find_elements(By.XPATH,"//a")
        for a in all_a_tags:
            if a.get_attribute('href') and '/services/filestore/api/dokument/v2/binary/inline' in a.get_attribute('href'):
                a.click()

    except:
        break


