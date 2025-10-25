---
name: Braiins Mini Miner
description: Gjør Mining enkelt hjemmefra.
---
![cover](assets/cover.webp)



## Innledning



Mini Miner braiins BMM 100 er et produkt laget av Mining pool Braiins. Denne enheten har et attraktivt design og er ekstremt stille. Den produserer 1,1 Th/s datakraft og bruker omtrent 40 watt. I motsetning til andre enheter er den ikke åpen kildekode, men den er veldig enkel å installere, det tar egentlig bare noen få klikk! Mini Miner BMM 100 er den første versjonen som ble utgitt. Nå er versjon 2 i produksjon, kalt BMM 101, som skiller seg fra den første ved å ha en større skjerm og tilstedeværelsen av Wi-Fi, men installasjonsprosedyrene er de samme.



Du kan også finne mye mer viktig informasjon ved å sjekke ut den komplette veiledningen direkte på [produsentens nettsted] (https://braiins.com/hardware/mini-Miner-bmm-100).



## Oversikt over BMM 100



enheten ser ut som en parallellpiped med en skjerm på forsiden



![image](assets/en/01.webp)



en vifte på oversiden



![image](assets/en/02.webp)



mens på baksiden har vi: hullet for strømmen, plass til et SD-kort (som kan være nødvendig for eventuelle oppdateringer), en liten knapp som sier `IP REPORT` som lar deg vite IP Address til mini Miner, hvilken Address som er nødvendig for å få tilgang til enhetens dashbord. Når du trykker på knappen, vises IP Address i ca. 5 sekunder, deretter forsvinner den, og den innstilte skjermen vises igjen. Men hvis du trenger å endre noen innstillinger, trykker du bare på den aktuelle knappen igjen, og IP Address vises på skjermen igjen. Videre på listen finner vi en Ethernet-port og en tilgang til å tilbakestille enheten, der du må ta tak i en pinne og holde den inne i 10 sekunder for å tilbakestille alle innstillingene til mini Miner. Til slutt finner vi to indikatorlamper, en Green og en rød, som indikerer statusen til Miner.



![image](assets/en/03.webp)



## Tilkobling av Mini Miner



Du må koble enheten til internett via ethernet, men merk at med den nye versjonen (BMM 101) er dette ikke lenger nødvendig. Tilbake til denne mini Miner, når vi har funnet stedet, må vi først koble den til internettlinjen og deretter til strømmen: enheten slås automatisk på og viser sin IP Address på skjermen.



## Konfigurasjon



Vi må åpne en nettleser og skrive inn IP Address som viser oss mini Miner i søkefeltet. Jeg minner deg om at for å finne enheten i nettverket må du være lokal, så du må ha datamaskinen du bruker koblet til det samme nettverket som mini Miner. når vi skriver inn IP Address, trykker vi på enter og påloggingssiden til mini Miners operativsystem, som er Braiins OS, vises på skjermen.



![image](assets/en/06.webp)



For å logge inn må du oppgi `root` som brukernavn, mens du kan la passordet stå tomt. Klikk på innlogging og ditt mini Miner dashbord vil vises.



![image](assets/en/07.webp)



## Generelle innstillinger



La oss gå til System



![image](assets/en/24.webp)



i innstillingene finner vi noen generelle innstillinger som tema (lys eller mørk), språk, tidssone og endring av passord.



![image](assets/en/25.webp)



Hvis vi går til "Mini Miner Screen" i stedet har vi innstillingene til vår mini Miner, for eksempel skjermvisningen. Vi kan velge om vi vil vise klokkeslettet eller prisen på Bitcoin, eller skjermen med informasjon om maskinens status, for eksempel produkt Hash, temperatur, wattforbruk og så videre. Her er det opp til deg å velge hva du vil se på skjermen; vi kan også endre lysstyrken på skjermen, stille inn nattmodus og vise klokkeslettet med 12-timers eller 24-timers format.



![image](assets/en/26.webp)



Når du har gjort endringer, klikker du på `Lagre endringer`, og du vil se endringene på skjermen på enheten din



![image](assets/en/27.webp)



## Tilkobling til Mining pool



Nå er vi ennå ikke i drift, fordi vi må koble oss til et basseng for å starte Mining, så vi må gå til "Konfigurasjon"



![image](assets/en/08.webp)



og den første oppføringen er bare `Pools`.



![image](assets/en/09.webp)



Her må vi bestemme hvilket basseng vi skal bruke. I denne opplæringen vil jeg vise deg to alternativer. Det første er å koble oss til Mining pool Braiins, som også brukes av profesjonelle gruvearbeidere, som du kan se i denne veiledningen:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Det andre alternativet er å koble oss til en Mining pool som mina i solo, som Public Pool, følg denne guiden for å gjøre det:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Braiins basseng



For å koble oss til dette bassenget må vi opprette en konto. dette bassenget foretar også betalinger med Lightning Network, så vi vil kunne motta noen Sats per dag. For å gjøre dette må vi sette opp et Address-lyn som vi kan motta belønningene på. Hvis du ikke vet hvordan du oppretter en konto på braiins pool eller hvordan du setter opp din Address lightning, kan du følge denne guiden:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Når det er gjort, er vi i Braiins bassengets dashbord. Det vi må gjøre er å fortelle bassenget at vi ønsker å koble oss til en av gruvearbeiderne våre, så på venstre side av skjermen finner du en rekke oppføringer. Vi må gå til "arbeidere"



![image](assets/en/04.webp)



og vi må klikke på den lilla knappen til høyre der det står "Koble til arbeidere"



![image](assets/en/05.webp)



Her kommer vinduet med informasjonen vi trenger for å koble vår mini Miner til bassenget. Her er den eneste endringen vi kan gjøre å velge Stratum V2. For å finne ut hva Stratum v2 er, se denne oppføringen i [glossary] (https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Nå må vi kopiere denne strengen som starter med stratumv2. Så vi klikker på det lille "kopier"-symbolet, og så går vi til dashbordet til vår mini Miner som vi hadde igjen i konfigurasjon og bassenger. Vi klikker på Legg til nytt basseng



![image](assets/en/11.webp)



og lim inn strengen vi kopierte inn i feltet under Pool URL.



![image](assets/en/12.webp)



Nå må vi legge til brukernavn og passord. La oss gå tilbake til bassengets dashbord. Under har vi også en brukerID og et passord. BrukerID og brukernavn, det vi oppga da vi opprettet kontoen, pluss navnet på Miner som vi vil legge inn. Du kan velge om du vil gi et navn til enheten du kobler til bassenget eller ikke, det er valgfritt, men det anbefales å legge det inn, så hvis du kobler til flere enheter, vil det være lettere å identifisere dem med en gang. Hvis du ikke ønsker å skrive inn noe, kan du la `workerName` stå.



![image](assets/en/13.webp)



Vi går deretter til vår mini Miner og skriver inn brukernavnet. Her vil vi i mitt tilfelle skrive inn "finalstepbitcoin" som er min brukerID, miniminer dot. Dette er navnet jeg bestemte meg for å gi enheten. Hvis du ikke vil navngi det, skriver du bare userid dot workername. I mitt tilfelle ville det være finalstepbitcoin.workername. Når du har skrevet inn brukernavnet, kan du velge et passord og skrive det i det tomme feltet. Du kan også skrive anithing123, som er det som også vises i bassengskjermen, men det vil bare indikere at du kan skrive hvilket passord du vil.



Når du har lagt inn alle dataene, trykker du på lagringsknappen til høyre (den som er formet som en diskett), og på denne måten har du konfigurert bassengdataene i mini Miner.



![image](assets/en/14.webp)



Nå må du gå tilbake til bassengets dashbord og klikke på "Connected! Gå tilbake"



![image](assets/en/15.webp)



Vi har koblet vår mini Miner til braiins-poolen! Du kan nå se den i listen over arbeidere. Hvis den ikke vises, kan du bare oppdatere og vente et øyeblikk. Når den dukker opp, kontrollerer du at den har statusen "OK" med en Green-brikke.



![image](assets/en/17.webp)



hvis du går tilbake til dashbordet, bør du begynne å se bevegelse på grafen og se Hashrate på enheten vår. Dette betyr at bassenget mottar arbeidet vårt, og derfor undergraver vi for alle praktiske formål.



![image](assets/en/16.webp)



### Offentlig basseng



Gjennom denne poolen kan man prøve lykken og utvinne alene, ved å lene seg på en pool. I dette tilfellet vil vi ikke motta belønning, men vi vil motta full belønning hvis vi noen gang klarer å utvinne en blokk. Vi kobler oss deretter til det offentlige bassenget, et basseng som kun består av Mining, og som er helt åpent. Vi åpner et nytt vindu i nettleseren og går til [web.public-pool.io] (https://web.public-pool.io/#/).



![image](assets/en/18.webp)



får vi opp en side med all informasjonen vi trenger. Vi kopierer deretter stratumet Address dit



![image](assets/en/19.webp)



så går vi tilbake til dashbordet til vår mini Miner, går til konfigurasjon og til bassenger, klikker på legg til nytt basseng (samme prosess som sett ovenfor) og limer inn 'stratum Address under basseng-url.



![image](assets/en/20.webp)



La oss nå gå tilbake til bassengsiden og se at som brukernavn må vi oppgi en Bitcoin Address, som vil være den vi vil motta belønningen i tilfelle vi undergraver en blokk, deretter en prikk og deretter navnet på enheten vår, som vi gjorde tidligere med Braiins Pool, mens passordet vi kan velge selv.



![image](assets/en/21.webp)



Vi går tilbake til mini Miner og under brukernavn limer vi inn en Address Bitcoin etterfulgt av punktum og navnet, jeg vil sette `miniminer`. I passordet i stedet vil jeg sette test, du skriver inn hva du vil.



![image](assets/en/22.webp)



Nå lagrer vi innstillingene og deaktiverer Braiins-bassenget.



![image](assets/en/23.webp)



Bra! Vi er nå Mining på offentlig basseng!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)