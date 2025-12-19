---
name: Mullvad VPN
description: Een VPN opzetten betaald met bitcoins
---
![cover](assets/cover.webp)


Een VPN ("*Virtual Private Network*") is een dienst die een veilige en versleutelde verbinding tot stand brengt tussen uw telefoon of computer en een externe server die wordt beheerd door een VPN-provider.


Technisch gezien wordt je internetverkeer, wanneer je verbinding maakt met een VPN, omgeleid via een versleutelde tunnel naar de VPN-server. Dit proces maakt het moeilijk voor derden, zoals Internet Service Providers (ISP's) of kwaadwillende actoren, om je gegevens te onderscheppen of te lezen. De VPN-server fungeert vervolgens als tussenpersoon die namens jou verbinding maakt met de service die je wilt gebruiken. Het wijst een nieuw IP Address toe aan je verbinding, wat helpt om je echte IP Address te verbergen voor de sites die je bezoekt. In tegenstelling tot wat sommige online advertenties suggereren, kun je met een VPN echter niet anoniem op het internet surfen, omdat je de VPN-provider, die al je verkeer kan zien, moet vertrouwen.

![MULLVAD VPN](assets/fr/01.webp)

De voordelen van het gebruik van een VPN zijn talrijk. Ten eerste beschermt het de privacy van je online activiteiten tegen ISP's of overheden, op voorwaarde dat de VPN-provider je informatie niet deelt. Ten tweede beveiligt het je gegevens, vooral wanneer je verbonden bent met openbare Wi-Fi-netwerken, die kwetsbaar zijn voor MITM-aanvallen ("**man-in-the-middle**"). Ten derde kunt u met een VPN, door uw IP Address te verbergen, geografische beperkingen en censuur omzeilen en toegang krijgen tot inhoud die anders niet beschikbaar of geblokkeerd zou zijn in uw regio.


Zoals je kunt zien, verschuift de VPN het risico van verkeersobservatie naar de VPN-provider. Daarom is het belangrijk om bij het kiezen van je VPN-provider rekening te houden met de persoonlijke gegevens die nodig zijn voor registratie. Als de provider vraagt om informatie zoals je telefoonnummer, e-mail Address, bankkaartgegevens, of erger nog, je post Address, neemt het risico toe dat je identiteit in verband wordt gebracht met je verkeer. In het geval van een compromittering van de provider of een gerechtelijke inbeslagname, zou het gemakkelijk zijn om je verkeer in verband te brengen met je persoonlijke gegevens. Daarom is het aan te raden om een provider te kiezen die geen persoonlijke gegevens vereist en anonieme betalingen accepteert, zoals met bitcoins.


In deze tutorial presenteer ik een eenvoudige, efficiënte, redelijk geprijsde VPN-oplossing waarvoor geen persoonlijke gegevens nodig zijn.


## Inleiding tot Mullvad VPN

Mullvad VPN is een Zweedse dienst die zich onderscheidt door zijn Commitment voor gebruikersprivacy. In tegenstelling tot mainstream VPN-providers vraagt Mullvad geen persoonlijke gegevens bij het aanmelden. Je hoeft geen e-mail Address, telefoonnummer of naam op te geven; in plaats daarvan wijst Mullvad je een anoniem accountnummer toe dat wordt gebruikt voor betaling en toegang tot de service. Bovendien beweert Mullvad geen activiteitenlogs bij te houden die via hun servers passeren.

![MULLVAD VPN](assets/notext/02.webp)

Voor betaling is het niet per se nodig om creditcardgegevens op te geven, want Mullvad accepteert Bitcoin betalingen (onchain alleen op hun officiële site, maar er is een onofficiële methode om via Lightning te betalen). Ze accepteren ook contante betalingen via de post.


Mullvad VPN onderscheidt zich ook door zijn transparantie en veiligheid. Hun software is open-source en ze ondergaan regelmatig onafhankelijke beveiligingsaudits om hun toepassingen en infrastructuur te beoordelen, waarvan de resultaten [op hun website worden gepubliceerd](https://mullvad.net/fr/blog/tag/audits). Het bedrijf achter Mullvad is gevestigd in Zweden, een land dat bekend staat om zijn strenge privacywetgeving. Ze maken uitsluitend gebruik van zelf gehoste servers en elimineren daarmee de risico's die gepaard gaan met het gebruik van cloudservices van derden, zoals hyperscalers AWS, Google Cloud of Microsoft Azure.


Qua functies biedt Mullvad alles wat je van een goede VPN-client verwacht, waaronder een kill switch die je verkeer beschermt als de VPN verbinding verbreekt, een optie om de VPN voor specifieke toepassingen uit te schakelen en de mogelijkheid om je verkeer via meerdere VPN-servers te routeren.


Natuurlijk hangt er een prijskaartje aan deze kwaliteit van dienstverlening, maar een eerlijke prijs is vaak een indicator van kwaliteit en eerlijkheid. Het kan een signaal zijn dat het bedrijf een bedrijfsmodel heeft zonder dat het nodig is om je persoonlijke gegevens aan derden te verkopen. Mullvad VPN biedt een vast tarief van 5 euro per maand, bruikbaar op maximaal 5 verschillende apparaten.

![MULLVAD VPN](assets/notext/03.webp)

In tegenstelling tot mainstream VPN-aanbieders heeft Mullvad een model waarbij je toegangstijd tot de service koopt in plaats van een terugkerend, automatisch abonnement. Je maakt gewoon een eenmalige betaling in bitcoins voor de gekozen duur. Als je bijvoorbeeld een jaar toegang koopt, kun je de service voor die periode gebruiken, waarna je terug moet keren naar de website van Mullvad om je toegangstijd te verlengen.

Vergeleken met IVPN, een andere VPN-provider van hoge kwaliteit, is Mullvad iets voordeliger. Bijvoorbeeld, zelfs als je kiest voor een driejarige afname bij IVPN, bedragen de maandelijkse kosten ongeveer €5,40. IVPN biedt echter wel enkele extra diensten aan en heeft ook een goedkoper plan dan dat van Mullvad (het Standard-plan), maar dit is beperkt tot slechts 2 apparaten en sluit het "multi-hop" protocol uit.

Ik heb ook wat informele snelheidstests uitgevoerd om IVPN en Mullvad te vergelijken. Hoewel IVPN een lichte superioriteit liet zien in termen van prestaties, waren de snelheden bij Mullvad nog steeds zeer bevredigend. Vergeleken met mainstream VPN-providers bleken IVPN en Mullvad minstens zo efficiënt, zo niet superieur in sommige gevallen.


## Hoe installeer je Mullvad VPN op een computer?


Ga naar de [officiële Mullvad-website](https://mullvad.net/en/download/) en klik op het menu "*Downloads*".

![MULLVAD VPN](assets/notext/04.webp)

Windows- of macOS-gebruikers kunnen de software rechtstreeks van de site downloaden en de instructies van de installatiewizard volgen om de installatie te voltooien.

![MULLVAD VPN](assets/notext/05.webp)

Voor Linux-gebruikers kun je de instructies specifiek voor jouw distributie vinden in de ["*Linux*"](https://mullvad.net/en/download/vpn/linux) sectie.

![MULLVAD VPN](assets/notext/06.webp)

Zodra de installatie is voltooid, moet je je account-ID invoeren. We zullen zien hoe je dit verkrijgt in de volgende secties van deze tutorial.


## Hoe installeer je Mullvad VPN op een smartphone?


Download Mullvad VPN van uw app store, of het nu de [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) is voor iOS-gebruikers, de [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) voor Android, of [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Als je Android gebruikt, heb je ook de optie om het `.apk` bestand direct van [de Mullvad site](https://mullvad.net/en/download/vpn/android) te downloaden.

![MULLVAD VPN](assets/notext/07.webp)

Bij het eerste gebruik van de app word je uitgelogd. Je moet je account-ID invoeren om de service te activeren.

![MULLVAD VPN](assets/notext/08.webp)

Laten we nu Mullvad activeren op je apparaten.


## Hoe betaal en activeer ik Mullvad VPN?


Ga naar de [officiële Mullvad website](https://mullvad.net/) en klik op de knop "*Get Started*".

![MULLVAD VPN](assets/notext/09.webp)

Klik op de knop "*generate rekeningnummer*".

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

Klik dan op de knop "*Tijd toevoegen aan je account*".

![MULLVAD VPN](assets/notext/12.webp)

Je komt dan op de inlogpagina voor je account. Voer je accountnummer in en klik vervolgens op de knop "*Log in*".

![MULLVAD VPN](assets/notext/13.webp)

Kies je betaalmethode. Ik raad aan om in bitcoins te betalen, omdat je dan profiteert van 10% korting, wat de kosten terugbrengt naar €4,50 per maand. Als je liever via Lightning betaalt, zal ik in het volgende deel een alternatieve methode geven.

![MULLVAD VPN](assets/notext/14.webp)

Klik op de knop "*Eenmalige betaling Address*".

![MULLVAD VPN](assets/notext/15.webp)

Betaal dan met je Bitcoin Wallet het aangegeven bedrag aan de ontvangende Address die je hebt gekregen.

![MULLVAD VPN](assets/notext/16.webp)

Het kan een paar minuten duren voordat de site je betaling heeft gedetecteerd, zodra de transactie is bevestigd. Zodra de betaling door Mullvad is gedetecteerd, verschijnt de duur van je abonnement linksboven op de pagina, in plaats van de vermelding "*Geen tijd over*".

![MULLVAD VPN](assets/notext/17.webp)

Je kunt dan je accountnummer invoeren op de software om het VPN te activeren.

![MULLVAD VPN](assets/notext/18.webp)

Om de VPN op je mobiele applicatie te activeren, is het proces precies hetzelfde. Je hoeft alleen maar je accountnummer in te voeren.

![MULLVAD VPN](assets/notext/19.webp)

## Hoe betaal je voor Mullvad VPN met Lightning?


Zoals je hebt begrepen, accepteert Mullvad nog geen betalingen via de Lightning Network. Dankzij een aanbeveling van [Lounès](https://x.com/louneskmt) heb ik echter een informele dienst ontdekt waarmee je deze beperking kunt omzeilen. Deze service, beschikbaar op [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), accepteert je betalingen op Lightning en geeft je in ruil daarvoor een geldig plan voor Mullvad.

![MULLVAD VPN](assets/notext/20.webp)

Je hebt 2 verschillende opties op deze site: je kunt de beheerder van de site vertrouwen en direct je accountnummer invoeren en dan op "*Log in*" klikken om je Mullvad-pakket automatisch te laten valideren. Of je kunt op de knop "*Heck yeah!*" klikken om een Lightning-voucher te kopen, die je vervolgens op de officiële Mullvad-site kunt gebruiken om je pakket te krijgen. mULLVAD VPN](assets/notext/21.webp) In beide gevallen wordt je gevraagd om de duur van je pakket te kiezen. Je kunt kiezen tussen 6 maanden en 1 jaar. mULLVAD VPN](assets/notext/22.webp) Klik vervolgens op de knop "*Top-up with Lightning*". mULLVAD VPN](assets/notext/23.webp) Om de aankoop af te ronden, betaalt u de Invoice met uw Lightning Wallet. mULLVAD VPN](assets/notext/24.webp) Als je een tegoedbon hebt gekocht, selecteer je op de Mullvad-website "*Voucher*" bij de betaalmethoden die beschikbaar zijn op je account. Voer vervolgens het tegoedbonnummer dat u van de site vpn.sovereign.engineering hebt ontvangen in het daarvoor bestemde vakje in. mULLVAD VPN](assets/notext/25.webp) ## Hoe gebruik en configureer ik Mullvad VPN?


Nu je een actieve account hebt en je accountnummer hebt ingevoerd in de Mullvad software of app, kun je volledig genieten van de diensten van je VPN. mULLVAD VPN](assets/notext/26.webp) Om de verbinding met het VPN te verbreken, klikt u gewoon op de knop "*Disconnect*". mULLVAD VPN](assets/notext/27.webp) Met de kleine rode pijl naast de knop "*Disconnect*" kunt u van server veranderen zonder de huidige locatie te wijzigen. mULLVAD VPN](assets/notext/28.webp) Als u van stad wilt veranderen voor uw VPN-server, klikt u op "*Switch location*" om een nieuwe locatie te kiezen. mULLVAD VPN](assets/notext/29.webp) Bovenaan het scherm ziet u de bijnaam van uw apparaat en de resterende duur van uw pakket. mULLVAD VPN](assets/notext/30.webp) Door op het pictogram van de kleine man te klikken, krijgt u toegang tot gedetailleerde informatie over uw account. mULLVAD VPN](assets/notext/31.webp) Klik op het tandwieltje om naar de instellingen te gaan. mULLVAD VPN](assets/notext/32.webp) In het menu "*Gebruiker Interface instellingen*" kun je de instellingen van je software aanpassen, inclusief de Interface taal en het gedrag op je systeem. mULLVAD VPN](assets/notext/33.webp) In het menu "*VPN instellingen*" vind je opties met betrekking tot je VPN. Ik raad aan om de opties "*Auto-connect*" en "*Launch app on start-up*" in te schakelen zodat je VPN-verbinding automatisch wordt gestart wanneer je machine opstart.

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

Tot slot kunt u met het menu "*Split tunneling*" specifieke toepassingen op uw machine selecteren waarvoor internetverkeer niet via het VPN wordt geleid.

![MULLVAD VPN](assets/notext/36.webp)

Om een overzicht te krijgen van je Mullvad account en de verschillende aangesloten apparaten te beheren, kun je klikken op het "*Devices*" menu op de website.

![MULLVAD VPN](assets/notext/37.webp)

En daar heb je het, je bent nu uitgerust om ten volle te genieten van Mullvad VPN. Als je geïnteresseerd bent in het ontdekken van een andere VPN-provider die vergelijkbaar is met Mullvad, zowel wat betreft functies als prijzen, raad ik je ook aan om onze tutorial over IVPN te bekijken:


https://planb.academy/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68