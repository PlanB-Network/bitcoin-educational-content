---
name: Heritage
description: Een Bitcoin portfolio met geïntegreerd overervingsmechanisme via Taproot scripts
---

![cover](assets/cover.webp)



Het doorgeven van bitcoins in geval van overlijden of onbekwaamheid vormt een grote uitdaging voor elke houder van crypto-activa. Zonder een geschikt successieplan worden deze bezittingen oninbaar voor je nabestaanden.



Heritage biedt een elegant antwoord door een dodemanswisselmechanisme rechtstreeks op de Bitcoin blockchain te implementeren. Met deze open-source wallet kunnen on-chain opvolgingsvoorwaarden worden geconfigureerd: als de eigenaar gedurende een bepaalde periode geen transacties meer uitvoert, kunnen vooraf aangewezen alternatieve sleutels de fondsen vrijgeven.



## Wat is erfgoed?



Heritage is een Bitcoin portfolio die van nature een overervingsmechanisme integreert via Taproot scripts. Deze open-source software is ontwikkeld onder MIT-licentie door Jérémie Rodon en garandeert transparantie en duurzaamheid.



Heritage gebruikt Taproot scripts gecodeerd in Bitcoin adressen. Elke UTXO integreert twee soorten bestedingsvoorwaarden:





- Primair pad** : De eigenaar kan zijn bitcoins op elk moment uitgeven met zijn primaire sleutel
- Alternatieve paden**: Voor elke aangewezen erfgenaam combineert een script zijn openbare sleutel met een tijdslot



Elke eigenaarstransactie stelt automatisch de activeringsdatum van de erfclausules uit. Bij langdurige inactiviteit (overlijden, onbekwaamheid) worden de voorwaarden automatisch geactiveerd.



## Erfgoedservice (optioneel)



Heritage biedt twee gebruiksopties:



**Doe het zelf (gratis)**: Alleen de open-source toepassing. Je beheert alles autonoom met je eigen node. Deze optie biedt ingebouwde back-uptoegang, ingebouwde overerving en exclusieve controle over je bitcoins. Je moet echter je eigen waarschuwingen aanmaken (kalender, herinneringen) zodat je niet vergeet je timelocks te vernieuwen, en er zijn geen automatische meldingen voor je erfgenamen.



**Gebruik de service (0,05% per jaar)** : De btc-heritage.com service voegt functies toe om het beheer te vereenvoudigen:




- Automatische herinneringen voordat je deadlines verlopen
- Automatische meldingen aan erfgenamen om hen door het herstelproces te leiden
- Prioriteit ondersteuning
- Vereenvoudigd descriptorbeheer



Vergoeding: 0,05% van het beheerde bedrag per jaar, minimaal 0,5 mBTC/jaar. Eerste jaar gratis.



De service blijft onaantastbaar: uw privésleutels verlaten nooit uw apparaat. Heritage heeft geen toegang tot uw fondsen.



## Erfgoed CLI



Voor gevorderde gebruikers die de voorkeur geven aan de terminal, biedt Heritage een opdrachtregeltool (CLI) voor granulaire besturing en bediening van luchtgedempte machines.



![Page Heritage CLI](assets/fr/03.webp)



