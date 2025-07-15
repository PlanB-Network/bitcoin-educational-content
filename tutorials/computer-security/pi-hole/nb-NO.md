---
name: Pi-Hole
description: En annonseblokkering for hele nettverket ditt
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian Duchemin publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___



## I. Presentasjon



Vi har alle gjort det så snart vi starter opp favorittleseren vår: installert en **adblocker** (annonseblokkering). Men når du bruker TV-nettleseren eller en Android-enhet osv... Er det litt vanskeligere å finne noe som fungerer. Og hvis det er mer enn én enhet i huset, må du gjenta operasjonen for hver nettleser!



I denne veiledningen skal vi løse et enkelt problem**: å tilby en annonseblokkering til alle maskinene i nettverket vårt og administrere den sentralt**



For å gjøre dette bruker vi et verktøy som er utviklet for dette formålet: **Pi-Hole**



Pi-Hole er et DNS-sinkhole. Den bruker DNS-forespørsler fra enhetene dine til å validere eller avvise trafikk, og beskytter deg dermed mot adresser og domener som er kjent for å distribuere reklame, skadelig programvare og så videre.



DNS står for Domain Name System. Så hva er et domenenavn? Vel, "it-connect.fr" er bare ett eksempel. Et domenenavn er en unik identifikator for en eller flere ressurser, som vanligvis administreres av én enkelt enhet.



Maskinnavnet pluss domenenavnet kalles FQDN for *Fully Qualified Domain Name*. Det gjør at du kan nå en bestemt maskin bare ved å "ringe" den. Når du for eksempel skriver "www.trucmachin.com", ringer du faktisk til maskinen "www", som tilhører domenet "trucmachin.com".



Men datamaskinene våre forstår ikke menneskespråk, alt de forstår er binært, så de trenger en IP Address, som tilsvarer et telefonnummer, for å nå nettstedet.



Så hver gang du skriver inn navnet på et nettsted i nettleseren eller klikker på en lenke, spør datamaskinen først en DNS-server om IP Address som tilsvarer navnet.



**Pi-Hole vil deretter inspisere disse forespørslene (det er hundrevis av dem hver dag!) og automatisk blokkere de som er kjent for å være vert for reklame eller til og med ondsinnede filer



## II. Installere Pi-Hole



Med et navn som Pi-Hole kan du med rette anta at du trenger en Raspberry-Pi... Men det er ikke helt sant. **Pi-Hole kan installeres på en hvilken som helst Linux-maskin (Debian, Fedora, Rocky, Ubuntu osv.)



På den annen side må du huske på at **denne enheten må kjøre 24 timer i døgnet av en enkel grunn: ingen DNS, ikke noe Internett!** Raspberry er derfor en god idé, siden den bruker nesten ingen energi.



For å installere, kobler du deg til Linux-maskinen din via SSH og skriver inn følgende kommando som "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Merk**: Under normale omstendigheter er det ikke tilrådelig å "hacke" et skript uten først å vite hva det gjør. Hvis du ikke er sikker, kan du gå til siden med en nettleser eller laste ned innholdet som en fil.
>


> **Merk: På minimale versjoner av Debian 11 er Curl ikke installert, så du må installere det manuelt med kommandoen **apt-get install curl** før du skriver inn kommandoen ovenfor.

Når skriptet er kjørt, utføres en rekke tester, og selve installasjonen går av seg selv:



![Image](assets/fr/019.webp)



Installere Pi-Hole



Når installasjonen er fullført, kommer du til dette skjermbildet:



![Image](assets/fr/020.webp)



Pi-Hole startskjerm



> **Merk**: Hvis du bruker DHCP på maskinen din, vil du få en advarsel om dette. For riktig bruk anbefaler vi selvfølgelig på det sterkeste at du tildeler en fast IP til maskinen din.

Etter dette skjermbildet får du noen få informasjonsmeldinger, og deretter kommer du til konfigurasjonsveiviseren, der du først blir spurt om hvilken DNS-server Pi-Hole skal videresende forespørsler til. For min del har jeg valgt Quad9, som har en personvernerklæring.



![Image](assets/fr/021.webp)



Valg av DNS - Pi-Hole



