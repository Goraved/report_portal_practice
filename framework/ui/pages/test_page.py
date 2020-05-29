from random import randint

from selenium.webdriver.common.by import By

from framework.ui.base_page import BasePage


class QaCartPage(BasePage):
    def purchase_item(self):
        self.go_to_exact_url("http://automationpractice.com/index.php")
        self.click(*(By.CSS_SELECTOR, 'li:nth-child(3) > a[title="T-shirts"]'))
        self.click(*(By.CSS_SELECTOR, '[itemprop="name"]'))

        self.click(*(By.CSS_SELECTOR, '[title="Add to cart"]'))
        self.click(*(By.CSS_SELECTOR, '[title="Proceed to checkout"]'))
        self.click(*(By.CSS_SELECTOR, "p > a.button.btn.btn-default.standard-checkout.button-medium"))
        self.click(*(By.CSS_SELECTOR, "#email_create"))
        self.type(f'goraved@test{randint(1, 1000)}.com', *(By.CSS_SELECTOR, "#email_create"))
        self.click(*(By.CSS_SELECTOR, "#SubmitCreate"))
        self.click(*(By.CSS_SELECTOR, '[name="id_gender"]'))
        self.click(*(By.CSS_SELECTOR, '[name="customer_firstname"]'))
        self.type("test", *(By.CSS_SELECTOR, '[name="customer_firstname"]'))
        self.type("Goraved", *(By.CSS_SELECTOR, '[name="customer_lastname"]'))
        self.click(*(By.CSS_SELECTOR, '[name="passwd"]'))
        self.type("123asd", *(By.CSS_SELECTOR, '[name="passwd"]'))
        self.select_by_value("1", *(By.CSS_SELECTOR, "#days"))
        self.select_by_value("1", *(By.CSS_SELECTOR, "#months"))
        self.select_by_value("2020", *(By.CSS_SELECTOR, "#years"))
        self.click(*(By.CSS_SELECTOR, '[name="optin"]'))
        self.click(*(By.CSS_SELECTOR, "#newsletter"))
        self.click(*(By.CSS_SELECTOR, '[name="firstname"]'))
        self.click(*(By.CSS_SELECTOR, '[name="address1"]'))
        self.type("street", *(By.CSS_SELECTOR, '[name="address1"]'))
        self.click(*(By.CSS_SELECTOR, "#city"))
        self.type("test", *(By.CSS_SELECTOR, "#city"))
        self.select_by_value("1", *(By.CSS_SELECTOR, "#id_state"))
        self.click(*(By.CSS_SELECTOR, "#postcode"))
        self.type("11111", *(By.CSS_SELECTOR, "#postcode"))
        self.click(*(By.CSS_SELECTOR, "#other"))
        self.type("123", *(By.CSS_SELECTOR, "#other"))
        self.click(*(By.CSS_SELECTOR, "#phone_mobile"))
        self.type("123", *(By.CSS_SELECTOR, "#phone_mobile"))
        self.click(*(By.CSS_SELECTOR, "#alias"))
        self.click(*(By.CSS_SELECTOR, "#alias"))
        self.click(*(By.CSS_SELECTOR, "#alias"))
        self.click(*(By.CSS_SELECTOR, "#submitAccount"))
        self.click(*(By.CSS_SELECTOR, "#center_column > form > p > button"))
        self.click(*(By.CSS_SELECTOR, '[name="cgv"]'))
        self.click(*(By.CSS_SELECTOR, "#form > p > button"))
        self.click(*(By.CSS_SELECTOR, '[title="Pay by bank wire"]'))
        self.click(*(By.CSS_SELECTOR, "#cart_navigation > button"))
        self.click(*(By.CSS_SELECTOR, '[title="View my customer account"]'))
        self.click(*(By.CSS_SELECTOR, '[title="Orders"]'))

    def is_order_present(self):
        return self.is_element_visible(*(By.CSS_SELECTOR, '#order-list > tbody > tr'))
