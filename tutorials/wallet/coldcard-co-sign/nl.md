---
name: COLDCARD - Medeondertekenen
description: Ontdek de Co-Sign-functie en gebruik deze op je COLDCARD
---

![cover](assets/cover.webp)


*NB: Deze tutorial is bedoeld voor mensen die al enige ervaring hebben met multisignature wallets, Coinkite apparaten en software zoals Sparrow wallet of Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Waarom ColdCard medeondertekenen?



Met deze functie kunt u **bestedingsvoorwaarden** toevoegen aan uw ColdCard (Q of Mk4) apparaat op de manier van een Hardware Security Module (HSM), om uw geld te beschermen terwijl u aanzienlijke flexibiliteit en controle behoudt.



Bestedingsvoorwaarden kunnen bijvoorbeeld zijn:





- Limieten op grootte**: beperk de hoeveelheid bitcoins die je kunt uitgeven in een enkele transactie.
- Snelheidslimieten:** bepaal hoeveel transacties je kunt uitvoeren per tijdseenheid (per uur, dag, week, etc.), waarbij je een minimum aantal blokken ertussen nodig hebt.
- Vooraf goedgekeurde adressen:** Sta alleen toe dat bitcoins worden verzonden naar vooraf goedgekeurde adressen.
- Authenticatie met twee factoren:** Vereist bevestiging van een mobiele 2FA-toepassing van derden (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) op een smartphone/tablet met internettoegang die NFC ondersteunt.



**Hoe het werkt



Door een tweede seed toe te voegen aan uw ColdCard Mk4 of Q apparaat, genaamd de "Spending Policy Key", waar we in deze tutorial naar zullen verwijzen als de "C Key".


Naast deze extra seed, wordt je gevraagd om Supply minstens één extra sleutel (XPUB) te geven, die we een "Backup Key" zullen noemen, om een Wallet Multisig 2-op-N te maken.



Samengevat, we gaan een Wallet Multisig aanmaken en uw ColdCard apparaat zal 2 van de private sleutels bevatten die nodig zijn om het geld uit te geven, de seed master van het apparaat en de "Spending Policy Key".



Elke keer dat de "C Key" wordt gevraagd om te tekenen, zullen de gespecificeerde bestedingsvoorwaarden van toepassing zijn en zal de ColdCard alleen tekenen als de transactie hieraan voldoet.



Als je af wilt zien van deze bestedingsvoorwaarden, dan kan dat:




- door te ondertekenen met één van de reservesleutels en de seed hand, of 2 reservesleutels afhankelijk van de grootte van je Multisig.
- door in het menu "Medeondertekenen" de "Beleidsregelsleutel Uitgaven" of de "C-sleutel" in te voeren. **De laatste kan niet rechtstreeks op het apparaat worden geraadpleegd, anders zou iedereen de ingestelde bestedingsvoorwaarden kunnen annuleren.**




## ColdCard medeondertekening configureren



![video](https://youtu.be/MjMPDUWWegw)



### 1- Functionaliteit activeren



Zorg er allereerst voor dat je apparaat ten minste de nieuwste firmwareversie heeft:




- Mk4: v5.4.2
- V: v1.3.2Q




Op uw Mk4 of ColdCardQ, ga naar *Advanced Tools > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*In de volgende tutorial worden voor het gemak screenshots genomen op een ColdCardQ, maar de stappen en menu's zijn identiek tussen de Mk4 en de Q.*



Er wordt een samenvatting van de functionaliteit weergegeven.


De terminologie die gebruikt wordt om de sleutels aan te duiden, en die we opnieuw zullen gebruiken in de 2-op-3 multi-handtekening Wallet die we gaan maken, is:



Toets A = coldcard master seed


Toets B = Back-up toets


Toets C = Sleutel uitgavenbeleid



Klik op **"ENTER"**.



![Co-Sign](assets/fr/02.webp)



De volgende stap is beslissen welke privésleutel zal fungeren als de "Beleidsleutel Uitgeven" of "Sleutel C".



We zien dat we verschillende opties hebben:





- Of druk op **"ENTER"** om generate een nieuwe seed zin van 12 woorden te maken.





- Klik op **"(1) "** om een bestaande seed van 12 woorden te importeren, of kies **"(2) "** om een bestaande seed van 24 woorden te importeren.





- Of druk op **"(6) "** om een seed uit de kluis van je apparaat te importeren.



Voor deze tutorial hebben we besloten een bestaande seed met 12 woorden te importeren door op **"(1)"** te drukken. Dit kan een seed BIP39 zijn die je al bezit en waarvan je uiteraard een back-up hebt.



Gebruik je toetsenbord om de 12 woorden van je seed in te voeren. Voor dit voorbeeld kiezen we de seed geldige zin rund x 12. Druk vervolgens op **"ENTER"**.


*NB: als je geen back-up van deze seed hebt, kun je de "Medeondertekenen"-instellingen op je apparaat niet meer wijzigen om je bestedingsvoorwaarden te wijzigen*



De functie "Medeondertekenen" is nu geactiveerd op het apparaat. Vervolgens moeten we onze bestedingsvoorwaarden kiezen en het aanmaken van de Wallet met meerdere handtekeningen voltooien.



![Co-Sign](assets/fr/03.webp)



### 2- Kies de bestedingsvoorwaarden of "*bestedingsbeleid*"



Hier geven we de bestedingsvoorwaarden op waaraan moet worden voldaan als de **"C Key"** of **"Spending Policy Key**" een transactie ondertekent.



Klik in het menu **"Medeondertekenen"** op **"Uitgavenbeleid**".



Je kunt dan de maximale grootte kiezen, d.w.z. het maximale aantal satoshi's dat in één transactie kan worden uitgegeven.



Voor dit voorbeeld kiezen we een maximale magnitude van **21212** satoshis. Klik op **"ENTER"** om te bevestigen.




![Co-Sign](assets/fr/04.webp)



Vervolgens kiezen we ervoor om de maximale snelheid in te stellen, d.w.z. het aantal transacties dat het apparaat per tijdseenheid kan ondertekenen. Voor deze tutorial kiezen we voor onbeperkte snelheid, d.w.z. geen limiet op het aantal transacties.




![Co-Sign](assets/fr/05.webp)



### 3- Maak Wallet Multisig 2-op-N



We moeten nog een derde sleutel kiezen voor onze Wallet Multisig, namelijk de **"Backup Key"** (Sleutel B), naast de **master seed** (Sleutel A) en de **"Spending Policy Key"** (Sleutel C).



Onze "B Key" moet worden geïmporteerd via SD-kaart of via QR-code in het geval van ColdCardQ.


Hiervoor hebben we een tweede ColdCard Mk4 of Q apparaat nodig, waarop onze "Key B" wordt gebruikt.



Op dit tweede apparaat met uw **"Backup Key"**, bijvoorbeeld een ColdCard Mk4 in dit voorbeeld, gaat u vanuit het hoofdmenu naar **"Instellingen"**, dan, **"Multisig Wallet"**, en tenslotte **"Export Xpub"**.


(Als je tweede apparaat een ColdCardQ is, heb je natuurlijk de optie om je Xpub via QR-code te exporteren).





![Co-Sign](assets/fr/06.webp)





Plaats in het volgende scherm een SD-kaart en klik rechtsonder op de knop **"Valideren"**. Klik vervolgens op **"(1) "** om het bestand op de SD-kaart op te slaan.



Het bestand bevat de vingerafdruk van de openbare sleutel (*fingerprint*) in de naam en heeft de vorm `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Plaats vervolgens de SD kaart in de "initiële" ColdCardQ om onze "Backup Key" (sleutel B) te importeren.


Kies in het menu "ColdCard Co-Signing" voor "Build 2-of-N" en klik op het volgende scherm op **"ENTER"** en vervolgens nogmaals **"ENTER"** om de "Backup Key" van de SD-kaart te importeren.



![Co-Sign](assets/fr/08.webp)



Op het volgende scherm laat je "Account Number" leeg (tenzij je precies weet wat je doet) en klik je weer op **"ENTER"**.



![Co-Sign](assets/fr/09.webp)



Eindelijk zijn we klaar om onze nieuwe Wallet Multisig 2-sur-3 te gebruiken, als volgt samengesteld:



Toets A= Coldcard Q master seed


Sleutel B= Back-up sleutel (net geïmporteerd van een tweede Coldcard apparaat)


Sleutel C= Beleidsregelsleutel Uitgaven (indien gebruikt om te ondertekenen, legt vooraf gedefinieerde uitgavenvoorwaarden op)



## Medeondertekenen met Sparrow wallet



Raadpleeg indien nodig de onderstaande tutorials om vertrouwd te raken met de Sparrow wallet software:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Uitvoer Wallet Multisig 2-sur-3 naar Sparrow wallet



We moeten nu onze Wallet Multisig exporteren naar Sparrow, zodat we daar onze eerste satoshi's kunnen plaatsen.



Vanuit het hoofdmenu van uw ColdCardQ, kies **"Instellingen"**, dan **"Multisig Portemonnees"**.


De set Multisig wallets die bekend zijn bij uw ColdCard worden nu getoond, met hier het aantal sleutels "2/3" (2-sur3). Kies de Multisig **"ColdCard Co-Sign"** die we zojuist hebben aangemaakt en klik dan op **"ColdCard Export"**.



![Co-Sign](assets/fr/10.webp)




Kies tenslotte de methode waarmee je Wallet naar Sparrow kunt exporteren. In ons geval kiezen we SD-kaart, dus klik op **"(1) "** na het plaatsen van een SD-kaart in sleuf A van het apparaat.



![Co-Sign](assets/fr/11.webp)



Selecteer dan in Sparrow wallet "Import Wallet".



![Co-Sign](assets/fr/12.webp)



Klik vervolgens op **"Bestand importeren"**. Kies vervolgens het bestand **"export-Coldcard_Co-sign.txt"** op je SD-kaart.



![Co-Sign](assets/fr/13.webp)



Geef je Wallet een naam zoals hij zal verschijnen in Sparrow, en kies een wachtwoord om je Wallet te coderen (of niet).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



We zijn nu klaar om onze eerste satoshi's te ontvangen en de bestedingsvoorwaarden te testen die we op onze Wallet hebben toegepast.



![Co-Sign](assets/fr/16.webp)



### 2- Testen van vooraf gedefinieerd uitgavenbeleid



Ter herinnering, we hadden besloten tot een maximale omvang van 21212 satoshi voor onze Wallet Multisig. Dit betekende dat elke keer dat de Spending Policiy Key (Sleutel C) een transactie ondertekende, deze alleen geldig zou zijn als het uitgegeven bedrag kleiner dan of gelijk aan 21212 satoshi's was.



Laten we het testen.


Laten we eerst op het tabblad "Ontvangen" in Sparrow klikken en een paar Satss op Wallet laten vallen, die we in deze tutorial zullen gebruiken.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Laten we dan proberen om meer uit te geven dan de 21212 toegestane satoshi's door een 50.000 Sats transactie te simuleren.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Na het scannen van de QR code van de *onondertekende* transactie met onze ColdCardQ om de transactie te importeren, is dit wat we te zien krijgen op het scherm. Een waarschuwing vertelt ons dat niet is voldaan aan de bestedingsvoorwaarden. Als we de transactie toch ondertekenen, dan zal slechts een van de 2 sleutels (de seed master op het apparaat, maar niet "Key C") ondertekenen.




![Co-Sign](assets/fr/23.webp)



Hier, na het importeren van onze transactie in Sparrow, kunnen we zien dat slechts één van de handtekeningen is toegepast op de transactie.



![Co-Sign](assets/fr/24.webp)




Laten we nu het experiment herhalen, maar dan voor een transactie van 21.000 satoshi's, dus minder dan de maximale magnitude (21212 Sats) die we voor deze Wallet hebben ingesteld.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Laten we proberen deze transactie te ondertekenen met onze ColdCardQ.



Geen probleem deze keer, er verschijnt geen waarschuwingsbericht en wanneer we de ondertekende transactie in Sparrow wallet importeren, zijn deze keer de 2 handtekeningen toegepast, waardoor de transactie geldig is en klaar voor distributie.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Medeondertekenen met Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA & adressen op witte lijsten



In deze paragraaf gebruiken we onze Wallet Multisig Co-Sign met Nunchuk en maken we van de gelegenheid gebruik om nieuwe bestedingsvoorwaarden toe te passen om te zien hoe het gaat.



Ga naar *Geavanceerde tools > ColdCard medeondertekening*.


We worden gevraagd om onze "Spending Policy Key" in te voeren om toegang te krijgen tot het menu waarmee we de bestedingsvoorwaarden kunnen wijzigen. In ons geval voeren we 12 x "rundvlees" in.



We hebben besloten om een magnitude van 21212 Sats aan te houden, en een maximale "Limit Velocity" om praktische redenen in verband met deze tutorial. Aan de andere kant gaan we het **"Whitelist Addresses"** menu gebruiken om de adressen op te leggen waaraan onze fondsen kunnen worden besteed.




![Co-Sign](assets/fr/31.webp)




Scan de QR-codes die horen bij de adressen (we kiezen er 2) die je wilt toevoegen aan je witte lijst en klik vervolgens op **"ENTER"**. Nadat je je adressen hebt gevalideerd door achtereenvolgens op **"ENTER"** te drukken, zien we dat de limieten voor Magnitude- en begunstigde adressen zijn toegepast.



![Co-Sign](assets/fr/32.webp)



Laten we tot slot, om een volledig beeld te krijgen van de mogelijkheden die "Co-Sign" biedt, de optie "Web 2FA" activeren.


Met deze functie kun je een TOTP RFC-6238-compatibele toepassing gebruiken, zoals Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / of Aegis Authenticator, om een extra Layer beveiliging toe te voegen.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Concreet betekent dit dat u, voordat u een transactie ondertekent, uw NFC-compatibel apparaat met internetverbinding in de buurt van uw Coldcard moet brengen. Dit brengt je automatisch naar een coldcard.com webpagina, waar je wordt gevraagd om de 6-cijferige code voor je aanvraag in te voeren. Als u de juiste code invoert, zal de webpagina u ofwel een QR code tonen om te scannen voor de ColdCardQ, of een 8-cijferige code om in te voeren op uw Mk4, om uw apparaat te autoriseren om te ondertekenen.





![Co-Sign](assets/fr/33.webp)



Na het scannen van de QR code in uw dubbele authenticatie applicatie en het toevoegen van uw ColdCard Co-Sign (CCC) account, wordt u gevraagd om te controleren of alles in orde is door uw 2FA code in te voeren.



Voer uw ColdCard in op de achterkant van uw NFC-apparaat.



![Co-Sign](assets/fr/34.webp)



Op de webpagina die opent voert u de 2FA code in van uw favoriete applicatie. Scan vervolgens de QR code die getoond wordt bij uw ColdCardQ (of voer de 8-cijferige code in die getoond wordt in uw Mk4).



![Co-Sign](assets/fr/35.webp)




We hebben nu een limiet ingesteld op de grootte (21212 Sats), bestemmingsadressen en dubbele authenticatie.



![Co-Sign](assets/fr/36.webp)



### 2- Wallet Multisig 2-op-3 uitvoeren naar Nunchuk



Laten we Wallet Multisig 2-on-3 deze keer exporteren naar Nunchuk, zoals we eerder deden met Sparrow.


Ga naar *Instellingen > Multisig Portemonnees > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Kies deze keer de NFC optie voor export door te klikken op de ColdcardQ knop met dezelfde naam **"NFC"**.



![Co-Sign](assets/fr/37.webp)



In Nunchuk, als u de toepassing voor de eerste keer opent, klikt u op **"Recover existing Wallet"**.



![Co-Sign](assets/fr/38.webp)



Als u al een Wallet in de toepassing hebt, klik dan op de **"+"** rechtsboven en vervolgens op **"Bestaande Wallet herstellen"**.



![Co-Sign](assets/fr/39.webp)




Kies dan **"Wallet herstellen van COLDCARD"** en vervolgens **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Tik tenslotte met de achterkant van uw smartphone op het scherm van uw ColdCardQ om de Wallet via NFC te importeren.



![Co-Sign](assets/fr/41.webp)



Onze rekening en de satoshis die eerder via Sparrow wallet werden gestort, zijn terug.



![Co-Sign](assets/fr/42.webp)



### 3- Testen van vooraf gedefinieerd uitgavenbeleid



Laten we nu proberen een transactie te doen die in strijd is met de 2 bestedingsvoorwaarden die we hebben ingesteld. **We proberen meer dan 21212 Sats uit te geven aan een Address die niet is goedgekeurd.** Laten we proberen 22 222 Sats naar een willekeurige Address te sturen.



![Co-Sign](assets/fr/43.webp)



Zodra de transactie is aangemaakt, klikt u op de 3 kleine puntjes in de rechterbovenhoek om deze te exporteren naar uw ColdCard.



![Co-Sign](assets/fr/44.webp)



Kies dan **"Exporteren via BBQR"**, en scan de QR code die bij je ColdCardQ staat.



![Co-Sign](assets/fr/45.webp)



Uw ColdcardQ toont dan een waarschuwing die, als u naar de onderkant van het scherm scrollt, verduidelijkt dat de transactie de bestedingsvoorwaarden schendt, zoals verwacht.



**Noteer dat het apparaat ons niet vertelt om welke bestedingsvoorwaarden het gaat, om te voorkomen dat een potentiële aanvaller de beperkingen probeert te omzeilen.**




![Co-Sign](assets/fr/46.webp)



Als u nog steeds valideert door op **"ENTER"** te drukken, verschijnt de QR-code die de ondertekende transactie voorstelt. Als u deze op de Nunchuk importeert, kunt u zien dat er slechts één handtekening is toegepast.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Laten we precies dezelfde operatie uitvoeren, maar deze keer met een transactie die de magnitudenlimiet (21212 Sats) respecteert en de satoshi's uitgeeft aan een van de 2 adressen die we vooraf hebben geconfigureerd.



We sturen de Nunchuk 12121 Sats naar een van onze 2 adressen. Daarna exporteren we de transactie naar onze ColdCard zoals eerder gedaan.



![Co-Sign](assets/fr/49.webp)




Na het importeren van de niet-ondertekende transactie in onze ColdCardQ, laten we eens kijken wat we deze keer te zien krijgen.



Een waarschuwing is altijd aanwezig, maar deze keer, scrollend naar de onderkant van het scherm, zien we dat het een kwestie is van het valideren van de transactie via 2FA. Het apparaat vraagt ons om onze ColdcardQ dicht bij onze NFC terminal (smartphone of tablet) met internetverbinding te brengen, wat we doen.



![Co-Sign](assets/fr/50.webp)



Een webpagina opent op onze smartphone en vraagt ons om onze 2FA-code in te voeren, wat we doen dankzij Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Scan vervolgens de QR code die op de webpagina verschijnt om uw ColdCard te autoriseren om de transactie te ondertekenen.


De transactie is nu ondertekend door de 2 sleutels en daarom geldig.



Als "Push Tx" is ingeschakeld op uw ColdCardQ, kunt u de transactie direct broadcasten naar het netwerk met een simpele tik op de achterkant van uw smartphone.



![Co-Sign](assets/fr/52.webp)




Als u "Push tx" niet geactiveerd heeft, druk dan op de "QR" knop op uw ColdCardQ om de ondertekende transactie weer te geven als een QR code, en importeer het op Nunchuk, op dezelfde manier als in het vorige voorbeeld.



![Co-Sign](assets/fr/53.webp)



Deze keer zien we dat er 2 handtekeningen zijn gezet, dus de transactie is klaar om uitgezonden te worden op het Bitcoin netwerk.



![Co-Sign](assets/fr/54.webp)




We zijn aan het einde gekomen van deze tutorial, die je een overzicht geeft van de mogelijkheden van de Co-Sign functionaliteit die geïntegreerd is in de ColdCardQ en Mk4 apparaten van Coinkite, maar ook het gebruik ervan via wallets zoals de Sparrow en Nunchuk.