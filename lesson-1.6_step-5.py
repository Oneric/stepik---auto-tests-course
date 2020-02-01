from selenium import webdriver

link = "https://www.degreesymbol.net/"

with webdriver.Chrome() as browser:
    browser.get(link)
    t = browser.find_element_by_link_text("» Degree symbol examples")
    browser.click()
