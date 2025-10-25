---
name: BIP-39 Passphrase Ledger
description: Hoe voeg ik een passphrase toe aan mijn Ledger Wallet?
---
![cover](assets/cover.webp)


Een BIP39 passphrase is een optioneel wachtwoord dat, in combinatie met uw Mnemonic zinsdeel, een extra Layer beveiliging biedt voor deterministische en hiërarchische Bitcoin wallets. In deze tutorial bekijken we samen hoe je een passphrase instelt op je beveiligde Bitcoin Wallet op een Ledger (ongeacht het model).


Voordat je aan deze tutorial begint, als je niet bekend bent met het concept van een passphrase, hoe het werkt en de implicaties voor je Bitcoin Wallet, raad ik je ten zeerste aan dit andere theoretische artikel te raadplegen, waarin ik alles uitleg:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Hoe werkt de passphrase op een Ledger?


Met Ledger apparaten heb je twee verschillende opties om een passphrase op je Wallet te configureren: de "*PIN-tied*" optie en de "*temporary*" optie.


Met de optie "*PIN-gekoppeld*" koppelt u een passphrase aan een tweede pincode op uw Ledger. Dit betekent dat u 2 pincodes hebt: één om toegang te krijgen tot uw gewone Wallet zonder passphrase, en de andere om toegang te krijgen tot uw tweede Wallet die wordt beveiligd door de passphrase.


![PASSPHRASE BIP39](assets/notext/03.webp)


In principe, zelfs met deze passphrase optie gekoppeld aan de tweede PIN, blijft jouw passphrase jouw passphrase. Dit betekent dat als je je Ledger verliest en je bitcoins wilt terughalen op een ander apparaat of in andere software, je absoluut je 24-woorden zin en je **volledige passphrase** nodig hebt. De PIN-code die bij de passphrase hoort, wordt alleen gebruikt om toegang te krijgen op je huidige Ledger, maar werkt niet op andere grootboeken of andere software. Het is daarom belangrijk om een volledige back-up van uw passphrase te maken op een fysiek medium. **Het kennen van de secundaire PIN alleen is niet genoeg om weer toegang te krijgen tot uw Wallet**; het is gewoon een gemaksfunctie op uw Ledger.


Deze tweede PIN-optie is vooral interessant voor het afhandelen van fysieke aanvallen. Als een aanvaller je bijvoorbeeld dwingt om je apparaat te ontgrendelen om je tegoeden te stelen, kun je de eerste PIN gebruiken om toegang te krijgen tot een lok Wallet met een kleine hoeveelheid bitcoins, terwijl je hoofdtegoeden veilig blijven achter de tweede PIN.


Bovendien biedt deze optie alle veiligheidsvoordelen van de BIP39 passphrase zonder de beperking dat je het elke keer handmatig moet invoeren als je je signeerapparaat gebruikt. Hierdoor kunt u een lange en willekeurige passphrase gebruiken, waardoor de bescherming tegen brute force aanvallen wordt versterkt, terwijl u de moeilijkheid vermijdt om het elke keer handmatig in te voeren op de kleine toetsen van het apparaat.

De optie 'tijdelijke passphrase' slaat de passphrase niet op het apparaat op. Elke keer dat je toegang wilt tot je beveiligde Wallet, moet je handmatig de passphrase op de Ledger invoeren. Dit maakt het gebruik omslachtiger, maar verhoogt ook de veiligheid doordat er geen spoor van de passphrase op het apparaat achterblijft. Zodra je het apparaat uitschakelt, keert het terug naar de standaardtoestand en is een nieuwe invoer van de volledige passphrase nodig om toegang te krijgen tot de verborgen accounts. Deze "tijdelijke passphrase" optie is dus vergelijkbaar met de werking van andere hardware wallets.

In deze tutorial gebruik ik de Ledger Flex als voorbeeld. Als je echter een ander Ledger model gebruikt, blijft het proces hetzelfde. Voor de Ledger Stax is de Interface hetzelfde als die van de Ledger Flex. Wat betreft de Nano S, Nano S Plus en Nano X modellen, hoewel de Interface anders is, blijven het proces en de namen van de menu's hetzelfde.


