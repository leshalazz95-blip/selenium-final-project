from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    # Сообщение об успешном добавлении (название товара)
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    # Сообщение со стоимостью корзины
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    # Название товара на странице
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    # Цена товара на странице
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")