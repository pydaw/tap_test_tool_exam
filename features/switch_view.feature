 Feature: Ändra vy
 
    Som en användare, vill jag kunna navigera mellan vyerna, så att jag kan komma åt alla funktioner som sidan har att erbjuda.

    Scenario Outline: Kontrollera att korrekt vy visas

        Given användaren befinner sig på landningssidan
        When trycker på "<menu_button>"
        Then sidan skall visa vy för "<menu_button>"

        Examples: 
            | menu_button   |
            | Katalog       |
            | Lägg till bok |
            | Mina böcker   |


    Scenario Outline: Kontrollera att knapp blir inaktiverad
    
        Given användaren befinner sig på landningssidan
        When trycker på "<menu_button>"
        Then ska "<menu_button>" bli inaktiverad 

        Examples: 
            | menu_button   |
            | Katalog       |
            | Lägg till bok |
            | Mina böcker   |