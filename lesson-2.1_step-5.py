from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    ans = browser.find_element_by_css_selector("input#answer.form-control[required]")
    ans.send_keys(y)
    checkrobot = browser.find_element_by_css_selector(".form-check > input#robotCheckbox")
    checkrobot.click()
    robotsrule = browser.find_element_by_css_selector(".form-check > label[for=\"robotsRule\"]")
    robotsrule.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
