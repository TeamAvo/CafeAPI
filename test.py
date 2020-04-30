from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def click(element):
    driver.execute_script("arguments[0].click();", element)


chrome_options = Options()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)

print("Initialized")

driver.get('https://avonoldfarms.flikisdining.com/menu/avon-old-farms?mode=browse')
driver.implicitly_wait(10)
driver.find_element_by_xpath("//button[@class='primary']").click()

print("Navigated to menu selection section")

driver.implicitly_wait(10)
driver.find_element_by_xpath("//li[@class='menu-item']//a").click()

print("Navigated to breakfast")

driver.implicitly_wait(10)
driver.find_elements_by_xpath("//ul[@class='nav-content']//li//a")[2].click()

print("Navigated to lunch")

driver.implicitly_wait(10)
click(driver.find_element_by_xpath("//li[@class='arrow']//a"))

print("Clicked element")

# driver.implicitly_wait(5)
# Select(driver.find_element_by_xpath("//select")).select_by_index(2)

driver.implicitly_wait(10)
driver.find_elements_by_xpath("//li[@class='day']//ul[li[@class='food text-links']]")

driver.implicitly_wait(10)
driver.find_elements_by_xpath("//li[@class='day']//h3")

driver.implicitly_wait(10)
week = driver.find_elements_by_xpath("//li[@class='day']//ul[@class='items']//li[@class='food text-links'] |"
                                     " //li[@class='day']//h3")


def package(elem_arr):
    for i, item in enumerate(elem_arr):
        elem_arr[i] = item.text

    val = {}
    day = ""
    for item in elem_arr:
        try:
            int(item[0])
            day = item
            val[day] = []
        except ValueError:
            val[day].append(item)
    return val


print(package(week))

# //*[contains(concat(' ', @class, ' '), ' Iknowthis_ ')]

#
#
# def arr_to_dict(a):
#     temp = {}
#     for i, k in enumerate(a):
#         temp[i] = k
#     return temp
#
#
# dictionary = arr_to_dict(arr)
#
# json_file = json.dumps(dictionary)
#
# print(json_file)

#
# def hrs_mins(t=None):
#     if not t:
#         hrs = datetime.datetime.now().time().hour
#         mins = datetime.datetime.now().time().minute
#         return (hrs * 100) + mins
#     hrs = int(str(t.time())[0:2])
#     mins = int(str(t.time())[3:5])
#     return (hrs * 100) + mins
#
#
# print(hrs_mins(None))

# print(list(range(6)))
# print(3 in range(6))
