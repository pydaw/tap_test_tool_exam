Feature: Landningssida

    Som en användare, vill jag får feedback att jag kommit till "Läslistan", så att vet att jag kommit till rätt sida.

    @smoke
    Scenario: Användare besöker sidan
        Given användaren befinner sig på landningssidan
        Then sidan visas med titeln "Läslistan"

    Scenario: Användare presenteras en rubrik unik för sidan
        Given användaren befinner sig på landningssidan
        Then sidan visas med rubriken "Läslistan"
    
    Scenario: Användaren presentersas en bakgrundsbild
        Given användaren befinner sig på landningssidan
        Then sidan visar en bakgrundsbild

    Scenario: Menyvalet "Katalog" är förvalt för användaren
        Given användaren befinner sig på landningssidan
        Then menyvalet "Katalog" visas
