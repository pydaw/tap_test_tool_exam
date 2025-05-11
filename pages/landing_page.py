from playwright.sync_api import Page
from pages.base_page import BasePage

class LandingPage(BasePage):
    """ A class that includes abstraction of 'landing page' view, inherent common features from class BasePage """

    def __init__(self, page: Page):
        super().__init__(page)