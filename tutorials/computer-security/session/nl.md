---
name: Session
description: Versleutelde berichten verzenden, geen metagegevens
---
![cover](assets/cover.webp)



Session is een versleutelde berichtentoepassing die in 2020 is ontwikkeld om een hoger niveau van vertrouwelijkheid te bieden dan traditionele berichtentoepassingen. Het werd eerst ontwikkeld door de *Oxen Privacy Tech Foundation*, daarna door de *Session Technology Foundation*.



Session heeft een aantal interessante technische kenmerken: end-to-end versleuteling van berichten, een gedecentraliseerd netwerk dat is georganiseerd om beschikbaarheid en redundantie te garanderen en op Tor geïnspireerde onion routing. In tegenstelling tot WathsApp of Signal, die een telefoonnummer vereisen voor registratie, vraagt Session niet om persoonlijke informatie (geen nummer, geen e-mail, alleen een paar cryptografische sleutels).



Met Session kun je berichten, bestanden, spraakberichten, audiogesprekken en groepen tot 100 leden (en communities daarboven) verzenden, terwijl het lekken van metadata tot een minimum wordt beperkt.



![Image](assets/fr/01.webp)



Session richt zich vooral op gebruikers die vertrouwelijkheid hoog in het vaandel hebben staan. Deze berichtenservice is een serieus alternatief voor WhatsApp, met een architectuur die is ontworpen om moderne bewakingsmodellen te weerstaan.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-endencryptie*



## De toepassing Session installeren



