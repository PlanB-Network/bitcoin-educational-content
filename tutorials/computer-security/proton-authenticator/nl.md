---
name: Proton Authenticator
description: Hoe kan ik Proton Authenticator gebruiken om mijn accounts te beveiligen met 2FA?
---
![cover](assets/cover.webp)



Twee-factor authenticatie (2FA) voegt een extra veiligheidsbarrière toe aan je accounts door, naast je wachtwoord, extra bewijs te vereisen dat alleen jij het hebt. Het inschakelen van 2FA vermindert het risico op hacken drastisch, zelfs als je wachtwoord gecompromitteerd is door phishing of een datalek. Zonder 2FA zou een aanvaller alleen je wachtwoord nodig hebben om toegang te krijgen tot je accounts; met 2FA zou hij ook je tweede factor nodig hebben, waardoor de meeste pogingen tot accountdiefstal worden verijdeld.



Er bestaan verschillende soorten 2FA. SMS codes zijn beter dan niets, maar blijven kwetsbaar voor SIM swapping aanvallen en onderschepping. We raden SMS niet aan als primaire 2FA. Authenticatietoepassingen (TOTP) generate tijdelijke codes lokaal op je toestel, waardoor ze veel moeilijker te onderscheppen zijn. Fysieke beveiligingssleutels bieden de beste beveiliging, maar vereisen speciale hardware.



Proton Authenticator is een TOTP-authenticator. Het is Protons antwoord op de beperkingen van bestaande applicaties: veel zijn propriëtair, bevatten advertentietrackers en bieden geen versleutelde back-up. Proton Authenticator onderscheidt zich door een open source applicatie te bieden, vrij van advertenties en trackers, met een end-to-end versleutelde back-up.



## Even voorstellen: Proton Authenticator



Proton Authenticator is een TOTP-authenticatietoepassing voor mobiele en desktopcomputers, ontwikkeld door Proton, dat bekend staat om zijn privacygerichte diensten. Zoals alle Proton-producten is de applicatie open source en heeft het onafhankelijke beveiligingsaudits ondergaan. Het is gratis beschikbaar op alle platforms (Android, iOS, Windows, macOS, Linux).



Proton Authenticator biedt de volgende belangrijke functies:





- Genereren van TOTP**-codes voor je 2FA-accounts, compatibel met de meeste sites die Google Authenticator, Authy, enz. gebruiken.





- Optionele versleutelde cloudback-up**: je kunt de applicatie koppelen aan je Proton-account om een back-up te maken van je codes en ze te synchroniseren met end-to-end versleuteling. Als je je apparaat verliest, kun je gewoon een nieuw apparaat koppelen om al je codes te herstellen.





- Multi-device synchronisatie**: door in te loggen op Proton in de app, worden je 2FA-codes automatisch gesynchroniseerd tussen meerdere apparaten via end-to-end encryptie. Op iOS is synchronisatie via iCloud een alternatief.





- Lokale vergrendeling met wachtwoord of biometrie**: de applicatie biedt vergrendeling met PIN en/of vingerafdruk/gezichtsidentificatie. Dus zelfs als iemand fysiek toegang heeft tot je ontgrendelde telefoon, kan hij Proton Authenticator niet openen.





- Geen gegevensverzameling of trackers**: Proton streeft ernaar geen persoonlijke gegevens te verzamelen via de applicatie. Er is geen verborgen reclame of gedragsanalyse.





- Gemakkelijk importeren/exporteren**: een van de sterke punten van Proton Authenticator is de importwizard voor bestaande accounts, die compatibel is met andere applicaties (Google Authenticator, Authy, Aegis, enz.). Je kunt je codes desgewenst ook exporteren naar een bestand.



Kortom, Proton Authenticator wil een compromisloze 2FA-oplossing zijn: veilig, privé, flexibel.



## Installatie



Proton Authenticator is gratis beschikbaar op alle platforms. Ga naar de officiële pagina om de applicatie te downloaden: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Officiële Proton Authenticator-pagina met de belangrijkste functies en Interface* van de applicatie



Op deze pagina vind je downloadlinks voor alle besturingssystemen: Android, iOS, Windows, macOS en Linux. Klik gewoon op het besturingssysteem van je keuze en volg de standaard installatiestappen.



In deze tutorial laten we je zien hoe je de app installeert en configureert op macOS, en daarna bekijken we hoe je de app installeert op iOS en je codes synchroniseert tussen de twee apparaten.



### Installatie op macOS



Zodra je de applicatie hebt gedownload en geïnstalleerd, start je Proton Authenticator. Bij de eerste start leidt de applicatie je door een paar schermen voor de eerste configuratie:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticator welkomstscherm met "Veiligheid in elke code" bericht en "Aan de slag"* knop



