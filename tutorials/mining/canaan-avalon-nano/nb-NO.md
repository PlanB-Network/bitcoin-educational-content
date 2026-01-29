---
name: Canaan Avalon Nano 3S
description: Konfigurere ASIC Avalon for solomining eller Miner-sammenslåing
---

![cover](assets/cover.webp)



I denne veiledningen tar vi en titt på hvordan du setter opp Canaan Avalon Nano 3S, for enkel hjemmebruk av Miner.



Frem til nå har ASIC-maskiner (*Application Specific Integrated Circuit*) som er spesielt utviklet for å utføre en gitt oppgave - i dette tilfellet Hash-beregning (SHA-256) for Miner av Bitcoin - vært spesielt uegnet for hjemmebruk. Støy, varmeutvikling og behovet for å tilpasse det elektriske anlegget til den enorme kraften i disse maskinene har hindret de fleste av oss i å delta.



I dag har Canaan, en av de ledende produsentene av ASIC-maskiner, bestemt seg for å gå løs på markedet for privatpersoner som ønsker Miner hjemme, ved å tilby en rekke produkter som er relativt stillegående og svært enkle å installere (plug & play).



Disse enhetene markedsføres enten som en tilleggsvarmer, som **Avalon Nano 3S (140W)**, eller som en miniradiator med en effekt på **800W**, som **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Vær oppmerksom på at prisforskjellen i forhold til tradisjonelle ovner med tilsvarende effekt i de aller fleste tilfeller ikke gir deg mulighet til å tjene penger. Satoshiene som genereres av Minings aktivitet vil aldri kompensere for denne prisforskjellen, med mindre du har tilgang til gratis (overskudd) eller svært billig strøm.



Etter min mening bør disse enhetene sees mer som en enkel måte å Miner hjemme for de som ønsker å gjøre det av personlige grunner: *få ikke-KYC Satss / spille "lotteriet" ved å solominere / delta i Hashrate desentralisering etc..*. mens du drar nytte ** som en bonus ** fra varmen som genereres for å varme opp rommet ditt om vinteren. Men ikke som en måte å spare penger på i de fleste tilfeller i det minste (vestlige land).



## Unboxing og funksjoner



La oss først se hva som er inni Avalon Nano 3S-esken.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Når du har åpnet esken, finner du en papphylse som inneholder en WIFI-mottaker som du, som vi skal se senere, må plugge inn i USB-porten på enheten for å koble den til det lokale nettverket ditt. Bruksanvisningen er også inkludert, samt en metallpinne for å tilbakestille enheten til fabrikkinnstillingene om nødvendig.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Når alt er tatt ut av esken, er det følgende som følger med: selve maskinen, selvfølgelig, brukerhåndboken, WIFI-mottakeren, den nevnte metallspissen og enhetens strømadapter Supply. Kredittkortet som følger med, er etter vår mening ikke verdt å nevne.



![image](assets/fr/05.webp)



Nedenfor er en tabell som oppsummerer de generelle tekniske spesifikasjonene til Nano 3S :




| Karakteristikk                                      | Verdi                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Hash-rate                                      | 6 Th/s +- 5%                                            |
| Strømforbruk                               | 140 W                                                   |
| Støy                                                | 30 - 40 dB                                              |
| Område for utgangslufttemperatur                 | 60-70°C (ved omgivelsetemperatur 25°C)                |
| Omgivelsetemperaturkrav for bruk | -5 til 30°C                                            |
| Enhetens inngangsspennningsområde                         | 28V 5A kontinuerlig                                          |
| Adapterens inngangsspennningsområde                       | 110-240V AC 50/60Hz                                     |
| Enhetsstørrelse                                 | Lengde: 205 mm / Bredde: 115 mm / Høyde: 58.5 mm |
| Enhetsvekt                                  | 0.86 kg                                                 |

## Slå på strømmen og koble til det lokale nettverket



Når du har pakket ut Avalon Nano 3 S, plasserer du den om mulig i et relativt åpent område slik at varmen kan sirkulere. Begynn deretter med å sette inn den lille WIFI-mottakermodulen som vist nedenfor:



![image](assets/fr/06.webp)


Koble deretter USB-C-kontakten til Supply til USB-C-porten på enheten for å gi den strøm.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Enheten starter opp, og Avalon Nano-logoen vises på skjermen, etterfulgt av en "mobiltelefon"-logo med ordene "Please Configure the Network With Avalon Family App".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Dette gjør du ved å gå til mobilapplikasjonsbutikken din, søke etter og laste ned **Avalon Family**-applikasjonen.



![image](assets/fr/11.webp)


Når du har installert programmet, åpner du det ved å klikke på "Hopp over" øverst i høyre hjørne, deretter på "Legg til"-knappen og til slutt på "Søk". Sørg for at du har Bluetooth aktivert på smarttelefonen din, slik at deteksjonen av enheten går greit.



![image](assets/fr/12.webp)


Når enheten har blitt oppdaget av programmet, klikker du på den og velger "Koble til". Du kommer da til et skjermbilde der du kan oppgi informasjon om WIFI-tilkoblingen din.


![image](assets/fr/13.webp)


Når enheten er koblet til det lokale nettverket, vil skjermen se slik ut



![image](assets/fr/14.webp)



Den viser en "fiktiv" Hashrate, siden det ennå ikke er konfigurert noen pool, og enhetens klokkeslett, dato, strøm og IP Address - veldig nyttig hvis du vil ha tilgang til enhetens Interface via en PC og nettleser (mer om dette senere).



![image](assets/fr/15.webp)




## Koble til en Mining pool



