---
name: Proton Wallet
description: De Proton Bitcoin Wallet installeren en gebruiken
---
![cover](assets/cover.webp)


Proton is een Zwitsers bedrijf gespecialiseerd in digitale privacy, opgericht in 2014 door CERN-wetenschappers. Proton staat bekend om zijn open source-oplossingen en biedt een reeks diensten waaronder Proton Mail, Proton VPN en Proton Drive.


Proton heeft onlangs Proton Wallet geïntroduceerd, een open-source Bitcoin Wallet die beschikbaar is als mobiele app of webclient, gekoppeld aan je Proton-account. De functionaliteiten van de Wallet zijn vooralsnog vrij klassiek, met de essentiële tools die je van een goede Bitcoin Wallet verwacht, zoals RBF (*Replace-by-fee*), tagging, of de mogelijkheid om een BIP39 passphrase toe te voegen.


De speciale eigenschap van deze Wallet is de mogelijkheid om bitcoins te versturen met behulp van de e-mail Address van de ontvanger, waarvoor Proton automatisch een lege Bitcoin Address genereert die gekoppeld is aan de Wallet van de gebruiker. Proton is van plan om in de toekomst nieuwe functies toe te voegen, waaronder Lightning en coinjoins (waarschijnlijk met Whirlpool, zoals gesuggereerd door activiteit op hun GitHub repository).


## Maak een Proton-account aan


Om Proton Wallet te kunnen gebruiken, heb je een Proton account nodig. Je kunt er gratis een aanmaken door de eerste stappen van deze tutorial over het aanmaken van een Proton mailbox te volgen (alleen het gedeelte "*Een Proton account aanmaken*"). Zodra je account is aangemaakt, kun je verder met de rest van deze handleiding.


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Verbinden met Proton Wallet


