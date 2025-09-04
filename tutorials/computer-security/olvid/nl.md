---
name: Olvid
description: Privéberichten voor iedereen
---
![cover](assets/cover.webp)



Olvid is een Franse instant messaging-applicatie die in 2019 is gelanceerd en is ontworpen om een hoog beveiligingsniveau te bieden, zonder in te leveren op privacy. In tegenstelling tot WhatsApp of Signal vraagt Olvid geen persoonlijke gegevens bij de registratie: geen telefoonnummer, geen e-mail, niets. Identificatie tussen gebruikers is gebaseerd op een Exchange van sleutels, zonder directory server of gedeeld Address boek.



Alle berichten worden end-to-end versleuteld met behulp van een origineel cryptografisch protocol, ontworpen om ook metadata te beschermen: niemand weet met wie je praat, of wanneer. De clientcode is open source, maar de centrale server die wordt gebruikt om versleutelde berichten te routeren, blijft propriëtair en wordt gehost op AWS.


Het beveiligingsmodel van Olvid is gebaseerd op een belangrijk principe: de volledige afwezigheid van vertrouwde derde partijen bij het vaststellen van digitale identiteiten. In tegenstelling tot de meeste versleutelde messengers die vertrouwen op een gecentraliseerde directory om gebruikersidentiteiten te beheren, is Olvid niet afhankelijk van een gecentraliseerde infrastructuur om de integriteit van de communicatie te waarborgen. Deze architectuur elimineert de risico's die gepaard gaan met het compromitteren van mappen.


Olvid gebruikt echter wel een centrale berichtendistributieserver, die strikt beperkt is tot een logistieke rol: hij handelt de asynchrone overdracht van versleutelde berichten af. Deze server speelt geen rol in het versleutelingsproces en kent noch de echte identiteiten van de gebruikers noch de inhoud of metadata van de berichten (behalve de publieke sleutel van de ontvanger, die nodig is voor de routering). Het kan daarom standaard als vijandig worden beschouwd zonder de algehele veiligheid van het systeem in gevaar te brengen. Zelfs als het gecompromitteerd zou zijn, zou het geen toegang verlenen tot de inhoud van berichten. Olvid gaat dus uit van centralisatie voor het afleveren van berichten (voor efficiëntie en kwaliteit van de service), terwijl het een beveiliging garandeert die onafhankelijk is van deze infrastructuur.



Olvid biedt een gratis versie en een abonnementsversie voor €4,99 per maand. De gratis versie biedt volledige functionaliteit, met uitzondering van het voeren van audio- en videogesprekken (hoewel het wel mogelijk is om deze te ontvangen), en maakt het niet mogelijk om je account op meerdere apparaten te synchroniseren. Dus als je van plan bent om alleen je smartphone te gebruiken en niet hoeft te bellen, is Olvid een uitstekende oplossing.



Olvid is gecertificeerd door ANSSI (de Franse autoriteit voor cyberveiligheid). Deze applicatie is een uitstekend alternatief voor traditionele berichtendiensten (WhatsApp, Facebook Messenger, WeChat...) voor wie op zoek is naar privacy en toch eenvoudig in gebruik wil blijven.


| Application          | E2EE 1:1      | E2EE groups   | Anonymous registration | Open-source client license | Open-source server license | Decentralized server | Year of creation |
| -------------------- | ------------- | ------------- | ---------------------- | -------------------------- | -------------------------- | -------------------- | ---------------- |
| WhatsApp             | ✅             | ✅             | ❌                      | ❌                          | ❌                          | ❌                    | 2009             |
| WeChat               | ❌             | ❌             | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Facebook Messenger   | ✅             | 🟡 (optional) | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Telegram             | 🟡 (optional) | ❌             | 🟡                     | ✅                          | ❌                          | ❌                    | 2013             |
| LINE                 | ✅             | ✅             | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Signal               | ✅             | ✅             | ❌                      | ✅                          | ✅                          | ❌                    | 2014             |
| Threema              | ✅             | ✅             | ✅                      | ✅                          | ❌                          | ❌                    | 2012             |
| Element (Matrix)     | ✅             | ✅             | ✅                      | ✅                          | ✅                          | 🟡 (federated)       | 2016             |
| Delta Chat           | ✅             | ✅             | ✅                      | ✅                          | N/A                        | 🟡 (via email)       | 2017             |
| Conversations (XMPP) | ✅             | ✅             | ✅                      | ✅                          | ✅                          | 🟡 (federated)       | 2014             |
| Session              | ✅             | ✅             | ✅                      | ✅                          | ✅                          | ✅                    | 2020             |
| SimpleX              | ✅             | ✅             | ✅                      | ✅                          | ✅                          | ✅                    | 2021             |
| **Olvid**            | **✅**         | **✅**         | **✅**                  | **✅**                      | **❌**                      | 🟡(no directory)     | **2019**         |
| Keet                 | ✅             | ✅             | ✅                      | ❌                          | N/A                        | ✅                    | 2022             |
| Jami                 | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2005             |
| Briar                | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2018             |
| Tox                  | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2013             |

