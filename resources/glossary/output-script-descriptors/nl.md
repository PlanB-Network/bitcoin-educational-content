---
term: UITVOER SCRIPT DESCRIPTORS
---

Output script descriptors, of gewoon descriptors, zijn gestructureerde expressies die een output script (`scriptPubKey`) volledig beschrijven en alle benodigde informatie geven om transacties van of naar een specifiek script te volgen. Deze descriptors vergemakkelijken het beheer van sleutels in HD wallets door middel van een standaard beschrijving van de structuur en soorten gebruikte adressen.


Het belangrijkste belang van descriptors ligt in hun vermogen om alle essentiële informatie voor het herstellen van een Wallet in een enkele string in te kapselen (naast de herstelzin). Door een Descriptor met de overeenkomstige Mnemonic zinnen op te slaan, is het mogelijk om niet alleen de private sleutels te herstellen, maar ook de precieze structuur van de Wallet en de bijbehorende scriptparameters. Het herstellen van een Wallet vereist namelijk niet alleen kennis van de initiële seed, maar ook specifieke indexen voor de afleiding van kind sleutelparen, evenals de `xpub` van elke factor in het geval van een Multisig Wallet. Voorheen werd aangenomen dat deze informatie impliciet bekend was bij iedereen. Echter, met de diversificatie van scripts en het ontstaan van complexere configuraties, zou deze informatie moeilijk te extrapoleren kunnen worden, waardoor deze gegevens privé en Hard-to-bruteforce informatie worden. Het gebruik van descriptoren vereenvoudigt het proces enorm: het is voldoende om de herstelzin(nen) en de bijbehorende Descriptor te kennen om alles betrouwbaar en veilig te herstellen.


Een Descriptor bestaat uit meerdere Elements:


- Scriptfuncties zoals `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) en `sortedmulti` (Multisignature met gesorteerde sleutels);
- Afgeleide paden, bijvoorbeeld `[d34db33f/44h/0h/0h]` die een afgeleid pad en een specifieke vingersleutelafdruk aangeven;
- Sleutels in verschillende formaten zoals hexadecimale openbare sleutels of uitgebreide openbare sleutels (`xpub`);
- Een controlesom, voorafgegaan door een Hash, om de integriteit van de Descriptor te verifiëren.


Een Descriptor voor een P2WPKH Wallet zou er bijvoorbeeld zo uit kunnen zien:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

In deze Descriptor geeft de afleidingsfunctie `wpkh` een Pay-to-Witness-Public-Key-Hash scripttype aan. Het wordt gevolgd door het afleidingspad dat bevat:


- `cdeab12f`: de vingerafdruk van de hoofdsleutel;
- `84h`: wat het gebruik van een BIP84 doel aangeeft, bedoeld voor SegWit v0 adressen;
- `0h`: wat aangeeft dat het een BTC-valuta is op de Mainnet;
- `0h`: dat verwijst naar het specifieke rekeningnummer dat in de Wallet wordt gebruikt.


De Descriptor bevat ook de uitgebreide openbare sleutel die in deze Wallet wordt gebruikt:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Vervolgens specificeert de notatie `/<0;1>/*` dat de Descriptor generate adressen kan afleiden uit de externe (`0`) en interne (`1`) keten, met een jokerteken (`*`) dat de opeenvolgende afleiding van meerdere adressen op een configureerbare manier toestaat, vergelijkbaar met het beheer van een "gatlimiet" op traditionele Wallet software.


Tenslotte stelt `#jy0l7nr4` de controlesom voor om de integriteit van de Descriptor te verifiëren.