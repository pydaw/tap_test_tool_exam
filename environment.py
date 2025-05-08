from playwright.sync_api import sync_playwright
from pages.base_page import BASE_URL

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=True)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = BASE_URL

def after_scenario(context, scenario):
    if context.page:
        context.page.close()

def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()