from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# A class that crawls through the flik website to retrieve the menus
class Crawler:
    def __init__(self):
        self.buttons = []
        self.menu = []

        # chrome_options to run the crawler headless (without window) with Chrome
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.set_headless()

        # firefox_options to run the crawler headless with Firefox
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_headless()

        # Declare the driver to control the browser
        self.driver = webdriver.Firefox(firefox_options=firefox_options)

        print("Crawler: Initiated Driver")

    def nav(self):
        # Navigate to the Flik Dining website
        self.driver.get('https://avonoldfarms.flikisdining.com/menu/avon-old-farms?mode=browse')

        # Click on a button to go to the menus
        self.driver.implicitly_wait(60)
        self._click(self.driver.find_element_by_xpath("//button[@class='primary']"))

        print("Crawler: Navigated to website")

        # --------------------- Breakfast ------------------------
        # Select the breakfast menu from the list of menus
        self.driver.implicitly_wait(60)
        self._click(self.driver.find_element_by_xpath("//li[@class='menu-item']//a"))

        # TODO: Comment this out to reflect the correct menu for this week

        wait = WebDriverWait(self.driver, 60)

        for _ in range(6):
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loading')))
            self.driver.implicitly_wait(60)
            self._click(self.driver.find_element_by_xpath("//li[@class='arrow']//a"))

        print("Crawler: Navigated to Breakfast")

        # TODO: Get the menus for the entire month
        # self.driver.implicitly_wait(5)
        # Select(self.driver.find_element_by_xpath("//select")).select_by_index(2)

        # Get the information from the web menus
        self.driver.implicitly_wait(60)
        week = self._get_menu()

        # Adds the breakfast foods to the crawler's menu
        self.menu.append(self._package(week))

        del week
        print("Crawler: Got Breakfast Data")

        # --------------------- Lunch ------------------------
        # Go to the Lunch menu
        self.driver.implicitly_wait(60)
        self._click(self.driver.find_elements_by_xpath("//ul[@class='nav-content']//li//a")[1])

        print("Crawler: Navigated to Lunch website")

        # Get the foods and dates from the Lunch menu
        self.driver.implicitly_wait(60)
        week = self._get_menu()

        # Add the Lunch menu to the crawler's menu
        self.menu.append(self._package(week))

        del week
        print("Crawler: Got Lunch Data")

        # --------------------- Dinner ------------------------
        # Go to the Dinner menu
        self.driver.implicitly_wait(60)
        self._click(self.driver.find_elements_by_xpath("//ul[@class='nav-content']//li//a")[2])

        print("Crawler: Navigated to Dinner website")

        # Get the foods and dates from the Dinner menu
        self.driver.implicitly_wait(60)
        week = self._get_menu()

        # Add the Dinner menu to the crawler's menu
        self.menu.append(self._package(week))

        del week
        print("Crawler: Got Dinner data")

    # TODO: Delete entries with empty brackets, []
    # Packages the data into a list of dictionaries
    # Keys: First three letters of the respective days with the first letter capital
    # Values: List of foods for that day
    def _package(self, text_arr):
        val = {}
        day = ""
        for item in text_arr:
            try:
                int(item[0])
                day = item[-3:]
                val[day] = []
            except ValueError:
                val[day].append(item)
        return val

    # Allows the crawler to click on an element regardless of if it's visibility
    def _click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    # Simplifies the process of getting the foods from the menus
    def _get_menu(self):
        # Make sure that the food items in the web menu are there
        self.driver.implicitly_wait(60)
        self.driver.find_elements_by_xpath("//li[@class='day']//ul[li[@class='food text-links']]//a")

        # Make sure that the dates on the web menu are there
        self.driver.implicitly_wait(60)
        self.driver.find_elements_by_xpath("//li[@class='day']//h3")

        # Get the food items and dates from the web menu
        self.driver.implicitly_wait(60)
        elem_arr = self.driver.find_elements_by_xpath("//li[@class='day']//ul[@class='items']//li[@class='food text-lin"
                                                      "ks']//a[@class='food-name-inner'] "
                                                      "| //li[@class='day']//h3[@class='day-label']")

        for i, item in enumerate(elem_arr):
            elem_arr[i] = item.text

        return elem_arr

    # Get menus in dict form
    def get_info(self):
        # TODO: Return conglomerate of menu
        return self.menu

    # Get menus in json form
    def get_json(self):
        return json.dumps(self.menu)

    # Quit the driver
    def quit(self):
        self.driver.close()
        print("Stage: Exited Navigator")

    # Function that allows the Crawler to be used with encapsulation
    def __enter__(self):
        return self

    # Manages when the code leaves the encapsulation
    def __exit__(self, t, value, traceback):
        self.quit()


if __name__ == '__main__':
    with Crawler() as c:
        c.nav()
        print(c.get_info())
        input("Type any key to quit: ")
