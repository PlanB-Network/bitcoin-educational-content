---
name: Nostr
description: Ontdek en begin met het gebruik van NOSTR
---



![A new challenger has arrived](assets/cover.webp)


*Aan het einde van deze gids begrijp je wat Nostr is, heb je een account aangemaakt en kun je het gebruiken.*

## Wat is Nostr?


Nostr is een protocol dat Twitter, Telegram en andere sociale mediaplatforms kan vervangen. Het is een eenvoudig open protocol dat in staat is om voor eens en altijd een wereldwijd bestendig sociaal netwerk te creëren.


## Hoe werkt het?


Nostr is gebaseerd op drie componenten: sleutelparen, clients en relais.


Elke gebruiker heeft een of meer identiteiten en elke identiteit wordt bepaald door een cryptografisch sleutelpaar.


Om toegang te krijgen tot het netwerk moet je clientsoftware gebruiken en verbinding maken met relais om inhoud te ontvangen en te verzenden.


![Key system](assets/2.webp)


## 1. Cryptografische sleutels


In tegenstelling tot Facebook of Twitter, waar gebruikers een e-mail Address en een overvloed aan informatie moeten verstrekken aan een privébedrijf, werkt Nostr zonder centrale autoriteit. Gebruikers generate een cryptografisch sleutelpaar, een geheime sleutel (ook wel privésleutel genoemd) en een publieke sleutel.


De geheime sleutel, nsec, die alleen de gebruiker kent, wordt gebruikt voor authenticatie en het publiceren van inhoud.


De publieke sleutel, npub, is een unieke identificatie waaraan alle inhoud die door een gebruiker wordt gepubliceerd, is gekoppeld. Je publieke sleutel is als een gebruikersnaam waarmee andere gebruikers je kunnen vinden en zich kunnen abonneren op je Nostr feed.


## 2. Klanten


Clients zijn software die interactie met Nostr mogelijk maken. De belangrijkste clients zijn:



- iOS: damus
- Android: amethyst
- Web: iris.to; snort.social; astral.ninja


Clients stellen gebruikers in staat om generate een nieuw sleutelpaar te maken (gelijk aan het aanmaken van een account) of zich te authenticeren met een bestaand sleutelpaar.


## 3. Relais


Relays zijn simplistische servers die je op elk moment kunt verlaten als de inhoud die ze je leveren je niet bevalt. Je kunt ook je eigen relay draaien als je dat wilt.


💡 **Pro tip:** Betaalde relays zijn over het algemeen effectiever in het filteren van spam en ongewenste inhoud.


## Gids


Nu weet je genoeg over Nostr om aan de slag te gaan en je eerste identiteit aan te maken op dit protocol.


In deze handleiding gebruiken we iris.to (https://iris.to/) omdat deze webclient op elk platform werkt.


## Stap 1: Sleutels genereren


ris maakt een set sleutels voor je aan zonder dat je meer hoeft te doen dan een naam (echt of fictief) in te voeren voor je profiel. Klik vervolgens op GO en je bent klaar!


![Main menu](assets/3.webp)


⚠️ **Let op!** Je moet je sleutels bijhouden als je weer toegang wilt krijgen tot je profiel nadat je sessie is afgesloten. Aan het einde van deze handleiding laat ik je zien hoe je dit doet.


## Stap 2: Inhoud publiceren


Het publiceren van inhoud is zo eenvoudig en intuïtief als het schrijven van een paar woorden in het publicatieveld.


![Publication](assets/4.webp)


Ziezo! Je hebt je eerste notitie gepubliceerd op Nostr.


![Post](assets/5.webp)


## Stap 3: Zoek een vriend


Vind me op Nostr en wees nooit meer alleen. Ik abonneer me op iedereen die zich op mijn feed abonneert. Om dit te doen, voer je gewoon mijn publieke sleutel in


npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 in de zoekbalk.


![My profile](assets/6.webp)


Klik op "volgen" en binnen maximaal een paar dagen abonneer ik me ook op jouw feed. Dan zijn we vrienden. Ik lees ook graag je bericht als je er een wilt schrijven.


Tot slot, zorg ervoor dat je je ook abonneert op Agora256's feed om een berichtje te ontvangen elke keer als we iets nieuws publiceren: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx


## Stap 4: Je profiel aanpassen


Je moet nog wat werk doen om je profiel aan te passen. Om dit te doen, klik je op de avatar die iris automatisch voor je heeft gegenereerd in de rechterbovenhoek van het scherm en klik je vervolgens op "profiel bewerken".


![Profile](assets/7.webp)


Het enige wat je nu nog hoeft te doen is iris vertellen waar je afbeelding en profielbanner op internet te vinden zijn. Ik raad aan om je eigen inhoud te hosten: bescherm wat van jou is.


![Another option](assets/8.webp)


Als je wilt, kun je ook afbeeldingen uploaden. Deze worden dan door iris voor je opgeslagen op nostr.build, een gratis hostingservice voor visuele content op Nostr.


Zoals je kunt zien, kun je je client ook zo instellen dat hij Sats kan ontvangen en versturen. Op deze manier kun je de auteurs van inhoud die je leuk vond belonen of, nog beter, Sats verzamelen voor de geweldige inhoud die je zult publiceren.


## Stap 5: Een back-up maken van het sleutelpaar


Deze stap is cruciaal als je toegang wilt houden tot je profiel nadat je bent afgemeld bij de client of als je sessie is verlopen.

Klik eerst op het pictogram "instellingen", weergegeven door een tandwiel

![Setting](assets/9.webp)


Kopieer en plak vervolgens één voor één je npub, npub hex, nsec en nsec hex in een tekstbestand dat je veilig bewaart. Ik raad aan om dit bestand te versleutelen als je weet hoe dat moet.


![Key](assets/10.webp)


⚠️ **Let op de waarschuwing die iris je geeft:** Terwijl je je publieke sleutel zonder angst kunt delen, is het een ander verhaal voor je privésleutel. Iedereen die deze sleutel heeft, kan toegang krijgen tot uw account.


## Conclusie


Ziezo, kleine struisvogel, je hebt je eerste stappen op Nostr gezet. Nu moet je leren om bliksemsnel te werken. We zullen binnenkort gidsen publiceren die je laten zien hoe je je sleutels beheert en hoe je bliksem kunt integreren in je Nostr-ervaring met getalby.