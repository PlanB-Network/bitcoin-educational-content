---
name: Bacca
description: Ledger configureren zonder Ledger Live software
---
![cover](assets/cover.webp)


Als je een Ledger gebruikt, heb je waarschijnlijk gemerkt dat je de Ledger Live software moet gebruiken, tenminste voor de initiële configuratie van het apparaat, om de authenticiteit ervan te controleren en de Bitcoin applicatie erop te installeren. Na deze configuratie geven veel bitcoiners er echter de voorkeur aan om gespecialiseerde Bitcoin Wallet beheersoftware te gebruiken, zoals Sparrow of Liana in plaats van Ledger Live. Hoewel Ledger uitstekende hardware wallets produceert die snel de nieuwste Bitcoin functies bevatten, is hun software niet noodzakelijk aangepast aan de specifieke behoeften van bitcoiners. Ledger Live bevat namelijk veel functies die zijn ontworpen voor altcoins, terwijl de opties die zijn gewijd aan Bitcoin Wallet beheer beperkt zijn. Maar het probleem met Sparrow en Liana (op dit moment), is dat je de Bitcoin toepassing niet op de Ledger kunt installeren.


Om Ledger Live niet te hoeven gebruiken tijdens de eerste configuratie van uw Ledger, kunt u de Bacca-tool (of "Ledger Installer") gebruiken. Met deze software kun je de Bitcoin-toepassing installeren en bijwerken, de authenticiteit van je Ledger controleren en zelfs later de firmware van het apparaat bijwerken. Bacca is gemaakt door Antoine Poinsot (Darosior), Bitcoin core ontwikkelaar bij Chaincode Labs, medeoprichter [van Revault en Liana](https://wizardsardine.com/), en Pythcoiner.


In deze tutorial laat ik u zien hoe u deze tool kunt gebruiken, zodat u voorgoed zonder Ledger Live software kunt, en nog steeds kunt genieten van Ledger apparaten. Het werkt op alle apparaten: Nano S Classic, Nano S Plus, Nano X, Flex en Stax.


---
*Merk op dat deze tool vrij nieuw is en dat de ontwikkelaars aangeven dat het nog **in de testfase** is. Ze raden aan om het alleen voor testdoeleinden te gebruiken, en niet voor een apparaat dat bedoeld is om een echte Bitcoin Wallet te hosten, hoewel dat wel mogelijk is. In dit verband raad ik je aan om de aanbevelingen van de ontwikkelaars van deze tool te volgen, die gespecificeerd zijn [in de README van hun GitHub repository](https://github.com/darosior/ledger_installer).*


---
## Vereisten


Op je computer heb je twee tools nodig om Bacca te gebruiken:




- Git ;
- Rust.


Als je ze al hebt geïnstalleerd, kun je deze stap overslaan.


**Linux:**


Op een Linux distributie is Git over het algemeen voorgeïnstalleerd. Om te controleren of Git geïnstalleerd is op je systeem, kun je het volgende commando in de terminal typen :


```bash
git --version
```


Als Git niet geïnstalleerd is op je systeem, dan is hier het commando om het te installeren op een Debian :


```bash
sudo apt install git
```


Gebruik tenslotte het commando :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


Om Git te installeren, ga je naar [de officiële website van het project](https://git-scm.com/). Download de software en volg de installatie-instructies.


![BACCA](assets/fr/01.webp)


Ga op dezelfde manier te werk om Rust te installeren vanaf [de officiële website](https://www.Rust-lang.org/tools/install).


![BACCA](assets/fr/02.webp)


**MacOS:**


Als Git nog niet geïnstalleerd is op je systeem, open dan een terminal en voer het volgende commando uit om het te installeren:


```bash
git --version
```


Als Git niet geïnstalleerd is op je systeem, zal er een venster geopend worden dat je aanbiedt om Xcode te installeren, dat Git bevat. Volg gewoon de instructies op het scherm om door te gaan met de installatie.


Voer het volgende commando uit om Rust te installeren:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Bacca installatie


Open een terminal en ga naar de map waar je de software wilt opslaan, voer dan het volgende commando uit:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Navigeer naar de softwaremap:


```bash
cd ledger_installer
```


Gebruik dan Cargo om het project te compileren en de Bacca GUI uit te voeren:


```bash
cargo run -p ledger_manager_gui
```


Je hebt nu toegang tot de software Interface.


![BACCA](assets/fr/03.webp)


## De Ledger configureren


Voordat u begint, als uw Ledger nieuw is, moet u ervoor zorgen dat u de pincode hebt ingesteld en de herstelzin hebt opgeslagen. Je hebt Ledger Live niet nodig voor deze eerste stappen. Sluit uw Ledger gewoon aan via de USB-kabel om hem van stroom te voorzien. Als je niet zeker weet hoe je verder moet gaan met deze twee stappen, kun je het begin van de handleiding voor jouw model raadplegen:


https://planb.academy/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Bacca gebruiken


Sluit uw Ledger aan op uw computer en ontgrendel hem met de pincode die u hebt ingesteld. Bacca zou je Ledger automatisch moeten detecteren.


![BACCA](assets/fr/04.webp)


Om de echtheid van uw Ledger te bevestigen, klikt u op de knop "*Check*". U moet de verbinding op uw Ledger apparaat autoriseren om verder te kunnen gaan.


![BACCA](assets/fr/05.webp)


Bacca laat je dan weten of je Ledger echt is. Als dat niet zo is, betekent dit dat het apparaat gecompromitteerd is of dat het een vervalsing is. Stop in dat geval onmiddellijk met het gebruik ervan.


![BACCA](assets/fr/06.webp)


In het menu "*Apps*" kun je de lijst met toepassingen raadplegen die al op je Ledger geïnstalleerd zijn.


![BACCA](assets/fr/07.webp)


Om de Bitcoin-toepassing te installeren, klik je op "*Install*", waarna je de installatie op je Ledger autoriseert.


![BACCA](assets/fr/08.webp)


De applicatie is goed geïnstalleerd.


![BACCA](assets/fr/09.webp)


Als je niet de laatste versie van de Bitcoin-toepassing hebt geïnstalleerd, toont Bacca een knop "*Update*" in plaats van de aanduiding "*Laatst*". Klik gewoon op deze knop om de toepassing bij te werken.


![BACCA](assets/fr/10.webp)


Nu je Ledger correct geconfigureerd is met de laatste versie van de Bitcoin toepassing, ben je klaar om je Wallet te importeren en te gebruiken op managementsoftware zoals Sparrow of Liana, zonder Ledger Live!


Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan deze tutorial over GnuPG te bekijken, die uitlegt hoe je de integriteit en authenticiteit van je software kunt controleren voordat je het installeert. Dit is een belangrijke praktijk, vooral wanneer je Wallet beheersoftware zoals Liana of Sparrow installeert:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc