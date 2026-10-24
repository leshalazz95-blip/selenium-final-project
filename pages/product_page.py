from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_success_message(self):
        # Получаем название товара со страницы
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Получаем текст сообщения об успехе
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        # Проверяем, что название товара есть в сообщении
        assert product_name in success_message, \
            f"Product name '{product_name}' is not in success message '{success_message}'"

    def should_be_basket_total_price(self):
        # Получаем цену товара со страницы
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Получаем стоимость корзины
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        # Проверяем, что цена товара есть в стоимости корзины
        assert product_price in basket_total, \
            f"Product price '{product_price}' is not in basket total '{basket_total}'"