from pages.base_page import BasePage

class MyBooksPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.my_books_div = self.page.locator("div.favorites")


    def is_my_books_view_visible(self):
        return self.my_books_div.is_visible()