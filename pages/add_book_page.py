from pages.base_page import BasePage

class AddBookPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.add_book_div = self.page.locator("div.form")


    def is_add_book_view_visible(self):
        return self.add_book_div.is_visible()