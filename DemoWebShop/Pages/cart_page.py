import re
from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):   
        self.page = page

    def open_cart(self):
        self.page.get_by_role("link", name="Shopping cart").first.click()
        expect(self.page).to_have_url(re.compile(r"/cart", re.I))

    def assert_product_in_cart(self, product_name: str):
        cart_products = self.page.locator("td.product a")
        expect(cart_products).to_contain_text([product_name])

    def accept_terms_and_checkout(self):
        
        self.page.locator("#CountryId").select_option(value="49")
        self.page.locator("#ZipPostalCode").fill("1000")
        self.page.get_by_role("button", name="Estimate shipping").click()
        
        self.page.locator("#termsofservice").check()
        self.page.locator("#checkout").click()
        
        self.page.get_by_role("button", name="Continue").click()
  
  
        self.page.locator("#PickUpInStore").click()
        self.page.get_by_role("button", name="Continue").click()
        self.page.locator("#paymentmethod_2").click()
        self.page.get_by_role("button", name="Continue").click()
        self.page.locator("#CreditCardType").select_option("Master card")
        self.page.locator("#CardholderName").fill("mariam jana")
        self.page.locator("#CardNumber").fill("378282246310005")
        self.page.locator("#ExpireMonth").select_option("5")
        self.page.locator("#ExpireYear").select_option("2029")
        self.page.locator("#CardCode").fill("456")
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Confirm").click()


       
    
        expect(self.page.get_by_text("Your order has been successfully processed!")).to_be_visible()