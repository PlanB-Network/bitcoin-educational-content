---
name: Threema
description: Veilige, anonieme instant messaging
---
![cover](assets/cover.webp)



Threema werd in 2012 opgericht in Zwitserland en is een instant messaging-app die is ontworpen om privacy en veiligheid te garanderen. In tegenstelling tot WhatsApp, Telegram of Signal heeft Threema geen telefoonnummer of e-mail Address nodig om een account aan te maken. Elke gebruiker heeft een unieke identificatiecode, waardoor een volledig anonieme registratie mogelijk is.



Technisch gezien is de communicatie via Threema end-to-end versleuteld. De code van de mobiele applicatie is sinds 2020 open source, maar de serverinfrastructuur blijft propriëtair en gecentraliseerd. Servers worden uitsluitend gehost in Zwitserland (een land dat bekend staat om zijn wettelijk kader voor gegevensbescherming).



![Image](assets/fr/01.webp)



Threema heeft basisclients voor Android en iOS. Er is ook een webapplicatie en software beschikbaar voor Windows, Linux en macOS. Om deze te gebruiken, moet je je echter eerst registreren op een mobiel apparaat.



De Threema-applicatie is niet gratis. Het werkt op basis van een eenmalig aankoopmodel: €5,99 om de app levenslang te gebruiken (of €4,99 als je hem rechtstreeks koopt). Om Threema echt anoniem te kunnen gebruiken, moet de betaling ook anoniem zijn. Daarom kun je op de "*Threema Shop*" een activatiesleutel in bitcoins of contant geld kopen om de Android-versie te activeren. Op iOS daarentegen moet de aankoop via de App Store lopen, vanwege de beperkingen die Apple stelt aan het monetariseren van apps.



Er is ook een speciale zakelijke versie genaamd "*Threema Work*". In deze tutorial concentreren we ons op de thuisversie.



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



## Installeer de Threema-toepassing



Threema is beschikbaar op alle platforms. Je kunt de applicatie rechtstreeks downloaden in de app store van je telefoon:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



