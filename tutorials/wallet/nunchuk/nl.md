---
name: Nunchuk
description: Wallet mobiel geschikt voor alle
---
![cover](assets/cover.webp)



## Een krachtige Wallet


Nunchuk kwam eind 2020 met een duidelijke filosofie: multi-handtekening tot standaard maken. Het is daarom ontworpen om zeer geavanceerde functies uit te voeren, met de waardevolle keuze om het ontwerp direct op Bitcoin core te bouwen, de referentiesoftware voor het Bitcoin ecosysteem.



Na meer dan 4 jaar van ontwikkeling en gebruik, is het klaar om op schaal uitgeprobeerd te worden. Als je een beginner bent en onbekend met Nunchuk, zal deze gids je helpen om je eerste stappen te zetten en deze software te ontdekken, waarvan je de geavanceerde functies zult kunnen leren nadat je voorbij de eerste schok bent. De tutorial zelf is gewijd aan gemiddelde gebruikers die de nodige vaardigheden bezitten om alle stappen te volgen, maar het kan een inspiratie zijn voor iedereen om uit te vinden hoe je je vaardigheden kunt vergroten. We beginnen met de mobiele versie, en dit is nodig omdat Nunchuk de software ook op computers heeft draaien.



## Downloaden


De eerste stap is beslissen waar je de app kunt downloaden. Ga naar de [officiële site](https://nunchuk.io/) waar je wat documentatie kunt vinden (niet veel, maar het is een begin), de presentatie van de functies en, aan het einde van de pagina, alle downloadlinks.



📌 Voor deze tutorial heb ik besloten om je te laten zien hoe je Software Wallet kunt downloaden van de Github repository en hoe je de release kunt verifiëren voordat je het installeert op je mobiele telefoon. **De volgende procedure kan alleen worden uitgevoerd vanaf je computer**, dus ik raad je aan al deze stappen uit te voeren vanaf je desktop of laptop en - na alle controles - het `.apk` bestand over te zetten naar je mobiele telefoon.



![image](assets/en/01.webp)



Als je vaardigheden niet erg geavanceerd zijn, kun je besluiten om de `.apk` van de officiële winkels te downloaden en direct door te gaan naar het configuratiegedeelte van deze tutorial. Als je daarentegen de sprong wilt wagen, blijf dan stap voor stap volgen.



Dus klik vanaf je desktopcomputer op _Bekijk onze open source opslagplaats_



De link brengt je naar Nunchuk's Github pagina, waar je een aantal repo's kunt vinden. We zullen ons richten op de _nunchuk-android_ repository



![image](assets/en/02.webp)



Ga in het volgende scherm naar rechts naar het gedeelte _Releases_ en kies _Latest_



![image](assets/en/03.webp)



Download onder _Assets_ de release (in dit voorbeeld 1.67.apk), samen met het SHA256SUMS-bestand en SHA256SUMS.asc.



![image](assets/en/04.webp)



Om de GPG-sleutel van de ontwikkelaar te vinden, ga terug naar de _Releases_ sectie van het archief en zoek naar 1.9.53 (of eerder) die de link bevat om de _GPG-sleutel_ te verkrijgen en te downloaden



![image](assets/en/05.webp)



We gaan verder met de verificatie via een handige tool van Sparrow wallet, die hiervoor een speciaal venster heeft en PGP-handtekeningen en SHA256-manifesten ondersteunt.



Start dan Sparrow en kies in het menu _Tools_ de optie _Verify Download_.



![image](assets/en/06.webp)



In het venster dat verschijnt, vind je velden om "in te vullen": kies de knop _Browse_ aan de rechterkant en selecteer voor elk veld de corresponderende bestanden die je zojuist van Github hebt gedownload. Als je alle stappen hebt doorlopen, ziet het venster er als volgt uit, met Green vinkjes en Hash bevestiging van het manifest.



![image](assets/en/07.webp)


**N.B.** de schermafbeelding is van een Windows PC, dezelfde praktijk kan gebruikt worden voor elk besturingssysteem op je computer, je hoeft alleen Sparrow wallet geïnstalleerd te hebben. En geverifieerd!



Je kunt de Sparrow wallet gids vinden om deze Software Wallet te downloaden


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Vervolgens kun je het `.apk` bestand van je computer overbrengen naar je telefoon



![image](assets/en/08.webp)



en installeer Nunchuk



![image](assets/en/09.webp)



Voordat je Nunchuk op je telefoon start, open je Orbot en zet je de nieuwkomer in de lijst met apps die onder Tor moeten worden gerouteerd.



![image](assets/en/11.webp)



Start nu Nunchuk. Voor project features, die niet het onderwerp van deze tutorial zijn, zal Nunchuk, eenmaal geopend, je uitnodigen om in te loggen via een email of Google profiel. Totdat je van plan bent om gebruik te maken van de geavanceerde plannen van Nunchuk Inc, **vermijd inloggen** en ga verder door de _Continue as guest_ optie te kiezen.



![image](assets/en/12.webp)



## Instellingen


Nunchuk presenteert zichzelf met een _Home_ venster, waar het makkelijk is om de bedieningsfilosofie te begrijpen en waar we zo op in zullen gaan.



Onderaan vind je de menu's en als eerste stap kies je _Profile_ om toegang te krijgen tot de instellingen.



![image](assets/en/10.webp)



Kies dan _Weergave-instellingen_ en blijf de uitnodiging om een account aan te maken negeren.



![image](assets/en/14.webp)



In het onderstaande scherm kun je controleren of Wallet online is en of je verbinding kunt maken met je server, let goed op de instructies bij de link die wordt aangeboden door op _deze handleiding_ te klikken.



![image](assets/en/15.webp)



Sla de instellingen op met de opdracht _Netwerkinstellingen opslaan_, keer terug naar het menu _Profiel_ en selecteer _Veiligheidsinstellingen_.



![image](assets/en/16.webp)



In dit menu stelt u in hoe het openen van de app moet worden verdedigd. Om ongewenste toegang te voorkomen kunt u de Nunchuk beschermen met de biometrische gegevens van de telefoon en/of een beveiligings-PINcode toevoegen.



![image](assets/en/17.webp)



Kijk ook eens naar het _Over_ menu, dat je altijd vindt in het _Profiel_ venster



![image](assets/en/18.webp)



hiermee kun je de versie van de app controleren of indien nodig contact opnemen met de ontwikkelaars.



![image](assets/en/19.webp)



## Sleutelgeneratie en Wallet


Zoals gemakkelijk te raden is uit de filosofie van Nunchuk, is de software bedoeld als een handig hulpmiddel voor het beheren van multi-handtekening Wallets. Om deze functie uit te voeren, staat Nunchuk de creatie van Wallet toe door ze te scheiden van de sleutels die nodig zijn om digitale handtekeningen te regelen.



In feite houdt de ideale werking van Nunchuk in dat er Wallets worden gemaakt die alleen kunnen worden bekeken, afhankelijk van toetsen die "Colds" kunnen zijn



In de vorige schermen is het je misschien opgevallen dat er een menu onderaan is genaamd _Keys_. Als je Nunchuk net hebt gedownload, zie je in zowel _Home_ als _Keys_ een grote knop die je uitnodigt om een sleutel toe te voegen, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Dit is precies hoe Nunchuk werkt:** eerst generate/import je de sleutels en dan maak je de Wallet aan en configureer je hem om te kiezen welke sleutels de ontgrendeling van het geld dat erop staat toestaan.



Zelfs in het geval van Wallet singlesig, maak je eerst de sleutel en dan pas de Wallet. En dat is precies wat we nu gaan doen, te beginnen met een Wallet singlesig om het ijs te breken en de functies van de Nunchuk te ontdekken.



Klik op _Sleutel toevoegen_



![image](assets/en/22.webp)



Nunchuk toont een aantal ondersteunde handtekeningapparaten, maar om te beginnen kies je _Software_.



![image](assets/en/23.webp)



Nunchuk zal generate een Mnemonic die wordt opgeslagen op het apparaat. Je moet dan de volgorde van de woorden voor de back-up opschrijven, de beste omgevingsomstandigheden creëren en zorgen dat je de tijd hebt om het goed en rustig te doen. De software laat de Mnemonic maar één keer zien, of je er nu voor kiest of later, dus kies _Create and backup now_.



![image](assets/en/24.webp)



Nunchuk genereert Mnemonic zinnen van 24 woorden, die onmiddellijk op het volgende scherm verschijnen



![image](assets/en/25.webp)



en voerde vervolgens een snelle controle uit, waarbij je werd gevraagd het juiste woord te kiezen uit 3 keuzes, dat overeenkomt met het nummer in de Mnemonic reeks.


Als je de Mnemonic correct hebt geschreven, wordt de knop _Continue_ operationeel. Druk erop om verder te gaan.



![image](assets/en/26.webp)



Geef je sleutel een naam en druk op _Continue_.



![image](assets/en/27.webp)



Aan het einde van deze stappen wordt je gevraagd of je een [passphrase](https://planb.academy/en/resources/glossary/passphrase-bip39) aan je Mnemonic zin wilt toevoegen. Als je niet weet hoe je passphrase moet gebruiken, zijn back-up moet regelen, of hoe het werkt, raad ik je aan om _I don't need a passphrase_ te kiezen.



![image](assets/en/28.webp)



De sleutel wordt uiteindelijk aangemaakt en wordt weergegeven in het menu:




- Met _Key Spec_ wordt de hoofdvingerafdruk aangegeven
- Je hebt instellingen, de drie puntjes rechtsboven, waar je de sleutel kunt verwijderen of een bericht kunt ondertekenen
- Naast de naam van de sleutel vind je een puntpictogram waarop je de naam van de sleutel kunt bewerken, bijvoorbeeld om je sleutels in de toekomst op orde te houden.
- Als laatste opdracht kun je de gezondheidsstatus van de sleutel controleren: door op _Run health check_ te drukken kun je de app laten controleren of een sleutel gecompromitteerd is.



Als je klaar bent, klik je op _Verwijder_



![image](assets/en/29.webp)



In het menu _Keys_ zie je je eerste toets verschijnen.



![image](assets/en/30.webp)



Door naar het _Home_ menu te gaan, verschijnt de optie om Wallet aan te maken. Klik op _Creëer nieuwe portemonnee_.



![image](assets/en/31.webp)



Nunchuk laat je een aantal mogelijkheden zien die voor het grootste deel te maken hebben met diensten die het bedrijf aanbiedt en die niet het onderwerp van deze tutorial zijn.



In deze gids zullen we een _Hot Wallet en een _Custom wallet_ maken door de details in detail te beschrijven.


Laten we beginnen met _Custom wallet_.



![image](assets/en/32.webp)



Op een eenvoudige manier vraagt de app je om deze nieuwe Wallet een naam te geven en het script voor de adressen te kiezen. Voor de tutorial koos ik ervoor om de standaard instelling, _Native segwit_, te laten staan. Als je klaar bent, kies je _Continue_



![image](assets/en/33.webp)



De configuratie van de Wallet vraagt je vervolgens in te stellen met welke sleutel de fondsen van deze Wallet ontgrendeld worden. Als er meerdere sleutels zijn, krijg je een lijst te zien waaruit je kunt kiezen. Wij hebben er op dit moment maar één gemaakt, dus die vinken we aan. In de rechter benedenhoek zie je hoe Nunchuk je zal vragen om je toekomstige Wallet met meerdere handtekeningen in te stellen, waardoor het aantal _Verplichte sleutels_ toeneemt.



![image](assets/en/34.webp)



Omdat we een singlesig maken, laten we `1` staan en klikken op _Continue_.



Tot slot verschijnt er een verificatiescherm, waar je de functies van Wallet kunt controleren:




- de naam
- de `1/1 Multisig` tage, zo noemt Nunchuk de Wallet singlesig
- het scripttype, `Native SegWit`
- de `Keys` sleutel, met zijn vingerafdruk en afleidingspad



Als je tevreden bent, druk je op _Create wallet_



![image](assets/en/35.webp)



Wallet is aangemaakt en je kunt het [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) bestand downloaden als back-up. Om terug te keren naar het hoofdmenu klik je op de pijl in de linkerbovenhoek.



![image](assets/en/36.webp)



U bevindt zich in _Home_, waar u de nieuw aangemaakte Wallet ziet met de balans en status van de verbinding. Door in het blauwe vlak te klikken, krijgt u toegang tot de hoofdfuncties van Wallet.



![image](assets/en/37.webp)





- Met het lenspictogram in de rechterbovenhoek kun je een transactie zoeken;
- `View Wallet config` geeft toegang tot het configuratiemenu, waar je de naam van de Wallet kunt wijzigen en geavanceerde opties kunt inschakelen, rechtsboven (waarvan je geen screenshots kunt krijgen). Hier kun je de Wallet configuratie exporteren, labels, toetsen vervangen, de [gap limit] (https://planb.academy/en/resources/glossary/gap-limit) veranderen en meer.



## Transacties met Nunchuk



Onderscheidingen _ontvangen_



![image](assets/en/38.webp)



De app is geprogrammeerd om de QR Code van de Address te tonen of de scriptPubKey te kopiëren/delen om onchain fondsen te ontvangen.



![image](assets/en/39.webp)



Er arriveerde een UTXO op deze eerste Address,



![image](assets/en/40.webp)



maar we klikken nog steeds op _Receive_ om een andere te ontvangen.



![image](assets/en/41.webp)



De bedoeling is dat je erachter komt dat Nunchuk deze nieuwe Address aan je rapporteert als een _Ongebruikt adres_ maar je ook laat zien dat je _Gebruikte adressen_ hebt en het aantal daarvan.



### Bestedingstransactie met Coin besturing



Als deze tweede UTXO ook is aangekomen, ga dan terug naar het Wallet hoofdscherm om de status van de twee inkomende transacties te controleren en, het belangrijkste, klik op de _View coins_ optie



![image](assets/en/42.webp)



waar je individuele UTXO's te zien krijgt. Hier kun je kiezen om er een in het bijzonder te bekijken door op het kleine pijltje naast het bedrag te klikken



![image](assets/en/43.webp)



en controleer wanneer het is aangekomen, de beschrijving, blokkeer UTXO zodat het niet wordt uitgegeven en meer.



![image](assets/en/44.webp)



Maar als je teruggaat naar het menu _Coins_ door op de pijl in de rechterbovenhoek te klikken, kun je "Coin Control" aanzetten om je UTXO's op een meer gecontroleerde manier uit te geven.



In het volgende voorbeeld heb ik UTXO van 21.000 Sats geselecteerd en vervolgens op het symbool linksonder geklikt.



![image](assets/en/45.webp)



Nunchuk opent automatisch het venster _Nieuwe transactie_ om deze UTXO uit te geven. In de bestedingstransactie moet je eerst het bedrag handmatig instellen of door _Alles selecteren verzenden_ te selecteren om al het Coin controlesaldo te verzenden, zonder restbedragen te genereren. Zodra het bedrag is ingesteld, kies je _Continue_



![image](assets/en/46.webp)



Nu laat Nunchuk zien waar de Address moet worden geplakt waarnaar dit geld moet worden overgeboekt, geef een beschrijving en voltooi de transactie.



![image](assets/en/47.webp)



Door _Create transaction_ te kiezen, delegeer je automatisch fee- en transactiebeheer naar de app. Ik raad aan om _Custom transaction_ te kiezen voor meer controle.



In dit nieuwe scherm is het belangrijk om




- trek de vergoeding af van het te verzenden bedrag_, om te voorkomen dat een andere UTXO in Wallet de vergoeding betaalt, deze uitgeeft en een restbedrag genereert (wat een vermijdbaar verlies van privacy is);
- en stel dan de vergoedingen handmatig in na controle op de verkenner.



Klik na al deze stappen op _Continue_



![image](assets/en/48.webp)



Het volgende scherm is de volledige samenvatting van de transactie. Als alles in orde is, bevestig dan door _Confirm and create transaction_ te selecteren.



![image](assets/en/49.webp)



Met _Wachtende handtekeningen_ waarschuwt de Nunchuk u dat de transactiep wacht op uw handtekening om de uitgave goed te keuren, die u aanbrengt door te klikken op _Teken_.



![image](assets/en/50.webp)



Het _Broadcast_ commando verschijnt onderaan om de afgeronde en ondertekende transactie te propageren.



![image](assets/en/51.webp)



### Transactie uitgeven via menu _Versturen_



Terwijl we op de hoofdpagina van Wallet de transactie zien uitgaan en wachten op bevestiging, gebruiken we het _Verstuur_ menu om een dagelijkse uitgave te simuleren.



![image](assets/en/52.webp)



Als je op _Versturen_ klikt, verschijnt het scherm voor het verzenden van de transactie, dat hetzelfde is als zojuist, maar dan zonder Coin controle.



Ook in dit tweede voorbeeld heb ik besloten om _Custom transaction_ te selecteren en het hele bedrag te versturen, maar ik had het ook handmatig kunnen instellen. Zodra je hebt besloten welk bedrag je wilt verzenden, druk je op _Continue_.



![image](assets/en/53.webp)



Maak dan altijd een keuze of de vergoedingen worden afgetrokken van de UTXO in kwestie (in dit voorbeeld is de keuze geforceerd, omdat er maar één is), pas de vergoedingen handmatig aan volgens de situatie op dat moment in Mempool, en druk op _Continue_.



![image](assets/en/54.webp)



Als het overzichtsscherm bevredigend is, kies je _Confirm en maak je transactie aan_.



![image](assets/en/55.webp)



Onderteken de transactie met _Sign_



![image](assets/en/56.webp)



en propageert het naar het netwerk.



![image](assets/en/57.webp)



Wallet staat op dit punt met het saldo op nul en de geschiedenis wordt bijgewerkt.



![image](assets/en/58.webp)



## Creatie van een "Hot Wallet"



Als laatste en om niets weg te laten uit de beginfase van Nunchuk mobile, laten we eens kijken hoe dit iets creëert wat de app "Hot Wallet" noemt



Klik in het _Home_ menu van Nunchuk, waar de lijst met portemonnees verschijnt, op de `+` in de rechterbovenhoek.



![image](assets/en/59.webp)



Kies _Hot wallet_ uit de opties



![image](assets/en/60.webp)



Nunchuk geeft advies over het omgaan met Hot portemonnees op de presentatiepagina, waar je _Continue_ selecteert om verder te gaan.



![image](assets/en/61.webp)



Na enkele ogenblikken is de Wallet aangemaakt en verschijnt in de lijst in een bruinachtige kleur. Dit is de kleur waarmee Nunchuk je waarschuwt dat je nog geen back-up van Wallet hebt gemaakt.



![image](assets/en/62.webp)



Klik op de naam van de Wallet, om toegang te krijgen tot zijn configuraties, en je ziet misschien een uitnodiging om onmiddellijk een back-up te maken van de Mnemonic zin.



![image](assets/en/63.webp)



De procedure is hetzelfde als we eerder hebben gezien, dus we zullen het niet opnieuw doen. Zodra het klaar is, brengt Nunchuk je naar de relevante sleutelpagina, die je kunt bewerken zoals degene die je hebt gemaakt met de _Custom_ procedure.



![image](assets/en/64.webp)



Probeer ook _Run health check_



![image](assets/en/65.webp)



of om te zien hoe je al je Wallets kunt weergeven in de _Home_ van de app.



![image](assets/en/66.webp)



## Om in gedachten te houden om zelfstandig verder te gaan


Net zoals er een volgorde is voor het aanmaken, namelijk eerst de sleutels genereren en dan de Wallet, moet je de omgekeerde volgorde aanhouden voor het verwijderen van deze items uit je app.



Als je één van de sleutels wilt verwijderen, moet je eerst de vooruitziende blik hebben om Wallet of Wallets te verwijderen, die één van de handtekeningensleutels voor transacties gebruiken: eerst verwijder je Wallets en dan pas de sleutels. Als je deze volgorde niet aanhoudt, zul je merken dat je de sleutel niet kunt verwijderen.



Nu je weet hoe je aan de slag gaat met de Nunchuk, kun je deze app verder bestuderen en zijn geheimen ontdekken. In deze tutorial hebben we alleen de eerste stappen genomen, maar er zijn geavanceerdere toepassingen en geavanceerde behoeften waar deze Software Wallet je bij kan helpen.