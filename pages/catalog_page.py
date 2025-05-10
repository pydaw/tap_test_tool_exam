import re
from pages.base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.catalog_div = self.page.locator("div.catalog")


    def is_catalog_view_visible(self):
        return self.catalog_div.is_visible()


    def is_book_in_catalog(self, title, author):
        new_book_locator = self.catalog_div.locator(
            "div.book",
            has_text=re.compile(rf"{title}.*{author}")
        )
        return new_book_locator.count() > 0