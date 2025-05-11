import re
from playwright.sync_api import Page
from pages.base_page import BasePage

class MyBooksPage(BasePage):
    """ A class that includes abstraction of 'My books' view, inherent common features from class BasePage """

    def __init__(self, page: Page):
        super().__init__(page)

        self.my_books_div = self.page.locator("div.favorites")
        self.my_books_list = self.page.get_by_test_id("book-list")
        self.empty_list_text = self.my_books_div.get_by_text("När du valt, kommer dina favoritböcker att visas här.")


    def navigate(self):
        super().navigate()
        self.click_my_books_button()


    def is_my_books_view_visible(self) -> bool:
        return self.my_books_div.is_visible()


    def get_book_list_length(self) -> int:
        return self.my_books_list.get_by_role("listitem").count()


    def is_book_list_ordered_list(self) -> bool:
        tag_name = self.my_books_list.evaluate("el => el.tagName")
        return  tag_name == "OL"


    def is_book_in_list(self, title: str) -> bool:  
        return self.my_books_list.get_by_text(title).count() > 0
    

    def is_empty_list_text_visible(self) -> bool:
        return self.empty_list_text.is_visible()
