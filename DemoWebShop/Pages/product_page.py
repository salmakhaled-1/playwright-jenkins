import re
from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):  
        self.page = page

    def open_books(self):
        self.page.get_by_role("link", name="Books").first.click()
        expect(self.page).to_have_url(re.compile(r"/books", re.I))

    def filter_under_25(self):
        self.page.locator('a[href*="/books?price=-25"]').click()
        expect(self.page.locator("div.item-box").first).to_be_visible()

    def assert_all_prices_under_25(self):
        prices = self.page.locator("span.price.actual-price")
        count = prices.count()
        assert count > 0, "No products found after applying filter"

        for i in range(count):
            value = float(prices.nth(i).inner_text().replace("$", ""))
            assert value < 25

    def get_first_product_name(self) -> str:
        return self.page.locator("h2.product-title a").first.inner_text().strip()

    def add_first_product_to_cart(self):
        self.page.locator('input[value="Add to cart"]').first.click()
        expect(self.page.locator("#bar-notification")).to_be_visible()