> **Merk: Hvis du jobber i en bedrift, er det stor sannsynlighet for at din nåværende DNS-server er Active Directory-domenekontrolleren. Men ikke vær redd, du kan senere angi en betinget omdirigering for et domene etter eget valg. Vanligvis vil du kunne omdirigere alle forespørsler som gjelder ditt lokale domene, til DNS-serveren din.

Du vil legge merke til at noen valg inkluderer et DNSSEC-alternativ. I utgangspunktet er ikke DNS-protokollen sikker (den ble ikke designet med dette i tankene på den tiden). DNSSEC løser dette problemet ved å legge til en Layer av sikkerhet gjennom kryptering og signering av utvekslinger, som forklart i den tilsvarende artikkelen: [DNS-sikkerhet] (https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Alle annonseblokkere er avhengige av en eller flere lister for å gjøre jobben sin. Pi-Hole leveres med én liste som standard, så velg den og legg til flere senere.



![Image](assets/fr/022.webp)



Kom spørsmålet om Interface web, er installasjonen valgfri, da verktøyet har sin egen kommandolinje for administrasjon og visualisering. Men denne Interface er ganske hyggelig og godt utført, så jeg anbefaler at du installerer den samtidig:



![Image](assets/fr/023.webp)



Hvis du installerer Pi-Hole på en maskin som allerede har en webserver, kan du svare "nei" på følgende spørsmål. Vær imidlertid oppmerksom på at PHP og flere moduler er påkrevd for at dette skal fungere. Ellers vil **lighttpd bli installert med alle nødvendige moduler**.



![Image](assets/fr/024.webp)



Deretter blir du spurt om du ønsker å registrere DNS-forespørsler. **Hvis du ønsker å føre historikk, setter du dette til ja; ellers setter du dette til nei, men da mister du noe av funksjonaliteten** (se neste skjermbilde).



![Image](assets/fr/025.webp)



For Interface-nettet bruker Pi-Hole en egen funksjon kalt FTLDNS, som tilbyr et API og genererer statistikk fra DNS-forespørsler. Denne funksjonen kan inkludere en "personvern"-modus som maskerer domenene som forespørres, kundene bak forespørselen, eller begge deler. Det er praktisk hvis du vil overvåke uten å krenke personvernet, eller rett og slett hvis du vil overholde relevante forskrifter ved bruk i et offentlig nettverk.



![Image](assets/fr/026.webp)



Valg av privat livsstil



Når dette siste spørsmålet er besvart, vil skriptet gjøre det det skal: laste ned GitHub-repositoriene og konfigurere Pi-Hole. På slutten av installasjonen vises en oppsummeringsskjerm med viktig informasjon:



![Image](assets/fr/027.webp)



Skjermbilde for installasjonssammendrag



Noter Interface-nettpassordet og nettverksinformasjonen. Nå er det på tide å konfigurere DHCP-tjenesten på vår nåværende lokasjon.



## III. DHCP-konfigurasjon



For å fungere må Pi-Hole "løse" DNS-forespørsler fra klienter, slik at de vet at det er den de skal sende dem til. Det finnes flere måter å gjøre dette på:





- Endre DNS-innstillingene på DHCP-serveren (f.eks. boksen din)
- Deaktiver denne serveren og bruk den som leveres av Pi-Hole
- Endre hver enhet manuelt til å bruke Pi-Hole som DNS



Personlig velger jeg den første løsningen. Sjansen er stor for at **du har en DHCP-server der du er** (vanligvis boksen din). Så det er ingen grunn til å bry deg.



Siden det er et stort antall muligheter, mellom de forskjellige operatørenes bokser (som jeg ikke vet om alle) og de som har sin egen ruter, vil jeg ikke gi et skjermbilde for disse endringene. I alle fall må du gå til DHCP-innstillingene og endre "DNS" -parameteren for å inkludere IP Address til Pi-Hole.



Når dette er gjort, vil eventuelle enheter som har vært slått på tidligere, ha beholdt de gamle innstillingene, og du må derfor starte konfigurasjonsforespørselen på nytt.



På Windows-arbeidsstasjoner, med en ledetekst :



```
ipconfig /renew
```



På en Linux-arbeidsstasjon :



```
dhclient
```



For alle andre enheter må de slås av og på igjen.



Så de bør få de riktige parametrene, for å sjekke:



```
ipconfig /all
```



I DNS-feltet skal du ha Address til Pi-Hole, i mitt tilfelle 192.168.1.42 :



![Image](assets/fr/029.webp)



## IV. Bruk av Interface web Pi-Hole



For å forenkle administrasjonen har **Pi-Hole** en veldesignet Interface web Interface. Den er brukervennlig og tilgjengelig, og lar deg :





- Se antall forespørsler, blokkerte forespørsler osv. i sanntid.
- Administrer hviteliste og svarteliste
- Legg til statiske oppføringer, aliaser osv.
- Legg til lister
- Og mange andre funksjoner!



For min del kommer jeg til å legge til en blokkeringsliste. Som nevnt ovenfor ble bare én liste installert samtidig med Soft. Det finnes mange lister for annonsesider, men det er best å velge minst én som er spesifikk for det landet du bor i. En av de mest kjente listene er **EasyList**, og en av dem er spesifikk for Frankrike: [EasyList-ListFR] (https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



For å legge den til, må du først koble deg til Interface-administratoren: **http://<ip_du_PiHole>/admin**



Administratorpassordet er allerede generert (se skjermbildet ved slutten av installasjonen), så alt du trenger å gjøre er å skrive det inn for å få tilgang til Interface :



![Image](assets/fr/030.webp)



Interface fra Pi-Hole



Vi kan for eksempel se at det er to kunder som er koblet til Pi-Hole, at den har behandlet 442 forespørsler og at 8 av disse har blitt blokkert. Disse grafene kan være en god kilde til informasjon, spesielt i en profesjonell sammenheng.



For å legge til listen vår, gå til menyene "**Group Management**" og "**Adlists**":



![Image](assets/fr/031.webp)



Vi kan se vår første liste "**StevenBlack**", for å legge til vår, kopier lenken jeg ga deg ovenfor og sett den inn i feltet "**Address**", for beskrivelsen velger jeg å sette navnet på listen:



![Image](assets/fr/032.webp)



Legge til en liste i Pi-Hole



Alt som gjenstår er å klikke på "**Add**" for å legge den til. For å aktivere det, må vi utføre et ekstra trinn for å "advare" Pi-Hole om å ta over denne listen. For å gjøre dette :





- Du kan enten bruke den innebygde kommandolinjen
- Enten Interface web



Jeg valgte personlig den andre, for hvis du har sett nøye etter, er lenken til PHP-skriptet som utfører oppdateringen direkte på siden vi er på (ordet "online"). Så alt du trenger å gjøre er å klikke på den, og da kommer du til en side med bare ett alternativ:



![Image](assets/fr/033.webp)



Når skriptet er fullført, vises resultatet av skriptet på siden, noe som betyr at listen er tatt i betraktning (med mindre det vises en feilmelding, selvsagt).



Som annonsert i begynnelsen av denne veiledningen, lar Pi-Hole deg også **blokkere domener som er kjent for å distribuere skadelig programvare. For å forsterke denne funksjonen foreslår jeg at du også legger til den jevnlig oppdaterte domenelisten som distribueres av Abuse.ch**, noe som vil styrke sikkerheten i nettverket ditt betydelig, tilgjengelig på [this Address] (https://urlhaus.abuse.ch/downloads/hostfile/).



Du kan selvfølgelig legge til alle lister du mener er relevante, eller administrere svartelisten manuelt via svartelistemenyen.



## V. Pi-Hole-tester



Nå som alt er på plass, trenger du bare å teste løsningen for å forsikre deg om at den fungerer som den skal.



Jeg vil for eksempel prøve å nå domenet *http://admin.gentbcn.org/*, som står på Abuse.ch-listen fordi det er kjent for å være vert for skadelig programvare:



![Image](assets/fr/034.webp)



Jeg har tydeligvis blitt blokkert et sted. For å forsikre oss om at det er Pi-Hole som har gjort jobben, kan vi sjekke spørringsloggen i Interface-nettets "Query Log" for å se at det er en blokkering fra en listeoppføring:



![Image](assets/fr/035.webp)



## VI. Konklusjon



I denne veiledningen viser vi deg hvordan du setter opp en DNS-server som ikke bare eliminerer de fleste annonsene, men som også gir **en Layer av sikkerhet ved å blokkere domener som sprer phishing og skadelig programvare**.



Alt er gratis og økonomisk hvis det installeres på en Raspberry-Pi (når det gjelder strømforbruk).