De volledige CLI documentatie is beschikbaar op [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Hier vindt u instructies voor het downloaden, verbinden met de dienst, aanmaken van wallets (met Ledger of lokale sleutels), beheren van erfgenamen en transacties.



Deze tutorial richt zich op de desktopapplicatie, die toegankelijker is voor de meeste gebruikers.



## Erfgoed Desktop



Heritage Desktop is een grafische toepassing met een intuïtieve interface die de gebruiker door elke stap van het configuratieproces leidt.



### Downloaden



Ga naar [btc-heritage.com](https://btc-heritage.com) en klik op "Download applicatie".



![Page d'accueil Heritage](assets/fr/01.webp)



Kies de versie die overeenkomt met je besturingssysteem (Linux 64bits of Windows 64bits). De binaire bestanden zijn niet digitaal ondertekend, wat veiligheidswaarschuwingen kan veroorzaken.



![Page de téléchargement](assets/fr/02.webp)



### Installatie op Linux



Op Linux wordt de applicatie gedistribueerd in AppImage formaat. Voordat je het kunt draaien, moet je de `libfuse2` afhankelijkheid installeren:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Maak het bestand vervolgens uitvoerbaar en voer het uit:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Eerste lancering



Bij de eerste start biedt de onboarding wizard je drie keuzes:



![Onboarding initial](assets/fr/05.webp)





- Een Wallet met erfgoed instellen**: Maak een nieuwe wallet met erfgoedplan
- Bitcoins erven**: Bitcoins terugkrijgen als erfgenaam
- Zelf verkennen**: Zonder hulp functies verkennen



Selecteer "Een erfgoed Wallet instellen" om uw eerste wallet te maken.



### Bitcoin netwerkverbinding



Kies hoe je verbinding wilt maken met het Bitcoin netwerk:



![Choix connexion](assets/fr/06.webp)





- Gebruik de nalatenschapsdienst**: Beheerde infrastructuur, eenvoudiger voor erfgenamen
- Mijn eigen knooppunt gebruiken**: Maak verbinding met uw eigen Bitcoin Core of Electrum knooppunt



Voor deze tutorial gebruiken we ons eigen knooppunt.



### Beheer van privésleutels



Selecteer hoe u uw privésleutels wilt beheren:



![Gestion des clés](assets/fr/07.webp)





- Met een Ledger hardware-apparaat** : Maximale veiligheid met wallet hardware (aanbevolen)
- Lokale opslag met wachtwoord**: Lokaal opgeslagen sleutels met wachtwoordbeveiliging
- Herstellen van een bestaande wallet** : Herstellen van een bestaande seed



### Node-configuratie



Als je je eigen node gebruikt, leidt de toepassing je door de configuratie. Zorg ervoor dat je Bitcoin of Electrum node :




- Geïnstalleerd en actief
- Gesynchroniseerd met Bitcoin netwerk
- Geconfigureerd om RPC verbindingen te accepteren (voor Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Klik op "My Bitcoin node is up and running" wanneer je node klaar is.



### Statuspaneel



Klik op "Status" in de rechterbovenhoek en vervolgens op "Configuratie openen" om toegang te krijgen tot de verbindingsparameters.



![Panneau Status](assets/fr/09.webp)



Stel de URL van je Electrum server in (bijvoorbeeld `umbrel.local:50001` als je Umbrel gebruikt).



![Configuration Electrum](assets/fr/10.webp)



### Creatie van wallet



Zodra de verbinding tot stand is gebracht, klikt u op "Wallet aanmaken" in het tabblad WALLETS.



![Créer wallet](assets/fr/11.webp)



Een pop-up geeft uitleg over de gesplitste architectuur van Heritage :



![Architecture split](assets/fr/12.webp)



1. **Key Provider (Offline)**: Beheert je privésleutels en ondertekent transacties. Kan een Ledger of een wallet software zijn.


2. **Online Wallet**: Zorgt voor synchronisatie met het Bitcoin netwerk, adresaanmaak en transactie broadcasting.



Vul het aanmaakformulier in:



![Formulaire création wallet](assets/fr/13.webp)





- Wallet naam**: Een unieke naam om je wallet te identificeren
- Sleutelaanbieder**: Kies Lokale Sleutelopslag voor deze tutorial
- Nieuw/herstellen**: Selecteer "Nieuw" om generate een nieuwe seed te maken
- Aantal woorden**: 24 woorden aanbevolen voor maximale veiligheid



Voer een sterk wachtwoord in en kies opties voor Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Lokaal knooppunt**: Gebruikt uw eigen Electrum of Bitcoin Core-knooppunt
- Erfgoeddienst**: Gebruikt de Heritage-service (aanbevolen voor meldingsfuncties)



Klik op "Wallet aanmaken" om het aanmaken te voltooien.



### Interface van wallet



Uw wallet is nu aangemaakt. De interface toont :



![Interface wallet](assets/fr/15.webp)





- Saldo
- Knoppen VERZENDEN en ONTVANGEN
- Transactiegeschiedenis
- Erfgoedconfiguratie geschiedenis
- wallet adressen



### Erfgenamen creëren



Ga naar het tabblad "IERDEN" om je erfgenamen aan te maken.



![Page Heirs](assets/fr/16.webp)



Het informatievenster legt uit:




- Erfgenamen zijn Bitcoin publieke sleutels geassocieerd met individuen
- Elke erfgenaam heeft zijn eigen geheugensteuntje
- De eerste erfgenaam zou een "Back-up" voor jezelf moeten zijn (in geval van verlies van je hoofd wallet)



#### Back-up erfgenaam maken



Klik op "Erfgenaam maken" en geef het de naam "Back-up".



![Création héritier Backup](assets/fr/17.webp)



De popup legt uit waarom een zin van 12 woorden zonder passphrase veilig is voor erfgenamen:


1. **Geen onmiddellijke toegang**: Erfgenamen-sleutels hebben geen toegang tot tegoeden totdat het tijdslot is verstreken


2. **Compromisdetectie**: Als iemand toegang krijgt tot de zin, kunt u de Heritage-configuratie bijwerken


3. **Toegankelijkheid op lange termijn**: Een passphrase kan na vele jaren vergeten worden



De erfgenaam configureren :



![Configuration héritier](assets/fr/18.webp)





- Sleutelaanbieder** : Lokale sleutelopslag
- Nieuw**: Genereer een nieuwe seed
- Aantal woorden**: 12 woorden



De creatie afronden :



![Finalisation héritier](assets/fr/19.webp)





- Erfgenaam Type**: Uitgebreide openbare sleutel
- Exporteren naar service**: Optioneel, maakt automatische kennisgeving aan erfgenamen mogelijk



De back-up erfgenaam is nu aangemaakt:



![Héritier créé](assets/fr/20.webp)



#### De geheugensteun van de erfgenaam opslaan



Klik op de Back-up heir en dan op "Mnemonic weergeven" :



![Afficher mnemonic](assets/fr/21.webp)



**BELANGRIJK: Noteer deze 12 woorden en bewaar ze op een veilige plek. Dit is de sleutel tot het terugkrijgen van de fondsen.



![Phrase mnémotechnique](assets/fr/22.webp)



#### seed verwijderen uit de toepassing



Zodra je de zin hebt opgeschreven, ga je naar de erfparameters (tandwielpictogram):



![Paramètres héritier](assets/fr/23.webp)



Gebruik "Strip Heir Seed" om de privésleutel uit de toepassing te verwijderen. Bevestig dat je de zin hebt opgeslagen.



![Strip Heir Seed](assets/fr/24.webp)



Dit is een veiligheidsmaatregel: alleen de publieke sleutel blijft in de applicatie, voldoende om overerving te configureren.



#### Creatie van een tweede erfgenaam



Herhaal het proces om een tweede erfgenaam te maken (bijvoorbeeld "Satoshi"). Je hebt nu twee erfgenamen:



![Deux héritiers](assets/fr/25.webp)





- Back-up**: Je persoonlijke noodsleutel
- Satoshi**: Een aangewezen erfgenaam



### Erfgoedconfiguratie



Ga terug naar uw wallet en klik op het pictogram Instellingen:



![Paramètres wallet](assets/fr/26.webp)



Klik in de sectie "Erfgoedconfiguratie" op "Aanmaken":



![Heritage Configuration](assets/fr/27.webp)



Stel tijdslimieten in voor elke erfgenaam:



![Configuration délais](assets/fr/28.webp)





- Back-up**: 180 dagen (6 maanden) - Vervaldatum: 2026-06-18
- Satoshi**: 455 dagen (15 maanden) - Vervaldatum: 2027-03-20



**Belangrijk**: Elke erfgenaam moet een langere vertraging hebben dan de vorige. De eerste erfgenaam (Backup) heeft als eerste toegang tot het geld.



Ook configureren :



![Configuration finale](assets/fr/29.webp)





- Referentiedatum**: Startdatum voor het berekenen van doorlooptijden
- Minimum looptijdvertraging**: Minimale vertraging na een transactie (10 dagen aanbevolen)



Klik op "Create" om de configuratie te valideren.



De Heritage-configuratie is nu actief:



![Configuration active](assets/fr/30.webp)



Het toont beide erfgenamen met hun respectievelijke deadlines en vervaldata.



### Descriptors opslaan



**Belangrijk**: Bewaar je wallet beschrijvingen. Zonder deze, zelfs met het geheugensteuntje, is fondsherstel onmogelijk.



Klik op "Backup Descriptors" :



![Bouton Backup](assets/fr/31.webp)



Sla het JSON-bestand op dat je Bitcoin descriptors bevat:



![Backup descripteurs](assets/fr/32.webp)



Dit bestand moet worden doorgegeven aan je erfgenamen, samen met hun respectievelijke geheugensteunzinnen.



### Bitcoins ontvangen



Klik op "RECEIVE" om generate een ontvangstadres te geven:



![Recevoir bitcoins](assets/fr/33.webp)



Gefeliciteerd! Uw Heritage Wallet is klaar om bitcoins te ontvangen. Elk gegenereerd adres bevat automatisch uw Heritage voorwaarden.



Na ontvangst van een transactie wordt je saldo bijgewerkt:



![Solde mis à jour](assets/fr/34.webp)



De geschiedenis geeft de transactie en de bijbehorende Erfgoedconfiguratie weer.



---

## Terugvordering door een erfgenaam



Als de ingestelde tijd verstreken is, kan de erfgenaam het geld terugvorderen.



### Vereisten



De erfgenaam heeft :


1. Zijn 12-woorden geheugensteuntje


2. Het oorspronkelijke wallet descriptor back-upbestand (JSON)



### Een erfgenaam creëren Wallet



Op het tabblad "OVERERFOMEN" herinnert een pop-up je aan deze vereisten:



![Page Heir Wallets](assets/fr/35.webp)



**Let op**: Zonder het descriptorback-upbestand is toegang tot de fondsen ONMOGELIJK, zelfs met de juiste geheugensteunzin.



Klik op "Creëer erfgenaam Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Vul het formulier in:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Erfgenaam Wallet Naam**: Een naam om deze erfgenaam te identificeren wallet
- Sleutelaanbieder** : Lokale sleutelopslag
- Herstellen**: Selecteer deze optie om een bestaande zin in te voeren



Voer de 12 woorden van de mnemonische zin van de erfgenaam in en configureer de Erfgoedprovider:



![Entrée mnemonic](assets/fr/38.webp)





- Erfgoedleverancier**: "Local" om je eigen knooppunt met het back-upbestand te gebruiken



Laad het JSON back-upbestand en klik op "Create Heir Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Erfgenaam Wallet



De Erfgenaam Wallet wordt aangemaakt. Aanvankelijk, als het tijdslot nog niet is verlopen, is er geen overerving beschikbaar:



![Pas d'héritage disponible](assets/fr/40.webp)



Zodra de vertraging is verstreken en de fondsen zijn gesynchroniseerd met het Bitcoin netwerk, verschijnen ze in de lijst met erfenissen:



![Héritage disponible](assets/fr/41.webp)



De interface geeft weer :




- Type sleutel en vingerafdruk
- Totaal geërfde fondsen
- Huidig besteedbaar bedrag (0 zat als tijdslot nog niet is verlopen)
- Vervaldata en vervaldata



Wanneer de vervaldatum is bereikt, zet de knop "Spend" de bitcoins over naar een persoonlijke wallet.



---

## Beste praktijken



### Descriptors opslaan



wallet descriptors zijn essentieel voor het reconstrueren van je Heritage-adressen. **Zonder de descriptoren, zelfs met je geheugensteuntje, kun je je fondsen niet terugvinden.



### Sleutelbeveiliging





- Gebruik indien mogelijk een Ledger voor de hoofdsleutel
- Bewaar de zinnen van erfgenamen nooit op dezelfde plaats als die van jezelf
- Informatie verspreiden via meerdere media en locaties



### Documentatie voor je dierbaren



Schrijf duidelijke instructies waarin elke stap van het herstelproces wordt uitgelegd. Je erfgenamen zijn misschien niet bekend met Bitcoin op het kritieke moment.



## Alternatieven



Er bestaan andere oplossingen om de overdracht van je bitcoins te beheren, waaronder Liana en Bitcoin Keeper. Je vindt onze tutorials hieronder:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Conclusie



Met Heritage kunt u uw Bitcoin opvolging op een soevereine manier plannen via de Desktop-toepassing. Voor de implementatie moet je goed nadenken over de juiste tijdschema's en het veiligstellen van geheimen. Vergeet niet om door te geven aan je erfgenamen:




- Hun 12-woorden geheugensteun
- Het descriptor-back-upbestand
- Herstelinstructies



## Bronnen





- [Officiële website erfgoed](https://btc-heritage.com)
- [Documentatie CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)