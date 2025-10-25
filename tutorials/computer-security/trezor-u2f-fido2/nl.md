---
name: "Trezor U2F & FIDO2"
description: Versterk je online beveiliging met Trezor
---
![cover](assets/cover.webp)



Trezor apparaten zijn hardware wallets die oorspronkelijk ontworpen zijn om een Bitcoin Wallet te beveiligen, maar ze beschikken ook over geavanceerde opties voor sterke authenticatie op het web. Dankzij hun compatibiliteit met de **U2F**- en **FIDO2**-protocollen kun je de toegang tot je online accounts beveiligen zonder alleen op wachtwoorden te hoeven vertrouwen.



Het U2F-protocol (*Universal 2nd Factor*) werd in 2014 geïntroduceerd door Google en Yubico en vervolgens gestandaardiseerd door de FIDO Alliance. Het maakt het mogelijk om een tweede fysieke authenticatiefactor (2FA) toe te voegen bij het inloggen. Eenmaal geactiveerd moeten gebruikers, naast het klassieke wachtwoord, elke poging om verbinding te maken met hun account goedkeuren door op een knop op hun Trezor te drukken. In deze context werkt de Trezor op een vergelijkbare manier als een Yubikey.



Deze methode is gebaseerd op asymmetrische cryptografie: er worden geen geheime gegevens verzonden, waardoor phishing- of onderscheppingsaanvallen geen effect hebben. U2F wordt nu door veel online diensten ondersteund.



Naast U2F, dat tweefactorauthenticatie mogelijk maakt, ondersteunen Trezors ook FIDO2 (*Fast IDentity Online 2.0*), een evolutie van U2F. Dit is een gestandaardiseerd authenticatieprotocol uit 2018, dat de logica van U2F uitbreidt en wachtwoorden volledig wil vervangen. Het is gebaseerd op twee componenten: *WebAuthn* (browserkant) en *CTAP2* (fysieke sleutelkant). FIDO2 maakt "wachtwoordloze" authenticatie mogelijk: gebruikers identificeren zich alleen via hun Trezor-apparaat, dat fungeert als een uniek cryptografisch token, zonder extra wachtwoord. Dit protocol is nu compatibel met een aantal online diensten, met name die gericht zijn op het bedrijfsleven.



Naast "wachtwoordloze" functionaliteit maakt FIDO2 ook twee-factor authenticatie mogelijk op een vergelijkbare manier als U2F.



FIDO2 introduceert ook het begrip "resident credentials", d.w.z. identifiers die rechtstreeks in de Trezor zijn opgeslagen en die zowel de privésleutel bevatten die verbinding mogelijk maakt als de identificatiegegevens van de gebruiker. Dit mechanisme maakt authenticatie zonder wachtwoorden mogelijk: sluit gewoon je Trezor aan en bevestig de toegang, zonder ID of wachtwoord in te voeren. Bij niet-residente referenties, die conventioneler zijn, wordt alleen de privésleutel opgeslagen in het apparaat; de gebruikers-ID blijft opgeslagen op de server en moet dus bij elke verbinding worden ingevoerd. We zullen later bekijken hoe je ze kunt opslaan met je Trezor.



In deze tutorial ontdekken we hoe je U2F of FIDO2 activeert voor twee-factor authenticatie, en vervolgens hoe je FIDO2 configureert om toegang te krijgen tot je accounts zonder wachtwoord, rechtstreeks met je Trezor.



**Noot:** U2F is compatibel met alle Trezor-modellen, maar FIDO2 wordt alleen ondersteund op de Safe 3, Safe 5 en Model T, niet op de Model One.



## U2F/FIDO2 gebruiken voor 2FA op een Trezor



Voordat je begint, moet je ervoor zorgen dat je Bitcoin Wallet op je Trezor hebt ingesteld. Het is belangrijk om je Mnemonic correct op te slaan, omdat de sleutels die worden gebruikt voor U2F en FIDO2 in twee-factor authenticatie zijn afgeleid van deze Mnemonic. Als je Trezor zoekraakt of beschadigd raakt, kun je de toegang tot je sleutels herstellen door je Mnemonic zin in te voeren op een ander Trezor apparaat (merk op dat voor FIDO2 referenties in "*wachtwoordloze*" modus, seed alleen niet genoeg is, zoals we zullen zien in de volgende secties).



Sluit je Trezor aan op je computer en ontgrendel hem.



![Image](assets/fr/01.webp)



Ga naar het account dat je wilt beveiligen met twee-factor authenticatie. Ik ga bijvoorbeeld een Bitwarden-account gebruiken. Je vindt de 2FA-optie meestal in de service-instellingen, onder de tabbladen "*authentication*", "*security*", "*login*" of "*password*".



