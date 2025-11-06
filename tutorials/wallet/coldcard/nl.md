---
name: COLDCARD Mk

description: Een Bitcoin private sleutel aanmaken, back-uppen en gebruiken met een Coldcard apparaat en Bitcoin core
---

![cover](assets/cover.webp)


een Bitcoin private sleutel maken, back-uppen en gebruiken met een Coldcard apparaat en Bitcoin Core_


## Complete handleiding voor het genereren van een private sleutel met een Coldcard en het gebruik ervan via de Interface van je Bitcoin core knooppunt!


De kern van het netwerkgebruik van Bitcoin ligt in het concept van asymmetrische cryptografie: een paar sleutels - een privé en een publiek - die gegevens versleutelen en ontsleutelen, een concept dat de privacy van communicatie garandeert.


In het geval van Bitcoin zijn we door het genereren van zo'n paar private en publieke sleutels in staat om bitcoins op te slaan (UTXO of Unspent Transaction Output) en transacties te ondertekenen om ze uit te geven.


Tegenwoordig zijn er meerdere tools beschikbaar om het willekeurig genereren van een private sleutel en de back-up ervan in tekstvorm te vergemakkelijken met behulp van BIP 39 - een standaard die bepaalt hoe wallets een Mnemonic zin (seed zin) associëren met encryptiesleutels. Meestal bestaat de Mnemonic zin uit 12 of 24 woorden, waarvan een veilige back-up moet worden gemaakt om een Wallet en de bijbehorende bitcoins te kunnen herstellen.


In dit artikel leren we hoe we een private sleutel generate kunnen maken met een Coldcard Mk4, een van de meest gebruikte en veilige apparaten in de wereld van Bitcoin, met behulp van de dobbelsteenrolmethode om maximale entropie te garanderen, en hoe we het kunnen gebruiken met Bitcoin core op een air-gapped manier!


**Opmerking:🧰** Gebruik de volgende hulpmiddelen om de gids te gebruiken:



- Coldcard-apparaat (Mk3 of Mk4)
- MicroSD-kaart (4 GB is voldoende)
- Magnetische USB-kabel met alleen voeding (mini-usb voor Mk3, usb-c voor Mk4)
- Een of meer kwaliteitsdobbelstenen


## Een nieuwe Mnemonic zin genereren met een Coldcard


We beginnen het proces van het maken van een private key vanaf nul, uitgaande van een vers uitgepakte Coldcard waarop al een PIN is ingesteld (volg de stappen op de Coldcard tijdens de initialisatie van het apparaat).


**Note🚨:** Volg deze stappen om de privésleutel van een reeds geconfigureerde Coldcard opnieuw in te stellen:

geavanceerd/Gereedschappen > Gevarenzone > seed functies > seed vernietigen > ✓_


**Let op:** uw Coldcard zal na deze stappen de private key vergeten. Zorg ervoor dat u een goede back-up hebt gemaakt van uw Mnemonic zinsdeel als u het later wilt kunnen herstellen.


## Te volgen stappen:


Verbinding maken met de Coldcard met PIN > Nieuwe seed woorden > 24 woorden dobbelen


Werp 100 keer met een dobbelsteen en noteer na elke worp het resultaat van 1 tot 6 op de Coldcard. Door deze methode toe te passen, creëer je 256 bytes aan entropie, wat de creatie van een volledig willekeurige privésleutel bevordert. Coinkite levert ook de nodige documentatie voor onafhankelijke verificatie van hun entropiegeneratiesysteem.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


Zodra de 100 dobbelstenen zijn gegooid, druk je op ✓ en schrijf je de 24 verkregen woorden op volgorde op. Verifieer twee keer en druk op ✓. Tot slot hoef je alleen nog maar de verificatietest van de 24 woorden op de Coldcard te voltooien en voila, je nieuwe privésleutel is gemaakt!


Kies vervolgens of je de NFC- (Mk4) en USB-functies wel of niet wilt activeren door de weergegeven stappen te volgen. Eenmaal in het hoofdmenu is het nu tijd om de firmware van het apparaat bij te werken. Ga naar Geavanceerd/Tools > Firmware upgraden > Versie weergeven en controleer de officiële website om de laatste beschikbare versie te valideren en te downloaden. Het is raadzaam om de Coldcard te updaten om te profiteren van maximale beveiliging.


