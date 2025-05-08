from behave import given, when, then
from playwright.sync_api import Page
from pages.landing_page import LandingPage


@given(u'användaren befinner sig på landningssidan')
def step_impl(context):
    landing_page = LandingPage(context.page)
    landing_page.navigate()

@then(u'sidan visas med titeln "Läslistan"')
def step_impl(context):
    landing_page = LandingPage(context.page)
    assert landing_page.get_title() == "Läslistan"

@then(u'sidan visas med rubriken "Läslistan"')
def step_impl(context):
    landing_page = LandingPage(context.page)
    assert landing_page.is_heading_visible()

@then(u'sidan visar en bakgrundsbild')
def step_impl(context):
    landing_page = LandingPage(context.page)
    assert landing_page.is_image_visible()

@then(u'menyvalet "Katalog" visas')
def step_impl(context):
    landing_page = LandingPage(context.page)
    assert landing_page.is_catalog_button_chosen()
