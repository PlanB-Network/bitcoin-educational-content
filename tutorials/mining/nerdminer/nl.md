---
name: Nerdminer
description: Mining Bitcoin beginnen met een winkans van bijna 0
---

![cover](assets/cover.webp)

## Configuratie van uw NerdMiner v2


In deze tutorial leiden we je door de noodzakelijke stappen om een NerdMiner_v2 op te zetten, een hardware apparaat (een ESP-32 S3) speciaal voor Bitcoin Mining.

Het is duidelijk dat de rekenkracht van een dergelijk apparaat niet kan concurreren met de ASIC's van amateur of professionele mijnwerkers. Toch is de NerdMiner een perfect educatief hulpmiddel om Bitcoin Mining tastbaar te maken. En wie weet, met (veel) geluk, vind je een blok en de beloning die daarbij hoort. Voor de nieuwsgierigen, we zullen het zien in de [Schatting van de winkans](#schatting-de-la-probabilite-de-winst) sectie. Qua stroomverbruik verbruikt een NerdMiner 0,5W; ter vergelijking, een LED-lamp verbruikt gemiddeld 20 keer meer.


Voordat we de verschillende stappen doorlopen, zetten we eerst de benodigdheden op een rijtje:



- a [Lilygo T-display S3] (https://lilygo.cc/products/t-display-s3)
- a [USB-C voeding Supply] (https://amzn.eu/d/gIOot90)
- een 3D-koffer: als je een 3D-printer hebt, kun je het [3D-bestand] downloaden (https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) en anders kun je er een kopen in de [Silexperience online winkel] (https://silexperience.company.site/NerdMiner_V2-p544379757).
- een pc met geïnstalleerde Chrome-browser
- een internetverbinding
- a Bitcoin Address


Je kunt ook een voorgemonteerde NerdMiner kit kopen bij verschillende wederverkopers, zoals:



- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)


Eerst zullen we zien hoe we de software op de ESP-32 S3 kunnen flashen en daarna hoe we het kunnen herstarten om het wifi-netwerk te veranderen. Deze stappen zijn voor Windows gebruikers, als u een Linux OS gebruikt, voer dan de [voorbereidende stappen] uit (#etapes-preliminaires-pour-utilisateurs-linux) om de ESP-32 S3 te laten herkennen door uw systeem.


De **Installatie van NerdMiner_v2 Software** is sterk vereenvoudigd dankzij het gebruik van de webflasher.


## Stap 1: Voorbereiding van de Webflasher


Eerst moet je naar de [online NM2 flasher] (https://bitmaker-hub.github.io/diyflasher/) gaan.


Selecteer vervolgens de firmware die overeenkomt met je ESP-32. Meestal is dit de standaard firmware: T-Display S3. Klik dan op "Flash".


**Note⚠️ :** Het is belangrijk dat je de Chrome-browser gebruikt, omdat deze standaard het gebruik van flash en toegang tot je USB-poorten toestaat.


![image](assets/webflasher.webp)


## Stap 2: De ESP-32 aansluiten


Zodra de webflasher is gestart, wordt een pop-upvenster geopend met de verschillende USB-poorten die door de browser worden herkend.

Je kunt dan je ESP-32 aansluiten en er wordt een nieuwe poort weergegeven (in dit geval is het de ttyACM0 poort). Selecteer deze en klik op "connect".


![image](assets/flasher-port-serial.webp)


De software wordt dan binnen enkele seconden naar je ESP32 gedownload.


![image](assets/NM2-sucessfully-installed.webp)


## Stap 3: NerdMiner configuratie


De configuratie van je NerdMiner gebeurt via een smartphone of een computer.

Schakel WiFi in en maak verbinding met het lokale NerdMinerAP netwerk. Als je een smartphone gebruikt, wordt de configuratieportal automatisch geopend. Typ anders Address 192.168.4.1 in een browser.

Selecteer vervolgens "WiFi configureren".


Je kunt nu je NerdMiner configureren.

Maak eerst verbinding met je WiFi-netwerk door je netwerknaam te selecteren en het bijbehorende wachtwoord in te voeren.


Dan kun je kiezen aan welke Mining pool je wilt deelnemen. Het is inderdaad gebruikelijk in de Bitcoin Mining industrie om rekenkracht te bundelen om de kans te vergroten een blok te vinden in Exchange om de beloning evenredig te delen met de verstrekte Hashrate.

Voor NerdMiners kun je kiezen om verbinding te maken met een van deze pools:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

Als je je pool hebt gekozen, moet je je Bitcoin Address invoeren om de beloning te ontvangen als er (uitzonderlijk) een blok wordt gevonden.


Kies ook je tijdzone zodat de NerdMiner de tijd correct kan weergeven.

Je kunt nu op "opslaan" klikken.


![image](assets/wifi-configuration.webp)


Gefeliciteerd, je maakt nu deel uit van het Bitcoin Mining netwerk!


## NerdMiner werking


De NerdMinerv2 software heeft 3 verschillende schermen, die je kunt openen door op de bovenste knop aan de rechterkant van je scherm te klikken:



- Het hoofdscherm geeft toegang tot de statistieken van je NerdMiner.
- Het tweede scherm geeft toegang tot de tijd, je Hashrate, de prijs van Bitcoin en de blokhoogte.
- Het derde scherm geeft toegang tot statistieken over het wereldwijde Bitcoin Mining netwerk.

![image](assets/NM2-screens.webp)


Als je je NerdMiner opnieuw wilt opstarten, bijvoorbeeld om het WiFi-netwerk te veranderen, moet je 5 seconden op de bovenste knop drukken.


Eenmaal op de onderste knop drukken schakelt je NerdMiner uit. Twee keer klikken zal de schermoriëntatie draaien.


### Inleidende stappen voor Linux-gebruikers


Hier zijn de stappen voor Chrome om je seriële poort op Linux te detecteren.


1. Identificeer de bijbehorende poort:



- Sluit uw ESP-32 aan op uw computer.
- Open een terminal.
- Voer het volgende commando in om alle poorten op te sommen:
  - `dmesg | grep tty`
  - of `ls /dev/tty*`
- Om zeker te zijn van de poort, kan het commando worden herhaald zonder dat de ESP-32 is aangesloten.


2. Wijzig de toestemming van de geassocieerde poort:



- Standaard kan toegang tot seriële poorten rootrechten vereisen, dus zullen we ze beschikbaar maken door uw gebruiker toe te voegen aan de `dialout` groep.
  - `sudo usermod -a -G dialout YOUR_USERNAME`, vervang `YOUR_USERNAME` door je gebruikersnaam.
  - log dan uit en log weer in als deze gebruiker, of herstart het systeem om ervoor te zorgen dat de groepswijzigingen van kracht worden.


Nu uw ESP-32 wordt herkend door uw systeem, kunt u teruggaan naar de [eerste stap](#etape-1-preparation-du-webflasher) voor de software-installatie.


## Conclusie


En daar heb je het! Je NerdMiner_v2 is nu geconfigureerd en klaar voor gebruik.


Happy Mining en moge het geluk aan je zijde zijn!


### De winkans schatten


Laten we eens een leuke schatting maken van de kans om een Block reward te winnen. Deze schatting zal grof zijn en is alleen bedoeld om de orde van grootte van de waarschijnlijkheid te bepalen.

De pool waarmee een NerdMiner verbinding kan maken is alleen "solo Mining pool", wat betekent dat de pool de Hashrate van alle verbonden miners niet onderling verdeelt, maar alleen als coördinator optreedt.

Laten we nu aannemen dat onze NerdMiner een Hashrate heeft van ongeveer 45kH/s.


Wetende dat de totale Hashrate ongeveer 450 EH/s is (of 4,5 x 10^20 hashes per seconde), kunnen we stellen dat de kans op het vinden van het volgende blok 1 op 100 miljoen miljarden is, wat heel erg onwaarschijnlijk is. Dus naast een educatief hulpmiddel en een object van nieuwsgierigheid, kan een NerdMiner dienen als een lot uit de loterij in Bitcoin Mining tegen marginale elektrische kosten van 0,5 W - hoewel zoals we net zagen de waarschijnlijkheid om te winnen belachelijk laag is. Maar waarom zou je je geluk niet op de proef stellen?


### Aanvullende informatie


Hier zijn enkele links als je meer wilt lezen over het onderwerp:



- [NerdMiner_v2 projectpagina](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Volledige documentatie van NerdMiners](https://docs.bitwater.ch/nerd-Miner-v2/)