### Eerste invoer



Als Proton Authenticator detecteert dat je eerder een andere 2FA-toepassing hebt gebruikt, kan er een importwizard verschijnen. Het ondersteunt rechtstreeks importeren vanuit bepaalde toepassingen (Google Authenticator, 2FAS, Authy, Aegis, enz.). Je kunt deze stap ook overslaan en je accounts later handmatig toevoegen.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Importwizard voor het overbrengen van codes van andere verificatietoepassingen*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Compatibele invoertoepassingen: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth en Google Authenticator*



### Lokale applicatiebeveiliging



Stel een ontgrendelings-PIN in of schakel biometrische ontgrendeling (Touch ID) in als die beschikbaar is. Deze stap is cruciaal om te voorkomen dat iemand die je Mac gebruikt gratis toegang krijgt tot je 2FA-codes.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Touch ID-configuratiescherm met het bericht "Bescherm uw gegevens" en de knop "Touch ID activeren"*



### Synchronisatie-opties



Met de applicatie kun je ook iCloud-synchronisatie activeren om een veilige back-up van je gegevens te maken tussen je Apple apparaten.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*ICloud-synchronisatieoptie met het bericht "Maak een veilige back-up van uw gegevens met versleutelde iCloud-synchronisatie"*



Zodra deze stappen zijn voltooid, is Proton Authenticator klaar voor gebruik.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface lege Proton Authenticator met "Nieuwe code maken" en "Codes importeren"* opties



## Een 2FA-account toevoegen met ProtonMail



We zullen nu bekijken hoe je je eerste 2FA-code toevoegt, met ProtonMail als voorbeeld. Deze methode werkt identiek voor alle diensten die twee-factor authenticatie ondersteunen.



### 2FA inschakelen op ProtonMail



Allereerst kun je onze gids over ProtonMail raadplegen voor meer informatie:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Log in op je ProtonMail-account en ga naar de beveiligingsinstellingen. Zoek naar de optie "Twee-factor authenticatie" en activeer deze.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMail instellingenpagina met de "Authenticator app" optie in de "Twee-factor authenticatie"* sectie



Klik op de knop om de authenticator te activeren en ProtonMail vraagt je om een authenticatietoepassing te kiezen.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA configuratievenster met "Annuleren" en "Volgende"* knoppen



ProtonMail toont dan een QR-code die je kunt scannen met je verificatietoepassing.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR-code om te scannen met uw verificatietoepassing, met optie "Voer sleutel handmatig in" beschikbaar*



Als je de sleutel liever handmatig invoert, klik dan op "Sleutel handmatig invoeren" om de geheime sleutel te zien.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Handmatige invoer van 2FA-informatie: Sleutel, Interval (30) en Cijfers (6)*



### Scan de QR-code met Proton Authenticator



Klik in Proton Authenticator op macOS op "Een nieuwe code maken". De applicatie biedt je verschillende opties: **Scan een QR-code** of **Voer de sleutel handmatig in**.



Gebruik de camera van je Mac om de QR-code te scannen die wordt weergegeven op het ProtonMail-scherm. Zodra je de QR-code hebt gescand, kom je in het configuratiescherm voor nieuwe codes.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Nieuw venster voor het maken van invoer met velden voor Titel (ProtonMail), Geheim, Afzender (Proton), cijferparameters en interval*



Proton Authenticator vult de informatie automatisch in. Je kunt de naam desgewenst aanpassen en vervolgens op "Opslaan" klikken.



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*TOTP-code gegenereerd voor ProtonMail (848 812) met weergave van resterende tijd*



### Configuratie valideren



ProtonMail zal je vragen om een 6-cijferige code in te voeren die wordt gegenereerd door Proton Authenticator om te bevestigen dat de 2FA correct werkt.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMail-validatiescherm waarin u wordt gevraagd de 6-cijferige code (848812)* in te voeren



Kopieer de code van de applicatie (door erop te klikken) en plak deze in ProtonMail om de activering te voltooien.



Na validatie vraagt ProtonMail je om je herstelcodes te downloaden. Het is belangrijk dat je ze zorgvuldig opslaat.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMail herstelcodes scherm met lijst van herstelcodes en "Download"* knop



### Codes voor noodgevallen



Wanneer je een account toevoegt, bewaar dan de herstelcodes die door de service worden geleverd. De meeste sites bieden statische herstelcodes voor eenmalig gebruik die je op een veilige plek kunt bewaren. Bewaar deze back-upcodes buiten Proton Authenticator zodat je toegang tot je account kunt krijgen als je de toegang tot de 2FA-toepassing verliest.



