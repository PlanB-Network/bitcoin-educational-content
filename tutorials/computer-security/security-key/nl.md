---
name: YubiKey 2FA
description: Hoe gebruik je een fysieke beveiligingssleutel?
---
![cover](assets/cover.webp)


Tegenwoordig is twee-factor authenticatie (2FA) essentieel geworden voor het verbeteren van de beveiliging van online accounts tegen ongeautoriseerde toegang. Met de toename van cyberaanvallen is het soms niet voldoende om alleen op een wachtwoord te vertrouwen om je accounts te beveiligen.


2FA introduceert een extra Layer van beveiliging door een tweede vorm van authenticatie te vereisen naast het traditionele wachtwoord. Deze verificatie kan verschillende vormen aannemen, zoals een code die via sms wordt verstuurd, een dynamische code die wordt gegenereerd door een speciale app of het gebruik van een fysieke beveiligingssleutel. Het gebruik van 2FA vermindert het risico dat je accounts worden gecompromitteerd aanzienlijk, zelfs als je wachtwoord wordt gestolen.


In een andere tutorial heb ik uitgelegd hoe je een TOTP 2FA-applicatie instelt en gebruikt:


https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Hier zullen we zien hoe je een fysieke beveiligingssleutel kunt gebruiken als tweede authenticatiefactor voor al je accounts.


## Wat is een fysieke beveiligingssleutel?


Een fysieke beveiligingssleutel is een apparaat dat wordt gebruikt om de beveiliging van je online accounts te verbeteren door middel van twee-factor authenticatie (2FA). Deze apparaten lijken vaak op kleine USB-sleutels die in de poort van een computer moeten worden gestoken om te verifiëren dat het inderdaad de legitieme gebruiker is die verbinding probeert te maken.

![SECURITY KEY 2FA](assets/notext/01.webp)

Wanneer je inlogt op een account die beschermd is door 2FA en een fysieke beveiligingssleutel gebruikt, moet je niet alleen je gebruikelijke wachtwoord invoeren, maar ook de fysieke beveiligingssleutel in je computer steken en op een knop drukken om de verificatie te valideren. Deze methode voegt dus een extra Layer beveiliging toe, want zelfs als iemand je wachtwoord weet te bemachtigen, kan hij geen toegang krijgen tot je account zonder de sleutel fysiek te bezitten.


De fysieke beveiligingssleutel is bijzonder effectief omdat het twee verschillende soorten authenticatiefactoren combineert: het bewijs van kennis (het wachtwoord) en het bewijs van bezit (de fysieke sleutel).


Deze 2FA methode heeft echter ook nadelen. Ten eerste moet je altijd de beveiligingssleutel bij de hand hebben als je toegang wilt tot je accounts. Je moet hem misschien toevoegen aan je sleutelbos. Ten tweede brengt het gebruik van een fysieke beveiligingssleutel, in tegenstelling tot andere 2FA-methoden, initiële kosten met zich mee omdat je het kleine apparaatje moet kopen. De prijs van beveiligingssleutels varieert over het algemeen tussen €30 en €100, afhankelijk van de gekozen functies.


## Welke fysieke beveiligingssleutel kiezen?


Om je beveiligingssleutel te kiezen, moet je rekening houden met verschillende criteria.

Eerst en vooral moet je controleren welke protocollen het apparaat ondersteunt. Ik adviseer minimaal een sleutel te kiezen die OTP, FIDO2 en U2F ondersteunt. Deze details worden meestal door fabrikanten aangegeven in productbeschrijvingen. Om de compatibiliteit van elke sleutel te controleren, kun je ook [dongleauth.com](https://www.dongleauth.com/dongles/) bezoeken.

Controleer ook of de sleutel compatibel is met je besturingssysteem, hoewel bekende merken zoals Yubikey over het algemeen alle veelgebruikte systemen ondersteunen.


Je moet de sleutel ook kiezen op basis van het type poorten dat beschikbaar is op je computer of smartphone. Als je computer bijvoorbeeld alleen USB-C poorten heeft, kies dan een sleutel met een USB-C aansluiting. Sommige sleutels bieden ook verbindingsmogelijkheden via Bluetooth of NFC.

![SECURITY KEY 2FA](assets/notext/02.webp)

Je kunt toestellen ook vergelijken op basis van hun extra functies, zoals water- en Dust-bestendigheid, en op basis van de vorm en grootte van de toets.


Wat betreft merken van beveiligingssleutels is Yubico het meest bekend met zijn [YubiKey apparaten](https://www.yubico.com/), die ik persoonlijk gebruik en aanbeveel. Google biedt ook een apparaat met de [Titan Security Key](https://store.google.com/fr/product/titan_security_key). Voor open-source alternatieven zijn [SoloKeys](https://solokeys.com/) (non OTP) en [NitroKey](https://www.nitrokey.com/products/nitrokeys) interessante opties, maar ik heb nooit de kans gehad om ze te testen.


## Hoe gebruik je een fysieke beveiligingssleutel?


Zodra u uw beveiligingssleutel hebt ontvangen, hoeft u deze niet meer in te stellen. De sleutel is normaal gesproken klaar voor gebruik na ontvangst. Je kunt hem meteen gebruiken om je online accounts te beveiligen die dit type authenticatie ondersteunen. Ik zal je bijvoorbeeld laten zien hoe ik mijn Proton mail account kan beveiligen met deze fysieke beveiligingssleutel.

![SECURITY KEY 2FA](assets/notext/03.webp)

Je vindt de optie om 2FA te activeren in je accountinstellingen, vaak onder het gedeelte "*Wachtwoord*" of "*Veiligheid*". Klik op het selectievakje of de knop waarmee je 2FA kunt activeren met een fysieke sleutel.

![SECURITY KEY 2FA](assets/notext/04.webp)

Sluit je sleutel aan op je computer.

![SECURITY KEY 2FA](assets/notext/05.webp)

Raak de knop op je beveiligingssleutel aan om te valideren.

![SECURITY KEY 2FA](assets/notext/06.webp)

Voer een naam in om te onthouden welke toets je hebt gebruikt.

![SECURITY KEY 2FA](assets/notext/07.webp)

En daar heb je het, je beveiligingssleutel is succesvol toegevoegd voor de 2FA-verificatie van je account.

![SECURITY KEY 2FA](assets/notext/08.webp)

In mijn voorbeeld, als ik opnieuw verbinding probeer te maken met mijn Proton mail account, zal ik eerst gevraagd worden om mijn wachtwoord in te voeren samen met mijn gebruikersnaam. Dit is de eerste authenticatiefactor.

![SECURITY KEY 2FA](assets/notext/09.webp)

Vervolgens wordt mij gevraagd om mijn beveiligingssleutel in te voeren voor de tweede authenticatiefactor.

![SECURITY KEY 2FA](assets/notext/10.webp)

Vervolgens moet ik de knop op de fysieke sleutel aanraken om de verificatie te valideren en ben ik opnieuw verbonden met mijn Proton e-mailaccount.

![SECURITY KEY 2FA](assets/notext/11.webp)

Herhaal deze handeling voor alle online accounts die u op deze manier wilt beveiligen, vooral voor kritieke accounts zoals uw e-mailaccounts, uw wachtwoordbeheerders, uw cloud- en online opslagdiensten of uw financiële accounts.