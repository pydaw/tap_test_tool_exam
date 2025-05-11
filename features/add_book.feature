Feature: Lägg till bok

    Som en användare, vill jag kunna lägga till en bok, så att jag kan utöka katalogen med fler böcker.

    Scenario Outline: Lägg till en bok
        Given anvädaren är på vy "Lägga till bok"
        When anger titel "<title>" och författare "<author>"
        And trycker på knappen "lägg till ny bok"
        Then sparas bok i katalog

        Examples: 
            | title   | author        |
            | Test123 | Test Testsson |
            | -       | -             |
                

    Scenario: Kontrollera att det inte går att lägga till bok utan titel
        Given anvädaren är på vy "Lägga till bok"
        When anger titel "" och författare "Test Testsson"
        Then kan ej spara bok i katalog


    Scenario: Kontrollera att det inte går att lägga till bok utan författare
        Given anvädaren är på vy "Lägga till bok"
        When anger titel "Test123" och författare ""
        Then kan ej spara bok i katalog
