from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FormFiller:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def fill_out_form(self, form_url, links_list, prices_list, addresses_list):
        self.driver.get(form_url)

        # Make sure to add a delay to prevent crashing (frequent bugs are locating elements
        # on websites that haven't been fully loaded yet)
        time.sleep(5)

        # Iterate over the classes
        for property_id in range(len(form_url)):
            inputs_list = self.driver.find_elements(By.CSS_SELECTOR, '[type="text"]')
            inputs_list[0].send_keys(links_list[property_id])
            inputs_list[1].send_keys(prices_list[property_id])
            inputs_list[2].send_keys(addresses_list[property_id])

            # Submit info
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div["
                                               "1]/div/span/span").click()

            # Start anew
            self.driver.find_element(By.CSS_SELECTOR, "a").click()
            time.sleep(5)

        # Finish up
        self.driver.quit()