**Attentie:** Als je al bitcoins hebt ontvangen op je Ledger voordat je de passphrase activeerde, moet je ze overmaken via een Bitcoin transactie. De passphrase genereert een set nieuwe sleutels, en creëert zo een Wallet die volledig onafhankelijk is van je initiële Wallet. Als u de passphrase toevoegt, hebt u een nieuwe Wallet, die leeg is. Dit verwijdert echter niet uw eerste Wallet zonder passphrase. U hebt er nog steeds toegang toe, rechtstreeks via uw Ledger zonder de passphrase in te voeren, of via een andere software met behulp van uw 24-woorden zin.


Voordat je met deze tutorial begint, moet je ervoor zorgen dat je je Ledger al geïnitialiseerd hebt en je Mnemonic frase al gegenereerd is. Als dit niet het geval is en je Ledger nieuw is, volg dan de specifieke tutorial voor jouw model die beschikbaar is op PlanB Network. Zodra deze stap is voltooid, kunt u terugkeren naar deze tutorial.


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Hoe installeer ik een tijdelijke passphrase met een Ledger?


Klik op de startpagina van je Ledger op het tandwiel voor instellingen.


![PASSPHRASE BIP39](assets/notext/04.webp)


Selecteer het menu "Geavanceerd" en vervolgens "passphrase instellen".


![PASSPHRASE BIP39](assets/notext/05.webp)


Dit is de stap waar je kunt kiezen tussen de "gekoppeld aan PIN" optie of de "tijdelijke" optie waar we het in het vorige deel over hadden. Hier leg ik uit hoe je een tijdelijke passphrase instelt, dus klik op "Tijdelijke passphrase instellen".


![PASSPHRASE BIP39](assets/notext/06.webp)

Je wordt dan gevraagd om je passphrase in te voeren. Kies een sterke passphrase en ga meteen verder met een fysieke back-up, op een medium zoals papier of metaal. In dit voorbeeld koos ik de passphrase: `fH3&kL@9mP#2sD5qR!82`. Klik na het invoeren van je passphrase op de knop "*Doorgaan*".

![PASSPHRASE BIP39](assets/notext/07.webp)


Controleer of je passphrase overeenkomt met wat je op je fysieke back-up hebt genoteerd en klik dan op de knop "*Ja, het klopt*" om te bevestigen.


![PASSPHRASE BIP39](assets/notext/08.webp)


Om het aanmaken van uw passphrase te voltooien, voert u de PIN-code van uw Ledger in. Vanaf nu, wanneer je met een passphrase toegang wilt krijgen tot je Wallet op de Ledger, moet je precies dezelfde stappen volgen als hier beschreven.


![PASSPHRASE BIP39](assets/notext/09.webp)


U kunt nu uw set publieke sleutels op Sparrow wallet importeren om uw Wallet te beheren. Op Sparrow zal dit overeenkomen met een andere Wallet dan uw initiële Wallet zonder passphrase.


Open Sparrow wallet. Zorg ervoor dat de software verbonden is met een knooppunt, klik dan op het tabblad "*Bestand*" en selecteer "*Nieuw Wallet*".


![PASSPHRASE BIP39](assets/notext/10.webp)


Kies een naam voor je Wallet die beschermd wordt door een passphrase. Voor dit voorbeeld heb ik gekozen voor een naam waarin expliciet de term "*passphrase*" voorkomt. Als je echter liever de discretie van deze Wallet op je computer houdt, kun je een minder suggestieve naam kiezen.


![PASSPHRASE BIP39](assets/notext/11.webp)


Kies het type script voor je Wallet. Ik raad je aan "*Taproot*" of "*Native SegWit*" te kiezen.


![PASSPHRASE BIP39](assets/notext/12.webp)


Sluit je Ledger aan op je computer en klik dan op "*Gekoppelde Hardware Wallet*". Controleer of je je passphrase al op je Ledger hebt ingevoerd. Zo niet, ga dan terug naar de vorige stappen om uw passphrase in te voeren. Voordat je verder gaat met scannen, moet je ook de "*Bitcoin*"-toepassing op je Ledger openen.


![PASSPHRASE BIP39](assets/notext/13.webp)


Klik op de knop "*Scan...*".


![PASSPHRASE BIP39](assets/notext/14.webp)


Klik op "*Import Keystore*" naast je Ledger.


![PASSPHRASE BIP39](assets/notext/15.webp)


Je Wallet, beschermd door de passphrase, is nu aangemaakt op Sparrow. Klik ter bevestiging op de knop "*Apply*".


