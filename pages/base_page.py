from playwright.sync_api import Page

BASE_URL = "https://tap-ht24-testverktyg.github.io/exam-template/"

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)