**Denne delen er felles for Nano 3s og Mini 3, ettersom prosessene er helt identiske**.



Enten vi ønsker å "solominere" eller Miner-"pool", må vi koble oss til en Mining pool. Enheten vår er faktisk ikke noe annet enn en Hash-maker uten kjennskap til Bitcoin-nettverket. Ved å koble den til en pool får den tilgang til Bitcoin-nettverket, og kan motta blokkmaler som den kan jobbe med.



### Bruke applikasjonen til å koble til en Mining pool



I Avalon Family-applikasjonen velger du enheten som vist nedenfor. Du blir automatisk bedt om å endre maskinens administratorpassord. Klikk på "OK" hvis du ønsker å gjøre dette, eller på "Avbryt" for å beholde standardpassordet "admin".


![image](assets/fr/16.webp)


Velg deretter "Settings" og deretter "Pool Config", og angi parametrene for de tre ønskede bassengene.


Basseng nr. 2 og 3 fungerer som sikkerhetskopier hvis ett av dem skulle svikte, slik at Miner ikke fungerer til ingen nytte. Som standard vil Hashrate pekes til basseng #1



I vårt tilfelle velger vi:




- 1 - Offentlig basseng,
- 2 - CkPool,
- 3 - Havet.



![image](assets/fr/17.webp)



Hvis du vil ha mer informasjon om hvordan du kobler til en Mining pool, kan du se disse veiledningene :



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

For å oppsummere trenger vi





- bassenget Address, vanligvis **stratum+tcp://xxxxxxxx:port**.





- navnet på "arbeideren" som består av *din Bitcoin Address* og *pseudo* du velger for enheten din, de to atskilt med en *prik*, for eksempel:**bc1qxxxxxxxxxxxxxxxxxxx.MonAvalonNano3S**





- passordet, som vanligvis alltid er "**x**"



Når bassenginformasjonen er lagt inn, klikker du på "Lagre".



![image](assets/fr/18.webp)


Start enheten på nytt som anvist, og vent noen minutter til Hashrate er rettet mot det foretrukne bassenget (#1).



### Bruke nettleseren til å koble til en Mining pool



Du kan også koble deg til en Mining pool og, mer generelt, få tilgang til enhetens Interface-styringssystem via favorittleseren din.



Dette gjør du ved å skrive inn IP Address for enheten som vises på skjermen nedenfor, i vårt eksempel **192.168.144.6**, i nettleserens søkefelt



![image](assets/fr/15.webp)



Følgende side vises, der du blir bedt om å åpne Avalon Family-applikasjonen og skanne QR-koden som vises sammen med applikasjonen.



![image](assets/fr/20.webp)



Åpne applikasjonen, og klikk på de tre strekene øverst til høyre, og deretter på skann. Skann QR-koden i nettleseren, skriv deretter inn administratorpassordet for applikasjonen og klikk OK.



![image](assets/fr/21.webp)



Her er du på nettsiden som lar deg samhandle med Avalon. Det er mer et instrumentpanel for visning av maskinens beregninger enn en måte å konfigurere den på.



Men du kan fortsatt få tilgang til bassenginnstillingene på denne måten, ved å klikke på **"Pool Config"** nederst i høyre hjørne.



![image](assets/fr/22.webp)



På samme måte som med mobilapplikasjonen kan du legge inn bassengparametrene dine her.



![image](assets/fr/23.webp)



## Styr enheten din via Avalon Family-appen



Vi har nå koblet hjemme-Miner til vårt lokale nettverk, og rettet Hashrate mot Minings-bassenger. La oss nå oppdage de viktigste funksjonene til maskinen vår gjennom Avalon Family-applikasjonen.



I Avalon-familieapplikasjonen klikker du på ikonet som tilsvarer Avalon Nano 3S.


blir du presentert for tre menyer: "Arbeidsmodus", "Lysstyring" og "Innstillinger". Klikk først på "Arbeidsmodus". Du vil da bli tilbudt 3 strømmoduser for maskinen din.



**Lav**: gir deg rundt 3 Th/s Hashrate for 70 W strømforbruk


**Medium**: gir deg ca. 4,5 Th/s Hashrate for 100 W strømforbruk


**Høy**: gir deg ca. 6 Th/s Hashrate ved maksimalt forbruk på 140 W



![image](assets/fr/31.webp)


La oss ta et skritt tilbake og utforske menyen "Light Control". Denne er rent kosmetisk. Det finnes en rekke alternativer for å variere farge, intensitet, varme, slå av lysdiodene på enheten om natten osv. Det er lett å finne ut av selv.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Den siste menyen som er tilgjengelig for oss, er "Settings"-menyen som vi allerede har sett for tilkobling til Mining-bassengene våre. Her kan du administrere bassengene dine, endre enhetens administratorpassord og observere ulike beregninger, for eksempel utløpsdato for garantien, filterets renhet eller hvordan du kontakter kundestøtte i tilfelle feil.



![image](assets/fr/35.webp)


For vedlikehold og for å holde filteret så rent som mulig, anbefaler vi at du bruker en støvsuger og regelmessig støvsuger luftinntakene og -utløpene for å unngå tilstopping.



Vi har nå kommet til slutten av denne veiledningen, som har lært oss hvordan vi kobler Avalon Nano 3 S til vårt lokale nettverk, hvordan vi peker Hashrate mot Mining-bassenger, og hvordan vi navigerer gjennom alternativer og innstillinger ved hjelp av Avalon Family-applikasjonen.



Hvis du vil vite mer, kan du ta en titt på veiledningen vår om den overlegne versjonen av Avalon: Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7