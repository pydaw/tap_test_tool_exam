from behave import given, when, then
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage
from pages.my_books_page import MyBooksPage


@when(u'trycker på "{menu_button}"')
def step_impl(context, menu_button):
    base_page = BasePage(context.page)
    if menu_button == "Katalog":
        base_page.click_add_book_button()
        base_page.click_catalog_button()
    elif menu_button == "Lägg till bok":
        base_page.click_add_book_button()
    elif menu_button == "Mina böcker":
        base_page.click_my_books_button()
    else:
        raise NotImplementedError(f'STEP: When trycker på "{menu_button}"')


@then(u'sidan skall visa vy för "{menu_button}"')
def step_impl(context, menu_button):
    catalog_page = CatalogPage(context.page)
    add_book_page = AddBookPage(context.page)
    my_books_page = MyBooksPage(context.page)
    if menu_button == "Katalog":
        assert catalog_page.is_catalog_view_visible()
    elif menu_button == "Lägg till bok":
        assert add_book_page.is_add_book_view_visible()
    elif menu_button == "Mina böcker":
        assert my_books_page.is_my_books_view_visible()
    else:
        raise NotImplementedError(f'STEP: Then sidan skall visa "{menu_button}"')


@then(u'ska "{menu_button}" bli inaktiverad')
def step_impl(context, menu_button):
    base_page = BasePage(context.page)
    if menu_button == "Katalog":
        assert base_page.is_catalog_button_disabled()
        assert not base_page.is_add_book_button_disabled()
        assert not base_page.is_my_books_button_disabled()
    elif menu_button == "Lägg till bok":
        assert not base_page.is_catalog_button_disabled()
        assert base_page.is_add_book_button_disabled()
        assert not base_page.is_my_books_button_disabled()
    elif menu_button == "Mina böcker":
        assert not base_page.is_catalog_button_disabled()
        assert not base_page.is_add_book_button_disabled()
        assert base_page.is_my_books_button_disabled()
    else:
        raise NotImplementedError(f'STEP: ska "{menu_button}" bli inaktiverad')

