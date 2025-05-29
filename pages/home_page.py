class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://magento.softwaretestingboard.com/"
        self.logo_selector = "img.logo"
        self.search_box_selector = "#search"

    def load(self):
        self.driver.get(self.url)

    def is_logo_visible(self):
        return self.driver.find_element("css selector", self.logo_selector).is_displayed()

    def is_search_box_present(self):
        return self.driver.find_element("css selector", self.search_box_selector).is_displayed()
