---
name: SimpleX Chat
description: De eerste mailbox zonder gebruikers-ID
---
![cover](assets/cover.webp)



SimpleX, gelanceerd in 2021, is een gratis instant messaging-applicatie met een radicaal andere benadering van privacy. In tegenstelling tot WhatsApp, Signal en andere gecentraliseerde berichtendiensten, onderscheidt SimpleX zich door zijn gebruikersbeheer: er zijn geen gebruikersidentificatoren, pseudoniemen, nummers of zichtbare publieke sleutels. Deze totale afwezigheid van identifiers maakt het vrijwel onmogelijk om gebruikers te correleren en garandeert een hoog niveau van privacy.



In tegenstelling tot de meeste applicaties die een account of telefoonnummer vereisen, kun je met SimpleX gesprekken starten door een link of een kortstondige QR-code te delen. Elke link creëert een uniek versleuteld kanaal en contactpersonen kunnen de afzender niet vinden of opnieuw contacteren zonder een expliciete Exchange. Berichten worden van begin tot eind versleuteld en passeren relaisservers die ze na verzending verwijderen en noch de verzender, noch de ontvanger, noch hun sleutels zien.



![Image](assets/fr/01.webp)



De netwerkarchitectuur is volledig gedecentraliseerd en niet-gefederaliseerd: servers kennen elkaar niet, ze houden geen globale directory bij en ze hosten geen gebruikersprofielen. Sterker nog, elke gebruiker kan zijn of haar eigen relay server inzetten en gebruiken, terwijl het interoperabel blijft met de servers op het openbare netwerk.



SimpleX is volledig open-source (clients, protocollen en servers), beschikbaar op Android, iOS, Linux, Windows en macOS. De lokale opslag is versleuteld en draagbaar, zodat je een profiel van het ene apparaat naar het andere kunt overzetten zonder afhankelijk te zijn van een gecentraliseerde server.



SimpleX integreert alle klassieke functies van messaging-applicaties. De ergonomie is echter minder vloeiend dan die van WhatsApp of Signal. Het gebruik kan ook beperkter zijn, vooral bij het toevoegen van contacten. Naar mijn mening is het dus een relevant alternatief voor WhatsApp of Signal voor gebruikers die privacy hoog in het vaandel hebben staan en om die reden bereid zijn een paar concessies te doen aan het dagelijkse gebruiksgemak.



