---
name: Alby

description: Browseruitbreiding voor Bitcoin en Lightning Network
---

![cover](assets/cover.webp)




Betalingen steeds eenvoudiger maken met bitcoin is de uitdaging waar veel bedrijven in de sector voor staan. Alby onderscheidt zich met zijn Alby wallet extensie voor browsers. Deze extensie heeft als doel een vloeiend raamwerk op te zetten dat automatisch adressen detecteert en waarmee je frictieloze bitcoinbetalingen kunt doen. In deze tutorial ontdekken we de Alby extensie en testen we hoe deze betalingen vanuit de browser mogelijk maakt.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby uitbreiding



De Alby extensie is een hulpmiddel waarmee je webbrowser gemakkelijk en veilig kan communiceren met het Bitcoin netwerk en de Lightning Network laag. Het wordt gekenmerkt door drie aspecten:




- Lightning Network wallet: Koppel je Alby node of account om snel en goedkoop bitcoin te versturen en ontvangen via de Lightning Network laag.
- Vloeiende betalingen via het web: Je hoeft geen QR-codes meer te scannen of te wisselen tussen applicaties voor bitcoinbetalingen op websites die Lightning ondersteunen. Het maakt soepele transacties mogelijk met één klik, of zonder bevestiging als je een budget hebt ingesteld.
- Een Nostr manager: De extensie beheert je Nostr sleutels, waardoor het makkelijk is om verbinding te maken en te communiceren met Nostr applicaties als een veilige ondertekenaar, zonder je private sleutel bloot te stellen aan elk platform.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Verbinding maken met de extensie



In deze tutorial gebruiken we de Alby extensie in de Firefox browser onder een Ubuntu besturingssysteem. Het is echter ook beschikbaar op Windows en met browsers zoals Chrome.



Je kunt de Alby extensie aan je browser toevoegen door de [Firefox] extensie store (https://addons.mozilla.org/fr/firefox/addon/alby/) of de [Chrome] extensie store (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe) te bezoeken.



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Het is belangrijk om te controleren of de auteur van de extensie inderdaad het officiële Alby account is, om elke vorm van piraterij of diefstal van je bitcoins te voorkomen.



Voeg de extensie toe aan je browser door op de knop rechts te klikken.


Geef de nodige rechten om de extensie te installeren en te gebruiken en prik de extensie vast op de werkbalk zodat je deze gemakkelijk kunt terugvinden.



![pin](assets/fr/03.webp)



U moet ook een ontgrendelingscode instellen (erg belangrijk), die veilige toegang tot uw Lightning wallet vanaf uw browser garandeert. We raden je aan een sterk alfanumeriek wachtwoord in te stellen.



ℹ️ Bewaar dit wachtwoord op een veilige plaats zodat u het kunt raadplegen als u het vergeet, want het kan worden gewijzigd maar niet worden teruggehaald.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby toont zijn aanpassingsvermogen door je twee keuzes te bieden:




- Ga door met een Alby account als je wilt genieten van de toepassingen terwijl je controle houdt over je bitcoins.
- Sluit je eigen wallet of Lightning node aan als je er al een hebt die door de extensie wordt ondersteund.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


In deze tutorial kiezen we ervoor om door te gaan met het Alby account om te profiteren van de mogelijkheden van het Alby ecosysteem.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Log in op uw Alby account, of maak er een aan als u er nog geen heeft.



![signup](assets/fr/05.webp)



## Je eerste betalingen doen



Eenmaal ingelogd kun je op de Alby extensie in de werkbalk klikken om je portfolio te openen.



![buzzin](assets/fr/06.webp)



Zodra je een Alby account hebt aangemaakt, moet je het verbinden met een wallet om satoshis te kunnen uitgeven. Om de bitcoin wallet aan je Alby account te koppelen, raden we je aan een Alby Hub node te gebruiken, die je op je computer kunt installeren of je kunt abonneren op een plan dat Alby aanbiedt.



![hubplan](assets/fr/13.webp)




In deze tutorial wordt ons Alby account ondersteund door een lokale installatie op onze machine.


Om je eigen Alby node te bouwen, raden we je onze Alby Hub tutorial aan.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Met dit knooppunt kun je zelfgemaakte Lightning-portefeuilles maken en je Lightning-kanalen voor het verzenden en ontvangen van satoshi's efficiënt beheren.



![channels](assets/fr/14.webp)



Open ontvangstkanalen die het totale aantal satoshi's bepalen dat je kunt ontvangen.



![receivechanal](assets/fr/15.webp)



Open verzendkanalen door het blokkeren van satoshis op een bitcoin onchain adres. De geblokkeerde satoshis bepalen het totaal aan satoshis dat je kunt uitgeven.



![spend](assets/fr/16.webp)



Je kunt nu satoshi's verzenden en ontvangen via de Alby extensie.



![exchange](assets/fr/08.webp)



Vanaf dit punt is de Alby extensie in staat om Lightning-adressen en facturen te detecteren die beschikbaar zijn op de webpagina's die je bezoekt, en zal ze je voorstellen om ze rechtstreeks vanuit je extensie te betalen in bitcoin of Lightning.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Herstelsleutels beveiligen met de hoofdsleutel



De hoofdsleutel die wordt aangeboden door de Alby uitbreiding werkt als een beschermende overlay die u in staat stelt om veilig te communiceren met de hoofdlaag van het Bitcoin netwerk (Onchain), het Nostr systeem en stelt u in staat om de Lightning verbinding met Nostr toepassingen te activeren.



![masterKey](assets/fr/11.webp)



Deze hoofdsleutel heeft de vorm van 12 woorden die lijken op je herstelzin. We raden je daarom aan om de sleutel op een veilige manier op te slaan, zodat hij altijd toegankelijk is.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



U kunt nu wrijvingsloze bitcoin- en Lightning-betalingen ervaren met de Alby extensie. Als je deze tutorial leuk vond, raden we je onze Alby Hub tutorial aan om je eigen Alby node op te zetten en alle aspecten van je Alby wallets te beheren vanuit een soepele en krachtige interface.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a