Voordat je verder gaat, is het aan te raden om de Master Key Fingerprint (XFP) te noteren die bij de private sleutel hoort. Met deze gegevens kun je snel valideren of je de juiste Wallet hebt, bijvoorbeeld in het geval van herstel. Ga naar Geavanceerd/Tools > Identiteit weergeven > Master Key Fingerprint (XFP) en noteer de reeks van acht alfanumerieke tekens die u hebt verkregen. De XFP kan op dezelfde plaats genoteerd worden als de Mnemonic zin, het zijn geen gevoelige gegevens.


**Noot:💡** het is aanbevolen om de back-up van uw Mnemonic zin in een andere software te testen. Om dit veilig te doen, raadpleeg ons artikel Verifieer de back-up van een Bitcoin Wallet met Tails in minder dan 5 minuten.


## Beveiligingsbonus: de "geheime zin" (optioneel)


Een passphrase (geheime zin) is een geweldig element om toe te voegen aan een Wallet configuratie om een Layer van beveiliging toe te voegen om je bitcoins te beschermen. De passphrase fungeert als een soort 25e woord voor de Mnemonic zin. Eenmaal toegevoegd, wordt een compleet nieuwe Wallet aangemaakt, samen met een private sleutel en de bijbehorende Mnemonic zin. Het is niet nodig om de nieuwe Mnemonic zin op te schrijven, want deze Wallet is toegankelijk door de initiële Mnemonic zin te combineren met de gekozen passphrase.


Het doel is om de passphrase apart van de Mnemonic zin te noteren, omdat een aanvaller die toegang heeft tot beide items toegang heeft tot de fondsen. Aan de andere kant zal een aanvaller die slechts toegang heeft tot één van deze items geen toegang hebben tot de fondsen, en het is dit specifieke voordeel dat het veiligheidsniveau van de Wallet configuratie optimaliseert.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## Stappen om een passphrase toe te voegen met Coldcard:


passphrase > Woorden toevoegen (aanbevolen) > Toepassen. Het apparaat zal de XFP van de nieuw gegenereerde Wallet weergeven met de passphrase, die genoteerd moet worden met de passphrase om dezelfde redenen als eerder genoemd.


**Tip💡** Hier staan extra bronnen met betrekking tot de passphrase:



