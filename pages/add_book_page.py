import time

from pages.base_page import BasePage


class AddBookPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_book_div = self.page.locator("div.form")
        self.title_input = self.page.get_by_test_id("add-input-title")
        self.author_input = self.page.get_by_test_id("add-input-author")
        self.add_new_book_button =  self.page.get_by_test_id("add-submit")


    def navigate(self):
        super().navigate()
        self.click_add_book_button()
        

    def is_add_book_view_visible(self):
        return self.add_book_div.is_visible()
    

    def fill_title_input(self, title):
        self.title_input.fill(title)


    def fill_author_input(self, author):
        self.author_input.fill(author)


    def click_add_new_book_button(self):
        self.add_new_book_button.click()

    def is_add_new_book_button_disabled(self):
        return self.add_new_book_button.is_disabled()