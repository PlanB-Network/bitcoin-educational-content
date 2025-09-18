---
name: Bitcoin Core (Linux)
description: Je eigen knooppunt draaien met Bitcoin core op Linux
---

![cover](assets/cover.webp)


## Je eigen knooppunt laten draaien met Bitcoin core


Inleiding tot Bitcoin en het concept van een knooppunt, aangevuld met een uitgebreide installatiegids op Linux.


Een van de meest opwindende aspecten van Bitcoin is de mogelijkheid om het programma zelf uit te voeren en zo op een granulair niveau deel te nemen aan het netwerk en de verificatie van de openbare transactie Ledger.


Bitcoin is als open-source project sinds 2009 vrij beschikbaar en openbaar verspreid. Bijna 17 jaar na de oprichting is Bitcoin nu een robuust en onstuitbaar digitaal monetair netwerk, dat profiteert van een krachtig organisch netwerkeffect. Voor hun inspanningen en visie verdient Satoshi Nakamoto onze dankbaarheid. Tussen haakjes, we hosten de Bitcoin whitepaper hier op Agora 256 (noot: ook op de universiteit).


### Je eigen bank worden


Het runnen van je eigen node is essentieel geworden voor aanhangers van het Bitcoin ethos. Zonder iemands toestemming te vragen, is het mogelijk om de Blockchain vanaf het begin te downloaden en zo alle transacties van A tot Z te verifiëren volgens het Bitcoin protocol.


Het programma bevat ook zijn eigen Wallet. Zo hebben we controle over de transacties die we naar de rest van het netwerk sturen, zonder tussenpersoon of derde partij. Je bent je eigen bank.


De rest van dit artikel is daarom een gids voor het installeren van Bitcoin core - de meest gebruikte Bitcoin softwareversie - specifiek op Debian-compatibele Linux-distributies zoals Ubuntu en Pop!OS. Volg deze gids om een stap dichter bij je individuele soevereiniteit te komen.


## Bitcoin core Installatiegids voor Debian/Ubuntu


**Voorwaarden**


- Minimaal 6 GB gegevensopslag (knooppunt pruned) - 1 TB gegevensopslag (Full node)
- Verwacht dat de *Initial Block Download* (IBD) minstens 24 uur duurt. Deze handeling is verplicht, zelfs voor een pruned knooppunt.
- Laat ~600 GB bandbreedte toe voor de IBD, zelfs voor een pruned knooppunt.


**Noot:💡** de volgende commando's zijn voorgedefinieerd voor Bitcoin core versie 24.1.


### Bestanden downloaden en controleren



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, evenals de `SHA256SUMS` en `SHA256SUMS.asc` bestanden (je moet natuurlijk de laatste versie van de software downloaden).



- Open een terminal in de map waar de gedownloade bestanden zich bevinden. Voorbeeld: `cd ~/Downloads/`.



- Controleer of de controlesom van het versiebestand is opgenomen in het controlesombestand met de opdracht `sha256sum --ignore-missing --check SHA256SUMS`.



- De uitvoer van dit commando moet de naam van het gedownloade versiebestand bevatten, gevolgd door `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Installeer git met de opdracht `sudo apt install git`. Kloon vervolgens de repository met de PGP-sleutels van de Bitcoin core ondertekenaars met het commando `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Importeer de PGP-sleutels van alle ondertekenaars met het commando `gpg --import guix.sigs/builder-keys/*`



- Controleer of het checksum bestand is ondertekend met de PGP sleutels van de ondertekenaars met het commando `gpg --verify SHA256SUMS.asc`.



