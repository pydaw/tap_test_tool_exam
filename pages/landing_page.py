from pages.base_page import BasePage, BASE_URL

class LandingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.title = self.page.title()
        self.heading = page.get_by_role("heading", name="Läslistan")
        self.image = page.get_by_role("img", name="Bokklubb på café")
        self.catalog_button = page.get_by_test_id("catalog")

    def navigate(self):
        return super().navigate(BASE_URL)
    
    def get_title(self):
        return self.title

    def is_heading_visible(self):
        return self.heading.is_visible()

    def is_image_visible(self):
        return self.image.is_visible()

    def is_catalog_button_chosen(self):
        return self.catalog_button.is_disabled()