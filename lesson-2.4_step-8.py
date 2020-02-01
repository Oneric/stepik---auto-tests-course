from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Отправляем заполненную форму
    book = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
    book = browser.find_element_by_id("book")
    book.click()

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    ans = browser.find_element_by_css_selector("input#answer.form-control[required]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", ans)
    ans.send_keys(y)


    # Отправляем заполненную форму
    submit = browser.find_element_by_css_selector("button.btn#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
