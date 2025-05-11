import time
import random

from behave import given, when, then
from playwright.sync_api import Page

from pages.my_books_page import MyBooksPage
from pages.catalog_page import CatalogPage


@given(u'användaren befinner sig på vy "Mina böcker"')
def step_impl(context):
    my_books_page = MyBooksPage(context.page)
    my_books_page.navigate()


@given(u'inga favoritböcker i listan')
def step_impl(context):
    my_book_page = MyBooksPage(context.page)
    assert my_book_page.get_book_list_length() == 0
    

@when(u'anvädaren markerar "3" böcker i vy "Katalog"')
def step_impl(context):
    # Navigate to "Katalog" view, use button to save state on site
    catalog_page = CatalogPage(context.page)
    catalog_page.click_catalog_button()

    # Mark 3 random books as favorite and save titles and authors in context parameter
    # books is saved in a list format: [{"title": "<title>", "author": "<author>"}, ...]
    number_of_books_in_catalog = catalog_page.get_book_list_length()
    if number_of_books_in_catalog >=3:
        sample_of_book_index = random.sample(range(number_of_books_in_catalog),k=3)
        
        favorite_books_list = []
        for index in sample_of_book_index:
            catalog_page.mark_book_as_favorite(index)
            favorite_books_list.append(catalog_page.get_book(index))
        
        # Save lists to context
        context.favorite_books_list = favorite_books_list
        context.favorite_books_list_index = sample_of_book_index

        # Check number of favorites marks is 3
        assert catalog_page.number_of_books_marked_as_favorite() == 3

    else:
        raise Exception("Not enough books in catalog list")
    

@when(u'användaren avmarkerar de "3" böckerna i vy "Katalog"')
def step_impl(context):
    # Navigate to "Katalog" view, use button to save state on site
    catalog_page = CatalogPage(context.page)
    
    # Check if books is saved in list
    number_of_favorite_books = len(context.favorite_books_list)
    assert number_of_favorite_books > 0

    # Unmark the 3 saved favorite books
    if number_of_favorite_books >= 3:
        favorite_books_list_index = context.favorite_books_list_index
        for index in favorite_books_list_index:
            catalog_page.unmark_book_as_favorite(index)

    else:
        raise Exception("Not enough books that are marked as favorite")


@when(u'anvädaren har markerat "0" böcker i vy "Katalog"')
def step_impl(context):
    # Navigate to "Katalog" view, use button to save state on site
    catalog_page = CatalogPage(context.page)
    catalog_page.click_catalog_button()

    # Check number of favorites marks is 0
    assert catalog_page.number_of_books_marked_as_favorite() == 0


@then(u'ska böckerna visas i en numrerad lista under vyn "Mina böcker"')
def step_impl(context):
    # Navigate to "Mina böcker" view, use button to save state on site
    my_books_page = MyBooksPage(context.page)
    my_books_page.click_my_books_button()

    # Check if an order list is present
    assert my_books_page.is_book_list_ordered_list()

    # Check that selected books is saved in a list
    assert len(context.favorite_books_list) >= 0
    
    # Check that books that was checked in catalog is present in list
    for book in context.favorite_books_list:
        book_title = book["title"]
        assert my_books_page.is_book_in_list(book_title), f"Book title: {book_title} is not in list" 


@then(u'ska vy "Mina böcker" visa text: "När du valt, kommer dina favoritböcker att visas här."')
def step_impl(context):
    # Navigate to "Mina böcker" view, use button to save state on site
    my_books_page = MyBooksPage(context.page)
    my_books_page.click_my_books_button()

    # Check if text is visible when list is empty
    assert my_books_page.is_empty_list_text_visible()
    