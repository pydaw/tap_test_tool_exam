from playwright.sync_api import Page
BASE_URL = "https://tap-ht24-testverktyg.github.io/exam-template/"

class BasePage:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = self.page.title()
        self.main_heading = page.get_by_role("heading", name="Läslistan")
        self.main_image = page.get_by_role("img", name="Bokklubb på café")
        self.catalog_button = page.get_by_test_id("catalog")
        self.add_book_button = page.get_by_test_id("add-book")
        self.my_books_button = page.get_by_test_id("favorites")


    def navigate(self, url=BASE_URL):
        self.page.goto(url)

    def get_title(self):
        return self.page_title

    def is_heading_visible(self):
        return self.main_heading.is_visible()

    def is_image_visible(self):
        return self.main_image.is_visible()

    
    def click_catalog_button(self):
        self.catalog_button.click()
    
    def is_catalog_button_disabled(self):
        return self.catalog_button.is_disabled()
    
    
    def click_add_book_button(self):
        self.add_book_button.click()
    
    def is_add_book_button_disabled(self):
        return self.add_book_button.is_disabled()
    

    def click_my_books_button(self):
        self.my_books_button.click()
    
    def is_my_books_button_disabled(self):
        return self.my_books_button.is_disabled()
    