![Image](assets/fr/02.webp)



Selecteer in het gedeelte dat gewijd is aan twee-factor authenticatie de optie "*Passkey*" (de term kan variëren afhankelijk van de site die je gebruikt).



![Image](assets/fr/03.webp)



Vaak wordt u gevraagd om uw huidige wachtwoord te bevestigen.



![Image](assets/fr/04.webp)



Geef je beveiligingssleutel een naam voor gemakkelijke herkenning en klik dan op "*Read Key*".



![Image](assets/fr/05.webp)



Uw accountgegevens verschijnen op het scherm van de Trezor. Raak het scherm aan of druk op de knop om te bevestigen. U wordt ook gevraagd om uw pincode te bevestigen.



![Image](assets/fr/06.webp)



Registreer deze beveiligingssleutel.



![Image](assets/fr/07.webp)



Vanaf nu wordt je, wanneer je verbinding wilt maken met je account, naast je gebruikelijke wachtwoord ook gevraagd om je Trezor te verbinden.



![Image](assets/fr/08.webp)



Je kunt dan op het scherm van je Trezor drukken om de verificatie te bevestigen.



![Image](assets/fr/09.webp)



Het voordeel van het gebruik van een Hardware Wallet Trezor voor twee-factor authenticatie is dat je gemakkelijk je sleutels kunt terughalen dankzij de Mnemonic zin. Naast deze basisback-up kun je ook een noodcode gebruiken die wordt geleverd door elke service waarbij je 2FA hebt geactiveerd. Met deze noodcode kun je verbinding maken met je account als je je beveiligingssleutel verliest. Het vervangt dus de 2FA voor een verbinding indien nodig.



Op Bitwarden kunt u bijvoorbeeld toegang krijgen tot deze code door te klikken op "*Bekijk herstelcode*".



![Image](assets/fr/10.webp)



Ik raad je aan om deze code op een andere plaats te bewaren dan waar je je hoofdwachtwoord bewaart, om te voorkomen dat ze samen gestolen worden. Als je wachtwoord bijvoorbeeld is opgeslagen in een wachtwoordmanager, bewaar dan je 2FA-noodcode apart op papier.



Deze aanpak biedt je twee back-upniveaus in het geval van verlies van je Trezor voor 2FA-authenticatie: een eerste back-up met de Mnemonic zin voor al je accounts, en een tweede specifiek voor elke account met de noodcodes. Het is echter belangrijk **de rol van de Mnemonic niet te verwarren met die van de noodcodes**:




- De Mnemonic zin van 12 of 24 woorden geeft je niet alleen toegang tot de sleutels die worden gebruikt voor 2FA op al je accounts, maar ook tot je bitcoins die zijn beveiligd met je Trezor;
- Met de noodcode kunt u de 2FA-aanvraag tijdelijk alleen omzeilen op het betreffende account (in dit voorbeeld alleen op Bitwarden).



## FIDO2 gebruiken op een Trezor



Naast tweefactorauthenticatie maakt FIDO2 ook "wachtwoordloze" authenticatie mogelijk, d.w.z. zonder een wachtwoord te hoeven invoeren bij het aanmelden op een site. Sluit gewoon je Trezor aan op je computer om op deze manier toegang te krijgen tot je beveiligde account. Zo configureer je deze functie.



Voordat je begint, zorg ervoor dat je je Bitcoin Wallet op je Trezor hebt ingesteld. Het is belangrijk om de Mnemonic op te slaan, omdat de FIDO2 "*passwordless*" identifiers versleuteld zijn met je seed (hoe je deze identifiers correct opslaat, lees je in het volgende hoofdstuk).



Sluit de Trezor aan op je computer en ontgrendel hem.



![Image](assets/fr/01.webp)



Ga naar het account dat u wilt beveiligen in de **wachtwoordloze** modus. Ik gebruik een Bitwarden account als voorbeeld. Deze optie is meestal te vinden in de service-instellingen, vaak onder een tabblad *authenticatie*, *beveiliging* of *wachtwoord*.



Op Bitwarden is de optie bijvoorbeeld te vinden onder het tabblad "*Master password*". Klik op "*Aanzetten*" om authenticatie via FIDO2 te activeren.



![Image](assets/fr/11.webp)



Je wordt vaak gevraagd om je wachtwoord te bevestigen.



![Image](assets/fr/12.webp)



Uw accountgegevens verschijnen op het scherm van de Trezor. Raak het scherm aan of druk op de knop om te bevestigen. Je moet ook je pincode bevestigen.



