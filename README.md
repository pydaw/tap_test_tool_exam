# README
Author: Daniel Wärnelöv

## Sidstruktur
Landing page:
- Rubrik
- Bakgrundsbild
Meny:
- Katalog
	- Vy med boklista
	- Markera favoriter
- Lägg till bok
	- Vy för att lägga till bok
	- Lägga till titel
	- Lägga till författare
	- Lägga till ny bok i katalog
- Mina böcker
	- Vy med lista med favorit böcker
  
## Sidans - funktioner
Funktionerna delas in och anges vad som skall testas och kontrolleras.

### Landningssida
- Kontrollera att sidan har en titel med texten "Läslistan"
- Kontrollera att vyn innehåller rubriken "Läslistan"
- Kontrollera att vyn har en bakgrundsbild
### Menyknappar och navigering
- Kontrollera att vyn "Katalog" är förvalt
- Kontrollera att meny knapparna finns och gör att man kan komma runt till de olika sidorna
### Katalog
- Visas denna vyn som en default sida?
- Kontrollera att listan utökas med antalet böcker man lägger in
- Vad händer om man trycker flera ggr på favorit ikonen
### Lägg till bok
- Lägg till bok och kontrollera att den spara i listan
- Vy för att göra en ny bok  - Knappen blir inte aktiverad förrän fälten titel och författare är fyllda
- Kan man ha vilka tecken som (numeriska, specialtecken?)
### Mina böcker
- Vy med lista med favorit böcker
- Kontrollera att listan är tom om man inte har favoriter
- Om listan är tom skall text komma upp att man inte valt favorit än
- Kontrollera att listan öka om man markera favoriter

## User stories
Summering av [User Stories](STORIES.md)

User stories återfinns även i gherkin features-filerna:  
[landing_page.feature](features/landing_page.feature)  
[switch_view.feature](features/switch_view.feature)  
[book_catalog.feature](features/book_catalog.feature)  
[add_book.feature](features/add_book.feature)  
[favorite_books.feature](features/favorite_books.feature)  


## Installation och köra testerna

Installera pytest, behave och playwright med följabde kommando i terminalen:  
``` powershell
# Installera följande bibliotek
# OBS! Installera gärna i en virtuell python miljö: https://docs.python.org/3/library/venv.html
pip install pytest-playwright
playwright install
pip install behave

# Eller
pip install -r requirements.txt
playwright install
```

Kör testerna genom följande kommando i terminalen:
``` powershell
# Gå till projektets root-katalog och skriv
behave
```

