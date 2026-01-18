from playwright.sync_api import Page, expect

class GiftCardsPage:
    def __init__(self, page: Page):
        self.page = page

    def open_gift_cards(self):
        self.page.get_by_role("link", name="Gift Cards").first.click()

    def sort_price_high_to_low(self):
        dropdown = self.page.locator("#products-orderby")
        expect(dropdown).to_be_visible()
        dropdown.select_option(label="Price: High to Low")

    def assert_prices_sorted_high_to_low(self):
        prices_text = self.page.locator(".price.actual-price").all_inner_texts()
        prices = [float(price) for price in prices_text]

        assert prices == sorted(prices, reverse=True), (
            f"Prices not sorted correctly: {prices}"
        )

    def add_third_product_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").nth(2).click()

    def fill_gift_card_details(self):
        self.page.locator("#giftcard_2_RecipientName").fill("janaa")
        self.page.locator("#giftcard_2_RecipientEmail").fill("mariamkk@gmail.com")
        self.page.locator("#giftcard_2_Message").fill("Gift for you")

    def email_a_friend(self):
        self.page.get_by_role("button", name="Email a friend").click()

        self.page.locator("#FriendEmail").fill("mariamkk@gmail.com")
        self.page.locator("#PersonalMessage").fill("Enjoy your gift")
        self.page.get_by_role("button", name="Send email").click()

        expect(
            self.page.get_by_text("Your message has been sent.")
        ).to_be_visible()