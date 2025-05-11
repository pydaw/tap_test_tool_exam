Feature: Lista alla böcker i en katalog

    Som en användare, vill jag att se en katalog med böcker, så att jag kan vilka böcker som jag kan välja sätta som favoriter.

    Scenario: Lägg till 2 böcker så skall kataloglistan ökas med 2 böcker
        Given användaren befinner sig på landningssidan
        And räknar antalet böcker i katalog listan
        When navigerar till "Lägg till bok"
        And lägger till 2 böcker
        Then kataloglistan ökas med 2 böcker

    @wip    
    Scenario: Klicka 4 gånger på en bok
        Given användaren befinner sig på landningssidan
        And inga böcker är valda som favoriter
        When klickar på första boken i listan 4 gånger
        Then skall boken inte vara vald som favorit bok