Elke geldige handtekening zal een regel weergeven die begint met: `gpg: Goede handtekening` en een andere regel die eindigt met: `Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (voorbeeld van de PGP-sleutel vingerafdruk van Pieter Wuille).


**Note💡:** Het is niet nodig dat alle ondertekenaarsleutels een "OK" teruggeven. In feite kan er maar één nodig zijn. Het is aan de gebruiker om zijn eigen validatiedrempel voor PGP-verificatie te bepalen.


Je kunt de waarschuwingen negeren:



- `Deze sleutel is niet gecertificeerd met een vertrouwde handtekening!`



- `Er is geen aanwijzing dat de handtekening aan de eigenaar toebehoort.`


### Installatie van de Bitcoin core grafische Interface



- Gebruik in de terminal, nog steeds in de map waar het Bitcoin core versiebestand staat, het commando `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` om de bestanden in het archief uit te pakken.



- Installeer de eerder uitgepakte bestanden met het commando `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Installeer de benodigde afhankelijkheden met het commando `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Start _bitcoin-qt_ (Bitcoin core grafisch Interface) met het commando `Bitcoin-qt`.



- Om een pruned knooppunt te kiezen, vink je _Limit Blockchain storage_ aan en configureer je de datalimiet die opgeslagen moet worden:


![welcome](assets/fr/02.webp)


### Conclusie van deel 1: Installatiegids


Als Bitcoin core eenmaal geïnstalleerd is, is het aan te raden om het zoveel mogelijk draaiende te houden om bij te dragen aan het Bitcoin netwerk door transacties te verifiëren en nieuwe blokken naar andere peers te sturen.


Het blijft echter een goede gewoonte om je node met tussenpozen te draaien en te synchroniseren, zelfs al is het alleen maar om ontvangen en verzonden transacties te valideren.


![Creation wallet](assets/fr/03.webp)


## Tor configureren voor een Bitcoin core knooppunt


**Note💡:** Deze handleiding is ontworpen voor Bitcoin core 24.0.1 op Ubuntu/Debian compatibele Linux distributies.


### Tor installeren en configureren voor Bitcoin core


Eerst moeten we de Tor service (The Onion Router) installeren, een netwerk dat gebruikt wordt voor anonieme communicatie, waardoor we onze interacties met het Bitcoin netwerk kunnen anonimiseren. Voor een introductie tot online privacybeschermingstools, waaronder Tor, zie ons artikel over dit onderwerp.


Om Tor te installeren, open je een terminal en voer je `sudo apt -y install tor` in. Zodra de installatie is voltooid, wordt de service normaal gesproken automatisch op de achtergrond gestart. Controleer of het correct draait met het commando `sudo systemctl status tor`. Het antwoord zou `Active: active (exited)` moeten tonen. Druk op `Ctrl+C` om deze functie af te sluiten.


**Tip:** in ieder geval kun je de volgende commando's in de terminal gebruiken om Tor te starten, stoppen of herstarten:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Laten we vervolgens de grafische Bitcoin core Interface starten met het commando `Bitcoin-qt`. Schakel vervolgens de automatische functie van de software in om onze verbindingen via een Tor proxy te routeren: _Instellingen > Netwerk_, en vink daar _Connect through SOCKS5 proxy (standaard proxy)_ en _Use a separate SOCKS5 proxy to reach peers via Tor onion services_ aan.


![option](assets/fr/04.webp)


Bitcoin core detecteert automatisch of Tor geïnstalleerd is en zal, als dat zo is, standaard uitgaande verbindingen maken naar andere knooppunten die ook Tor gebruiken, naast verbindingen naar knooppunten die IPv4/IPv6 netwerken (clearnet) gebruiken.


**Note💡:** Ga naar het tabblad Weergave in Instellingen om de schermtaal te wijzigen in Frans.


### Geavanceerde Tor-configuratie (optioneel)


Het is mogelijk om Bitcoin core te configureren om alleen het Tor netwerk te gebruiken om verbinding te maken met peers, en zo onze anonimiteit via ons knooppunt te optimaliseren. Omdat er geen ingebouwde functionaliteit hiervoor is in de grafische Interface, moeten we handmatig een configuratiebestand maken. Ga naar Instellingen en dan Opties.


![option 2](assets/fr/05.webp)


Klik hier op _Configuratiebestand openen_. Eenmaal in het `Bitcoin.conf` tekstbestand, voeg je simpelweg de regel `onlynet=onion` toe en sla je het bestand op. Je moet Bitcoin core herstarten om dit commando te laten werken.


Vervolgens configureren we de Tor dienst zodat Bitcoin core inkomende verbindingen kan ontvangen via een proxy, waardoor andere knooppunten op het netwerk ons knooppunt kunnen gebruiken om Blockchain gegevens te downloaden zonder de veiligheid van onze machine in gevaar te brengen.


Voer in de terminal `sudo nano /etc/tor/torrc` in om het configuratiebestand van de Tor service te openen. Zoek in dit bestand naar de regel `#ControlPort 9051` en verwijder de `#` om het in te schakelen. Voeg nu twee nieuwe regels toe aan het bestand:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Om het bestand af te sluiten terwijl je het opslaat, druk je op `Ctrl+X > Y > Enter`. Terug in de terminal, herstart Tor door het commando `sudo systemctl restart tor` in te voeren.


Met deze configuratie kan Bitcoin core alleen via het Tor-netwerk (Onion) inkomende en uitgaande verbindingen maken met andere knooppunten op het netwerk. Om dit te bevestigen, klik je op het tabblad _Window_ en vervolgens op _Peers_.


![Nodes Window](assets/fr/06.webp)


### Aanvullende bronnen


Uiteindelijk zou het gebruik van alleen het Tor netwerk (`onlynet=onion`) je kwetsbaar kunnen maken voor een Sybil Attack. Daarom raden sommigen aan om een multi-netwerk configuratie te gebruiken om dit soort risico's te beperken. Verder worden alle IPv4/IPv6 verbindingen door de Tor proxy geleid zodra deze is geconfigureerd, zoals eerder aangegeven.


Als alternatief, om alleen op het Tor netwerk te blijven en het risico van een Sybil Attack te beperken, kun je de Address van een ander vertrouwd knooppunt toevoegen aan je `Bitcoin.conf` bestand door de regel `addnode=trusted_address.onion` toe te voegen. Je kunt deze regel meerdere keren toevoegen als je verbinding wilt maken met meerdere vertrouwde knooppunten.


Om de logs van je Bitcoin node te bekijken die specifiek gerelateerd zijn aan de interactie met Tor, voeg je `debug=tor` toe aan je `Bitcoin.conf` bestand. Je zult nu relevante Tor informatie in je debug log hebben, welke je kunt bekijken in het _Information_ venster met de _Debug File_ knop. Het is ook mogelijk om deze logs direct in de terminal te bekijken met het commando `bitcoind -debug=tor`.


**Tip💡:** hier zijn enkele interessante links:


- [Wiki-pagina met uitleg over Tor en de relatie met Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core configuratiebestand generator door Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Tor configuratiegids door Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Zoals altijd, als je vragen hebt, voel je vrij om ze te delen met de Agora256 gemeenschap. We leren samen om morgen beter te zijn dan vandaag!