![Image](assets/fr/13.webp)



Voeg op de site een naam toe om je beveiligingssleutel te onthouden en klik vervolgens op "*Aanzetten*".



![Image](assets/fr/14.webp)



Je wordt dan gevraagd om je te identificeren om te controleren of de sleutel goed werkt.



![Image](assets/fr/15.webp)



Vanaf nu is het bij het inloggen op je account niet meer nodig om je e-mail Address of login in te voeren. Klik gewoon op de knop om jezelf te verifiëren met een fysieke sleutel op het inlogformulier.



![Image](assets/fr/16.webp)



Bevestig de verbinding met uw Trezor door uw Hardware Wallet PIN in te voeren.



![Image](assets/fr/17.webp)



Je wordt verbonden met je account zonder dat je je wachtwoord hoeft in te voeren.



![Image](assets/fr/18.webp)



**Houd er rekening mee dat zelfs als je "*wachtwoordloze*" verificatie via FIDO2 op je Trezor activeert, het hoofdwachtwoord voor je online account nog steeds geldig is om in te loggen**



## Je FIDO2-referenties opslaan (credentials residents)



Als je FIDO2 of U2F gebruikt voor twee-factor authenticatie, d.w.z. om in te loggen bij accounts die een wachtwoord vereisen naast de 2FA validatie via je Trezor, dan zal de Mnemonic zinsnede alleen al toegang tot je sleutels geven. Als je echter FIDO2 gebruikt in de "*wachtwoordloze*" modus, zoals beschreven in de vorige sectie, dan is het nodig om een kopie te maken van je FIDO referenties en een back-up te maken van je Mnemonic zinsdeel, dat deze referenties versleutelt.



Hiervoor heb je een computer nodig waarop Python is geïnstalleerd. Open een terminal en voer het volgende commando uit om de benodigde Trezor-software te installeren:



```shell
pip3 install --upgrade trezor
```



Sluit je Trezor via USB aan op de computer en ontgrendel hem met je pincode.



![Image](assets/fr/01.webp)



Voer het volgende commando uit om de lijst met FIDO2-identifiers op te vragen die op de Trezor is opgeslagen:



```shell
trezorctl fido credentials list
```



Bevestig de export op je Trezor.



![Image](assets/fr/19.webp)



Uw FIDO2-inloggegevens worden weergegeven op uw terminal. Voor mijn Bitwarden-account kreeg ik bijvoorbeeld deze informatie:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Kopieer en bewaar al deze informatie in een tekstbestand. Er is geen significant risico verbonden aan deze back-up, behalve dat het onthult dat je deze diensten met FIDO2 gebruikt. De "*Credential ID*" is versleuteld met behulp van de seed van je Wallet, wat betekent dat een aanvaller die deze back-up bemachtigt geen verbinding kan maken met je accounts, maar alleen kan zien dat je deze accounts gebruikt. Om deze ID's te ontcijferen, heb je de seed in je Wallet nodig.



Je kunt dus meerdere kopieën van dit tekstbestand maken en deze op verschillende plaatsen opslaan, bijvoorbeeld lokaal op je computer, op een bestandshostingdienst en op externe media zoals een USB-stick. Houd er wel rekening mee dat deze back-up niet automatisch wordt bijgewerkt, dus je moet hem elke keer vernieuwen als je een nieuwe "*wachtwoordloze*" verbinding met je Trezor opzet.



Stel dat je Trezor kapot is. Om je FIDO2-gegevens terug te krijgen, moet je eerst je Wallet herstellen met je Mnemonic-zin op een nieuw FIDO2-compatibel Trezor-apparaat.



Zodra het herstel is voltooid, voert u de volgende opdracht uit in uw terminal om uw FIDO2-identifiers op het nieuwe apparaat te importeren:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Vervang gewoon `<CREDENTIAL_ID>` door een van je identifiers. In mijn geval zou dit bijvoorbeeld:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Je Trezor vraagt je om je FIDO2-identificatie te importeren. Bevestig dit door op het scherm te drukken.



![Image](assets/fr/20.webp)



Uw FIDO2-login is nu operationeel op uw Trezor. Herhaal deze procedure voor al uw identifiers.



Gefeliciteerd, je bent nu op de hoogte van het gebruik van je Trezor met U2F en FIDO2! Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om deze tutorial te delen op je sociale netwerken. Hartelijk dank!



Ik raad ook deze andere tutorial aan, waarin we kijken naar een andere oplossing voor U2F- en FIDO2-authenticatie:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e