![PASSPHRASE BIP39](assets/notext/16.webp)

Kies een sterk wachtwoord om de toegang tot Sparrow wallet te beveiligen. Dit wachtwoord verzekert de veiligheid van de toegang tot uw Wallet gegevens op Sparrow, waardoor uw openbare sleutels, adressen, labels en transactiegeschiedenis beschermd zijn tegen onbevoegde toegang.

Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager zodat je het niet vergeet.


![PASSPHRASE BIP39](assets/notext/17.webp)


En daar heb je het, je Wallet is nu aangemaakt! In het menu "*Instellingen*" geeft Sparrow je je "*Master fingerprint*". Dit is de vingerafdruk van je moedersleutel, die gebruikt wordt als basis voor het afleiden van je Wallet. Ik raad sterk aan om een kopie van deze vingerafdruk te bewaren. In mijn voorbeeld komt deze overeen met: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/18.webp)


Onthoud wat we in de vorige delen hebben gezegd: een fout, zelfs een kleine, bij het invoeren van je passphrase zal generate een geheel nieuwe Wallet met andere sleutels opleveren. Elke keer dat je er zeker van moet zijn dat je de juiste Wallet opent met de juiste passphrase, controleer dan of de vingerafdruk van je hoofdsleutel overeenkomt met degene die je hebt genoteerd. Deze informatie vormt op zichzelf geen risico voor de veiligheid van je geld of je privacy.


Voordat je je Wallet gebruikt met een passphrase, raad ik je sterk aan om een hersteltest uit te voeren. Noteer een referentiegegeven zoals je xpub of de vingerafdruk van je hoofdsleutel, reset dan je Ledger terwijl de Wallet nog leeg is. Probeer vervolgens uw Wallet te herstellen op de Ledger met behulp van uw papieren back-ups van de 24-woorden zin en de passphrase. Controleer of de informatie die na het herstel wordt gegenereerd, overeenkomt met wat je aanvankelijk noteerde. Als dat het geval is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn.


## Hoe stel ik een passphrase in die is gekoppeld aan een PIN met een Ledger?


Klik op de startpagina van je Ledger op het tandwiel voor instellingen.


![PASSPHRASE BIP39](assets/notext/19.webp)


Selecteer het menu "*Advanced*" en vervolgens "*Set passphrase*".


![PASSPHRASE BIP39](assets/notext/20.webp)


Dit is de stap waar je kunt kiezen tussen de "*gekoppeld aan PIN*" of "*tijdelijk*" optie waar we het in het vorige deel over hadden. Hier leg ik uit hoe je een passphrase aan een PIN kunt koppelen, dus klik op "*Stel passphrase in en koppel het aan een nieuwe PIN*".


![PASSPHRASE BIP39](assets/notext/21.webp)

Vervolgens moet je de PIN-code kiezen die aan je passphrase wordt gekoppeld. Net als bij de hoofd PIN code, is het aan te raden om een 8-cijferige PIN code te kiezen, zo willekeurig mogelijk. Zorg er ook voor dat je deze code op een andere locatie opslaat dan waar je Ledger Flex is opgeslagen.

In mijn geval is de hoofd PIN-code `58293647` en heb ik `71425839` gekozen als secundaire PIN-code voor de passphrase.


![PASSPHRASE BIP39](assets/notext/22.webp)


Je wordt dan gevraagd om je passphrase in te voeren. Kies een sterke passphrase en ga meteen verder met een fysieke back-up, op een medium zoals papier of metaal. In dit voorbeeld koos ik de passphrase: `fH3&kL@9mP#2sD5qR!82`. Klik na het invoeren van je passphrase op de knop "*Doorgaan*".


![PASSPHRASE BIP39](assets/notext/23.webp)


Controleer of je passphrase overeenkomt met wat je op je fysieke back-up hebt genoteerd en klik dan op de knop "*Ja, het klopt*" om te bevestigen.


![PASSPHRASE BIP39](assets/notext/24.webp)


Om het aanmaken van uw passphrase te voltooien, voert u de hoofdpincode van uw Ledger in (niet die van de passphrase).


![PASSPHRASE BIP39](assets/notext/25.webp)


Vanaf nu, wanneer je toegang wilt krijgen tot je Wallet met een passphrase op de Ledger, moet je niet de hoofd PIN-code invoeren, maar de secundaire PIN-code:


