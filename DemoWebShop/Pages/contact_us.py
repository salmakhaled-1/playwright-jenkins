from playwright.sync_api import expect

class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.get_by_role("link", name="Contact us").click()

    def submit_enquiry(self, name, email, enquiry):
        self.page.locator("#FullName").fill(name)
        self.page.locator("#Email").fill(email)
        self.page.locator("#Enquiry").fill(enquiry)
        self.page.get_by_role("button", name="Submit").click()

    def assert_success_message(self):
        message = self.page.locator(".page-body .result")
        expect(message).to_be_visible()
        expect(message).to_contain_text(
            "Your enquiry has been successfully sent to the store owner."
        )
