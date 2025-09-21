---
name: "Ledger U2F & FIDO2"
description: Verbeter uw online beveiliging met Ledger
---
![cover](assets/cover.webp)



Ledger apparaten zijn hardware wallets die oorspronkelijk ontworpen zijn om een Bitcoin Wallet te beveiligen, maar ze beschikken ook over geavanceerde opties voor sterke verificatie op het web. Dankzij hun compatibiliteit met de **U2F** en **FIDO2** protocollen kun je de toegang tot je online accounts beveiligen door een tweede authenticatiefactor in te stellen.



Het U2F-protocol (Universal 2nd Factor) werd in 2014 geïntroduceerd door Google en Yubico en vervolgens gestandaardiseerd door de FIDO Alliance. Het maakt het mogelijk om een tweede fysieke authenticatiefactor (2FA) toe te voegen bij het inloggen. Eenmaal geactiveerd moeten gebruikers, naast het klassieke wachtwoord, elke poging om verbinding te maken met hun account goedkeuren door op een knop op hun Ledger te drukken. In deze context werkt de Ledger op een vergelijkbare manier als een Yubikey. U2F is in feite een subcomponent van de FIDO2-standaard, die deze standaard omvat en tegelijkertijd belangrijke verbeteringen biedt, waaronder native ondersteuning voor moderne browsers en meer flexibiliteit bij het beheer van verificatiesleutels.



Deze methoden zijn gebaseerd op asymmetrische cryptografie: er worden geen geheime gegevens verzonden, waardoor phishing- of onderscheppingsaanvallen geen effect hebben. U2F en FIDO2 worden nu door veel online diensten ondersteund.



In deze tutorial laten we zien hoe je U2F en FIDO2 kunt activeren voor twee-factor authenticatie met je Ledger.



**Opmerking:** U2F en FIDO2 worden ondersteund op alle Ledger apparaten met recente firmware: vanaf versie 2.1.0 voor de Nano X en Nano S classic, en vanaf versie 1.1.0 voor de Nano S Plus. Stax- en Flex-modellen zijn standaard compatibel.



## Installeer de Ledger Security Key-toepassing



Als je een Ledger apparaat gebruikt, weet je waarschijnlijk dat de firmware alleen niet alle functies bevat die nodig zijn om cryptowallets te beheren. Om bijvoorbeeld een Bitcoin Wallet te gebruiken, moet je de "*Bitcoin*" applicatie installeren. Om MFA-sleutels te beheren, moet je de applicatie "*Security Key*" installeren.



Voordat je begint, moet je ervoor zorgen dat je je Bitcoin Wallet op je Ledger hebt ingesteld. Het is belangrijk dat je je Mnemonic correct opslaat, omdat de sleutels die voor 2FA worden gebruikt, van deze Mnemonic zijn afgeleid. Als je Ledger kwijtraakt of beschadigd raakt, kun je toegang tot je sleutels terugkrijgen door je Mnemonic zinsdeel op een ander Ledger apparaat in te voeren (op dit moment worden FIDO2-identifiers in "*wachtwoordloze*" modus nog niet ondersteund op Ledgers, dus er zijn geen residente identifiers).



Sluit uw Ledger aan op uw computer en ontgrendel hem.



![Image](assets/fr/01.webp)



Om de toepassing te installeren, opent u de [Ledger Live] software (https://www.Ledger.com/Ledger-live) en gaat u naar het tabblad "*Mijn Ledger*". Zoek de applicatie "*Security Key*" en installeer deze op uw apparaat.



![Image](assets/fr/02.webp)



De "*Security Key*" toepassing zou nu moeten verschijnen naast de andere toepassingen die geïnstalleerd zijn op uw Ledger.



![Image](assets/fr/03.webp)



Klik op de toepassing om deze open te laten voor de volgende stappen in de tutorial.



![Image](assets/fr/04.webp)



## U2F/FIDO2 gebruiken voor 2FA met een Ledger



Ga naar het account dat je wilt beveiligen met twee-factor authenticatie. Ik ga bijvoorbeeld een Bitwarden-account gebruiken. Je vindt de 2FA-optie meestal in de service-instellingen, onder de tabbladen "*authentication*", "*security*", "*login*" of "*password*".



![Image](assets/fr/05.webp)



Selecteer in het gedeelte dat gewijd is aan twee-factor authenticatie de optie "*Passkey*" (de term kan variëren afhankelijk van de site die je gebruikt).



![Image](assets/fr/06.webp)



Vaak wordt u gevraagd om uw huidige wachtwoord te bevestigen.



![Image](assets/fr/07.webp)



Geef je beveiligingssleutel een naam voor gemakkelijke herkenning en klik dan op "*Read Key*".



![Image](assets/fr/08.webp)



Uw accountgegevens verschijnen op het Ledger display. Druk op de toets "*Register*" om te bevestigen (of op beide toetsen tegelijk, afhankelijk van het model dat je gebruikt).



![Image](assets/fr/09.webp)



De toegangssleutel is succesvol geregistreerd.



![Image](assets/fr/10.webp)



Registreer deze beveiligingssleutel.



![Image](assets/fr/11.webp)



Vanaf nu wordt je, wanneer je inlogt op je account, naast je gebruikelijke wachtwoord ook gevraagd om je Ledger te verbinden.



![Image](assets/fr/12.webp)



Je kunt dan op de knop "*Log in*" op je Ledger display drukken om de verificatie te bevestigen (of op beide knoppen tegelijk, afhankelijk van het model dat je gebruikt).



![Image](assets/fr/13.webp)



Het voordeel van het gebruik van een Hardware Wallet Ledger voor twee-factor authenticatie is dat je gemakkelijk je sleutels kunt terughalen dankzij de Mnemonic zinsnede. Naast deze basisback-up kun je ook een noodcode gebruiken die wordt geleverd door elke dienst waarbij je 2FA hebt geactiveerd. Met deze noodcode kun je verbinding maken met je account als je je beveiligingssleutel verliest. Het vervangt dus de 2FA voor een verbinding indien nodig.



Op Bitwarden kunt u bijvoorbeeld toegang krijgen tot deze code door te klikken op "*Bekijk herstelcode*".



![Image](assets/fr/14.webp)



Ik raad je aan om deze code op een andere plaats te bewaren dan waar je je hoofdwachtwoord bewaart, om te voorkomen dat ze samen gestolen worden. Als je wachtwoord bijvoorbeeld is opgeslagen in een wachtwoordmanager, bewaar dan je 2FA-noodcode apart op papier.



Deze aanpak biedt u twee niveaus van back-up in het geval van verlies van uw Ledger voor 2FA authenticatie: een eerste back-up met behulp van de Mnemonic zin voor al uw accounts, en een tweede account-specifieke back-up met behulp van de noodcodes. Het is echter belangrijk **de rol van de Mnemonic niet te verwarren met die van de noodcode**:




- De 12- of 24-woord Mnemonic zin geeft je niet alleen toegang tot de sleutels die gebruikt worden voor 2FA op al je accounts, maar ook tot je bitcoins die beveiligd zijn met je Ledger ;
- Met de noodcode kunt u de 2FA-aanvraag tijdelijk alleen omzeilen op het betreffende account (in dit voorbeeld alleen op Bitwarden).



Gefeliciteerd, je bent nu op de hoogte van het gebruik van je Ledger voor MFA! Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om deze tutorial te delen op je sociale netwerken. Hartelijk dank!



Ik raad ook deze andere tutorial aan, waarin we kijken naar een andere oplossing voor U2F- en FIDO2-authenticatie:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e