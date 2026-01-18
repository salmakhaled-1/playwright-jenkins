class AccountPage:
    def __init__(self, page):
        self.page = page

    def open_addresses(self):
        self.page.get_by_role("link", name="My account").click()
        self.page.locator("a[href='/customer/addresses']").first.click()

    def add_new_address(
        self,
        first_name,
        last_name,
        email,
        country,
        city,
        address,
        zip_code,
        phone,
        fax
    ):
        self.page.get_by_role("button", name="Add new").click()

        self.page.locator("#Address_FirstName").fill(first_name)
        self.page.locator("#Address_LastName").fill(last_name)
        self.page.locator("#Address_Email").fill(email)
        self.page.locator("#Address_CountryId").select_option(country)
        self.page.locator("#Address_City").fill(city)
        self.page.locator("#Address_Address1").fill(address)
        self.page.locator("#Address_ZipPostalCode").fill(zip_code)
        self.page.locator("#Address_PhoneNumber").fill(phone)
        self.page.locator("#Address_FaxNumber").fill(fax)

        self.page.get_by_role("button", name="Save").click()


