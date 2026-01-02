---
name: Voltz
description: De alles-in-één Lightning wallet voor uw bedrijf.
---

![cover](assets/cover.webp)



Het idee voor het Voltz-platform kwam van een groep bitcoiners die hun eigen bitcoin wallet service wilden aanbieden. Het resultaat was een complete infrastructuur voor het accepteren van bitcoin in winkels. In deze tutorial nemen we je mee op een tour door Voltz en de bitcoin integratiemogelijkheden die het platform te bieden heeft.



## Aan de slag met Voltz



Voltz is niet alleen een custodial Lightning wallet waarmee je dagelijks kunt verzenden, ontvangen en betalen, het is ook een compleet platform dat talloze uitbreidingen biedt om bitcoin als verkooppunt of marktplaats in je bedrijf te integreren.



Ga naar het [Voltz] platform (https://www.voltz.com/en) en maak een account aan door op de knop "Probeer nu" te klikken.



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Het is belangrijk om een sterk alfanumeriek wachtwoord in te stellen om je kansen tegen brute-force aanvallen te vergroten, en controleer of je inderdaad op de officiële Voltz website bent om je inloggegevens in te vullen om je te beschermen tegen phishing.



De Voltz interface lijkt erg op die van het LnBits platform.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz is in feite gebouwd op een LnBits-server; bekijk onze tutorial om te leren hoe je je eigen LnBits-servers kunt koppelen en je oplossingen erop kunt bouwen.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Met het platform kun je efficiënt meerdere portefeuilles beheren. Als je je aanmeldt, heb je standaard automatisch een Lightning-portefeuille. Je kunt echter andere portefeuilles toevoegen.



![wallets](assets/fr/03.webp)



### Draagbaarheid



Voltz beperkt zich niet tot een webinterface: in de sectie **Mobiele toegang** kunt u uw actieve Voltz wallet verbinden met toepassingen zoals Zeus of Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Hiervoor moet je de **LndHub** extensie installeren en activeren op het platform.



![lndhub](assets/fr/04.webp)



Selecteer je actieve Voltz portfolio en scan, afhankelijk van de rechten die je wilt toekennen, de juiste QR-code.




- Met de QR-code voor facturen kun je alleen je portefeuillegeschiedenis lezen en generate nieuwe facturen.
- Met de admin QR code kun je de geschiedenis bekijken, generate facturen en ook Lightning facturen betalen.



![qrs](assets/fr/05.webp)



In deze tutorial verbinden we onze Voltz wallet met de Blue Wallet toepassing.



![connect](assets/fr/06.webp)



Zodra onze portfolio is gekoppeld, worden alle uitgevoerde acties gesynchroniseerd tussen Blue Wallet en Voltz. Wanneer je bijvoorbeeld een generate factuur op Blue Wallet maakt, heb je ook een geschiedenis op Voltz.



![sync](assets/fr/07.webp)



In het gedeelte **Portefeuilleconfiguratie** vindt u minimale parameters zoals het aanpassen van de naam van de portefeuille en de valuta waarin u uw betalingen wilt ontvangen.



![config](assets/fr/08.webp)



### Uitbreidingen



Een van de bijzondere kenmerken van het Voltz-platform is de modulariteit, waardoor je de extensies kunt activeren die je nodig hebt. De lijst met extensies vind je in het menu **Extensies**.



![extensions](assets/fr/09.webp)



Een van deze uitbreidingen is de TPoS, een betaalterminal die je kunt gebruiken om een inventaris bij te houden en betalingen van je klanten te innen.



![tpos](assets/fr/10.webp)



Vanaf de Point of Sale-terminal kunt u :




- Krijg een webpagina die je kunt delen met je klanten en partners;
- Beheer de productinventaris;
- Lightning-facturen genereren;
- Contante betalingen via Bolt kaarten.



De extensie is beschikbaar als gratis versie en als betaalde versie voor meer geavanceerde functies. Om een POS-terminal te maken, klik je op de knop **Openen** onder het extensielogo en vervolgens op **Nieuwe POS**.



![new_tpos](assets/fr/11.webp)



Bepaal de naam van je verkooppunt en sluit vervolgens je Voltz wallet aan op je terminal om betalingen te innen. Je kunt fooien activeren door het vakje **Fooien activeren** aan te vinken. Activeer ook de optie voor het afdrukken van facturen als je ontvangstbewijzen wilt uitgeven aan je klanten (deze functionaliteit is nog in ontwikkeling, dus er kunnen storingen optreden).



De betaalautomaat bevat ook een belastingconfiguratie als je de belasting van je land direct op je producten wilt toepassen.



![tpos](assets/fr/12.webp)



Zodra je POS-terminal is aangemaakt, kun je vooraf geconfigureerde producten en diensten toevoegen om een soepele betalings- en boekhoudervaring voor jou en je klanten te garanderen.



![product](assets/fr/13.webp)



Maak je producten aan door hun naam te definiëren, een afbeelding toe te voegen en een verkoopprijs in te stellen.  Je kunt je producten categoriseren om ze gemakkelijker te kunnen volgen. Je kunt belastingen direct op een specifiek product toepassen. Als het product geen belasting heeft, wordt de belasting die is ingesteld bij het aanmaken van de betaalautomaat automatisch toegepast.



![products](assets/fr/14.webp)



Je kunt je productlijst automatisch importeren vanuit een JSON-indeling door op de knop **Importeren/Exporteren** te klikken.



![exports](assets/fr/15.webp)



Ga naar de kassa via de link door op het pictogram **Nieuw tabblad** te klikken, of deel je kassaplatform via een QR-code met je klanten door op het pictogram **QR-code** te klikken.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Je klanten kunnen via deze interface je catalogus raadplegen en betalen.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



In de groep beschikbare extensies vind je ook tools zoals de **Invoice** en **Payment Link** extensies, waarmee je generate facturen met specifieke producten kunt maken om geïsoleerde betalingen te innen zonder via de betaalautomaat te gaan.



## Houd je betalingen bij



In het menu **Betalingen** geeft Voltz je een overzicht van de betalingen aan je verschillende portefeuilles.


Je kunt je betalingen volgen via :




- Status.
- Het label: bijvoorbeeld **TPOS** voor betalingen in verkooppunten en **lnhub** via de mobiele verbinding in Zeus en Blue Wallet wallets.
- De verzamelportefeuille.
- Totaal inkomende en uitgaande betalingen.
- Een goed gedefinieerde periode.



![payments](assets/fr/22.webp)



## Meer opties



Voltz is ook een infrastructuur waarop je je eigen oplossingen kunt bouwen. In de **Extensies** sectie vind je een handleiding voor het ontwikkelen van je eigen extensies binnen het Voltz en LnBits ecosysteem.



![build](assets/fr/23.webp)



In het geval dat je oplossingen wilt ontwikkelen buiten het ecosysteem om, maar toch hun infrastructuur wilt gebruiken, vind je in de **URL van node** sectie API sleutels en documentatie-informatie met een voorbeeld van wat je met deze gegevens kunt doen.



Je kunt Lightning-facturen maken vanuit je applicaties met je Voltz wallet, Lightning-facturen betalen, facturen decoderen en verifiëren.



![keys](assets/fr/24.webp)



Je hebt nu een goed begrip van Voltz. Als je deze tutorial leuk vond, dan weten we zeker dat je meer zult leren over de beste methodes en tools om bitcoin in je bedrijf te integreren met onze cursus: Bitcoin voor bedrijven.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a