Session is beschikbaar op alle platforms. Je kunt de applicatie rechtstreeks downloaden in de applicatiewinkel van je telefoon:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Op Android is het ook mogelijk om [te installeren via APK] (https://github.com/session-foundation/session-android/releases).



In deze tutorial concentreren we ons op de mobiele versie, maar [computerversies zijn ook beschikbaar](https://getsession.org/download) (MacOS, Linux en Windows). Later zullen we bekijken hoe je een account kunt synchroniseren op meerdere apparaten.



## Maak een account aan op Session



Klik bij de eerste keer opstarten op "*Account aanmaken*".



![Image](assets/fr/02.webp)



Kies een weergavenaam voor je profiel. Dit kan een pseudoniem of je echte naam zijn.



![Image](assets/fr/03.webp)



Je moet dan kiezen tussen twee beheermodi voor meldingen:





- Snelle modus (**Firebase Cloud Messaging/Apple Push Notification Service**): stelt je in staat om bijna in realtime berichtmeldingen te ontvangen, dankzij de notificatiediensten van Google of Apple (afhankelijk van je systeem). Om dit te laten werken, worden je IP Address en een unieke notificatie-ID doorgestuurd naar Google of Apple, en de Session account-ID wordt ook geregistreerd bij een STF-server (via Tor). Deze modus brengt (weliswaar minimale) blootstelling van metadata met zich mee, maar compromitteert de inhoud van berichten of contacten niet en staat niet toe dat je werkelijke activiteit wordt getraceerd. Deze modus is daarom efficiënter in termen van reactiesnelheid, maar is afhankelijk van een gecentraliseerde infrastructuur en is iets minder effectief in termen van vertrouwelijkheid.





- Langzame modus (**background polling**): de Session-toepassing blijft actief op de achtergrond en peilt periodiek het netwerk naar nieuwe berichten. Deze aanpak garandeert een grotere vertrouwelijkheid dan de eerste, omdat er geen gegevens worden verzonden naar servers van derden; noch Google, Apple of STF-servers ontvangen enige informatie. Aan de andere kant heeft deze modus twee nadelen: meldingen kunnen vertraagd zijn (tot enkele minuten) en het energieverbruik is over het algemeen hoger door de activiteit van de applicatie op de achtergrond.



![Image](assets/fr/04.webp)



U bent nu verbonden met de Session-toepassing en kunt berichten beginnen uitwisselen.



![Image](assets/fr/05.webp)



## Uw Session-account opslaan



Het eerste wat je moet doen voordat je Session gaat gebruiken, is je account opslaan zodat je het kunt herstellen als je je apparaat verliest. Klik hiervoor op de knop "*Doorgaan*" naast "*Bewaar je herstelwachtwoord*".



![Image](assets/fr/06.webp)



Session toont dan een Mnemonic zin. Kopieer deze zorgvuldig en bewaar hem op een veilige plaats. Deze zin geeft volledige toegang tot je Session-account, dus het is belangrijk dat je hem niet doorgeeft. Je hebt hem nodig om toegang te krijgen tot je account op een ander apparaat, vooral als je huidige telefoon zoekraakt of wordt vervangen.



![Image](assets/fr/07.webp)



Deze zin werkt op dezelfde manier als de Mnemonic zinnen die gebruikt worden in Bitcoin wallets. Ik raad je daarom aan deze andere tutorial te raadplegen, waarin ik de beste methodes uitleg voor het opslaan van een Mnemonic zin:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Let op**: In tegenstelling tot de Mnemonic zinnen die gebruikt worden op Bitcoin portemonnees, moet je bij Session **elk woord absoluut in zijn geheel opslaan**. De eerste 4 letters zijn niet genoeg!



## De sessietoepassing instellen



Om naar de applicatie-instellingen te gaan, klik je op je profielfoto linksboven op Interface. Hier kun je een profielfoto toevoegen. Hier kun je een profielfoto toevoegen.



![Image](assets/fr/08.webp)



In het menu "*Privacy*" kun je verschillende functies in- of uitschakelen (pas op, sommige kunnen je IP Address blootgeven). Ik raad ook aan om de optie "*Lock App*" te activeren, die authenticatie vereist om toegang te krijgen tot de applicatie.



![Image](assets/fr/09.webp)



In het menu "*Meldingen*" kun je kiezen tussen "*Snelle modus*" en "*Slow modus*" (zie vorige delen van de tutorial). Je kunt meldingen ook aanpassen aan je voorkeuren.



![Image](assets/fr/10.webp)



Ga tenslotte naar het "*Appearance*" menu om Interface aan te passen aan jouw smaak. In het menu "*Recovery Password*" kun je je Mnemonic zin opvragen als je een nieuwe back-up wilt maken.



![Image](assets/fr/11.webp)



## Berichten verzenden met Session



Klik op de knop "*+*" op de startpagina om contact op te nemen met andere mensen.



![Image](assets/fr/12.webp)



Er zijn verschillende opties beschikbaar. Als je een groep wilt maken of erbij wilt horen, selecteer je "*Groep maken*" of "*Gemeenschap joinen*".



![Image](assets/fr/13.webp)



Als je wilt dat iemand jou als contact toevoegt, kun je hem je Session ID als QR-code laten scannen.



![Image](assets/fr/14.webp)



Om uw aanmelding op afstand te verzenden, klikt u op "*Een vriend(in) uitnodigen*". U kunt dan uw sessie-ID kopiëren en verzenden via een ander communicatiekanaal. U kunt deze informatie ook opvragen door op uw profielfoto op de startpagina te klikken.



![Image](assets/fr/15.webp)



Als u de sessie-ID van een andere persoon hebt en deze wilt toevoegen, klikt u op "*Nieuw bericht*".



![Image](assets/fr/16.webp)



Je kunt de identificatiecode in tekst plakken of rechtstreeks scannen als je een QR-code hebt.



![Image](assets/fr/17.webp)



Stuur dan een eerste bericht naar deze persoon.



![Image](assets/fr/18.webp)



Zodra de persoon je verzoek accepteert, zie je zijn of haar gebruikersnaam verschijnen en kun je vrijuit met hem of haar chatten.



![Image](assets/fr/19.webp)



## Desktop-software synchroniseren



Om je account op je computer te synchroniseren, moet je de software installeren. [Download het van de officiële website](https://getsession.org/download). Ik raad je aan om de authenticiteit en integriteit te controleren voordat je het installeert.



![Image](assets/fr/20.webp)



Klik bij de eerste keer opstarten op "*Ik heb een account*".



![Image](assets/fr/21.webp)



Voer je Mnemonic zin in, en zorg ervoor dat je een spatie laat tussen elk woord.



![Image](assets/fr/22.webp)



Je hebt nu toegang tot je gesprekken vanaf je computer.



![Image](assets/fr/23.webp)



Gefeliciteerd, je hebt nu Session Messaging onder de knie, een uitstekend alternatief voor WathsApp!



Ik raad ook deze andere tutorial aan, waarin ik Threema presenteer, een ander interessant alternatief voor je berichtenapplicatie:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74