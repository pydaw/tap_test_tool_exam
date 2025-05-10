from behave import given, when, then
from playwright.sync_api import Page

from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage


@given(u'anvädaren är på vy "Lägga till bok"')
def step_impl(context):
    add_book_page = AddBookPage(context.page)
    add_book_page.navigate()


@when(u'anger titel "{title}" och författare "{author}"')
def step_impl(context,  title, author):
    add_book_page = AddBookPage(context.page)
    
    context.new_book_title = title
    add_book_page.fill_title_input(context.new_book_title)
    
    context.new_book_author = author
    add_book_page.fill_author_input(context.new_book_author)


@when(u'anger titel "" och författare "Test Testsson"')
def step_impl(context):
    add_book_page = AddBookPage(context.page)
    
    context.new_book_title = ""
    add_book_page.fill_title_input(context.new_book_title)
    
    context.new_book_author = "Test Testsson"
    add_book_page.fill_author_input(context.new_book_author)


@when(u'anger titel "Test123" och författare ""')
def step_impl(context):
    add_book_page = AddBookPage(context.page)
    
    context.new_book_title = "Test123"
    add_book_page.fill_title_input(context.new_book_title)
    
    context.new_book_author = ""
    add_book_page.fill_author_input(context.new_book_author)


@when(u'trycker på knappen "lägg till ny bok"')
def step_impl(context):
    add_book_page = AddBookPage(context.page)
    add_book_page.click_add_new_book_button()


@then(u'sparas bok i katalog')
def step_impl(context):
    catalog_page = CatalogPage(context.page)
    catalog_page.click_catalog_button()
    assert catalog_page.is_book_in_catalog(context.new_book_title, context.new_book_author)


@then(u'kan ej spara bok i katalog')
def step_impl(context):
    add_book_page = AddBookPage(context.page)
    assert add_book_page.is_add_new_book_button_disabled()

