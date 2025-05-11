from playwright.sync_api import sync_playwright


def before_all(context):
    """This function will called before running the tests"""
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=True)
    

def before_scenario(context, scenario):
    """This function will called before running scenario"""
    context.page = context.browser.new_page()
    context.page.set_default_timeout(1000)


def after_scenario(context, scenario):
    """This function will be called after running scenario"""
    if context.page:
        context.page.close()


def after_all(context):
    """This function will be called after running all tests"""
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()