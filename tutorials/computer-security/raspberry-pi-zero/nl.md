---
name: Raspberry Pi Zero
description: Hoe een minimale, geïsoleerde en goedkope computer te bouwen met een Raspberry Pi Zero en een accessoirekit.
---
![cover](assets/cover.webp)



Als je al een tijdje op de pagina's van Plan ₿ Network bent, heb je al geleerd dat een van de meest bepleite beveiligingsinstellingen, bijna een must, **het beheer van fondsen door offline opslag van je privésleutels** is.



Als je het nog niet ontdekt hebt, vind je in deze tutorial links naar open source bronnen om er meer over te leren.



Om privésleutels offline te beheren, is er dus een apparaat nodig dat permanent is losgekoppeld van het netwerk, of het nu een [hardware wallet](https://planb.network/resources/glossary/hardware-wallet) is of een airgap-computer die aan deze specifieke functie is gewijd.



Hoe doe je dat als je bijvoorbeeld niet de mogelijkheid hebt om hardware aan te schaffen die alleen deze taak uitvoert, maar je deze beveiligingsstap niet wilt opgeven?



## De oplossing


Wat als ik je zou vertellen dat je een offline apparaat kunt maken in de vorm van een airgap-computer die net zo groot en zwaar is als een USB-stick en 35 euro kost? Zou je het niet geloven?



Lees verder.



Ik zal je meer vertellen: lees helemaal door. De voorgestelde oplossing is goedkoop, maar niet bepaald de gemakkelijkste. Eerst krijg je het algemene idee, dan besluit je wat van je tijd te investeren in persoonlijk onderzoek en kies je, met zoveel mogelijk gemoedsrust, of en hoe je verder gaat.



## Vereisten


**1** Een [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): de PI Zero (zonder enig achtervoegsel) is de basis voor het bouwen van een computer met minimale prestaties, maar mist bovenal Wi-Fi- en Bluetooth-kaarten, vereisten die essentieel zijn voor het doel van deze oefening.





- **Kosten**: ongeveer 15,00 op het moment van schrijven van deze tutorial (augustus 2025).
- **Continuïteit van de productie**: Raspberry garandeert productie tot januari 2030.



PI Zero zonder Wi-Fi en Bluetooth zijn helaas vrijwel niet meer verkrijgbaar. Mogelijk kun je gemakkelijker alternatieven vinden voor de PI Zero W en PI Zero 2W. In dit geval kun je de verbindingsfuncties uitschakelen door het configuratiebestand te wijzigen. Na de installatie van het besturingssysteem moet je deze items toevoegen aan de configuratie:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



een deel van deze handleiding laat je zien hoe en waar je dat moet doen. Als je het echter echt zeker wilt weten, kun je op internet verschillende tutorials vinden voor het verwijderen van de Wi-Fi-chip met een klein mesje, het soort dat geschikt is voor het werken aan elektronische printplaten.



**2** Een _starterkit_ voor Raspberry PI Zero: zoals gebruikelijk voor de Raspberry-wereld, kaal, zonder externe behuizing. Bovendien beperken de beperkte middelen van zo'n klein bordje de mogelijkheden voor verbinding met de buitenwereld.



Toen ik besloot om verder te gaan, vond ik [deze kit](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) vol accessoires, om het volledige potentieel van de PI Zero te benutten. De kit bevat namelijk een USB A -> micro USB voeding Supply, een kleine USB hub, een mini-HDMI -> HDMI adapter, een koperen koellichaam en een aluminium behuizing. De kit bevat ook de schroeven en inbussleutel die nodig zijn om de PI Zero in de nieuwe behuizing te plaatsen.





- **Kosten**: 19.99 euro.



**3** Voor deze tutorial hoef je geen grote budgetten uit te geven aan de airgap-computer. Je moet echter wel weten dat je een USB-toetsenbord en muis nodig hebt (uitsluitend bedraad, vermijd Bluetooth) en een monitor. Afhankelijk van de ingang van je monitor, heb je misschien een adapter nodig van mini-HDMI, de enige uitgang die beschikbaar is op de PI Zero. Tot slot, kijk Hard voor het feit dat we allemaal wel ergens een niet-draadloos toetsenbord en muis in huis hebben-het is tijd om ze Dust uit te schakelen.



## Extra budget



**4** Je kunt de originele Supply van Raspberry krijgen, die ongeveer 15,00 euro kost.



**5** Ik heb er zelf voor gekozen om de voeding Supply te gebruiken die in de _starter kit_ zit, echter gecombineerd met een USBA → miniUSB zogenaamde `no data` kabel, die 3,70 euro kost.



**6** Een micro SD-kaart, minimaal 32 GB massaopslag; als industriële kwaliteit/niveau beter is.



**7** Je hebt een systeem nodig, een USB naar micro SD adapter, zoals degene die je op de foto ziet. Het besturingssysteem en het geheugen van je PI Zero zullen wel werken op die media.



![img](assets/it/06.webp)



## Installatie van het besturingssysteem


Voor je de PI Zero in de koffer stopt, raad ik je aan om het besturingssysteem te installeren. Je kunt dan meteen de LED controleren die de werking aangeeft.



Om het besturingssysteem te kiezen en te branden koos ik voor de makkelijkste manier: met Raspberry`s `PI Imager` tool.



![img](assets/it/01.webp)



Ga vervolgens naar de [Raspberry Github](https://github.com/raspberrypi/rpi-imager/releases) om de nieuwste release van de Imager te downloaden, en kies degene die het meest geschikt is voor jouw besturingssysteem (v. 1.9.6 ten tijde van schrijven). Je zult merken dat naast elk bestand ook de hash van het betreffende bestand staat. Dit zal nuttig zijn voor de verificatie.



![img](assets/it/02.webp)



Ik raad je aan om voor je eigen gemoedsrust het besturingssysteem dat je op je airgapcomputer gaat gebruiken te verifiëren. Dit geeft je het vertrouwen dat je werkt met een legitieme (geen kwaadaardige) versie van de Imager en dus ook van het Raspi OS.



Voer de verificatie direct na het downloaden uit, met uw machine die u normaal gebruikt verbonden met het internet



Open dan de Linux terminal en bereid de download voor door een `raspios` directory aan te maken die handig is om mee te werken.



![img](assets/it/19.webp)



Download de Imager voor jouw Linux-distributie met `wget`.



![img](assets/it/20.webp)



Voer tenslotte het `sha256sum` commando uit en vergelijk de Hash met degene die door Raspberry op zijn Github is geleverd.



![img](assets/it/21.webp)



Of, als je Windows hebt, open de Power Shell en typ het volgende commando:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Je krijgt de Hash die moet overeenkomen met de Hash die op Raspberry Github staat.



Zodra je de download hebt geverifieerd, kun je Imager op je dagelijkse computer installeren en openen. Imager is de tool die je nodig hebt om het besturingssysteem op de micro SD te branden, wat de "systeemschijf" van PI Zero wordt.



Het proces is uiterst eenvoudig: kies eerst het Raspberry-apparaat dat je gaat gebruiken (let dus op **jouw model** van Raspi Zero), dan de OS-versie en tot slot het koppelpunt van de micro SD-kaart waar je het OS naartoe wilt flashen.



### Eerste stap



![img](assets/it/03.webp)



### Tweede stap



![img](assets/it/07.webp)



**Let op**: kies `PI OS 32-bit`, de enige die werkt met PI Zero.



### Derde stap



![img](assets/it/08.webp)



(Zorg ervoor dat u _Exclude System Drive_ geselecteerd laat om te voorkomen dat u gevraagd wordt om het besturingssysteem van Raspi op uw computer te installeren)



Wanneer alles is ingesteld, vraagt de Imager of je aangepaste instellingen wilt gebruiken. Kies wat u wilt of klik op _No_ om door te gaan met de standaardopties.



![img](assets/it/09.webp)



Bevestig dat u de inhoud van de micro SD wilt verwijderen



![img](assets/it/10.webp)



De Imager begint met het flashen van het besturingssysteem naar de micro SD, een schuifbalk geeft de voortgang aan.



![img](assets/it/11.webp)



Aan het einde is er automatische verificatie, ik raad je aan dit niet te stoppen.



![img](assets/it/12.webp)



Uiteindelijk verschijnt er een bericht op het scherm en als alles goed is gegaan, ziet het eruit zoals je op de afbeelding kunt lezen.



![img](assets/it/13.webp)



Je kunt nu daadwerkelijk de microSD-kaart uit de lezer verwijderen en in de sleuf van de PI Zero plaatsen. Zet de kleine Raspberry aan en observeer de LED: we verwachten dat deze groen is en knippert, wat wijst op het normale laden van het besturingssysteem, en daarna continu blijft branden. Als je andere signalen ziet, bijvoorbeeld als de LED regelmatig knippert of rood is, raadpleeg dan de FAQ of [de ondersteuningsforumpagina's](https://forums.raspberrypi.com/).



## Eerste configuratie


De eerste keer dat Raspi OS opstart is iets langzamer dan normaal omdat het een aantal installatietaken moet uitvoeren. Maar als alles goed is gegaan, vind je een welkomstscherm.



![img](assets/it/14.webp)



Klik op _Next_ om de geografische regio in te stellen, vooral voor het laden van het juiste toetsenbord. Let vooral op dit laatste.



![img](assets/it/15.webp)



Klik op _Next_ en je wordt gevraagd om je gebruiker aan te maken, noteer je gegevens en bewaar ze goed.



![img](assets/it/16.webp)



De wizard vraagt je om een standaard webbrowser te kiezen, tussen Chromium en Firefox; het kan je ook vragen naar Wi-Fi-netwerkinstellingen als je werkt met een Zero W of 2 W PI. Ga je gang en klik op _Skip_.



Op een bepaald moment zal je gevraagd worden om de software en het besturingssysteem aan boord te upgraden. Kies _Skip_: voor deze oefening bouwen we in feite een offline machine, die vanaf nu offline moet blijven.



Tenslotte kan het je vragen om `ssh` in te schakelen, maar weiger ook deze stap aangezien het een Zero airgap IP is.



![img](assets/it/17.webp)



Er is niet veel meer te configureren. Start de Raspberry opnieuw op als je klaar bent, zodat de wijzigingen van kracht worden.



![img](assets/it/18.webp)



## Een nieuw computer luchtgat


Na het herstarten is je nieuwe airgap computer klaar. PI Zero toont je het nieuwe bureaublad, waarmee je kunt werken via GUI of vanaf de opdrachtregel.



![img](assets/it/22.webp)



### Eerste stappen voor PI Nul W of 2W


Als je werkt met een Raspberry PI Zero W of 2W series, dan heeft je board chips voor Wi-Fi en Bluetooth aan boord. Tijdens de eerste setup heb je de verbindingsconfiguratie overgeslagen, waardoor de PI Zero niet verbonden is met het internet. Nu kun je de twee chips permanent uitschakelen via software.



In feite levert Raspi OS een `config.txt` bestand dat je naar wens kunt bewerken. Het `config` staat op de `boot` partitie, in de `firmware` directory, en je kunt het bewerken en opslaan met `root` privileges.



Open de terminal vanaf het pictogram linksboven en het wordt `root`.(1)



![img](assets/it/23.webp)



(1) Als Raspi OS je niet het `root` wachtwoord liet aanmaken tijdens de vorige stappen, dan raad ik je aan om dat nu te doen, met het `passwd` commando. De `root` gebruiker onafhankelijk laten bewegen van je persoonlijke gebruiker kan erg handig zijn in herstelsituaties.



Controleer met de terminal het `config.txt` bestand en wees voorbereid om het te bewerken met de `nano` editor.



![img](assets/it/24.webp)



Het bewerken moet onderaan de hele `config` gebeuren, na de woorden `[All]`. Op dit punt voeg je de `dtoverlay` commando's toe die je aan het begin van de tutorial ziet.



![img](assets/it/25.webp)



Opslaan, afsluiten en opnieuw opstarten. In de volgende stap gaan we de kleine Raspberry verkennen.



## Wat kun je van dit apparaat verwachten?


Volgens de [technische specificaties](https://www.raspberrypi.com/products/raspberry-pi-zero/) op de Raspberry-website heeft de PI Zero een enkelvoudige BCM2835-processor en 512 MB RAM, en lijkt daardoor niet erg krachtig.



Aangezien de terminal lichter is, zullen we de opdrachtregel gebruiken om systeemconfiguraties te verkennen.



Bij het opstarten zie je een kort regenboogkleurig scherm, gevolgd door een welkomstbericht van Raspberry en, linksonder, kernelberichten met betrekking tot het opstarten.



Wanneer het bureaublad van PI OS verschijnt, open dan de terminal en typ:



```bash
uname -a
```


Dit commando toont je de kernelversie die momenteel in gebruik is op het scherm, plus andere informatie.



![img](assets/it/26.webp)



Je kunt ook informatie over CPU en hardware bekijken door te typen:



```bash
lscpu
```



![img](assets/it/27.webp)



En zie ook `proc/mem/info`.



![img](assets/it/28.webp)



Om de versie van Debian en de codenaam van de release te achterhalen:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Gebruik


Hoewel de prestaties beperkt lijken (op papier en vergeleken met de kracht van hedendaagse machines) is de PI Zero performant, vooral als terminal.





- Eerst kun je naar de hoofdmenu's gaan en je laten inspireren door het paneel _Add/Remove software_, waar je een aantal hulpprogramma's vindt om te programmeren en te oefenen. Onthoud dat je dit ook vanaf de terminal kunt doen, maar altijd met `root` privileges.



![img](assets/it/33.webp)





- Je kunt dit offline apparaat "adopteren" om verschillende vertrouwelijke documenten op te slaan, die toegankelijk blijven wanneer nodig, zonder ooit te worden blootgesteld aan het internet.
- U kunt deze configuratie gebruiken om uw GPG-sleutels veilig generate te maken.
- Je zou dit nieuwe "speeltje" zelfs kunnen gebruiken als een airgap-handtekeningapparaat, [door het advies van Arman The Parman te volgen](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Van de Wallets die ik ken, is Electrum de enige die een 32-bits release biedt. Welnu: met de Zero IP zoals we die in deze tutorial hebben voorbereid, zou je de private keys offline kunnen houden met de instelling voor Wallet airgap die we in deze tutorial hebben behandeld:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Conclusies


De opstelling heeft waarschijnlijk één grote zwakte: de micro SD is een medium dat problemen kan geven. Het is kwetsbaar voor intensief gebruik; misschien heb je hier al ervaring mee, door het te gebruiken met je telefoon. Na het installeren van alle software die je wilt gebruiken op de Zero airgap IP, maak je een goede back-up van de kostbare micro SD, met behulp van de Raspi OS tool die je tot je beschikking hebt.



![img](assets/it/34.webp)



Als je behoeften groeien, en daarmee je budgetmogelijkheden, kun je andere Raspberry of vergelijkbare oplossingen verkennen. Over geheugen gesproken, de PI 5 biedt bijvoorbeeld de mogelijkheid om een M2 NVME-schijf te monteren, die zeker robuuster is dan microSD.



Vergeet niet om notities te maken en elke stap van de installatie van de hulpprogramma's die je offline gaat gebruiken te documenteren. **Vroeg of laat komt er een geüpdatet Raspi OS** uit waar je zeker je voordeel mee wilt doen. Op dat moment moet je alles verwijderen en opnieuw doen (misschien met een nieuwe micro SD 😂).



De oefening die we zojuist hebben gedaan, ervan uitgaande dat het ook je eerste experiment is, zul je je nog lang herinneren. Het is niet altijd mogelijk om hardware offline aan `embedded` operaties te wijden, zonder de aandacht te verwaarlozen om een airgapped machine van tijd tot tijd aan te zetten en te controleren.



Maar je hebt het voor elkaar gekregen, gefeliciteerd! En je zult deze oplossing kunnen voorstellen aan iedereen die zijn budget laag moet houden.