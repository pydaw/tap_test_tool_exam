import re
from pages.base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.catalog_div = self.page.locator("div.catalog")
        self.book_list = self.catalog_div.locator("div.book")


    def is_catalog_view_visible(self):
        return self.catalog_div.is_visible()


    def is_book_in_list(self, title, author):
        new_book_locator = self.catalog_div.locator(
            "div.book",
            has_text=re.compile(rf"{title}.*{author}")
        )
        return new_book_locator.count() > 0
    

    def get_book_list_length(self):
        return self.book_list.count()


    def get_book(self, index: int):
        book_locator = self.book_list.nth(index)
        text = book_locator.text_content().strip().strip(('"❤️"')).replace('"','')
        
        # Expected format of book representation: "<title>", <author>
        if "," in text:
            title, author = map(str.strip, text.split(",", 1))
            return {"title": title, "author": author}
        else:
            return {"title": "", "author": ""}

    
    def mark_book_as_favorite(self, index: int):
        if self.book_list.nth(index).locator("div.star").is_visible():
            self.book_list.nth(index).get_by_role("button").click()
        else:
            raise Exception("Book cannot be marked as a favorite, already marked?")


    def unmark_book_as_favorite(self, index: int):
        if self.book_list.nth(index).locator("div.star.selected").is_visible():
            self.book_list.nth(index).get_by_role("button").click()
        else:
            raise Exception("Book cannot be unmarked as a favorite, already unmarked?")


    def click_favorite_button(self, index: int):
        self.book_list.nth(index).get_by_role("button").click()


    def number_of_books_marked_as_favorite(self):
        return self.book_list.locator("div.star.selected").count()
    