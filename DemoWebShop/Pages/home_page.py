from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page

    def vote_in_community_poll(self, option_id):
        self.page.locator(f"#pollanswers-{option_id}").click()
        self.page.locator("#vote-poll-1").click()

   
    def subscribe_to_newsletter(self, email):
        self.page.locator("#newsletter-email").fill(email)
        self.page.locator("#newsletter-subscribe-button").click()

    def assert_subscribe_success(self):
        message = self.page.locator("#newsletter-result-block")
        expect(message).to_be_visible()
        expect(message).to_contain_text(
            "Thank you for signing up! A verification email has been sent. We appreciate your interest."
        )