| Application          | E2EE 1:1       | E2EE groups    | Anonymous registration | Open-source client license | Open-source server license | Decentralized server | Year of creation  |
| -------------------- | -------------- | -------------- | ---------------------- | -------------------------- | -------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optional) | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Telegram             | 🟡 (optional) | ❌              | 🟡                     | ✅                          | ❌                          | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                      | ✅                          | ✅                          | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                      | ✅                          | ❌                          | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                      | ✅                          | N/A                        | 🟡 (via email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2014              |
| Session              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                      | ✅                          | ❌                          | 🟡(no directory)     | 2019              |
| Keet                 | ✅              | ✅              | ✅                      | ❌                          | N/A                        | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2013              |

*E2EE = End-to-endencryptie*



## Installeer de toepassing SimpleX Chat



SimpleX Chat is beschikbaar op alle platforms. Je kunt de applicatie direct downloaden in de app store van je telefoon:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



Op Android is het ook mogelijk om [te installeren via APK] (https://github.com/simplex-chat/simplex-chat/releases).



In deze tutorial concentreren we ons op de mobiele versie, maar [desktopversies zijn ook beschikbaar](https://simplex.chat/downloads/) (MacOS, Linux en Windows). Het is mogelijk om de desktopversie te koppelen aan een bestaand mobiel gebruikersprofiel, maar om deze synchronisatie te laten werken, moeten beide apparaten verbonden zijn met hetzelfde lokale netwerk.



![Image](assets/fr/02.webp)



## Maak een account aan op SimpleX Chat



Wanneer je de applicatie voor het eerst start, klik je op de knop "*Maak je profiel*".



![Image](assets/fr/03.webp)



Kies een gebruikersnaam, die je echte naam of een pseudoniem kan zijn, en klik dan op "*Create*".



![Image](assets/fr/04.webp)



Stel vervolgens de frequentie in waarmee de applicatie controleert op nieuwe berichten. Als de batterijduur van je telefoon geen probleem is, selecteer dan "*Instant*" om berichten in realtime te ontvangen. Als je liever je batterij spaart en voorkomt dat de applicatie op de achtergrond draait, selecteer dan "*Als app draait*": je ontvangt dan alleen berichten als de applicatie geopend is. Een mogelijk compromis is om te kiezen voor een periodieke controle om de 10 minuten.



Zodra je je keuze hebt gemaakt, klik je op "*Gebruik chat*".



![Image](assets/fr/05.webp)



Je bent nu verbonden met SimpleX Chat en klaar om te beginnen chatten.



![Image](assets/fr/06.webp)



## SimpleX Chat instellen



Ga eerst naar de instellingen door rechtsonder op je profielfoto te klikken en vervolgens op "*Instellingen*".



![Image](assets/fr/07.webp)



De standaardinstellingen zijn over het algemeen geschikt voor de meeste gebruikers. Ik raad je echter aan om naar het menu "*Database passphrase & exporteren*" te gaan. Hier kun je je SimpleX account database exporteren voor back-up doeleinden.



Je kunt ook de passphrase wijzigen die gebruikt wordt om deze database te versleutelen. Standaard wordt deze willekeurig gegenereerd en lokaal opgeslagen op je apparaat. Als je wilt, kun je je eigen passphrase definiëren en de lokale passphrase back-up verwijderen: je moet het dan handmatig invoeren elke keer dat je de applicatie opent, en ook wanneer je migreert naar een ander apparaat.



**Let op**: als je deze optie kiest, zal het verlies van de passphrase resulteren in het permanente verlies van al je SimpleX profielen en berichten.



![Image](assets/fr/08.webp)



Ik raad je ook aan om naar het menu "*Privacy & security*" te gaan, waar je de optie "*SimpleX Lock*" kunt activeren. Dit beschermt de toegang tot de applicatie met een slotcode.



![Image](assets/fr/09.webp)



Tenslotte kun je met de menu's "*meldingen*" en "*uiterlijk*" SimpleX Chat aanpassen aan jouw voorkeuren.



![Image](assets/fr/10.webp)



## Stuur berichten met SimpleX Chat



Om verbinding te maken met een andere persoon op SimpleX, heb je twee opties:




- Gebruik een link voor eenmalig gebruik;
- Gebruik een herbruikbare statische Address.



Met een statische Address kan iedereen die het kent contact met je opnemen op SimpleX. Het is een persistente Address, die meerdere keren gebruikt kan worden, door verschillende mensen, zonder tijdslimiet. Het is deze persistentie die het kwetsbaarder maakt voor spam. Echter, in tegenstelling tot andere berichtenapplicaties, is het verwijderen van je SimpleX Address voldoende om alle spam te stoppen, zonder bestaande gesprekken te beïnvloeden. In feite wordt deze Address alleen gebruikt om de initiële verbinding tot stand te brengen, en is niet langer nodig zodra de Exchange is begonnen.



Eenmalige koppelingen kunnen daarentegen maar één keer worden gebruikt, door een willekeurige gebruiker. Zodra een contact hem gebruikt, wordt de link ongeldig. Je moet generate een nieuwe geven voor elke nieuwe verbinding.



### Met statische Address



Als je de Address wilt gebruiken, klik dan op je profielfoto linksonder in de Interface en selecteer "*SimpelX Address* aanmaken". Klik dan nogmaals op "*Create SimpleX Address*".



![Image](assets/fr/11.webp)



Je herbruikbare Address is nu aangemaakt. Je kunt het delen met mensen die contact met je willen opnemen, door ze de QR-code te laten zien of door ze de link te sturen.



![Image](assets/fr/12.webp)



Klik op de knop "*Address instellingen*". Hier kun je de machtigingen configureren die bij je Address horen. De optie "*Delen met contacten*" maakt je Address zichtbaar op je SimpleX profiel. Je contacten kunnen het dan raadplegen en doorsturen naar andere mensen die contact met je willen opnemen.



De optie "*Auto-accept*" accepteert automatisch inkomende verbindingen via je Address. Dit betekent dat iedereen met jouw Address jouw profiel kan zien en je een bericht kan sturen, tenzij je de optie "*Accepteer incognito*" activeert. Dit verbergt je naam en profielfoto wanneer een nieuwe verbinding wordt gemaakt, en vervangt deze door een willekeurig pseudoniem, verschillend voor elke gesprekspartner.



![Image](assets/fr/13.webp)



### Met herbruikbare schakel



De tweede manier om verbinding te maken met een persoon is door een eenmalige link aan te maken. Om dit te doen, klik je op het potloodpictogram in de rechterbenedenhoek van Interface en selecteer je "*Eenmalige link maken*".



Als je contactpersoon je een link heeft gestuurd, klik dan op "*link scannen / plakken*" om deze te scannen of te plakken.



![Image](assets/fr/14.webp)



SimpleX genereert dan een link voor eenmalig gebruik. Je kunt deze op elke manier doorsturen naar je contact: fysiek Exchange, andere berichten, etc.



![Image](assets/fr/15.webp)



Je kunt ook kiezen welk profiel je wilt koppelen aan deze uitnodigingslink. Klik hiervoor op je profiel net onder de QR-code. Je zult dan in staat zijn om:




- selecteer een van je bestaande profielen (we zullen zien hoe je meerdere profielen kunt maken in de volgende sectie);
- of kies de "*Incognito*" modus, die je naam en profielfoto verbergt met een willekeurig gegenereerd pseudoniem voor je correspondent.



Hier kies ik voor de "*Incognito*" modus.



![Image](assets/fr/16.webp)



Mijn contact heeft de link gebruikt. Van zijn kant heeft hij de "*Incognito*" modus niet geactiveerd, daarom zie ik zijn profielnaam, "*Bob*". Aan de andere kant ziet Bob niet mijn echte naam "*Loïc Morel*", maar een willekeurig pseudoniem, in dit geval "*RealSynergy*".



![Image](assets/fr/17.webp)



Ik zou meteen kunnen beginnen met chatten, maar eerst wil ik controleren of ik met Bob praat en niet met een kwaadwillende die de link misschien heeft onderschept of een MITM-aanval heeft uitgevoerd.



Om dit te doen, gaan we onze beveiligingskoppeling **buiten de applicatie** controleren. Dit is belangrijk, want in het geval van een MITM-aanval zou de interne verificatie in gevaar komen. Gebruik dus een ander beveiligd berichtensysteem, of nog beter, controleer de codes persoonlijk.



Klik in de chat op de foto van Bob en vervolgens op "*Verifieer beveiligingscode*". Bob moet hetzelfde doen aan zijn kant.



![Image](assets/fr/18.webp)



Als je op afstand werkt, vergelijk dan de codes op een ander beveiligd berichtensysteem (ze moeten identiek zijn). Of nog beter, als je elkaar persoonlijk kunt ontmoeten, scan dan de QR-code van je contact door op "*Scan code*" te klikken.



![Image](assets/fr/19.webp)



Als de verificatie succesvol is, verschijnt er een schildpictogram met een vinkje naast de naam van je contactpersoon. Dit is uw verzekering dat u met Bob uitwisselt. Als de verificatie niet succesvol is, verschijnt er een waarschuwing "*Incorrect security code!*".



![Image](assets/fr/20.webp)



U kunt nu Exchange berichten, gesprekken en bestanden vrij laten met Bob, afhankelijk van de machtigingen die u voor deze conversatie hebt ingesteld.



## Pas je SimpleX Chat-profielen aan



Een van de krachtigste functies van SimpleX is de mogelijkheid om verschillende volledig gescheiden gebruikersprofielen te beheren, die allemaal toegankelijk zijn vanuit hetzelfde lokale account. Dit stelt je in staat om je verschillende identiteiten netjes te scheiden, zonder het beheer van berichten ingewikkelder te maken.



U kunt bijvoorbeeld:




- Een profiel met je echte naam en een echte foto voor je professionele uitwisselingen;
- Een profiel met je echte naam en een grappige foto voor je familie-uitwisselingen;
- Een profiel met een valse foto en een pseudoniem voor je persoonlijke gesprekken;
- Nog een pseudoniem profiel om met vreemden te chatten.



Dat is wat we hier gaan doen. Ik begin met het configureren van mijn hoofdprofiel, het profiel dat gekoppeld is aan mijn echte identiteit. Om dit te doen klik ik rechtsonder op mijn profielfoto en vervolgens op mijn gebruikersnaam.



![Image](assets/fr/21.webp)



Ik klik dan op mijn profielfoto om deze te wijzigen en een nieuwe toe te voegen.



![Image](assets/fr/22.webp)



Om andere profielen toe te voegen, klik je op het menu "*Uw chatprofielen*".



![Image](assets/fr/23.webp)



Hier zie je al je profielen. Klik op "*Profiel toevoegen*" om een nieuw profiel aan te maken.



![Image](assets/fr/24.webp)



Kies vervolgens de informatie voor je nieuwe profiel: naam, foto, enz. Hier gebruik ik een pseudoniem en een andere afbeelding om mijn echte identiteit te verbergen in bepaalde uitwisselingen.



![Image](assets/fr/25.webp)



Door je vinger op een profiel te houden, kun je het verbergen. Hierdoor wordt het onzichtbaar in de applicatie, samen met alle bijbehorende gesprekken. Je kunt er ook voor kiezen om het te "*Muten*" om geen meldingen meer te ontvangen.



![Image](assets/fr/26.webp)



Zodra je je profielen hebt aangemaakt, kun je ze onafhankelijk beheren. Selecteer op de startpagina gewoon het actieve profiel dat je wilt weergeven.



![Image](assets/fr/27.webp)



Wanneer je een uitnodigingslink of statische Address maakt, kun je nu kiezen welk profiel je eraan wilt koppelen. Als ik bijvoorbeeld het profiel "*Satoshi Nakamoto*" selecteer om generate een link te sturen naar Alice, zal ze alleen mijn pseudonieme identiteit "*Satoshi Nakamoto*" zien, zonder ooit mijn echte identiteit "*Loïc Morel*" te kennen. Omgekeerd, als ik haar een link geef van mijn echte profiel, zal ze geen mogelijkheid hebben om te linken naar mijn pseudoniem profiel.



![Image](assets/fr/28.webp)



Gefeliciteerd, je bent nu op de hoogte van SimpleX messaging, een uitstekend alternatief voor WathsApp!



Ik raad ook deze andere tutorial aan, waarin ik Threema presenteer, een ander interessant alternatief voor je berichtenapplicatie:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74