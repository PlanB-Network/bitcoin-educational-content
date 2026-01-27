---
name: Raspberry Pi Zero
description: Hvordan bygge en minimal, luftgapet og rimelig datamaskin ved hjelp av en Raspberry Pi Zero og et tilbehørssett.
---
![cover](assets/cover.webp)



Hvis du har vært på sidene til Plan ₿ Academy en stund, har du allerede lært at en av de mest anbefalte sikkerhetsinnstillingene, nesten et must, ** er forvaltning av midler ved offline lagring av dine private nøkler**.



Hvis du ikke har oppdaget det ennå, vil du i denne veiledningen finne lenker til ressurser med åpen kildekode som du kan bruke til å lære mer om det.



For å administrere private nøkler offline, trengs derfor en enhet som er permanent frakoblet nettverket, enten det er en [maskinvarelommebok](https://planb.academy/resources/glossary/hardware-wallet) eller en airgap-datamaskin, dedikert til denne spesifikke funksjonen.



Hvordan gjør du det hvis du for eksempel ikke har mulighet til å kjøpe maskinvare som kun utfører denne oppgaven, men du ikke ønsker å gi avkall på dette sikkerhetstrinnet?



## Løsningen


Hva om jeg fortalte deg at du kan lage en offline-enhet i form av en airgap-datamaskin som er på størrelse med og veier som en USB-minnepinne og koster 35 euro? Ville du ikke trodd på det?



Fortsett å lese.



Jeg skal fortelle deg mer: les hele veien gjennom. Den foreslåtte løsningen er billig, men det er ikke akkurat den enkleste. Først får du den generelle ideen, så bestemmer du deg for å investere litt av tiden din i litt personlig forskning og velge, med så mye ro i sjelen som mulig, om og hvordan du skal fortsette.



## Krav


**1** En [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (uten noe suffiks) er grunnlaget for å lage en datamaskin med minimal ytelse, men mangler fremfor alt Wi-Fi- og Bluetooth-kort, som er uunnværlige krav for formålet med denne øvelsen.





- **Kostnad**: ca. 15,00 i skrivende stund (august 2025).
- **Kontinuitet i produksjonen**: Bringebær garanterer produksjon frem til januar 2030.



PI Zero uten Wi-Fi og Bluetooth har dessverre blitt så godt som utilgjengelig. Det kan være lettere å finne alternativer til PI Zero W og PI Zero 2W. I dette tilfellet kan du deaktivere tilkoblingsfunksjonene ved å endre konfigurasjonsfilen. Etter at du har installert operativsystemet, må du legge til disse elementene i config:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



en del av denne guiden vil vise deg hvordan og hvor du gjør det. Men hvis du virkelig vil være sikker, kan du finne flere opplæringsprogrammer på nettet for å fjerne Wi-Fi-brikken med en liten kutter, den typen som passer for arbeid på elektroniske kort.



**2** Et _startersett_ for Raspberry PI Zero: som det er praksis for Raspberry-verdenen, bare bein, uten eksternt etui. I tillegg betinger de begrensede ressursene til et så lite brett mulighetene for forbindelse med omverdenen.



Da jeg bestemte meg for å gå videre, fant jeg [dette settet](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) fullt av tilbehør for å utnytte PI Zeros fulle potensial. Settet inneholder faktisk en USB A -> micro USB power Supply, en liten USB-hub, en mini-HDMI -> HDMI-adapter, en kjøleribbe i kobber og et ytterkabinett i aluminium. Settet inneholder også skruene og unbrakonøkkelen som trengs for å montere PI Zero i det nye kabinettet.





- **Kostnad**: 19.99 euro.



**3** Denne veiledningen krever ikke at du bruker store summer på airgap-datamaskinen. Du bør imidlertid vite at du trenger et USB-tastatur og en USB-mus (kun kablet, unngå Bluetooth) og en skjerm. Avhengig av inngangen til skjermen din, kan det hende du trenger en adapter fra mini-HDMI, den eneste utgangen som er tilgjengelig på PI Zero. Til slutt, se Hard for det faktum at vi alle har et ikke-trådløst tastatur og mus i huset et eller annet sted - det er på tide å Dust dem av.



## Ekstra budsjett



**4** Du kan få den originale kraften Supply fra Raspberry, som koster ca. 15,00 euro.



**5** Jeg personlig valgte å bruke strømmen Supply som følger med i _startpakken_, men kombinerte den imidlertid med en USBA → miniUSB såkalt `no data`-kabel, som koster 3,70 euro.



**6** Et micro SD-kort med minst 32 GB masselagring; hvis industriell kvalitet/nivå er bedre.



**7** Du trenger et system, en USB til micro SD-adapter, som den du ser på bildet. Operativsystemet og minnet til din PI Zero vil faktisk fungere på dette mediet.



![img](assets/it/06.webp)



## Installasjon av operativsystemet


Før du lukker PI Zero i kofferten, anbefaler jeg at du installerer operativsystemet. Da vil du kunne sjekke LED-lampen som indikerer drift, med en gang.



For å velge og brenne operativsystemet valgte jeg den enkleste måten: å bruke Raspberrys `PI Imager`-verktøy.



![img](assets/it/01.webp)



Gå deretter til [Raspberry Github](https://github.com/raspberrypi/rpi-imager/releases) for å laste ned den nyeste versjonen av Imager, og velg den som passer best til ditt operativsystem (v. 1.9.6 på tidspunktet for skrivingen). Du vil legge merke til at ved siden av hver ressurs finnes også hashen til den tilsvarende filen. Dette vil være nyttig for verifisering.



![img](assets/it/02.webp)



Jeg anbefaler at du verifiserer operativsystemet du skal bruke på airgap-datamaskinen din, for din egen personlige trygghet. Dette vil gi deg trygghet for at du bruker en legitim (ikke ondsinnet) versjon av Imager og følgelig Raspi OS.



Gjør verifiseringen umiddelbart etter nedlasting, med maskinen du vanligvis bruker, koblet til Internett



Deretter åpner du Linux-terminalen og forbereder nedlastingen, og oppretter en `raspios`-katalog som er nyttig for å jobbe med den.



![img](assets/it/19.webp)



Last ned Imager for din Linux-distribusjon med `wget`.



![img](assets/it/20.webp)



Til slutt kjører du kommandoen `sha256sum` og sammenligner Hash med den som Raspberry har lagt ut på Github.



![img](assets/it/21.webp)



Hvis du har Windows, kan du også åpne Power Shell og skrive inn følgende kommando:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Du vil få Hash som må samsvare med den som er publisert på Raspberry Github.



Når du har bekreftet nedlastingen, kan du installere Imager på din daglige datamaskin og åpne den. Imager er verktøyet du trenger for å brenne operativsystemet til micro SD-en, som vil være "systemdisken" til PI Zero.



Prosessen er ekstremt enkel: Velg først hvilken Raspberry-enhet du skal bruke (så vær oppmerksom på **din modell** av Raspi Zero), deretter OS-versjonen, og til slutt monteringspunktet for micro SD-kortet du vil flashe operativsystemet til.



### Første trinn



![img](assets/it/03.webp)



### Andre trinn



![img](assets/it/07.webp)



**Bemerk godt**: velg `PI OS 32-bit`, den eneste som fungerer med PI Zero.



### Tredje trinn



![img](assets/it/08.webp)



(Vær nøye med å la _Exclude System Drive_ være valgt for å unngå å bli bedt om å installere Raspis operativsystem på datamaskinen din)



Når alt er konfigurert, spør Imager deg om du vil bruke egendefinerte innstillinger. Velg det du ønsker, eller klikk på _Nei_ for å fortsette med standardalternativene.



![img](assets/it/09.webp)



Bekreft at du vil slette innholdet på micro SD-kortet



![img](assets/it/10.webp)



Imager begynner å blinke operativsystemet til micro SD-kortet, og en rullebjelke varsler deg om fremdriften.



![img](assets/it/11.webp)



På slutten er det automatisk bekreftelse, jeg anbefaler deg ikke å stoppe den.



![img](assets/it/12.webp)



Til slutt vises en melding på skjermen, og hvis alt var vellykket, ser det ut som det du leser på bildet.



![img](assets/it/13.webp)



Nå kan du virkelig fjerne micro SD-kortet fra leseren og sette det i sporet på PI Zero. Slå på den lille Raspberry og observer LED-en: vi forventer at den lyser grønt og blinker, noe som indikerer normal innlasting av operativsystemet, og deretter forblir kontinuerlig på. Hvis du ser andre indikasjoner, for eksempel hvis LED-en blinker regelmessig eller er rød, se FAQ eller [støtteforumsidene](https://forums.raspberrypi.com/).



## Første konfigurasjon


Den første oppstarten av Raspi OS er litt tregere enn vanlig fordi den må utføre en rekke faktiske installasjonsoppgaver. Men hvis alt har gått bra, vil du finne en velkomstskjerm.



![img](assets/it/14.webp)



Klikk på _Next_ for å angi den geografiske regionen, spesielt for å laste inn riktig tastatur. Vær spesielt oppmerksom på sistnevnte.



![img](assets/it/15.webp)



Klikk på _Neste_, så blir du bedt om å opprette en bruker, skrive ned legitimasjonen din og ta godt vare på den.



![img](assets/it/16.webp)



Veiviseren ber deg om å velge en standard nettleser, mellom Chromium og Firefox; den kan også spørre deg om Wi-Fi-nettverksinnstillinger hvis du arbeider med en Zero W eller 2W PI. Gå videre og klikk på _Skip_.



På et tidspunkt vil du bli bedt om å oppgradere den innebygde programvaren og operativsystemet. Velg _Skip_: I denne øvelsen bygger vi faktisk en frakoblet maskin, og den må forbli frakoblet fra og med nå.



Til slutt kan det hende at du blir bedt om å aktivere `ssh`, men avslå dette trinnet også, siden det er en Zero airgap IP.



![img](assets/it/17.webp)



Det er ikke så mye mer å konfigurere. Når du er ferdig, starter du Raspberry på nytt for at endringene skal tre i kraft.



![img](assets/it/18.webp)



## En ny luftspalte for datamaskiner


Etter omstart er den nye airgap-datamaskinen din klar. PI Zero viser deg det nye skrivebordet, som du kan arbeide med enten via GUI eller fra kommandolinjen.



![img](assets/it/22.webp)



### Første skritt for PI Zero W eller 2W


Hvis du jobber med en Raspberry PI Zero W- eller 2W-serie, har kortet ditt brikker for Wi-Fi og Bluetooth om bord. Under det første oppsettet hoppet du over tilkoblingskonfigurasjonen, slik at PI Zero ikke er koblet til Internett. Nå kan du deaktivere de to brikkene permanent via programvare.



Raspi OS inneholder faktisk en `config.txt`-fil som du kan redigere etter eget ønske. `config` ligger på `boot`-partisjonen, i `firmware`-katalogen, og du kan redigere og lagre den med `root`-rettigheter.



Åpne terminalen fra ikonet øverst til venstre, og den blir `root`.(1)



![img](assets/it/23.webp)



(1) Hvis Raspi OS ikke har fått deg til å opprette `root`-passordet under de foregående trinnene, anbefaler jeg at du gjør det nå, med kommandoen `passwd`. Å ha `root`-brukeren uavhengig av din personlige bruker kan vise seg å være veldig praktisk i gjenopprettingssituasjoner.



Se etter filen `config.txt` i terminalen, og vær forberedt på å redigere den med redigeringsprogrammet `nano`.



![img](assets/it/24.webp)



Redigeringen skal gjøres nederst i hele `config`, etter ordene `[All]`. Det er på dette punktet du skal legge til `dtoverlay`-kommandoene som ble vist i begynnelsen av veiledningen.



![img](assets/it/25.webp)



Lagre, lukk og start på nytt. I det følgende trinnet vil vi gå til utforskningen av den lille Raspberry.



## Hva kan du forvente av denne enheten?


Ifølge [tekniske spesifikasjoner](https://www.raspberrypi.com/products/raspberry-pi-zero/) på Raspberry-nettstedet har PI Zero en BCM2835-prosessor med én kjerne og 512 MB RAM, og fremstår derfor ikke som spesielt kraftig.



Siden terminalen er lettere, vil vi bruke kommandolinjen til å utforske systemkonfigurasjoner.



Når du slår på strømmen, ser du en kort regnbuefarget skjerm, etterfulgt av en velkomstmelding fra Raspberry og, i nedre venstre hjørne, kernel-meldinger relatert til oppstart.



Når PI OS-skrivebordet vises, åpner du terminalen og skriver inn:



```bash
uname -a
```


Denne kommandoen viser deg kjerneversjonen som for øyeblikket er i bruk på skjermen, samt annen informasjon.



![img](assets/it/26.webp)



Du kan også se informasjon om CPU og maskinvare ved å skrive inn :



```bash
lscpu
```



![img](assets/it/27.webp)



Se også `proc/mem/info`.



![img](assets/it/28.webp)



For å finne ut hvilken versjon av Debian og kodenavnet for utgivelsen:



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



## Bruk


Selv om ytelsen virker begrenset (på papiret og sammenlignet med kraften i dagens maskiner), er PI Zero ytelsessterk, spesielt som terminal.





- Først kan du gå til hovedmenyene og la deg inspirere av _Add/Remove software_-panelet, der du finner en rekke verktøy du kan programmere og øve deg på. Husk at du også kan gjøre dette fra terminalen, men alltid med `root`-rettigheter.



![img](assets/it/33.webp)





- Du kan "adoptere" denne frakoblede enheten for å lagre en rekke konfidensielle dokumenter, som vil være tilgjengelige når du trenger dem, uten å bli eksponert for Internett.
- Du kan bruke denne konfigurasjonen til å sikre GPG-nøklene dine med generate.
- Du kan til og med bruke denne nye "leken" som en airgap-signaturenhet, [ved å følge rådene fra Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Blant lommebøkene som jeg er kjent med, er Electrum den eneste som tilbyr en 32-biters utgivelse. Vel: Zero IP som vi forberedte den i denne opplæringen, vil tillate deg å holde de private nøklene offline oppsettet for Wallet luftgap som vi dekket i denne opplæringen:



https://planb.academy/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Konklusjoner


Oppsettet har sannsynligvis én stor svakhet: micro SD er et medium som kan gi problemer. Det er sårbart for tung bruk; kanskje har du allerede erfaring med dette, fra å bruke det med telefonen din. Etter at du har installert all programvaren du ønsker å bruke på Zero airgap IP, bør du ta en god sikkerhetskopi av den dyrebare micro SD-en ved hjelp av Raspi OS-verktøyet du har tilgjengelig.



![img](assets/it/34.webp)



Etter hvert som behovene dine vokser, og med dem budsjettmulighetene dine, kan du utforske andre Raspberry- eller lignende løsninger. Når vi snakker om minne, tilbyr for eksempel PI 5 muligheten til å montere en M2 NVME-stasjon, som absolutt er mer robust enn microSD.



Ikke glem å ta notater og dokumentere hvert trinn i installasjonen av verktøyprogramvare som du skal bruke offline. **Før eller siden kommer det en oppdatering av Raspi OS** som du garantert vil ønske å dra nytte av. På det tidspunktet må du slette alt og gjøre alt på nytt (kanskje med en ny micro SD 😂).



Øvelsen vi nettopp gjorde, forutsatt at det også er ditt første eksperiment, vil du huske lenge. Det er ikke alltid mulig å bruke maskinvare til "innebygde" operasjoner offline, uten å forsømme oppmerksomheten til en luftgapet maskin for å slå på og sjekke fra tid til annen.



Men du fikk det til, gratulerer! Og du vil kunne foreslå denne løsningen til alle dem som trenger å holde budsjettene nede.