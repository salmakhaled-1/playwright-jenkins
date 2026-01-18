from playwright.sync_api import Page, expect

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.get_by_role("link", name="Register").click()

    def register(self, first_name, last_name, email, password, confirm_password=None):
        if confirm_password is None:
            confirm_password = password

        self.page.locator("#gender-female").click()
        self.page.locator("#FirstName").fill(first_name)
        self.page.locator("#LastName").fill(last_name)
        self.page.locator("#Email").fill(email)
        self.page.locator("#Password").fill(password)
        self.page.locator("#ConfirmPassword").fill(confirm_password)
        self.page.locator("#register-button").click()

    def assert_registration_success(self):
        expect(
            self.page.get_by_text("Your registration completed")
        ).to_be_visible()

    def assert_password_mismatch_error(self):
        error = self.page.locator(
            'span[for="ConfirmPassword"]'
        )
        expect(error).to_be_visible()
        expect(error).to_have_text(
            "The password and confirmation password do not match."
        )