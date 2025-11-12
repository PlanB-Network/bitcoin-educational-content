---
name: Specter Desktop
description: Beheer uw Bitcoin-portefeuilles met meerdere handtekeningen volledig soeverein met uw eigen knooppunt
---

![cover](assets/cover.webp)



Specter Desktop is een open source applicatie (MIT licentie) ontwikkeld door Cryptoadvance sinds 2019 die het beheer van Bitcoin wallets met uw hardware wallets (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) en uw eigen Bitcoin infrastructuur (Bitcoin Core node of Electrum server) vergemakkelijkt. De applicatie blinkt vooral uit in configuraties met meerdere handtekeningen, waardoor u grote bedragen kunt beveiligen door de ondertekeningskracht te verdelen over meerdere onafhankelijke hardware wallets.



**In deze tutorial leer je hoe je:**




- Specter Desktop installeren en configureren op je computer (Windows, macOS of Linux)
- Verbind Specter met een Electrum server (in dit voorbeeld gebruiken we Umbrel)
- Een eenvoudige wallet maken met wallet hardware (Coldcard)
- Bitcoins ontvangen en versturen met volledige soevereiniteit
- Het opzetten van een 2-op-3 multisignature wallet met verschillende hardware wallets
- Specter installeren op een Umbrel-server (geavanceerde bonus)



Al je transacties worden lokaal gevalideerd via je eigen infrastructuur, zonder informatie naar externe servers te sturen, waardoor je vertrouwelijkheid en financiële soevereiniteit gegarandeerd zijn. Controleer transacties altijd op uw wallet hardwarescherm voordat u ondertekent.



## Downloaden en installeren



Ga naar de officiële website van Specter Desktop om de applicatie te downloaden.