*E2EE = End-to-endencryptie*



## De Olvid-toepassing installeren



Olvid is beschikbaar op alle platforms. Je kunt de applicatie rechtstreeks downloaden in de app store van je telefoon:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



Op Android is het ook mogelijk om [te installeren via APK] (https://www.olvid.io/download/).



In deze tutorial concentreren we ons op de mobiele versie, maar [er zijn ook computerversies beschikbaar](https://www.olvid.io/download/) (MacOS, Linux en Windows). Als je voor de betaalde versie kiest, kun je je account op meerdere apparaten synchroniseren.



![Image](assets/fr/01.webp)



## Maak een account aan op Olvid



Wanneer je de applicatie voor de eerste keer start, klik je op de knop "*Ik ben een nieuwe gebruiker*".



![Image](assets/fr/02.webp)



Kies een bijnaam of voer je voor- en achternaam in.



![Image](assets/fr/03.webp)



Voeg een profielfoto toe.



![Image](assets/fr/04.webp)



Je account is nu aangemaakt.



![Image](assets/fr/05.webp)



Om te voorkomen dat de toegang tot uw Olvid-account verloren gaat, raden wij u aan automatische back-ups in te stellen. Om dit te doen, open je de instellingen door op de drie puntjes rechtsboven in Interface te klikken en vervolgens "*Instellingen*" te selecteren.


⚠️ **Waarschuwing**: Sinds Olvid versie 3.7 is de procedure voor het maken van back-ups van je profielen en contactpersonen vervangen door een nieuwe. Deze handleiding geeft nog steeds de oude versie weer. Je kunt de nieuwe versie vinden op hun FAQ: [💾 Een back-up maken van je profielen](https://www.olvid.io/faq/sauvegarder-vos-profils/)


![Image](assets/fr/06.webp)



Ga naar het menu "*Sla toetsen en contacten op*".



![Image](assets/fr/07.webp)



Klik dan op "*generate een back-upsleutel*". Deze sleutel zal je back-ups versleutelen. Als je je account op een ander apparaat moet herstellen en er geen toegang meer toe hebt, heb je zowel een back-up als deze sleutel nodig om het te decoderen.



![Image](assets/fr/08.webp)



Bewaar deze sleutel op een veilige plaats. Je kunt ook een papieren kopie maken.



![Image](assets/fr/09.webp)



Je kunt dan kiezen om een lokale back-up te maken of een automatische back-up op een cloudservice. Deze tweede optie wordt sterk aangeraden om toegang tot je Olvid-account te garanderen in alle omstandigheden, zelfs als je je telefoon verliest.



![Image](assets/fr/10.webp)



Zorg ervoor dat de optie "*Automatische back-up inschakelen*" is aangevinkt.



![Image](assets/fr/11.webp)



Je kunt ook de andere beschikbare instellingen verkennen om de applicatie aan te passen aan jouw behoeften.



![Image](assets/fr/12.webp)



## Berichten versturen met Olvid



Om berichten te kunnen versturen, moet je eerst contacten toevoegen. Klik op de startpagina op de blauwe knop "*+*".



![Image](assets/fr/13.webp)



Olvid geeft dan je gebruikers-ID weer. Je kunt het dan doorgeven aan de mensen met wie je wilt communiceren, zodat ze je als contact kunnen toevoegen.



Om een persoon toe te voegen, scan je hun ID met je camera of plak je deze handmatig in door op de drie kleine puntjes in de rechterbovenhoek te klikken.



![Image](assets/fr/14.webp)



Zodra de ID is gescand, kun je je contactpersoon de getoonde QR-code laten scannen of hem of haar een verzoek voor verbinding op afstand sturen door op "*Contact op afstand*" te klikken.



![Image](assets/fr/15.webp)



De verbinding is nu tot stand gebracht.



![Image](assets/fr/16.webp)



Je kunt nu berichten en andere inhoud gaan uitwisselen met je correspondent!



![Image](assets/fr/17.webp)



Op de startpagina vind je al je gesprekken.



![Image](assets/fr/18.webp)



Het tweede tabblad bevat al je contacten.



![Image](assets/fr/19.webp)



Je kunt ook groepsdiscussies aanmaken.



![Image](assets/fr/20.webp)



Gefeliciteerd, je bent nu op de hoogte van het gebruik van Olvid messaging, een geweldig alternatief voor WathsApp! Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om deze tutorial te delen op je sociale netwerken. Hartelijk dank!



Ik raad ook deze andere tutorial aan, waarin ik je kennis laat maken met Proton Mail, een veel privacy-vriendelijker alternatief voor Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2