from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_product(self):
        self.driver.get("https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item")))

        # Кликаем по первому товару
        product = self.driver.find_element(By.CSS_SELECTOR, ".product-item a.product-item-link")
        product.click()

    def select_size_and_color(self):
        # Выбираем первый доступный размер
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.swatch-attribute.size .swatch-option")))
        size = self.driver.find_element(By.CSS_SELECTOR, "div.swatch-attribute.size .swatch-option")
        size.click()

        # Выбираем первый доступный цвет
        color = self.driver.find_element(By.CSS_SELECTOR, "div.swatch-attribute.color .swatch-option")
        color.click()

    def add_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))
        add_button.click()

    def verify_cart_updated(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".counter-number"), "1"))
        return True