Op Android is het ook mogelijk om [te installeren via APK] (https://shop.threema.ch/en/download).



Er zijn ook [computerversies](https://threema.ch/download) (MacOS, Linux en Windows). Deze tutorial laat zien hoe je ze synchroniseert.



## Licentie Threema kopen



Zodra je de applicatie hebt geïnstalleerd, als je rechtstreeks via een app store bent gegaan, heb je al betaald voor de licentie en zou je er direct toegang tot moeten hebben. Als je via F-Droid of de APK bent gegaan, moet je nu een licentie kopen op de officiële website.



[Ga naar de "*Threema Shop*"(https://shop.threema.ch/) en klik op de knop "*Koop Threema voor Android*".



![Image](assets/fr/02.webp)



Selecteer het aantal licenties dat je wilt kopen (slechts één als het alleen voor jou is), kies de valuta en selecteer de leveringsmethode voor de licentie. Je kunt ervoor kiezen om de licentie per e-mail te ontvangen, of direct op de site als je anoniem wilt blijven. Klik dan op "*Betaalwijze*".



![Image](assets/fr/03.webp)



Kies je betaalmethode. In mijn geval ga ik betalen in bitcoins, wat ik je ook aanraad, omdat je hiermee anoniem kunt blijven (mits je Bitcoin op de juiste manier gebruikt) en het veel handiger is dan een contante betaling op afstand. Klik dan op "*Volgende*".



![Image](assets/fr/04.webp)



Als je geen Invoice nodig hebt, klik dan weer op "*Next*" zonder persoonlijke informatie in te voeren.



Bevestig vervolgens je aankoop door op "*Betaling bevestigen*" te klikken.



![Image](assets/fr/05.webp)



Je moet dan het aangegeven bedrag naar de Bitcoin Address sturen (helaas wordt Lightning nog niet ondersteund). Zodra de transactie is bevestigd op de Blockchain, klik je op "*Sluiten*" naast de Invoice.



Je krijgt dan toegang tot je licentiesleutel. Let op: als je geen e-mail Address hebt ingevuld, wordt deze sleutel alleen hier weergegeven. Vergeet niet om de URL van de pagina op te slaan, zodat je er later toegang toe kunt krijgen als dat nodig is.



![Image](assets/fr/06.webp)



## Maak een account aan op Threema



Nu je je licentiesleutel hebt, kun je de applicatie eindelijk starten. Als je Threema niet via een applicatiewinkel hebt gekocht, wordt je bij de eerste keer opstarten gevraagd om je licentiesleutel in te voeren die je op de site hebt gekocht.



![Image](assets/fr/07.webp)



Klik vervolgens op de knop "*Nu instellen*".



![Image](assets/fr/08.webp)



Beweeg je vinger over het scherm om generate een bron van entropie te maken, die nodig is om je "*Threema ID*" te creëren.



![Image](assets/fr/09.webp)



Je "*Threema ID*" wordt dan weergegeven. Hiermee kunt u contact opnemen met andere gebruikers. Klik op "*Volgende*".



![Image](assets/fr/10.webp)



Kies een wachtwoord. Hiermee kun je de toegang tot je account herstellen als dat nodig is. Maak je wachtwoord zo lang en willekeurig mogelijk en bewaar een veilige kopie ervan, bijvoorbeeld in een wachtwoordmanager.



![Image](assets/fr/11.webp)



Kies vervolgens een gebruikersnaam, die je echte naam of een pseudoniem kan zijn.



![Image](assets/fr/12.webp)



Je kunt dan je Threema ID koppelen aan je telefoonnummer. Dit maakt het makkelijker om in je contacten te zoeken, maar als je Threema gebruikt, is het ook om je anonimiteit te bewaren: je kunt het dus beter niet koppelen. Klik op "*Volgende*".



![Image](assets/fr/13.webp)



Zodra je deze stap hebt voltooid, klik je op "*Finish*".



![Image](assets/fr/14.webp)



Je bent nu verbonden met Threema en kunt beginnen met communiceren.



![Image](assets/fr/15.webp)



## Threema instellen



Ga eerst naar de instellingen door op de drie kleine puntjes in de rechterbovenhoek te klikken en vervolgens "*Instellingen*" te selecteren.



![Image](assets/fr/16.webp)



In het tabblad "*Privacy*" vind je verschillende opties om aan te passen aan je behoeften:




- De contacten op uw telefoon synchroniseren ;
- Berichten accepteren van onbekende mensen;
- Indicator schrijven tijdens gegevensinvoer ;
- Bericht van ontvangst van berichten...



![Image](assets/fr/17.webp)



In het tabblad "*Security*" raad ik aan om de optie "*Locking mechanism*" te activeren om de toegang tot de applicatie te beveiligen. Het is ook aan te raden om passphrase te activeren om je lokale back-ups te beveiligen.



![Image](assets/fr/18.webp)



Voel je vrij om de andere secties van de instellingen te verkennen om de applicatie aan te passen aan jouw voorkeuren.



![Image](assets/fr/19.webp)



## Een back-up maken van je Threema-account



Voordat je begint met het uitwisselen van berichten, is het belangrijk om een manier te plannen om je account te herstellen, vooral als je telefoon is verwisseld of verloren. Klik hiervoor op de drie puntjes rechtsboven in de Interface en ga naar het menu "*Back-ups*".



![Image](assets/fr/20.webp)



Hier vindt u twee opties voor het maken van back-ups van uw gegevens:




- "*Threema Safe*";
- "*Data Backup*".



"Threema Safe* bewaart al je accountgegevens, behalve je gesprekken, op de servers van Threema. Deze gegevens worden versleuteld met het wachtwoord dat je hebt gekozen toen je je account aanmaakte, zodat Threema er geen toegang toe heeft. Back-ups worden automatisch en regelmatig gemaakt.



Met "*Threema Safe*" hoef je alleen maar je "*Threema ID*" en je wachtwoord in te voeren om je account op een nieuw apparaat te herstellen. Als een van deze twee gegevens ontbreekt, is het onmogelijk om je account te herstellen.



Met deze optie kun je alleen je ID, profiel, contactpersonen, groepen en bepaalde instellingen ophalen, maar **niet je gespreksgeschiedenis**.



Om "*Threema Safe*" te activeren, vink je gewoon de optie aan in het menu "*Backups*".



![Image](assets/fr/21.webp)



Als je ook een back-up wilt maken van je gespreksgeschiedenis en deze wilt herstellen, moet je de optie "*Data Backup*" gebruiken. Dit genereert een volledige back-up van je account, lokaal opgeslagen op je telefoon. Je moet deze back-up overzetten naar je nieuwe toestel en je wachtwoord (en mogelijk je passphrase) gebruiken om je volledige account te herstellen.



Omdat deze back-up alleen lokaal is, moet hij regelmatig naar externe media worden gekopieerd. Anders is herstel onmogelijk als je apparaat verloren raakt. Deze methode is daarom het meest geschikt voor een geplande overdracht van het ene apparaat naar het andere, in plaats van voor noodsituaties.



Let op: "*Data Backup*" werkt alleen als je hetzelfde besturingssysteem gebruikt. Je kunt het bijvoorbeeld niet gebruiken om van een Samsung naar een iPhone te migreren.



## Je Threema-profiel aanpassen



Klik linksboven in Interface op je profielfoto en selecteer dan "*Mijn profiel*".



![Image](assets/fr/22.webp)



Hier kunt u uw profiel aanpassen: een foto toevoegen, kiezen wie het kan zien of uw Threema-login bekijken.



![Image](assets/fr/23.webp)



## PC-software synchroniseren



Als je toegang wilt tot je gesprekken op je pc, kun je je Threema-account synchroniseren met de speciale software. Download de software voor jouw besturingssysteem [van de officiële website] (https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Klik op je telefoon op de drie puntjes rechtsboven en open het menu "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Klik op "*Apparaat toevoegen*" en scan vervolgens met uw telefoon de QR-code die door de software op uw computer wordt weergegeven.



![Image](assets/fr/26.webp)



Om de synchronisatie te bevestigen, klikt u op de emojigroep die in de software wordt weergegeven.



![Image](assets/fr/27.webp)



Log op je computer in met je wachtwoord.



![Image](assets/fr/28.webp)



Naast de mobiele applicatie heb je nu ook rechtstreeks vanaf je computer toegang tot je Threema-account.



![Image](assets/fr/29.webp)



## Berichten versturen met Threema



Nu alles correct is ingesteld, kun je beginnen met communiceren. Klik op de knop "*Start chat*".



![Image](assets/fr/30.webp)



Selecteer "*Nieuw contact*".



![Image](assets/fr/31.webp)



Voer het "*Threema ID*" van je correspondent in of scan het.



![Image](assets/fr/32.webp)



Klik op het berichtpictogram.



![Image](assets/fr/33.webp)



Stuur een eerste bericht naar je correspondent.



![Image](assets/fr/34.webp)



Wanneer je correspondent antwoordt, wordt de verbinding tot stand gebracht en kun je zijn of haar naam en profielfoto zien. Vervolgens kun je Exchange berichten en multimediabestanden versturen en zelfs bellen.



![Image](assets/fr/35.webp)



Gefeliciteerd, je bent nu op de hoogte van het gebruik van Threema messaging, een geweldig alternatief voor WathsApp! Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om deze tutorial te delen op je sociale netwerken. Hartelijk dank!



Ik raad ook deze andere tutorial aan, waarin ik je kennis laat maken met Proton Mail, een veel privacy-vriendelijker alternatief voor Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2