## IOS-installatie en importeren van code



Nu je Proton Authenticator hebt ingesteld op macOS, wil je het misschien ook gebruiken op je iPhone of iPad. Zo krijg je je 2FA-codes op meerdere apparaten.



### De applicatie downloaden op iOS



Ga naar de App Store en zoek naar "Proton Authenticator". Download en installeer de applicatie op je iOS-apparaat.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Installatieproces op iOS: welkomstscherm, importwizard, selectie van compatibele applicaties en het uiteindelijke scherm "Codes importeren van Proton Authenticator"*



### Methode 1: exporteren/importeren via een JSON-bestand



Als je geen automatische synchronisatie gebruikt (iCloud of Proton-account), moet je je codes handmatig overzetten van je Mac naar je iPhone:



**Stap 1 - Exporteren vanuit macOS** :



Open Proton Authenticator op je Mac en ga naar Instellingen (tandwielpictogram). Klik in het menu op "Exporteren".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Proton Authenticator instellingenmenu op macOS met de optie "Exporteren" zichtbaar*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Export venster met bestandsnaam "Proton_Authenticator_backup_2025" en "Save"* knop



Sla het JSON-bestand op je Mac op. Je kunt het per beveiligde e-mail versturen of opslaan in iCloud Drive voor toegang vanaf je iPhone.



**Stap 2 - Importeren op iOS** :



Installeer Proton Authenticator op je iPhone en kies tijdens de configuratie voor het importeren van codes. Selecteer "Proton Authenticator" uit de lijst en importeer het JSON-bestand.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Importproces op iOS: JSON-bestandslokalisatie, importbevestiging en configuratieschermen met Face ID- en iCloud-opties*



### Methode 2: Automatische synchronisatie



**Via Proton account (voor multi-platform synchronisatie)** :



Als je nog geen Proton-account hebt ingesteld en wilt synchroniseren tussen verschillende besturingssystemen, vraagt de toepassing je om een Proton-account aan te maken of te koppelen.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Apparaat synchronisatiescherm waarin u wordt gevraagd een gratis Proton-account aan te maken of verbinding te maken met een bestaande account*



**Via iCloud (alleen voor Apple ecosysteem)** :


Als je alleen Apple apparaten gebruikt, kun je in de applicatie-instellingen kiezen voor iCloud-synchronisatie. Met deze methode worden je codes automatisch en veilig gesynchroniseerd tussen al je Apple apparaten, zonder dat je een Proton-account nodig hebt.



## Versleutelde back-up en herstel



Een van de belangrijkste functies van Proton Authenticator is de end-to-end back-up van 2FA-codes, zodat je bij verlies of verandering van apparaat niet helemaal opnieuw hoeft te beginnen.



### End-to-endencryptie



Als het gaat om versleutelde cloudback-up met Proton Authenticator, worden je TOTP-geheimen lokaal op je apparaat versleuteld voordat ze naar de Proton-server worden verzonden. Ontcijfering is alleen mogelijk door jou, op je apparaten die verbonden zijn met je Proton account. Proton AG heeft niet de sleutel om je geregistreerde codes te lezen.



Als je op iOS kiest voor iCloud in plaats van het Proton-account, worden je gegevens versleuteld volgens Apple-standaarden. Bij lokale back-ups op Android kun je het back-upbestand versleutelen met een wachtwoord naar keuze.



### Herstel in geval van verlies



Als je telefoon verloren of gestolen is of als je van handset verandert :



**Met Proton back-up ingeschakeld**: Installeer Proton Authenticator op het nieuwe apparaat. Log tijdens de eerste installatie in op hetzelfde Proton-account. De applicatie zal onmiddellijk al je 2FA-codes synchroniseren en downloaden van de versleutelde back-up.



**Met iCloud-back-up (iOS)**: Verbind de nieuwe iPhone/iPad met dezelfde Apple ID en zorg ervoor dat iCloud Keychain geactiveerd is. Maak na het installeren van Proton Authenticator verbinding met iCloud. Je codes zouden moeten synchroniseren via iCloud en verschijnen.



**Geen cloudback-up**: Je moet je accounts handmatig importeren. Als je een back-upbestand hebt geëxporteerd, gebruik dan de importeerfunctie in Proton Authenticator. In het ergste geval, als je geen back-up had, moet je de back-upcodes voor elke service gebruiken of contact opnemen met ondersteuning.



Met Proton Authenticator kun je je accounts op elk gewenst moment exporteren, als een versleuteld bestand of als een QR-code voor meerdere accounts. Deze opties geven je extra zekerheid.



## Beste praktijken