![Page d'accueil Specter](assets/fr/01.webp)



Kies op de downloadpagina de versie die overeenkomt met je besturingssysteem: macOS, Windows of Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Installeer de applicatie na het downloaden volgens de gebruikelijke instructies van je besturingssysteem. Voor macOS sleep je het pictogram naar Toepassingen. Voor Windows voer je het installatieprogramma uit. Voor Linux volg je de instructies van het pakket.



## Eerste configuratie



Bij de eerste keer opstarten vraagt Specter Desktop je om je verbindingstype te kiezen. Je kunt verbinding maken met een Electrum server of met je eigen Bitcoin Core node.



![Choix du type de connexion](assets/fr/03.webp)



In dit voorbeeld gebruiken we een verbinding met een Electrum server die op Umbrel draait.



Raadpleeg voor meer informatie onze Umbrel-handleiding:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Deze optie biedt snellere synchronisatie dan Bitcoin Core. Als je dat liever hebt, kun je "Bitcoin Core" selecteren en de verbinding met je lokale knooppunt configureren. De volgende stappen blijven hetzelfde, ongeacht uw keuze.



Selecteer "Electrum Connection" en kies "Enter my own" om je eigen Electrum server te configureren.



![Configuration Electrum](assets/fr/04.webp)



Voer het adres van je Electrum server in. In ons geval met Umbrel is het adres `umbrel.local` met poort `50001`. Klik op "Connect" om de verbinding tot stand te brengen.



Zodra je verbinding hebt gemaakt, verschijnt het welkomstscherm met een checklist om je op weg te helpen. Je moet nu je hardware wallets toevoegen.



![Écran d'accueil](assets/fr/05.webp)



## wallet hardware toevoegen



Klik in het linkermenu op "Apparaat toevoegen" om uw wallet hardware toe te voegen.



Specter Desktop ondersteunt tal van hardware wallets: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault en vele andere.



Als je meer wilt leren, bekijk dan onze wallet tutorials over hardware.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Selecteer je wallet hardware. In dit voorbeeld gebruiken we een Coldcard MK4.



Hieronder vind je onze tutorial voor deze wallet hardware:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Voor een Coldcard moet u de publieke sleutels exporteren vanaf de wallet hardware via een USB-verbinding of een microSD-kaart.



![Import des clés du Coldcard](assets/fr/07.webp)



Volg de weergegeven instructies om de sleutels van uw Coldcard te exporteren. Geef uw wallet hardware een naam (hier "MK4 Tuto"). Zodra de sleutels geïmporteerd zijn, kunt u een wallet met één enkele sleutel aanmaken, of andere hardware wallets toevoegen voor een wallet met meerdere handtekeningen.



![Dispositif ajouté](assets/fr/08.webp)



## Portfolio maken



Nadat u uw wallet hardware hebt toegevoegd, klikt u op "Maak enkele sleutel wallet" om een wallet met enkele handtekening te maken.



Geef je portefeuille een naam (bv. "Wallet voor tuto") en selecteer het adrestype. Selecteer "Segwit" om native bech32-adressen te gebruiken die de transactiekosten optimaliseren.



![Configuration du portefeuille](assets/fr/09.webp)



Zodra je portfolio is aangemaakt, biedt Specter aan om een back-up PDF-bestand op te slaan dat alle publieke informatie bevat die nodig is om je portfolio te herstellen (descriptors, uitgebreide publieke sleutels). Dit bestand bevat niet uw privésleutels.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Bitcoins ontvangen



Om bitcoins te ontvangen, selecteer je wallet in het linkermenu en klik je vervolgens op de tab "Ontvangen".



Specter genereert automatisch een nieuw ontvangstadres met een QR-code.



![Génération d'une adresse de réception](assets/fr/11.webp)



Je kunt het adres kopiëren of de QR-code scannen. Controleer altijd het adres op je wallet hardwarescherm voordat je het aan iemand doorgeeft.



## Geschiedenis en adressen bekijken



Zodra je bitcoins hebt ontvangen, kun je je transacties bekijken op het tabblad "Transacties".



![Historique des transactions](assets/fr/12.webp)



Op het tabblad "Adressen" kun je alle adressen bekijken die door je portfolio zijn gegenereerd, met hun gebruiksstatus en bijbehorende bedragen.



![Liste des adresses](assets/fr/13.webp)



## Bitcoins versturen



Om bitcoins te versturen, klik je op de tab "Verzenden". Voer het adres van de ontvanger in, het bedrag dat moet worden verzonden en vink de geavanceerde opties aan als je de UTXO's (muntcontrole) handmatig wilt selecteren.



![Création d'une transaction](assets/fr/14.webp)



Klik op "Create Unsigned Transaction" om de transactie op te bouwen. Specter zal je dan vragen om de transactie te ondertekenen met je wallet hardware.



![Signature de la transaction](assets/fr/15.webp)



Als je een Coldcard gebruikt, heb je de keuze om te ondertekenen via USB of via de microSD-kaart (air-gapped). Bevestig de transactie op je wallet hardwarescherm en controleer zorgvuldig het bestemmingsadres en het bedrag.



Zodra de transactie is ondertekend, kun je deze uitzenden op het Bitcoin netwerk.



![Options de diffusion](assets/fr/16.webp)



Klik op "Transactie verzenden" om de transactie te verzenden. Specter zal bevestigen dat je transactie is verzonden en je kunt de status ervan volgen op het tabblad Transacties.



![Diffusion de la transaction](assets/fr/17.webp)



## Een portfolio met meerdere handtekeningen maken en gebruiken



Een van de belangrijkste troeven van Specter Desktop is de mogelijkheid om het beheer van portefeuilles met meerdere handtekeningen te vereenvoudigen. Een multisig wallet vereist meerdere handtekeningen om een transactie te autoriseren, waardoor het single point of failure wordt geëlimineerd. Een 2-op-3 configuratie, bijvoorbeeld, vereist twee handtekeningen van drie afzonderlijke hardware wallets om een uitgave te valideren.



Om een multisig wallet te maken, begin je met het toevoegen van alle ondertekenende hardware wallets via "Add device". In dit voorbeeld zullen we drie verschillende hardware wallets gebruiken: een Coldcard MK4 (al eerder toegevoegd), een Passport en een Ledger. Deze diversificatie van fabrikanten versterkt de veiligheid door afhankelijkheid van een enkele toeleveringsketen of firmware te vermijden.



Hier zijn de links naar de Ledger en Passport tutorials:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Voeg de Passport toe door de wallet hardware een naam te geven (bijvoorbeeld "Passport multi") en de sleutels te importeren via een microSD-kaart of QR-code. Klik vervolgens op "Doorgaan" om verder te gaan.



![Ajout du Passport](assets/fr/23.webp)



Voeg dan de Ledger toe door deze aan te sluiten via USB en de Bitcoin toepassing te openen op de wallet hardware. Geef het een naam (bijvoorbeeld "ledger multi") en klik op "Get via USB" en vervolgens op "Continue" om de publieke sleutels te importeren.



![Ajout du Ledger](assets/fr/24.webp)



Zodra je je drie hardware wallets hebt geregistreerd in Specter, klik je op "wallet toevoegen" en selecteer je de optie "Meerdere handtekeningen" om een wallet met meerdere handtekeningen aan te maken.



![Choix du type de wallet](assets/fr/25.webp)



Selecteer de drie hardware wallets die je wilt opnemen in je multisignature quorum: MK4 Tuto, Passport multi en ledger multi. Klik op "Doorgaan" om door te gaan naar de volgende stap.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Kies uw configuratie voor meerdere handtekeningen. Selecteer "Segwit" als het adrestype om te profiteren van geoptimaliseerde kosten. Met de parameter "Vereiste handtekeningen om transacties te autoriseren (m van 3)" kunt u de drempel bepalen: voor een 2-op-3 configuratie zijn 2 handtekeningen vereist. Elke wallet hardware toont de bijbehorende multisig sleutel. Klik op "wallet aanmaken" om het aanmaken te voltooien.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Je "Multi tuto" portfolio met meerdere handtekeningen is nu aangemaakt. Specter raadt je onmiddellijk aan om het back-up PDF-bestand met de portfoliobeschrijving op te slaan. Klik op "Back-up PDF opslaan" om dit belangrijke bestand te downloaden.



![Wallet multisig créé](assets/fr/28.webp)



Specter laat je ook wallet informatie exporteren naar elk van je hardware wallets via QR code of bestand. Hierdoor kunnen bepaalde hardware wallets (zoals Coldcard of Passport) de multisig configuratie rechtstreeks in hun geheugen opslaan.



Voor Passport ontgrendel je je apparaat en ga je naar "Account beheren" > "Wallet verbinden" > "Specter" > "Multisig" > "QR Code", scan dan de QR-code die door Specter is gegenereerd. Uw Passport zal u dan vragen om een ontvangstadres van uw wallet te scannen om de multisig configuratie te valideren.



Voor de MK4 sluit je hem aan op je pc en ontgrendel je hem. Klik dan op "Sla MK4 Tuto bestand op" en sla het bestand op je MK4 op. De volgende keer dat je je wallet hardware signeert, zal de MK4 dit bestand gebruiken om de multisig te configureren.



![Export vers les hardware wallets](assets/fr/29.webp)



Ter informatie: je kunt op elk moment back-ups bekijken via het tabblad "Instellingen" van je portfolio en vervolgens "Exporteren":



![Accès au backup PDF](assets/fr/30.webp)



Het dagelijkse gebruik blijft vergelijkbaar met een eenvoudige wallet: je generate ontvangt adressen zoals normaal. Om bitcoins te versturen, ga je naar het tabblad "Verzenden", voer je het adres van de ontvanger en het bedrag in en klik je vervolgens op "Onondertekende transactie aanmaken".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter bouwt een PSBT (Partially Signed Bitcoin Transaction) en geeft "Verworven 0 van 2 handtekeningen" weer. Je moet nu tekenen met minstens twee van je drie hardware wallets. Klik op de eerste wallet hardware (bijv. "MK4 Tuto") om te ondertekenen met je Coldcard, daarna op de tweede (bijv. "Passport multi") om de tweede vereiste handtekening te verkrijgen.



![Signature de la transaction](assets/fr/32.webp)



Zodra je de 2 vereiste handtekeningen hebt verkregen (de interface toont "2 van de 2 handtekeningen verkregen" en "Transactie is klaar om te verzenden"), klik je op "Transactie verzenden" om de transactie uit te zenden op het Bitcoin netwerk.



![Transaction prête à être diffusée](assets/fr/33.webp)



Deze aanpak met meerdere handtekeningen is bijzonder geschikt voor bedrijven (meerdere managers moeten uitgaven goedkeuren), families (bescherming van een erfenis van meerdere generaties) of individuen die grote bedragen beheren (geografische verdeling van hardware wallets om gelokaliseerde rampen te weerstaan).



### Het cruciale belang van back-ups met meerdere handtekeningen



**Let op**: een back-up maken van een multisig-portefeuille is fundamenteel anders dan een back-up maken van een enkele portefeuille. Uw herstelzinnen (seed zinnen) alleen zijn niet voldoende om een multisig portfolio te herstellen. U moet ook een back-up maken van de **output descriptor** (output descriptor), die de configuratiegegevens voor uw multisig portfolio bevat.



De output descriptor bevat essentiële gegevens: de uitgebreide publieke sleutels (xpubs) van elke medeondertekenaar, de handtekeningdrempel (2-op-3 in ons voorbeeld), het gebruikte scripttype (native, genest of legacy Segwit) en de omleidingspaden voor elke wallet hardware. Zonder deze descriptor zul je, zelfs als je twee van je drie herstelzinnen hebt, niet in staat zijn om je wallet te herbouwen of toegang te krijgen tot je bitcoins. De descriptor laat je software weten hoe de publieke sleutels te combineren tot generate de Bitcoin adressen die overeenkomen met je fondsen.



Specter Desktop genereert automatisch een back-up PDF-bestand wanneer u uw multisig portfolio aanmaakt. Deze PDF bevat de volledige descriptor, de fingerprints van elke wallet hardware en alle publieke informatie die nodig is voor herstel. **Dit bestand bevat niet uw privésleutels** en stelt u daarom niet in staat om uw bitcoins uit te geven, maar het stelt iedereen die toegang heeft tot dit bestand wel in staat om uw volledige transactiegeschiedenis en saldo te zien.



Om een correcte back-up te maken van je configuratie met meerdere handtekeningen, volg je deze procedure: nadat je je portfolio hebt aangemaakt, klik je op het tabblad "Instellingen", vervolgens op "Exporteren" en selecteer je "Back-up PDF opslaan". Maak meerdere kopieën van deze PDF: print minstens twee kopieën op papier en bewaar ook een gecodeerde digitale kopie. Bewaar een kopie van de PDF bij elk van uw herstelzinnen, op geografisch gescheiden locaties.



Graveer je herstelzinnen op vuurvaste en waterdichte metalen platen om hun levensduur te garanderen. Onderschat nooit het belang van deze back-ups: als je de `~/.specter` map op je computer verliest EN je verliest een van je hardware wallets zonder een descriptor back-up, dan zijn al je fondsen onherroepelijk verloren, zelfs met een 2-op-3 configuratie. Redundantie met meerdere handtekeningen beschermt tegen het verlies van wallet hardware, maar alleen als je een correcte back-up hebt gemaakt van de descriptor van je wallet.



## Voordelen en beperkingen van Specter Desktop



**Voordelen**: Optimale vertrouwelijkheid met volledige lokale validatie zonder servers van derden. Flexibiliteit met meerdere handtekeningen voor geavanceerde configuraties (bedrijf, familie, individu). Uitgebreide hardware wallet ondersteuning met volledige interoperabiliteit (USB en air-gapped).



**Beperkingen**: Aanzienlijke leercurve voor geavanceerde Bitcoin concepten (UTXO's, descriptoren, afleidingspaden).



## Beste praktijken



Controleer altijd adressen en bedragen op je wallet scherm voor validatie, om jezelf te beschermen tegen malware.



Houd PDF-back-ups gescheiden van je zaden. Deze openbare beschrijvingen kunnen worden opgeslagen in een bankkluis of versleutelde cloud, waardoor herstel mogelijk wordt zonder dat je privésleutels worden blootgesteld.



Test herstel op token bedragen voordat je portefeuilles met grote fondsen gebruikt. Creëer, test, verwijder en herstel om je procedures te valideren.



Specter en uw firmware up-to-date houden. Verdeel je medeondertekenaars met meerdere handtekeningen geografisch (thuis/kantoor/nabij) om gelokaliseerde rampen te weerstaan. Gebruik beschrijvende labels om boekhouding en belastingaangifte te vergemakkelijken.



## Bonus: Installatie op een Bitcoin server (Umbrel, RaspiBlitz, Start9)



Als u al in het bezit bent van een Bitcoin server zoals Umbrel, RaspiBlitz, MyNode of Start9, dan kunt u Specter Desktop rechtstreeks vanuit hun applicatiewinkel installeren. Deze aanpak biedt een aantal belangrijke voordelen: de applicatie configureert zichzelf automatisch met uw lokale Bitcoin Core node, het blijft 24/7 toegankelijk via een webinterface vanaf elk apparaat op uw netwerk, en u kunt het zelfs veilig op afstand benaderen via Tor. Uw gehele Bitcoin infrastructuur is gecentraliseerd op een enkele dedicated server, wat het beheer vereenvoudigt en uw soevereiniteit versterkt.



### Installatie vanuit de Umbrel App Store



Ga vanuit je Umbrel-interface naar de App Store en zoek naar Specter Desktop. Klik op "Installeren" om de installatie te starten.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Zodra de installatie is voltooid, opent u Specter Desktop op uw Umbrel. Het welkomstscherm vraagt je om je verbindingstype te kiezen. Als je Specter gebruikt op je Umbrel, klik dan op "Instellingen bijwerken" om de verbinding te configureren.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Selecteer "Remote Specter USB connection" om het gebruik van USB hardware wallets verbonden met uw lokale computer mogelijk te maken tijdens het gebruik van Specter op de remote Umbrel server.



![Configuration Remote Specter USB](assets/fr/20.webp)



Volg de weergegeven instructies om de HWI Bridge te configureren. Je moet naar de bridge-instellingen van het apparaat gaan en het domein `http://umbrel.local:25441` toevoegen aan de witte lijst. Klik op "Update" om de configuratie op te slaan.



![HWI Bridge Settings](assets/fr/21.webp)



Als je je USB-hardwareportemonnees ook vanaf je lokale computer wilt gebruiken, download dan de Specter Desktop-toepassing naar je machine en stel deze in op "Ja, ik draai Specter op afstand". Klik op "Opslaan" om de configuratie af te ronden.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Conclusie



Specter Desktop democratiseert geavanceerde Bitcoin configuraties en maakt multisignature toegankelijk zonder dat dit ten koste gaat van uw soevereiniteit of vertrouwelijkheid. Voor gebruikers die aanzienlijke geldbedragen beheren, transformeert het institutionele praktijken in oplossingen die door particulieren kunnen worden ingezet.



Hoewel de applicatie een initiële investering in infrastructuur en opleiding vereist, biedt het volledige soevereiniteit: controle over de validatie-infrastructuur, fysiek eigendom van sleutels en transacties vrij van toezicht door derden. Of u nu een individu bent die zijn spaargeld veilig stelt, een familie die een kluis creëert voor meerdere generaties of een bedrijf dat zijn cashflow beheert, Specter Desktop is het referentiehulpmiddel voor het combineren van maximale veiligheid en absolute soevereiniteit.



## Bronnen



### Officiële documentatie




- [Officiële website van Specter Desktop](https://specter.solutions/desktop/)
- [GitHub broncode](https://github.com/cryptoadvance/specter-desktop)
- [Volledige documentatie](https://docs.specter.solutions/)



### Gemeenschap en ondersteuning




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Reddit discussieforum](https://reddit.com/r/specterdesktop/)
- [GitHub bugrapporten](https://github.com/cryptoadvance/specter-desktop/issues)