Ga naar [de Proton Wallet website] (https://proton.me/Wallet) en klik op de knop "*Krijg Proton Wallet*".


![Image](assets/fr/01.webp)


Kies de abonnementsoptie "*Gratis*" en klik vervolgens op "*Aanmelden*".


![Image](assets/fr/02.webp)


Voer het e-mailadres en wachtwoord in dat aan je Proton-account is gekoppeld om in te loggen.


![Image](assets/fr/03.webp)


Je account wordt nu weergegeven. Klik op "*Begin nu met Proton Wallet*".


![Image](assets/fr/04.webp)


## Maak een Bitcoin Wallet


Selecteer de standaard fiatvaluta voor je account en klik dan op "*Nieuw Wallet* aanmaken".


![Image](assets/fr/05.webp)


Je Bitcoin Wallet is nu aangemaakt. Je kunt het theoretisch meteen gaan gebruiken, maar het is erg belangrijk om eerst je Mnemonic op te slaan. Klik hiervoor op "*Bewaar je Wallet*" in de rechterbovenhoek van de Interface.


![Image](assets/fr/06.webp)


Als je dat nog niet hebt gedaan op Proton, wordt je gevraagd om een back-up voor je account te maken en het te beveiligen met een 2FA-methode. Deze veiligheidsmaatregelen gelden voor je hele Proton account, maar zijn des te relevanter als je Bitcoin Wallet erin geïntegreerd is. Ik raad je sterk aan ze te implementeren.


![Image](assets/fr/07.webp)


Om je Mnemonic zin op te slaan, klik je op "*Backup deze Wallet's seed zin*".


![Image](assets/fr/08.webp)


Voer uw Proton-wachtwoord in.


![Image](assets/fr/09.webp)


Klik dan op "*Bekijk Wallet seed zin*" om de Mnemonic zin van je Wallet weer te geven.


![Image](assets/fr/10.webp)


Proton Wallet toont jouw 12-woord Mnemonic zin. **Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins**. Iedereen die in het bezit is van deze zin kan je fondsen stelen, zelfs zonder toegang tot je Proton account. De 12-woorden zin kan worden gebruikt om de toegang tot je bitcoins te herstellen als je de toegang tot je account verliest. Het is daarom heel belangrijk om het zorgvuldig op te slaan en het op een veilige locatie te bewaren.


Je kunt het op een stuk papier schrijven of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.


![Image](assets/fr/11.webp)


Voor meer informatie over de juiste manier om je Mnemonic zinnen op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

je moet natuurlijk nooit een foto maken van deze woorden, in tegenstelling tot wat ik doe in deze tutorial.


Klik op de knop "*Done*" zodra je je zin hebt opgeslagen.


![Image](assets/fr/12.webp)


## Ontdek de Interface


De Interface van Proton Wallet is zeer intuïtief. Aan de linkerkant vind je je verschillende portemonnees en de bijbehorende accounts. De "*Primary*" rekening is je hoofdrekening. Om redenen van vertrouwelijkheid worden bitcoins die je ontvangt via de Proton e-mail Address op een aparte rekening gezet, genaamd "*Bitcoin via E-mail*".


![Image](assets/fr/13.webp)


Om een nieuwe account toe te voegen, klik je op "*Account toevoegen*".


![Image](assets/fr/14.webp)


Om een nieuwe Wallet aan te maken, klik je op het "*+*" symbool naast "*Wallets*".


![Image](assets/fr/15.webp)


Hier kun je een BIP39 passphrase toevoegen aan een nieuwe Wallet.


![Image](assets/fr/16.webp)


Om je kennis van de passphrase te verdiepen, raad ik je deze tutorial aan:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Bitcoins ontvangen


Om bitcoins te ontvangen in je Wallet, selecteer je het gewenste account aan de linkerkant van de Interface en klik je vervolgens op de knop "*Ontvangen*".


![Image](assets/fr/17.webp)


Proton Wallet genereert dan automatisch een nieuwe, lege Address.


![Image](assets/fr/18.webp)


Zodra de transactie is voltooid, vind je deze in het gedeelte "*Transacties*". Klik op "*+Toevoegen*" om een label aan de transactie toe te wijzen.


![Image](assets/fr/19.webp)


## Bitcoins versturen


Nu je bitcoins in je Wallet hebt, kun je ze versturen. Selecteer het account van je keuze aan de linkerkant van de Interface en klik dan op "*Versturen*".


![Image](assets/fr/20.webp)


Voer de Bitcoin Address van de ontvanger in. Je kunt een QR-code scannen door op het kleine logo te klikken. Om naar een e-mail Address te sturen, voer je het direct in dit veld in. Als je de Bitcoin Address hebt ingevoerd, klik je op het kleine pijltje en vervolgens op "*Bevestigen*".


![Image](assets/fr/21.webp)


Voer het te versturen bedrag in, in fiatvaluta of in bitcoins, en klik vervolgens op "*Review*".


![Image](assets/fr/22.webp)


Selecteer de transactiekosten op basis van de huidige marktsituatie.


![Image](assets/fr/23.webp)


Voeg een label toe aan je transactie en controleer vervolgens alle details. Als alles correct is, klik je op "*Bevestigen en verzenden*" om de transactie te ondertekenen en te verzenden.


![Image](assets/fr/24.webp)


Je transactie wordt nu ter bevestiging weergegeven in het gedeelte "*Transacties*" van je account.


![Image](assets/fr/25.webp)


## Inloggen op de applicatie


Naast de webclient is Proton Wallet ook toegankelijk via een mobiele applicatie. Door de Wallet aan je Proton-account te koppelen, kun je je Wallet synchroniseren tussen de webclient en de mobiele app.


Download Proton Wallet uit je applicatiewinkel:




- [In de App Store] (https://apps.apple.com/us/app/proton-Wallet-secure-btc/id6479609548);
- [In de Google Play Store] (https://play.google.com/store/apps/details?id=me.proton.Wallet.android).


![Image](assets/fr/26.webp)


Klik na de installatie op "*Log in*" en voer je e-mailadres Address en Proton-wachtwoord in.


![Image](assets/fr/27.webp)


Je hebt dan toegang tot je Bitcoin Wallet, met dezelfde functies als op de webclient.


![Image](assets/fr/28.webp)


Gefeliciteerd, je weet nu hoe je Proton Wallet instelt en gebruikt. Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!


Om verder te gaan, raad ik deze tutorial aan over Jade Plus, Blockstream's nieuwste Hardware Wallet:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262