- [Hier](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) staat de eerste van _Trezor_;
- [Hier](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) kun je de tweede vinden door _Coinkite_;
- En [hier](https://armantheparman.com/passphrase/) vindt u de laatste door _armantheparman_.


## Wallet exporteren naar Bitcoin core


De Wallet is nu klaar om geëxporteerd te worden naar software voor interactie met het Bitcoin netwerk. In deze handleiding gebruiken we Bitcoin core (v24.1).


Raadpleeg onze installatie- en configuratiegidsen voor Bitcoin core:



- **Je eigen knooppunt beheren met Bitcoin core:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- **Tor configureren voor een Bitcoin core knooppunt:** https://agora256.com/configuration-tor-Bitcoin-core/


Plaats eerst een micro SD-kaart in de Coldcard en exporteer dan de Wallet voor Bitcoin core door deze stappen te volgen: Geavanceerd/Tools > Exporteer Wallet > Bitcoin core. Er worden twee bestanden naar de micro SD-kaart geschreven: Bitcoin-core.sig & Bitcoin-core.txt. Plaats de micro SD-kaart in de computer waar Bitcoin core is geïnstalleerd en open het .txt-bestand. Je zult de regel "Voor Wallet met hoofdsleutel vingerafdruk" zien Controleer of de XFP van acht tekens overeenkomt met de XFP die u hebt genoteerd bij het maken van uw privésleutel

Voordat we de instructies in het bestand volgen, beginnen we met het voorbereiden van de Wallet in de Bitcoin core Interface door deze stappen te volgen: ga naar het tabblad File > Create a Wallet. Kies een naam voor uw Wallet (verwisselbare term met "porte-monnaie" in Core) en vink de opties Disable private keys, Create an empty Wallet, en Wallet descriptors aan, zoals in de afbeelding hieronder. Druk vervolgens op de knop Create.


![create a wallet](assets/guide-agora/3.webp)


Zodra de Wallet is aangemaakt in Bitcoin core, ga je naar het tabblad Venster > Console en zorg je ervoor dat de geselecteerde Wallet bovenaan de pagina de naam weergeeft van degene die je hebt aangemaakt.


Kopieer nu in het .txt-bestand dat eerder door de Coldcard is gegenereerd de regel die begint met importdescriptors en plak deze in de Bitcoin core console. Een antwoord met de regel "success": true zou moeten worden teruggezonden.


![nodes window](assets/guide-agora/4.webp)


Als het antwoord "message": "Ranged descriptors should not have a label", wis dan de regel "label": "Coldcard xxxx0000" in de gekopieerde regel uit het .txt-bestand en plak dan de volledige regel terug in de Bitcoin core console.


Indien nodig kunt u hulp vinden [hier](https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) op Coldcard Github.


## Validatie van Wallet import in Bitcoin core


Om er zeker van te zijn dat de operatie succesvol was, is het noodzakelijk om te valideren dat de gewenste Wallet in Bitcoin core is geïmporteerd. Een eenvoudige methode om dit te bevestigen is door te controleren of de adressen die in de Coldcard zijn gegenereerd, overeenkomen met de adressen die in Bitcoin core zijn gegenereerd.


Bitcoin core: Ontvangen > Een nieuwe ontvangende Address maken

Coldcard: Address Explorer > Kies de Address die begint met bc1q. De Coldcard Address 'bc1q' moet overeenkomen met de Address die in Bitcoin core wordt weergegeven.

Transacties ontvangen en verzenden in 'air-gapped' modus


Een transactie ontvangen is heel eenvoudig: druk op Ontvangen, label de transactie (optioneel, maar aanbevolen) en maak een nieuwe ontvangende Address aan. Daarna hoef je alleen nog maar de Address met de verzender te delen.


Nu, het sleutelelement van deze Coldcard + Bitcoin core setup is het versturen van transacties zonder dat de Coldcard en zijn private sleutel verbonden zijn met het internet, een methode genaamd air-gapped die gebruik maakt van de TBSP (PSBT - Partially Signed Bitcoin Transactions) functie van Bitcoin.

In essentie gebruiken we de Bitcoin core Interface om een transactie te construeren, die we vervolgens via de micro SD kaart exporteren naar de Coldcard om te ondertekenen, waarna we het ondertekende transactiebestand terugsturen naar de Bitcoin core en de transactie naar het netwerk zenden. We moeten het op deze manier doen, omdat de in Bitcoin core geïmporteerde Wallet geen private sleutel heeft, alleen de publieke sleutel (waarmee we generate onze ontvangstadressen kunnen bepalen), dus het is onmogelijk voor ons om een transactie direct in de software te ondertekenen om onze bitcoins uit te geven.


Controleer voordat u verder gaat of de volgende opties zijn ingeschakeld in Instellingen > Wallet:



- Coin controlefuncties inschakelen
- Onbevestigde munten uitgeven (optioneel)
- TBPS-controles inschakelen


![option ](assets/guide-agora/5.webp)


### Stappen om te verzenden in air-gapped modus:


Verzenden > Ingangen > kies de gewenste UTXO, voer dan de Address van de ontvanger in bij Betalen aan. Transactiekosten: Kies... > Aangepast > Voer de transactiekosten in (Bitcoin core berekent in Sats/kilobyte in plaats van sat/byte zoals de meeste alternatieve Wallet oplossingen. Dus 4000 Sats/kilobyte = 4 Sats/byte). Maak een niet-ondertekende transactie > sla het bestand op uw micro SD-kaart op en plaats deze in de Coldcard.


Druk in de Coldcard op Klaar om te ondertekenen, controleer de transactiegegevens, druk vervolgens op ✓ en plaats de micro SD-kaart terug in de computer zodra de ondertekende bestanden zijn gegenereerd.


Ga terug in Bitcoin core naar het tabblad Bestand > TBSP laden uit bestand en voer het ondertekende transactiebestand .PSBT in. Het vak PSBT Operations verschijnt op het scherm en bevestigt dat de transactie volledig ondertekend is en klaar om uitgezonden te worden. Je hoeft nu alleen nog maar op Broadcast transaction te drukken.


![PSBT operations](assets/guide-agora/6.webp)


### Conclusie


De combinatie van het Coldcard-apparaat met Bitcoin core, waarop je je eigen node draait, is krachtig. Voeg daar een privésleutel aan toe, gegenereerd met 100 dobbelsteenworpen en een geheime zin, en je Wallet configuratie wordt een geavanceerd en robuust fort.


Neem gerust contact met ons op om je opmerkingen en vragen te delen! Ons doel is om kennis te delen en ons begrip met de dag te vergroten.