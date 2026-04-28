---
name: Delta chat
description: Praktische handleiding voor een gedecentraliseerde messaging-tool
---

![image](assets/cover.webp)




## Inleiding - Chatbeheer en privacy



De laatste jaren wordt er steeds vaker gesproken over Chat Control, een regelgevingsvoorstel dat tot doel heeft het automatisch scannen van privéberichten op grote communicatieplatforms in te voeren. Het verklaarde doel is om illegale inhoud te bestrijden, het probleem is dat dit mechanisme in feite massasurveillance zou inhouden en end-to-end encryptie en dus de privacy van alle gebruikers zou ondermijnen, niet alleen van overtreders.



Het echte risico is dat chats gecontroleerde omgevingen worden, waar elk bericht, afbeelding of bijlage kan worden onderzocht voordat het zelfs de ontvanger bereikt. En dit is waar een mogelijke oplossing om de hoek komt kijken: overstappen van gecentraliseerde platforms naar gedecentraliseerde berichtensystemen, die niet afhankelijk zijn van een enkele provider en niet gemakkelijk kunnen worden onderworpen aan dit soort controle.



Eén zo'n oplossing wordt in deze tutorial gepresenteerd: Delta Chat. Een volwassen en reeds bruikbare tool.




## Waarom Delta Chat en hoe het werkt



Delta Chat is een al erg goede messaging-oplossing voor dagelijks gebruik: erg handig om met vrienden, familie en andere mensen te praten, net als een echt equivalent van WhatsApp.



Het is een gedecentraliseerd berichtensysteem dat volledig is gebaseerd op e-mail. Het maakt in principe gebruik van de infrastructuur van traditionele e-mail, maar bouwt er een moderne instant messenger interface en ervaring bovenop. Op het eerste gezicht lijkt dit een beetje geïmproviseerd, maar het werkt eigenlijk heel goed en is verrassend robuust. Je kunt speciale mailservers gebruiken met de naam ChatMail, maar het kan ook naadloos samenwerken met gewone mailservers. Dit betekent dat je kunt inloggen met een bestaand account als je dat wilt, zonder dat je iets nieuws hoeft aan te maken.



Een ander hoogtepunt is de ondersteuning voor WebXDCs, wat kleine webapplicaties zijn die direct in chats gebruikt kunnen worden, vergelijkbaar met de mini-apps in Telegram. Het belangrijke verschil is dat deze apps geen internettoegang hebben, dus ze kunnen de gebruiker niet volgen of gegevens van buitenaf versturen.



Vanuit een beveiligingsperspectief gebruikt Delta Chat geverifieerde end-to-end encryptie, gebaseerd op PGP maar met moderne uitbreidingen die het qua beschermingsniveau vergelijkbaar maken met Signal. Het enige huidige gebrek is Perfect Forward Secrecy, maar dat is een evoluerend aspect.



Delta Chat is uitsluitend gebaseerd op e-mail en vermijdt dit volledig:




- verplichte telefoonnummers
- Gecentraliseerde ID's
- registraties gekoppeld aan één dienst



En dat maakt deze tool zeer resistent tegen invasieve regelgeving zoals Chat Control.




## Installatie



Vanaf de officiële website van [Delta Chat](https://delta.chat/download) kun je naar de downloadsectie gaan. Op Linux is het gemakkelijk beschikbaar via Flathub, maar er zijn ook pakketten voor Arch, NixOS, Snap en standalone versies.



![image](assets/it/01.webp)



Het is ook beschikbaar voor:




- [F-Droid] (https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS] (https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch] (https://open-store.io/app/deltatouch.lotharketterer)
- en andere winkels...



Als je op zoek bent naar een handleiding om F-Droid te installeren, kan deze tutorial je helpen:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Eén heel belangrijk ding: voor desktopversies heb je geen telefoon nodig. In tegenstelling tot WhatsApp of SimpleX Chat hoef je je niet eerst mobiel te registreren. Je kunt je profiel rechtstreeks op je pc aanmaken of overzetten vanaf een ander apparaat.




## Profiel aanmaken



Zodra de app geopend is, vraagt Delta Chat of je een nieuw profiel wilt aanmaken of een bestaand profiel wilt gebruiken.



![image](assets/it/02.webp)



Door een nieuw profiel aan te maken kun je invoeren:




- een naam
- een afbeelding (optioneel)



Een ChatMail-server wordt standaard voorgesteld, maar het is mogelijk:




- kies een andere ChatMail-server
- een klassiek e-mailaccount gebruiken
- iMAP en SMTP handmatig configureren
- registreren met de uitnodigingscode van een andere gebruiker



Na een paar seconden is het profiel klaar en kun je de app gebruiken.



![image](assets/it/03.webp)




## Interface en chat



De interface is heel eenvoudig en ongecompliceerd:




- Apparaatberichten, die lokale communicatie zijn
- Opgeslagen berichten, vergelijkbaar met die in Telegram en synchroniseerbaar tussen apparaten



![image](assets/it/04.webp)



Om een contactpersoon toe te voegen:




- Je QR code tonen
- Scan de
- Uitnodigen via link (uitnodigingslink delen).



![image](assets/it/05.webp)



Zodra de verbinding tot stand is gebracht, wordt end-to-end-encryptie automatisch geconfigureerd. De gebruikersinterface van de chat lijkt erg op die van WhatsApp:




- tekst- en spraakberichten
- foto's, video's en bestanden
- reacties op berichten
- reacties
- pop-upberichten
- aanpasbare meldingen.



![image](assets/it/06.webp)



## WebXDC: apps in chats:



Delta Chat staat het gebruik van WebXDC toe, dat wil zeggen kleine toepassingen die in conversaties zijn ingebed. Hier volgt een korte lijst van de nuttigste toepassingen:




- enquêtes
- tekenborden
- tijdelijke privéchats
- games met gedeelde chatscores



Er kunnen ook complexere spellen worden gestart, wat de flexibiliteit van deze tool aantoont.



![image](assets/it/07.webp)



## Groepen, kanalen en geavanceerde functies



Je kunt groepen maken, stickers gebruiken (vooral op desktops) en, door de experimentele opties te activeren, zelfs kanalen, vergelijkbaar met die in Telegram.



In de geavanceerde instellingen kun je inschakelen:




- spraakoproepen (nog experimenteel)
- geavanceerd beheer van e-mailprofielen
- volledige back-ups.



![image](assets/it/08.webp)



## Meerdere apparaten en back-up



Delta Chat biedt volledige ondersteuning voor meerdere apparaten:




- je kunt een tweede apparaat toevoegen via een QR-code
- kunt u een volledige overdracht uitvoeren via een back-up.



In enkele seconden vind je je chats, groepen en volledige geschiedenis terug, zonder afhankelijk te zijn van een centrale server.



![image](assets/it/09.webp)




## Conclusie



In een tijd waarin er steeds meer wordt gesproken over het controleren van privécommunicatie, biedt Delta Chat een concreet antwoord: gedecentraliseerd, versleuteld berichtenverkeer dat echt elke dag bruikbaar is.



Het is de oplossing die me, van alle die ik heb geprobeerd, het meest heeft overtuigd op het gebied van eenvoud, privacy en vrijheid. Als je wilt, kun je ook contact met me opnemen op Delta Chat via de volgende [uitnodigingslink](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Als je deze gids leuk vond, kun je me steunen door te doneren en een duim omhoog achter te laten. En onthoud: alleen door Delta Chat mobiel en desktop te gebruiken en te verkennen, ontdek je echt de volledige functionaliteit.



Tot de volgende keer.