Het gebruik van een 2FA authenticator verhoogt je veiligheid aanzienlijk, maar je moet wel bepaalde best practices in acht nemen:



### Sla uw noodcodes op



Wanneer je 2FA activeert op een dienst, krijg je vaak een lijst met herstelcodes. Bewaar deze niet op je telefoon (op papier, in een versleutelde wachtwoordmanager, etc.). In het geval van totaal verlies van je authenticator, zullen deze statische codes je redden.



### Haal je wachtwoorden en 2FA-codes niet door elkaar



Het is verleidelijk om een wachtwoordmanager te gebruiken die ook TOTP's opslaat. Maar als je het wachtwoord en de 2FA-code op dezelfde plek bewaart, creëer je één enkel foutpunt en verzwak je de dubbele authenticatie. Voor maximale beveiliging raden veel experts aan om de twee factoren te scheiden: wachtwoorden in een veilige manager en 2FA-codes in een aparte applicatie zoals Proton Authenticator. Het gebruik van een geïntegreerde manager is echter nog altijd beter dan helemaal geen 2FA.



### Meerdere 2FA-methoden activeren



Gebruik bij voorkeur meer dan één tweede factor voor uw belangrijke accounts. Aarzel niet om een fysieke beveiligingssleutel toe te voegen als de service dat toestaat. Zie onze handleiding over Yubikey fysieke sleutels voor meer informatie:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Houd ook gedrukte noodcodes bij de hand.



### Blijf discreet en bescherm je apparaat



Laat niemand je ontgrendelde telefoon doorzoeken. Met Proton Authenticator zijn je codes beschermd door PIN/biometrie - geef deze PIN niet vrij. Pas ook op voor phishing: zelfs met 2FA kan een code die je in realtime aan een frauduleuze site geeft, gebruikt worden door een aanvaller.



### Updates en audits



Proton Authenticator up-to-date houden (updates corrigeren mogelijke fouten). Omdat de code open is, voert de gemeenschap informele controles uit en publiceert Proton de resultaten van formele controles.



## Vergelijking met andere toepassingen



Hoe verhoudt Proton Authenticator zich tot andere verificatietoepassingen? Hier is een vergelijkend overzicht:



**Proton Authenticator**: Open source, optionele E2EE versleutelde cloudback-up, synchronisatie met meerdere apparaten, lokale vergrendeling, geen tracering, beschikbaar op mobiel en desktop.



**Google Authenticator**: Bedrijfseigen, back-up via Google-account sinds 2023 maar zonder end-to-end-encryptie (sleutels kunnen door Google worden gezien), synchronisatie met meerdere apparaten toegevoegd in 2023, standaard geen toepassingsslot, bevat Google-trackers.



**Aegis Authenticator**: Open source, alleen lokale back-up, geen cloudsynchronisatie, code/biometrisch slot, geen tracering, alleen Android.



**Authenty**: Eigendomsrecht, wachtwoordversleutelde cloudback-up maar gesloten code, synchronisatie met meerdere apparaten, PIN-slot/vingerafdruk, verzamelt telefoonnummer, desktoptoepassing beëindigd in maart 2024.



Hieronder vind je onze gids voor Authy:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator is een van de meest uitgebreide en veilige oplossingen die beschikbaar is: open source, versleutelde synchronisatie met meerdere apparaten, geen commerciële follow-up.



## Hulpmiddelen en ondersteuning



### Officiële documentatie




- Officiële website**: [proton.me/authenticator](https://proton.me/authenticator) - Productpresentatie en downloads
- Downloadpagina**: [proton.me/nl/authenticator/download](https://proton.me/fr/authenticator/download) - Koppelingen voor alle besturingssystemen
- Proton-ondersteuning**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Officiële 2FA activeringsgids
- Proton blog**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Aankondiging en gedetailleerde functies



### Broncode en transparantie




- GitHub Proton Authenticator** : [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Open broncode
- Beveiligingsaudits**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Onafhankelijke auditrapporten



### Aanbevolen veiligheidstests


Test je installatie na de configuratie:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Controleer of uw accounts zijn gecompromitteerd
- [2FA Directory](https://2fa.directory/) - Lijst met diensten die 2FA ondersteunen



### Gemeenschappen en discussies




- Reddit r/Proton** : [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Officiële Protongemeenschap
- Privacygidsen Forum** : [discuss.privacyguides.net](https://discuss.privacyguides.net) - Technische discussies over privacykwesties
- Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Algemene privacytips



### Andere




- [Have I Been Pwned](https://haveibeenpwned.com/) - Controleer of uw accounts zijn gecompromitteerd
- [2FA Directory](https://2fa.directory/) - Lijst met diensten die 2FA ondersteunen