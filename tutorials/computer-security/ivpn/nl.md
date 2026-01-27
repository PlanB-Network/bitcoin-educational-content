---
name: IVPN
description: Een VPN opzetten betaald met bitcoins
---
![cover](assets/cover.webp)


Een VPN ("*Virtual Private Network*") is een dienst die een veilige en versleutelde verbinding tot stand brengt tussen uw telefoon of computer en een externe server die wordt beheerd door de VPN-provider.


Technisch gezien wordt je internetverkeer, wanneer je verbinding maakt met een VPN, omgeleid via een versleutelde tunnel naar de VPN-server. Dit proces maakt het moeilijk voor derden, zoals Internet Service Providers (ISP's) of kwaadwillende actoren, om je gegevens te onderscheppen of te lezen. De VPN-server fungeert vervolgens als tussenpersoon die namens jou verbinding maakt met de service die je wilt gebruiken. Het wijst een nieuw IP Address toe aan je verbinding, wat helpt om je echte IP Address te verbergen voor de sites die je bezoekt. In tegenstelling tot wat sommige online advertenties suggereren, kun je met een VPN echter niet anoniem op het internet surfen, omdat het een vorm van vertrouwen vereist in de VPN-provider die al je verkeer kan zien.

![IVPN](assets/fr/01.webp)

De voordelen van het gebruik van een VPN zijn talrijk. Ten eerste beschermt het de privacy van je online activiteiten tegen ISP's of overheden, op voorwaarde dat de VPN-provider je informatie niet deelt. Ten tweede beveiligt het je gegevens, vooral wanneer je verbonden bent met openbare Wi-Fi-netwerken, die kwetsbaar zijn voor MITM-aanvallen (man-in-the-middle). Ten derde kun je met een VPN, door je IP Address te verbergen, geografische beperkingen en censuur omzeilen en krijg je toegang tot inhoud die anders in jouw regio niet beschikbaar of geblokkeerd zou zijn.


Zoals je kunt zien, verschuift de VPN het risico van verkeersobservatie naar de VPN-provider. Daarom is het belangrijk om bij het kiezen van je VPN-provider rekening te houden met de persoonlijke gegevens die nodig zijn voor registratie. Als de provider vraagt om informatie zoals je telefoonnummer, e-mail Address, bankkaartgegevens, of erger nog, je post Address, dan neemt het risico toe dat je identiteit in verband wordt gebracht met je verkeer. In het geval van een compromittering van de provider of een gerechtelijke inbeslagname, zou het gemakkelijk zijn om je verkeer in verband te brengen met je persoonlijke gegevens. Daarom is het aan te raden om een provider te kiezen die geen persoonlijke gegevens vereist en anonieme betalingen accepteert, zoals met bitcoins.


In deze tutorial presenteer ik een eenvoudige, efficiënte, redelijk geprijsde VPN-oplossing waarvoor geen persoonlijke gegevens nodig zijn.


## Inleiding tot IVPN


IVPN is een VPN-service die speciaal is ontworpen voor gebruikers die op zoek zijn naar een vorm van privacy. In tegenstelling tot populaire VPN-aanbieders die vaak op YouTube worden gepromoot, onderscheidt IVPN zich door transparantie, veiligheid en respect voor privacy.

Het privacybeleid van IVPN is strikt: bij het aanmelden zijn geen persoonlijke gegevens vereist. Je kunt een account openen zonder een e-mail Address, naam of telefoonnummer op te geven. Voor betalingen is het niet nodig om creditcardgegevens in te voeren, aangezien IVPN betalingen in bitcoins accepteert (onchain en Lightning). Bovendien beweert IVPN geen activiteitenlogs bij te houden, wat betekent dat je internetverkeer in theorie niet wordt geregistreerd door het bedrijf.

IVPN is ook [volledig open-source](https://github.com/ivpn), wat betreft hun software, applicaties en zelfs hun website, waardoor iedereen hun code kan controleren en bekijken. Ze ondergaan ook jaarlijks onafhankelijke veiligheidscontroles, waarvan de resultaten op hun website worden gepubliceerd.


IVPN maakt uitsluitend gebruik van zelf gehoste servers, waardoor de risico's die gepaard gaan met het gebruik van cloudservices van derden, zoals AWS, Google Cloud of Microsoft Azure, worden geëlimineerd.


De service biedt tal van geavanceerde functies, zoals multi-hop, waarmee verkeer via meerdere servers in verschillende rechtsgebieden wordt geleid om de anonimiteit te verbeteren. IVPN integreert ook een tracker en ad blocker en biedt de optie om uit verschillende VPN-protocollen te kiezen.


Natuurlijk hangt er een prijskaartje aan deze kwaliteit van dienstverlening, maar een adequate prijs is vaak een indicator van kwaliteit en eerlijkheid. Het kan een signaal zijn dat het bedrijf een bedrijfsmodel heeft zonder de noodzaak om persoonlijke gegevens te verkopen. IVPN biedt vervolgens 2 soorten plannen: het Standaard plan, waarmee je tot 2 apparaten kunt verbinden, en het Pro plan, waarmee je tot 7 verbindingen kunt maken en dat het "*Multi-hop*" protocol bevat dat je verkeer via meerdere servers routeert.


In tegenstelling tot reguliere VPN-aanbieders werkt IVPN op basis van een model waarbij je toegangstijd tot de service koopt, in plaats van een terugkerend abonnement. Je betaalt eenmalig in bitcoins voor de gekozen duur. Als u bijvoorbeeld een jaar toegang koopt, kunt u de service voor die periode gebruiken, waarna u terug moet keren naar de IVPN-website om meer toegangstijd te kopen.


De [IVPN tarieven](https://www.ivpn.net/en/pricing/) zijn progressief afhankelijk van de gekochte toegangsduur. Hier zijn de prijzen voor het Standard-plan:


- 1 week: $2
- 1 maand: $6
- 1 jaar: $60
- 2 jaar: $100
- 3 jaar: $140


En voor het Pro-plan:


- 1 week: $4
- 1 maand: $10
- 1 jaar: $100
- 2 jaar: $160
- 3 jaar: $220


## Hoe installeer ik IVPN op een computer?

Download [de nieuwste versie van de software](https://www.ivpn.net/en/apps-windows/) voor uw besturingssysteem en ga dan verder met de installatie door de stappen in de installatiewizard te volgen. iVPN](assets/notext/02.webp)

Linux-gebruikers moeten de specifieke instructies voor hun distributie raadplegen die beschikbaar zijn op [deze pagina](https://www.ivpn.net/en/apps-linux/).

![IVPN](assets/notext/03.webp)

Zodra de installatie is voltooid, moet je je account-ID invoeren. We zullen in de volgende secties van deze tutorial zien hoe je dit verkrijgt.

![IVPN](assets/notext/04.webp)

## Hoe installeer je IVPN op een smartphone?


Download IVPN van uw app store, of het nu de [AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683) voor iOS-gebruikers, de [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) voor Android, of [F-Droid](https://f-droid.org/en/packages/net.ivpn.client) is. Als u Android gebruikt, hebt u ook de optie om het `.apk`-bestand rechtstreeks van [de IVPN-site](https://www.ivpn.net/en/apps-android/) te downloaden.

![IVPN](assets/notext/05.webp)

Bij het eerste gebruik van de app word je uitgelogd. Je moet je account-ID invoeren om de service te activeren.

![IVPN](assets/notext/06.webp)

Laten we nu verder gaan met het activeren van IVPN op uw apparaten.


## Hoe betaal en activeer ik IVPN?


Ga naar de officiële IVPN-website [op de betaalpagina](https://www.ivpn.net/en/pricing/).

![IVPN](assets/notext/07.webp)

Selecteer het plan dat het beste bij je behoeften past. Voor deze tutorial kiezen we voor het Standard-plan, waarmee we de VPN bijvoorbeeld op onze computer en smartphone kunnen activeren.

![IVPN](assets/notext/08.webp)

IVPN maakt dan uw account aan. U hoeft geen persoonlijke gegevens op te geven. Het is alleen uw account-ID waarmee u kunt inloggen. Het fungeert een beetje als een toegangssleutel. Bewaar het op een veilige plaats, bijvoorbeeld in uw wachtwoordmanager. U kunt ook een papieren kopie maken.

![IVPN](assets/notext/09.webp)

Kies op dezelfde pagina de duur van je abonnement op de service.

![IVPN](assets/notext/10.webp)

Selecteer vervolgens je betaalmethode. Ik ga betalen via Lightning Network, dus ik klik op de knop "*Bitcoin*".

![IVPN](assets/notext/11.webp)

Controleer of alles naar wens is en klik dan op de knop "*Betalen met Lightning*".

![IVPN](assets/notext/12.webp)

Een Lightning Invoice zal u voorgesteld worden op hun BTCPay Server. Scan de QR-code met uw Lightning Wallet en ga verder met de betaling.

![IVPN](assets/notext/13.webp) Once the invoice is paid, click on the "*Return to IVPN*" button.

![IVPN](assets/notext/14.webp)

Uw account wordt nu weergegeven als "*Actief*" en u kunt de datum zien tot wanneer uw toegang tot het VPN geldig is. Na deze datum moet u uw betaling verlengen.

![IVPN](assets/notext/15.webp)

Om uw verbinding via IVPN op uw pc te activeren, kopieert u gewoon uw account-ID.

![IVPN](assets/notext/16.webp)

En plak het in de software die je eerder hebt gedownload.

![IVPN](assets/notext/17.webp)

Klik vervolgens op de knop "*Login*".

![IVPN](assets/notext/18.webp)

Klik op het vinkje om de VPN-verbinding te activeren en daar ga je, het internetverkeer van je computer is nu versleuteld en wordt omgeleid via een IVPN-server.

![IVPN](assets/notext/19.webp)

Voor uw smartphone is de procedure identiek. Plak uw account-ID of scan de QR-code gekoppeld aan uw IVPN-account die toegankelijk is vanaf de website. Klik vervolgens op het vinkje om de verbinding tot stand te brengen.

![IVPN](assets/notext/20.webp)

## Hoe gebruik en configureer ik IVPN?


Qua gebruik en instellingen is het vrij eenvoudig. Vanaf de hoofdpagina Interface kun je de verbinding activeren of deactiveren door het vinkje te zetten.

![IVPN](assets/notext/21.webp)

Je hebt ook de optie om je VPN voor een bepaalde tijd te pauzeren.

![IVPN](assets/notext/22.webp)

Door op de huidige server te klikken, kun je een andere server kiezen uit de beschikbare servers.

![IVPN](assets/notext/23.webp)

Het is ook mogelijk om de geïntegreerde firewall en de anti-trackerfunctie te activeren of deactiveren.

![IVPN](assets/notext/24.webp)

Klik op het instellingenpictogram om extra instellingen te openen.

![IVPN](assets/notext/25.webp)

In het tabblad "*Account*" vindt u instellingen die betrekking hebben op uw account.

![IVPN](assets/notext/26.webp)

In het tabblad "*Algemeen*" zijn er verschillende clientinstellingen. Ik raad je aan om de opties "*Launch at login*" en "*On launch*" in de "*Autoconnect*" sectie aan te vinken om automatisch de verbinding met de VPN tot stand te brengen bij het opstarten van je machine.

![IVPN](assets/notext/27.webp)

In het tabblad "*Connectie*" vindt u verschillende opties met betrekking tot de verbinding. Hier kunt u het gebruikte VPN-protocol wijzigen.

![IVPN](assets/notext/28.webp)

Met het tabblad "*IVPN Firewall*" kunt u de firewall systematisch activeren bij het opstarten van de computer, zodat er geen verbinding tot stand wordt gebracht buiten het VPN.

![IVPN](assets/notext/29.webp)

Het tabblad "*Split Tunnel*" biedt de mogelijkheid om bepaalde software uit te sluiten van de VPN-verbinding. Toepassingen die hier zijn toegevoegd blijven werken met een normale internetverbinding, zelfs wanneer de VPN is ingeschakeld.

![IVPN](assets/notext/30.webp)

In het tabblad "*WiFi control*" hebt u de mogelijkheid om specifieke acties te configureren op basis van de netwerken waarmee u verbonden bent. U kunt bijvoorbeeld uw thuisnetwerk aanwijzen als "*Trusted*" en de VPN configureren om niet te activeren op dit netwerk, maar automatisch te activeren op elk ander WiFi-netwerk.

![IVPN](assets/notext/31.webp)

Selecteer in het menu "*AntiTracker*" het blokkeerprofiel voor je anti-tracker. Dit is ontworpen om advertenties, malware en datatrackers te blokkeren door verzoeken aan trackingservices te blokkeren terwijl je op het internet surft. Dit verbetert je privacy door te voorkomen dat bedrijven je surfgegevens verzamelen en verkopen. Er is ook een "*Hardcore-modus*" beschikbaar om alle domeinen die eigendom zijn van Google en Meta en alle afhankelijke services volledig te blokkeren.

![IVPN](assets/notext/32.webp)

En daar heb je het, je bent nu uitgerust om ten volle te genieten van IVPN. Als je ook de beveiliging van je online accounts wilt verbeteren door een lokale wachtwoordmanager te gebruiken, nodig ik je uit om onze tutorial over KeePass te bekijken, een gratis en open-source oplossing:


https://planb.academy/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Als je geïnteresseerd bent in het ontdekken van een andere VPN-provider die vergelijkbaar is met IVPN, zowel wat betreft functies als prijs, raad ik je ook aan om onze tutorial over Mullvad te bekijken:


https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8