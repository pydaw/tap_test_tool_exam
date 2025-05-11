from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage
from pages.my_books_page import MyBooksPage


@given(u'räknar antalet böcker i katalog listan')
def step_impl(context):
    catalog_page = CatalogPage(context.page)
    context.catalog_book_list_length = catalog_page.get_book_list_length()
    

@given(u'inga böcker är valda som favoriter')
def step_impl(context):
    catalog_page = CatalogPage(context.page)

    # Check that no book is marked ad favorite
    assert catalog_page.number_of_books_marked_as_favorite() == 0
    

@when(u'navigerar till "Lägg till bok"')
def step_impl(context):
    add_book_page = AddBookPage(context.page)
    add_book_page.click_add_book_button()
    

@when(u'lägger till 2 böcker')
def step_impl(context):
    add_book_page = AddBookPage(context.page)
    
    # Add Book1
    add_book_page.fill_title_input("Book1")
    add_book_page.fill_author_input("Author1")
    add_book_page.click_add_new_book_button()
    
    # Add Book2
    add_book_page.fill_title_input("Book2")
    add_book_page.fill_author_input("Author2")
    add_book_page.click_add_new_book_button()


@when(u'klickar på första boken i listan 4 gånger')
def step_impl(context):
    catalog_page = CatalogPage(context.page)
    if catalog_page.get_book_list_length() > 0:
        # Click on favorite button 4 times
        for i in range(4):
            catalog_page.click_favorite_button(0)
    else:
        raise Exception("Catalog list is empty")


@then(u'kataloglistan ökas med 2 böcker')
def step_impl(context):
    # Navigate to "Katalog" view
    catalog_page = CatalogPage(context.page)
    catalog_page.click_catalog_button()

    # Is 2 books added in list? 
    assert context.catalog_book_list_length + 2 == catalog_page.get_book_list_length()


@then(u'skall boken inte vara vald som favorit bok')
def step_impl(context):
    catalog_page = CatalogPage(context.page)
    my_book_page = MyBooksPage(context.page)

    # Check that no book is marked ad favorite
    assert catalog_page.number_of_books_marked_as_favorite() == 0
    
    # Check that no book is in favorite list
    assert my_book_page.get_book_list_length() == 0