- Hoofdpincode (`58293647`) > Wallet zonder passphrase.
- Secundaire pincode (`71425839`) > Wallet met passphrase.


U kunt nu uw set publieke sleutels op Sparrow wallet importeren om uw Wallet te beheren. Op Sparrow zal dit overeenkomen met een andere Wallet dan uw initiële Wallet zonder passphrase.


Open Sparrow wallet. Zorg ervoor dat de software verbonden is met een knooppunt, klik dan op het tabblad "*Bestand*" en selecteer "*Nieuw Wallet*".


![PASSPHRASE BIP39](assets/notext/26.webp)


Kies een naam voor je Wallet die beschermd wordt door een passphrase. Voor dit voorbeeld heb ik gekozen voor een naam waarin expliciet de term "*passphrase*" voorkomt. Als je echter liever de discretie van deze Wallet op je computer houdt, kun je een minder suggestieve naam kiezen.


![PASSPHRASE BIP39](assets/notext/27.webp)


Kies het scripttype voor je Wallet. Ik raad je aan "*Taproot*" te kiezen, of anders "*Native SegWit*".


![PASSPHRASE BIP39](assets/notext/28.webp)

Sluit uw Ledger aan op uw computer en klik dan op "*Gekoppelde Hardware Wallet*". Controleer of uw passphrase al op uw Ledger staat door hem te ontgrendelen met de secundaire pincode. Zo niet, start dan uw Ledger opnieuw op en voer de pincode in die bij de passphrase hoort. Vergeet niet om de "*Bitcoin*"-toepassing op uw Ledger te openen, voordat u verder gaat met scannen.


![PASSPHRASE BIP39](assets/notext/29.webp)


Klik op de knop "*Scan...*".


![PASSPHRASE BIP39](assets/notext/30.webp)


Klik op "*Import Keystore*".


![PASSPHRASE BIP39](assets/notext/31.webp)


Je Wallet, beschermd door de passphrase, is nu aangemaakt op Sparrow. Klik ter bevestiging op de knop "*Toepassen*".


![PASSPHRASE BIP39](assets/notext/32.webp)


Kies een sterk wachtwoord om de toegang tot Sparrow wallet te beveiligen. Dit wachtwoord verzekert de veiligheid van de toegang tot uw Wallet-gegevens op Sparrow, wat helpt om uw openbare sleutels, adressen, labels en transactiegeschiedenis te beschermen tegen onbevoegde toegang.


Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager zodat je het niet vergeet.


![PASSPHRASE BIP39](assets/notext/33.webp)


En daar heb je het, je Wallet is nu aangemaakt! In het "*Instellingen*" menu, zal Sparrow je voorzien van je "*Master vingerafdruk*". Dit is de vingerafdruk van je hoofdsleutel, die gebruikt wordt als basis voor de afleiding van je Wallet. Ik raad sterk aan om een kopie van deze vingerafdruk te bewaren. In mijn voorbeeld komt het overeen met: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/34.webp)


Onthoud wat we in de vorige delen hebben gezegd: een fout, zelfs een kleine, bij het invoeren van uw passphrase zal generate een geheel nieuwe Wallet met andere sleutels opleveren. Elke keer dat je de toegang tot de juiste Wallet met de juiste passphrase moet verzekeren, controleer dan of de vingerafdruk van je moedersleutel overeenkomt met degene die je hebt genoteerd. Deze informatie vormt op zichzelf geen risico voor de veiligheid van uw geld of uw privacy.

Voordat je je Wallet met een passphrase gebruikt, raad ik je sterk aan om een dry-run hersteltest uit te voeren. Noteer een referentiegegeven, zoals je xpub of de vingerafdruk van je moedersleutel, en reset dan je Ledger terwijl de Wallet nog leeg is. Probeer vervolgens je Wallet te herstellen op de Ledger met behulp van je papieren back-ups van de 24-woorden zin en de passphrase. Controleer of de informatie die na het herstel wordt gegenereerd, overeenkomt met wat je in eerste instantie hebt genoteerd. Als dit het geval is, kunt u er zeker van zijn dat uw papieren back-ups betrouwbaar zijn.


Gefeliciteerd, je Bitcoin Wallet is nu beveiligd met een passphrase! Als je deze tutorial nuttig vond, zou ik het waarderen als je hieronder een duim omhoog achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan deze andere complete tutorial over het gebruik van de Ledger Flex te bekijken:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a