Exempel:
``` powershell
(.venv) PS C:\Users\dawa01\Documents\Python Scripts\nbi\tap_test_tool_exam> behave
Feature: Lägg till bok # features/add_book.feature:1
  Som en användare, vill jag kunna lägga till en bok, så att jag kan utöka katalogen med fler böcker.
  Scenario Outline: Lägg till en bok -- @1.1                  # features/add_book.feature:13
    Given anvädaren är på vy "Lägga till bok"                 # steps/add_book_steps.py:8
    When anger titel "Test123" och författare "Test Testsson" # steps/add_book_steps.py:14
    And trycker på knappen "lägg till ny bok"                 # steps/add_book_steps.py:47
    Then sparas bok i katalog                                 # steps/add_book_steps.py:53

  Scenario Outline: Lägg till en bok -- @1.2   # features/add_book.feature:14
    Given anvädaren är på vy "Lägga till bok"  # steps/add_book_steps.py:8
    When anger titel "-" och författare "-"    # steps/add_book_steps.py:14
    And trycker på knappen "lägg till ny bok"  # steps/add_book_steps.py:47
    Then sparas bok i katalog                  # steps/add_book_steps.py:53

  Scenario: Kontrollera att det inte går att lägga till bok utan titel  # features/add_book.feature:17
    Given anvädaren är på vy "Lägga till bok"                           # steps/add_book_steps.py:8
    When anger titel "" och författare "Test Testsson"                  # steps/add_book_steps.py:25
    Then kan ej spara bok i katalog                                     # steps/add_book_steps.py:60

  Scenario: Kontrollera att det inte går att lägga till bok utan författare  # features/add_book.feature:23
    Given anvädaren är på vy "Lägga till bok"                                # steps/add_book_steps.py:8
    When anger titel "Test123" och författare ""                             # steps/add_book_steps.py:36
    Then kan ej spara bok i katalog                                          # steps/add_book_steps.py:60

Feature: Lista alla böcker i en katalog # features/book_catalog.feature:1
  Som en användare, vill jag att se en katalog med böcker, så att jag kan vilka böcker som jag kan välja sätta som favoriter.
  Scenario: Lägg till 2 böcker så skall kataloglistan ökas med 2 böcker  # features/book_catalog.feature:5
    Given användaren befinner sig på landningssidan                      # steps/landing_page_steps.py:6
    And räknar antalet böcker i katalog listan                           # steps/catalog_steps.py:6
    When navigerar till "Lägg till bok"                                  # steps/catalog_steps.py:20
    And lägger till 2 böcker                                             # steps/catalog_steps.py:26
    Then kataloglistan ökas med 2 böcker                                 # steps/catalog_steps.py:52

  Scenario: Klicka 4 gånger på en bok               # features/book_catalog.feature:12
    Given användaren befinner sig på landningssidan # steps/landing_page_steps.py:6
    And inga böcker är valda som favoriter          # steps/catalog_steps.py:12
    When klickar på första boken i listan 4 gånger  # steps/catalog_steps.py:41
    Then skall boken inte vara vald som favorit bok # steps/catalog_steps.py:62

Feature: Mina favorit böcker # features/favorite_books.feature:1
  Som en användare, vill jag kunna lista mina favoritböcker, så att jag har mina favoritböcker samlade på ett ställe.
  Scenario: Markerade favoritböcker skall visas i en lista med favoritböcker  # features/favorite_books.feature:5
    Given användaren befinner sig på vy "Mina böcker"                         # steps/favorite_books_steps.py:10
    And inga favoritböcker i listan                                           # steps/favorite_books_steps.py:16
    When anvädaren markerar "3" böcker i vy "Katalog"                         # steps/favorite_books_steps.py:22
    Then ska böckerna visas i en numrerad lista under vyn "Mina böcker"       # steps/favorite_books_steps.py:79

  Scenario: Då inga böcker är markerade skall det visas en förklarande text                      # features/favorite_books.feature:11
    Given användaren befinner sig på vy "Mina böcker"                                            # steps/favorite_books_steps.py:10
    And inga favoritböcker i listan                                                              # steps/favorite_books_steps.py:16
    When anvädaren har markerat "0" böcker i vy "Katalog"                                        # steps/favorite_books_steps.py:69
    Then ska vy "Mina böcker" visa text: "När du valt, kommer dina favoritböcker att visas här." # steps/favorite_books_steps.py:97

  Scenario: Användaren ångar favorit markeringen                                                 # features/favorite_books.feature:17
    Given användaren befinner sig på vy "Mina böcker"                                            # steps/favorite_books_steps.py:10
    When anvädaren markerar "3" böcker i vy "Katalog"                                            # steps/favorite_books_steps.py:22
    And användaren avmarkerar de "3" böckerna i vy "Katalog"                                     # steps/favorite_books_steps.py:50
    Then ska vy "Mina böcker" visa text: "När du valt, kommer dina favoritböcker att visas här." # steps/favorite_books_steps.py:97

Feature: Landningssida # features/landing_page.feature:1
  Som en användare, vill jag får feedback att jag kommit till "Läslistan", så att vet att jag kommit till rätt sida.
  Scenario: Användare besöker sidan                 # features/landing_page.feature:5
    Given användaren befinner sig på landningssidan # steps/landing_page_steps.py:6
    Then sidan visas med titeln "Läslistan"         # steps/landing_page_steps.py:12

  Scenario: Användare presenteras en rubrik unik för sidan  # features/landing_page.feature:9
    Given användaren befinner sig på landningssidan         # steps/landing_page_steps.py:6
    Then sidan visas med rubriken "Läslistan"               # steps/landing_page_steps.py:18

  Scenario: Användaren presentersas en bakgrundsbild  # features/landing_page.feature:13
    Given användaren befinner sig på landningssidan   # steps/landing_page_steps.py:6
    Then sidan visar en bakgrundsbild                 # steps/landing_page_steps.py:24

  Scenario: Menyvalet "Katalog" är förvalt för användaren  # features/landing_page.feature:17
    Given användaren befinner sig på landningssidan        # steps/landing_page_steps.py:6
    Then menyvalet "Katalog" visas                         # steps/landing_page_steps.py:30

Feature: Ändra vy # features/switch_view.feature:1
  Som en användare, vill jag kunna navigera mellan vyerna, så att jag kan komma åt alla funktioner som sidan har att erbjuda.
  Scenario Outline: Kontrollera att korrekt vy visas -- @1.1   # features/switch_view.feature:13
    Given användaren befinner sig på landningssidan            # steps/landing_page_steps.py:6
    When trycker på "Katalog"                                  # steps/switch_view_steps.py:10
    Then sidan skall visa vy för "Katalog"                     # steps/switch_view_steps.py:27

  Scenario Outline: Kontrollera att korrekt vy visas -- @1.2   # features/switch_view.feature:14
    Given användaren befinner sig på landningssidan            # steps/landing_page_steps.py:6
    When trycker på "Lägg till bok"                            # steps/switch_view_steps.py:10
    Then sidan skall visa vy för "Lägg till bok"               # steps/switch_view_steps.py:27

  Scenario Outline: Kontrollera att korrekt vy visas -- @1.3   # features/switch_view.feature:15
    Given användaren befinner sig på landningssidan            # steps/landing_page_steps.py:6
    When trycker på "Mina böcker"                              # steps/switch_view_steps.py:10
    Then sidan skall visa vy för "Mina böcker"                 # steps/switch_view_steps.py:27

  Scenario Outline: Kontrollera att knapp blir inaktiverad -- @1.1   # features/switch_view.feature:25
    Given användaren befinner sig på landningssidan                  # steps/landing_page_steps.py:6
    When trycker på "Katalog"                                        # steps/switch_view_steps.py:10
    Then ska "Katalog" bli inaktiverad                               # steps/switch_view_steps.py:44

  Scenario Outline: Kontrollera att knapp blir inaktiverad -- @1.2   # features/switch_view.feature:26
    Given användaren befinner sig på landningssidan                  # steps/landing_page_steps.py:6
    When trycker på "Lägg till bok"                                  # steps/switch_view_steps.py:10
    Then ska "Lägg till bok" bli inaktiverad                         # steps/switch_view_steps.py:44

  Scenario Outline: Kontrollera att knapp blir inaktiverad -- @1.3   # features/switch_view.feature:27
    Given användaren befinner sig på landningssidan                  # steps/landing_page_steps.py:6
    When trycker på "Mina böcker"                                    # steps/switch_view_steps.py:10
    Then ska "Mina böcker" bli inaktiverad                           # steps/switch_view_steps.py:44

5 features passed, 0 failed, 0 skipped
19 scenarios passed, 0 failed, 0 skipped
61 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m5.468s
```
