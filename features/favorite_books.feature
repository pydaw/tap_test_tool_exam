Feature: Mina favorit böcker

    Som en användare, vill jag kunna lista mina favoritböcker, så att jag har mina favoritböcker samlade på ett ställe.

    Scenario: Markerade favoritböcker skall visas i en lista med favoritböcker
        Given användaren befinner sig på vy "Mina böcker"
        And inga favoritböcker i listan
        When anvädaren markerar "3" böcker i vy "Katalog"
        Then ska böckerna visas i en numrerad lista under vyn "Mina böcker"

    Scenario: Då inga böcker är markerade skall det visas en förklarande text
        Given användaren befinner sig på vy "Mina böcker"
        And inga favoritböcker i listan
        When anvädaren har markerat "0" böcker i vy "Katalog"
        Then ska vy "Mina böcker" visa text: "När du valt, kommer dina favoritböcker att visas här."
