from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import SessionNotCreatedException

"""
Scriptet måste köras med Mozilla Firefox, och geckodriver inlagd i PATH
"""


driver = webdriver.Firefox()
css = driver.find_element_by_css_selector
xpath = driver.find_element_by_xpath
classname = driver.find_element_by_class_name
name = driver.find_element_by_name
id = driver.find_element_by_id

#Ersätt Username med ditt datorid, Password med ditt lösenord.
#Exempel:
#username = "johndoe"
#password = "anonymous" 
username = "johndoe"
password = "anonymous"


def main():
    try:
        driver.get("https://kronox.mah.se/index.jsp")
        classname('signin').click()
        name('username').send_keys(username)
        name('password').send_keys(password)
        id('login_button').click()
        css("li.tab:nth-child(11)>a:nth-child(1)>em:nth-child(1)").click()
        css(".knapp-anmal").click()
        driver.close()
        driver.quit()
    except NoSuchElementException:
        print("Ingen Tenta att boka")
        driver.close()
        driver.quit()

main()
