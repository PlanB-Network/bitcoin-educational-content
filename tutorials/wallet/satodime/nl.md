---
name: Satodime
description: Ontdek hoe je Satodime kunt gebruiken met de mobiele applicatie
---
![cover](assets/cover.webp)



Deze handleiding leidt je door de installatie, de configuratie en het gebruik van de mobiele applicatie van Satodime. Je leert hoe je in het bezit komt van je kaart, kluizen aanmaakt, geld toevoegt, je private sleutels ontzegelt en terugvindt. In de bijlagen vind je bronnen, best practices en technische uitleg.



## Inleiding



**Satodime**, ontwikkeld door **[Satochip](https://satochip.io/fr/)**, is een veilige draagkaart voor het opslaan van Bitcoin op een tastbare en eenvoudige manier. Het fungeert als zelf-custodiale wallet hardware, waarbij je volledige controle hebt over je private sleutels zonder afhankelijk te zijn van een derde partij. Het is open-source en EAL6+ gecertificeerd en ondersteunt tot drie onafhankelijke kluizen.



### Achtergrond van het product



Satodime, een **carte au porteur, behoort toe aan wie deze fysiek bezit**, zonder noodzaak voor voorafgaande registratie of identificatie. Het voorziet in de behoefte aan veilige, draagbare opslag van bitcoins, zodat iedereen die de kaart bezit deze kan gebruiken of bitcoins kan overdragen door de kaart via de mobiele app te scannen om bezit te nemen of kluizen te ontzegelen. In tegenstelling tot een papieren biljet maakt de kaart gebruik van een veilige chip om de privésleutels te verzegelen, die pas worden onthuld na het ontzegelen, waardoor de kaart vergelijkbaar is met contant geld waarbij het eigendom wordt bepaald door fysiek bezit. De kaart is ideaal om bitcoins cadeau te geven en vergemakkelijkt de veilige overdracht van bitcoins van hand tot hand, terwijl de mobiele applicatie gebruik maakt van NFC voor toegankelijke smartphone-interactie.





- Beveiliging**: Privésleutels gegenereerd en opgeslagen in de fraudebestendige chip; zichtbare status (verzegeld, niet verzegeld, leeg).
- Kenmerken**: Bitcoins rechtstreeks kopen via de app (Paybis-partner); Mainnet en Testnet beheren.
- Open-source**: Code onder AGPLv3-licentie, controleerbaar op GitHub.



### Continue evolutie



De applicatie evolueert regelmatig. Kijk op de website of in de winkels van Satochip voor updates. Er kunnen bijvoorbeeld nieuwe blockchains of aankoopfunctionaliteiten worden toegevoegd. Controleer de [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) voor lopende ontwikkelingen.



## 1. Vereisten



Voordat je aan de slag gaat met **Satodime**, moet je ervoor zorgen dat je de volgende items hebt:





- Compatibele smartphone**: Android- of iOS-apparaat waarop NFC is ingeschakeld.
- Satodime**-kaart: Nieuw of niet geïnitialiseerd.
- Internetverbinding**: De app downloaden.
- Basiskennis**: Inzicht in private/publieke sleutels en de risico's van verlies (onomkeerbaar).
- Veilig medium**: Een veilige plaats om privésleutels op te slaan zodra ze zijn ontzegeld (papier, metaal; nooit digitaal).



## 2. Installatie





- Download de applicatie** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Controleer de ontwikkelaar (Satochip) om fraude te voorkomen.
 - Satodime is **open-source**. Broncode : [Satochip's GitHub](https://github.com/Toporin/Satodime-Applet).





- Installeer en start de applicatie**: Activeer indien nodig NFC op uw telefoon.



![image](assets/fr/01.webp)



## 3. Eerste configuratie



### 3.1 Toepassing starten en scannen



Open de app en volg de wizard. Plaats de Satodime-kaart op de NFC-lezer van je telefoon (meestal op de achterkant). Houd de kaart gedurende de hele bewerking ingedrukt voor een stabiele verbinding.





- Als NFC niet werkt, controleer dan de instellingen van je telefoon.
- Een toast bevestigt het succes: "Succesvol lezen".



![image](assets/fr/02.webp)



Als algemene regel geldt dat **voor alle volgende handelingen een bevestiging nodig is door de Satodime-kaart te scannen**



### 3.2 In bezit nemen van de kaart (*Ownership*)



Voor het eerste gebruik moet je eigenaar worden van de kaart om deze te beveiligen:





- Klik op "*Neem Ownership*" in de app.
- Bevestig de bewerking: dit genereert een unieke eigenaarsleutel.
- Scan de kaart opnieuw om de wijzigingen toe te passen.
- Waarschuwing**: Deze stap is onomkeerbaar. Raadpleeg [het artikel over *eigendom*](https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Creëer een veilige



Satodime ondersteunt tot 3 kluizen. Maak er een om bitcoin in op te slaan:





- Selecteer een lege kluis (bijvoorbeeld kluis 01).
- Selecteer blockchain (Bitcoin).
- Klik op "*Creëer & Seal*".
- Scan de kaart naar generate en verzegel de privésleutel (onbekend tot ontzegeling).
- Gefeliciteerd**: Je kluis is nu verzegeld en klaar om geld te ontvangen.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Fondsen toevoegen



Eenmaal verzegeld, laad je de kluis met bitcoins:





- Selecteer de kluis.
- Klik op "*Geld toevoegen*".
- Kopieer het openbare adres of scan de QR-code.
- Geld versturen vanuit een andere wallet.
- Controleer het saldo na bevestiging op de blockchain.
- Aankoopoptie: Klik op "*Koop*" om direct te kopen via Paybis (Visa, Mastercard, etc.). Toepasbare kosten.



![image](assets/fr/06.webp)



## 6. Een kluis ontzegelen



Om toegang te krijgen tot de privésleutel en het geld ergens anders naartoe over te maken, moet je de kluis ontgrendelen:





- Selecteer de verzegelde kluis.
- Klik op "Ontzegelen".
- Bevestig de waarschuwing: deze handeling is onomkeerbaar.
- Scan de kaart om deze te ontzegelen.
- De kluis is ingesteld op "*Unsealed*"; de privésleutel kan nu worden bekeken/geëxporteerd.
- Waarschuwing**: Eenmaal ontgrendeld, is de privésleutel toegankelijk. Als iemand je smartphone in handen krijgt, kan hij toegang krijgen tot deze sleutel en zo het geld in je kluis terugkrijgen (onomkeerbaar).



![image](assets/fr/07.webp)



## 7. Privé sleutel herstellen



Na het ontzegelen exporteer je de sleutel voor gebruik in een andere wallet:





- Zorg ervoor dat je in een veilige omgeving bent.
- Klik op "*Privésleutel weergeven*".
- Kies het formaat: Legacy, SegWit, WIF, enz.
- Kopieer de sleutel of scan de QR-code.
- Veiligheid**: Deel nooit je privésleutel. Sla hem offline op.
- Importeer het in een wallet softwareprogramma dat compatibel is met fondsbeheer (bijvoorbeeld Sparrow Wallet of Electrum).



![image](assets/fr/08.webp)





## 8. Kofferbak resetten



Het resetten van de kluis wist de bijbehorende privésleutel onherroepelijk. Met andere woorden, als u geen kopie van uw privésleutel hebt veiliggesteld of deze in een andere wallet hebt geïmporteerd, zal het resetten van de kluis leiden tot het onomkeerbare verlies van het geld dat erin zit.



![image](assets/fr/09.webp)



Het resetten van de koffer maakt de sleuf leeg en klaar voor een nieuwe koffer.



## 9. Eigendom overdragen



Om - bijvoorbeeld - bitcoins aan te bieden via Satodime, moet je :




- Word eigenaar van de kaart,
- Maak een Bitcoin kluis,
- Transfer zat daar,
- Eigendom van de kaart overdragen: de volgende persoon die de kaart scant, wordt de eigenaar,
- Geef de Satodime-kaart aan de persoon van je keuze en nodig hem of haar uit om de applicatie te downloaden en vervolgens de kaart te scannen om er eigenaar van te worden - en zo toegang te krijgen tot de bitcoins die erop 'opgeslagen' zijn.



![image](assets/fr/10.webp)




## BIJLAGEN



### A1. Beste praktijken



Om **Satodime** veilig te gebruiken:





- Beveilig de kaart**: Behandel hem als contant geld; verlies = verloren geld als het niet de eigenaar is.
- Back-up van sleutels**: Leg na het ontzegelen de privésleutels vast op een veilig fysiek medium. Nooit digitaal.
- Controleer status**: Scan altijd om het kaarteigendom en de verzegelde/onverzegelde status van kluizen te bevestigen.
- Vertrouwelijkheid**: Gebruik nieuwe adressen; vermijd gecentraliseerde uitwisselingen voor overdrachten.
- Updates**: Houd de app up-to-date via de stores.
- Herstel**: Als de kaart verloren is maar wel in bezit, staat het geld op de blockchain; gebruik de privésleutel als deze niet is verzegeld.



### A2. Extra middelen



Specifiek voor Satodime :




- [Satodime-product] (https://satochip.io/fr/product/satodime/)
- [Mobiele Gids](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy](https://planb.academy/) voor tutorials over zelfbehoud, privésleutels, enz.



**Sla je herstelzin** op:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutorial over de Satochip (het eerste product van het merk) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Zeedkeeper-tutorials:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Over Satochip



**Officiële links** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Ondersteuning: info@satochip.io



**Satochip** is een Belgisch bedrijf dat hardware- en softwareoplossingen ontwikkelt voor het beheren en opslaan van bitcoins en andere cryptocurrencies. Het vlaggenschipproduct, de Satochip hardware wallet, is een NFC-kaart uitgerust met een EAL6+ gecertificeerde secure element. Aangevuld met de Seedkeeper, een geheugensteuntje en geheimmanager, en de Satodime, een kaart aan toonder, biedt Satochip een uitgebreid assortiment dat is afgestemd op de behoeften van gebruikers. De apparaten, aangedreven door open source software, hebben als doel de beveiliging op Bitcoin te democratiseren.