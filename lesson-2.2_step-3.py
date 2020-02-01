from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, math

# Функция расчета суммы
def calc(x, y):
    return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элементов с x и y значения
    x_element = browser.find_element_by_css_selector("h2 > span#num1")
    y_element = browser.find_element_by_css_selector("h2 > span#num2")
    # Получение данных x и y
    x = x_element.text
    y = y_element.text
    # Вызов функции для отображения результата
    result = calc(x, y)

    # Код, который заполняет обязательные поля
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)
    #select.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type=\"Submit\"].btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()