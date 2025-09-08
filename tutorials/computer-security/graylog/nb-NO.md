---
name: Graylog
description: Sentraliser og analyser loggene dine på en enkel måte
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian BURNEL publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___



## Distribuere Graylog på Debian 12



### I. Presentasjon



Graylog er en åpen kildekode-løsning som er utviklet for å sentralisere, lagre og analysere logger fra maskiner og nettverksenheter i sanntid. I denne veiledningen lærer vi hvordan du installerer gratisversjonen av Graylog på en Debian 12-maskin!



I et informasjonssystem genererer hver **server**, enten den kjører **Linux** eller **Windows**, og hver **nettverksenhet** (svitsj, ruter, brannmur osv...) **sine egne logger**, som lagres lokalt. Når loggene lagres lokalt på hver maskin, er det svært vanskelig å analysere og korrelere hendelser... Det er her **Graylog** kommer inn i bildet. Den fungerer som en **loggsink**, noe som betyr at **alle maskinene dine sender sine logger** til den (for eksempel via syslog). Graylog vil deretter **lagre og indeksere disse loggene**, samtidig som du kan utføre globale søk og opprette varsler.



Graylog er et analyse- og overvåkingsverktøy som gjør det enklere å identifisere mistenkelig atferd og ulike problemer (stabilitet, ytelse osv.).




![Image](assets/fr/034.webp)



**Gratisversjonen, **Graylog Open**, er ikke en SIEM slik Wazuh er, spesielt fordi den mangler reelle funksjoner for å oppdage inntrengning.



### II. Forutsetninger



**stack Graylog** er basert på **flere komponenter** som vi må installere og konfigurere. Her installerer vi alle komponentene på samme server, men det er mulig å opprette klynger basert på flere noder og fordele rollene på flere servere. I denne veiledningen installerer vi **Graylog 6.1**, som er den nyeste versjonen til dags dato.





- MongoDB 7**, den nåværende anbefalte versjonen for Graylog (minimum 5.0.7, maksimum 7.x)
- OpenSearch**, en åpen kildekode Fork av Elasticsearch laget av Amazon (minimum 1.1.x, maksimum 2.15.x)
- OpenJDK 17**



**Graylog-serveren** kjører på **Debian 12**, men installasjon er mulig på andre distribusjoner, inkludert via Docker. Den virtuelle maskinen er utstyrt med **8 GB RAM** og **256 GB diskplass**, for å ha nok ressurser til alle komponenter (ellers kan dette ha en betydelig innvirkning på ytelsen). Dette er imidlertid en grov veiledning, ettersom **dimensjoneringen av Graylog-arkitekturen avhenger av mengden informasjon som skal behandles**. Graylog kan behandle 30 MB eller 300 MB data per dag, men også 300 GB data per dag... Det er en **skalerbar løsning** som kan håndtere **terabytes med logger** (se [denne siden](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Kilde: Graylog



Før du starter konfigurasjonen, må du tilordne en statisk IP Address til Graylog-maskinen og installere de nyeste oppdateringene. Sørg for å angi den lokale maskinens tidssone og definere en NTP-server for synkronisering av dato og klokkeslett. Her er kommandoen som skal kjøres:



```
sudo timedatectl set-timezone Europe/Paris
```



**Merk: **OpenSearch-installasjonen er valgfri** hvis du bruker **Graylog Data Node** i stedet.



### III Trinnvis installasjon av Graylog



La oss begynne med å oppdatere pakkebufferen og installere de verktøyene vi trenger for det som kommer.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Installere MongoDB



Når det er gjort, begynner vi å installere MongoDB. Last ned GPG-nøkkelen som tilsvarer MongoDB-depotet:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Legg deretter til MongoDB 6-depotet på Debian 12-maskinen:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Deretter oppdaterer vi pakkebufferen og prøver å installere MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB kan ikke installeres fordi en avhengighet mangler: **libssl1.1**. Vi må installere denne pakken manuelt før vi kan fortsette, fordi Debian 12 ikke har den i sine repositorier.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Vi skal laste ned DEB-pakken med navnet "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (nyeste versjon) med kommandoen **wget**, og deretter installere den med kommandoen **dpkg**. Dette gir følgende to kommandoer:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Start MongoDB-installasjonen på nytt:



```
sudo apt-get install -y mongodb-org
```



Start deretter MongoDB-tjenesten på nytt og aktiver den slik at den starter automatisk når Debian-serveren startes.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Når MongoDB er installert, kan vi gå videre til å installere neste komponent.



#### B. Installere OpenSearch



La oss gå videre til å installere OpenSearch på serveren. Følgende kommando legger til signaturnøkkelen for OpenSearch-pakker:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Deretter legger du til OpenSearch-repository, slik at vi kan laste ned pakken med **apt** etterpå:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Oppdater pakkebufferen din:



```
sudo apt-get update
```



Deretter **installerer du OpenSearch**, og sørger for å **definere standardpassordet for administratorkontoen**. Her er passordet "**IT-Connect2024!**", men erstatt denne verdien med et sterkt passord. **Unngå svake passord** som "**P@ssword123**", og bruk minst **8 tegn** med minst ett tegn av hver type (små og store bokstaver, tall og spesialtegn), ellers vil det oppstå en feilmelding på slutten av installasjonen. **Dette er en forutsetning siden OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Vær tålmodig under installasjonen...



Når du er ferdig, kan du bruke et øyeblikk på å utføre minimumskonfigurasjonen. Åpne konfigurasjonsfilen i YAML-format:



```
sudo nano /etc/opensearch/opensearch.yml
```



Når filen er åpen, angir du følgende alternativer:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Denne OpenSearch-konfigurasjonen er utformet for å sette opp en enkelt node. Her er noen forklaringer på de ulike parameterne vi bruker:





- cluster.name: graylog**: denne parameteren navngir OpenSearch-klyngen med navnet "**graylog**".
- node.name: ${HOSTNAME}**: Nodenavnet settes dynamisk slik at det samsvarer med navnet på den lokale Linux-maskinen. Selv om vi bare har én node, er det viktig å gi den riktig navn.
- path.data: /var/lib/opensearch**: Denne stien angir hvor OpenSearch lagrer dataene sine på den lokale maskinen, i dette tilfellet i "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: Denne banen definerer hvor OpenSearch-loggfiler lagres, her i "**/var/log/opensearch**".
- discovery.type: single-node**: Denne parameteren konfigurerer OpenSearch til å arbeide med en enkelt node, derav valget av alternativet "**single-node**".
- network.host: 127.0.0.1**: Denne konfigurasjonen sikrer at OpenSearch bare lytter på den lokale Interface-sløyfen, noe som er tilstrekkelig siden den er på samme server som Graylog.
- action.auto_create_index: false**: Ved å deaktivere automatisk indeksoppretting vil OpenSearch ikke automatisk opprette en indeks når et dokument sendes uten en eksisterende indeks.
- plugins.security.disabled: true**: Dette alternativet deaktiverer OpenSearchs sikkerhetsplugin, noe som betyr at det ikke vil være noen autentisering, tilgangsstyring eller kommunikasjonskryptering. Denne innstillingen sparer tid ved oppsett av Graylog, men bør unngås i produksjon (se [denne siden](https://opensearch.org/docs/1.0/security-plugin/index/)).



Noen alternativer er allerede til stede, så du trenger bare å fjerne "#" for å aktivere dem, og deretter angi verdien din. Hvis du ikke finner et alternativ, kan du deklarere det direkte på slutten av filen.



![Image](assets/fr/023.webp)



Lagre og lukk denne filen.



#### C. Konfigurere Java (JVM)



Du må konfigurere Java Virtual Machine som brukes av OpenSearch, for å justere hvor mye minne denne tjenesten kan bruke. Rediger følgende konfigurasjonsfil:



```
sudo nano /etc/opensearch/jvm.options
```



Med konfigurasjonen som er brukt her, vil **OpenSearch starte med 4 GB allokert minne og kan vokse opp til 4 GB**, slik at det ikke blir noen minnevariasjon under drift. Her tar konfigurasjonen hensyn til at den virtuelle maskinen har totalt **8 GB RAM**. Begge parameterne må ha samme verdi. Dette betyr at du må bytte ut linjene:



```
-Xms1g
-Xmx1g
```



Med disse linjene:



```
-Xms4g
-Xmx4g
```



Her er et bilde av modifikasjonen som skal gjøres:



![Image](assets/fr/022.webp)



Lukk denne filen etter at du har lagret den.



I tillegg må vi sjekke konfigurasjonen av parameteren "**max_map_count**" i Linux-kjernen. Den definerer grensen for minneområder som er tilordnet per prosess, for å oppfylle behovene til applikasjonen vår. **OpenSearch** anbefaler, i likhet med Elasticsearch**, å sette denne verdien til "262144" for å unngå feil i minnehåndteringen.



På en nyinstallert Debian 12-maskin er verdien i prinsippet allerede korrekt. Men la oss sjekke. Kjør denne kommandoen:



```
cat /proc/sys/vm/max_map_count
```



Hvis du får en annen verdi enn "**262144**", kjører du følgende kommando, ellers er det ikke nødvendig.



```
sudo sysctl -w vm.max_map_count=262144
```



Til slutt aktiverer du OpenSearch autostart og starter den tilknyttede tjenesten.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Hvis du viser systemstatusen din, bør du se en Java-prosess med 4 GB RAM.



```
top
```



![Image](assets/fr/029.webp)



Neste skritt: den etterlengtede installasjonen av Graylog!



#### D. Installere Graylog



For å **installere Graylog 6.1** i den nyeste versjonen, kjør følgende 4 kommandoer for å **laste ned og installere Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Når dette er gjort, må vi gjøre noen endringer i Graylogs konfigurasjon før vi prøver å starte den.



La oss begynne med å konfigurere disse to alternativene:





- password_secret**: Denne parameteren brukes til å definere en nøkkel som brukes av Graylog for å sikre lagringen av brukerpassord (i samme ånd som en saltingsnøkkel). Denne nøkkelen må være **unik** og **tilfeldig**.
- root_password_sha2**: denne parameteren tilsvarer standard administratorpassord i Graylog. Det lagres som en Hash SHA-256.



Vi begynner med å generere en nøkkel på 96 tegn for parameteren **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopier den returnerte verdien, og åpne deretter Graylog-konfigurasjonsfilen:



```
sudo nano /etc/graylog/server/server.conf
```



Lim inn nøkkelen i **password_secret**-parameteren, slik:



![Image](assets/fr/027.webp)



Lagre og lukk filen.



Deretter må du angi passordet for "**admin**"-kontoen som er opprettet som standard. I konfigurasjonsfilen må Hash for passordet lagres, noe som betyr at det må beregnes. Eksempelet nedenfor viser Hash for passordet "**LogsWells@**": Tilpass verdien til ditt eget passord.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopier verdien du får som utdata (uten bindestrek på slutten av linjen).



Åpne Graylog-konfigurasjonsfilen på nytt:



```
sudo nano /etc/graylog/server/server.conf
```



Lim inn verdien i alternativet **root_password_sha2** på denne måten:



![Image](assets/fr/026.webp)



Mens du er i konfigurasjonsfilen, angir du alternativet "**http_bind_address**". Angi "**0.0.0.0.0:9000**", slik at Graylogs Interface-nett kan nås på port **9000**, via en hvilken som helst server-IP Address.



![Image](assets/fr/024.webp)



Sett deretter alternativet "**elasticsearch_hosts**" til `http://127.0.0.1:9200` for å erklære vår lokale OpenSearch-forekomst. Dette er nødvendig, siden vi ikke bruker en **Graylog Data Node**. Og uten dette alternativet vil det ikke være mulig å gå videre...



![Image](assets/fr/025.webp)



Lagre og lukk filen.



Denne kommandoen aktiverer Graylog slik at den starter automatisk ved neste oppstart, og starter Graylog-serveren umiddelbart.



```
sudo systemctl enable --now graylog-server
```



Når dette er gjort, kan du prøve å koble deg til Graylog fra en nettleser. Skriv inn serverens IP Address (eller navn) og port 9000.



**For din informasjon:**



For ikke så lenge siden dukket det opp et autentiseringsvindu som lignet på det nedenfor når du logget deg på Graylog for første gang. Du måtte skrive inn innloggingsnavnet "**admin**" og passordet ditt. Og så ble man ubehagelig overrasket over at tilkoblingen ikke fungerte.



![Image](assets/fr/031.webp)



Det var nødvendig å gå tilbake til kommandolinjen på Graylog-serveren og se i loggene. Vi kunne da se at **for den første tilkoblingen** er det nødvendig å **bruke et midlertidig passord**, som er spesifisert i loggene.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Deretter måtte man prøve på nytt med brukeren "**admin**" og det midlertidige passordet, og da kunne man logge inn!



**Dette er ikke lenger tilfelle. Alt du trenger å gjøre er å logge inn med administratorkontoen din og passordet som er konfigurert på kommandolinjen



![Image](assets/fr/033.webp)



**Velkommen til Graylogs Interface!



![Image](assets/fr/019.webp)



#### E. Graylog: opprett en ny administratorkonto



I stedet for å bruke administratorkontoen som er opprettet av Graylog, kan du opprette din egen personlige administratorkonto. Klikk på "**System**"-menyen, deretter på "**Brukere og team**" for å klikke på "**Opprett bruker**"-knappen. Fyll deretter ut skjemaet og tildel administratorrollen til kontoen din.



![Image](assets/fr/020.webp)



En personlig konto kan inneholde tilleggsinformasjon, for eksempel for- og etternavn og e-postadressen Address, i motsetning til en vanlig administratorkonto. I tillegg sikrer dette bedre sporbarhet når hver person jobber med en navngitt konto.



## Send logger til Graylog med rsyslog



### I. Presentasjon



I denne andre delen skal vi lære hvordan du konfigurerer en Linux-maskin til å sende loggene sine til en Graylog-server. For å gjøre dette skal vi installere og konfigurere Rsyslog på systemet.



### II. Konfigurere Graylog til å motta Linux-logger



Vi begynner med å konfigurere Graylog. Det er tre trinn som må fullføres:





- Opprettelsen av en **Input** for å opprette et inngangspunkt som gjør det mulig for Linux-maskiner å **sende Syslog-logger via UDP**.
- Opprettelse av en ny **Index** for å lagre og **indeksere alle Linux-logger**.
- Opprettelse av en **Stream** for å **rute** loggene som mottas av Graylog til den nye Linux-indeksen.



#### A. Opprett en inngang for Syslog



Logg deg på Graylog Interface, klikk på "**System**" i menyen og deretter på "**Input**". I rullegardinlisten velger du "**Syslog UDP**" og klikker deretter på knappen "**Lansere ny inngang**". Det er også mulig å opprette en TCP Syslog Input, men dette krever bruk av et TLS-sertifikat: et pluss for sikkerheten, men ikke dekket i denne artikkelen.



![Image](assets/fr/001.webp)



En veiviser vises på skjermen. Begynn med å gi denne inngangen et navn, for eksempel "**Graylog_UDP_Rsyslog_Linux**", og velg en port. Som standard er porten "**514**", men du kan tilpasse den. Her er porten "**12514**" valgt.



![Image](assets/fr/016.webp)



Du kan også krysse av for "**Lagre full melding**" for å lagre hele loggmeldingen i Graylog. Klikk på "**Start inndata**".



![Image](assets/fr/017.webp)



Den nye inngangen er opprettet og er nå aktiv. Graylog kan nå motta Syslog-logger på port 12514/UDP, men vi er ikke ferdige med å konfigurere applikasjonen ennå.



![Image](assets/fr/018.webp)


**Merk: En enkelt inngang kan brukes til å lagre logger fra flere Linux-maskiner.



#### B. Opprett en ny Linux-indeks



Vi må opprette en indeks i Graylog for å lagre logger fra Linux-maskiner. En **indeks** i Graylog er en lagringsstruktur som inneholder de mottatte loggene, dvs. de mottatte meldingene. Graylog bruker OpenSearch som lagringsmotor, og meldingene indekseres for å muliggjøre raske og effektive søk.



I Graylog klikker du på "**System**" i menyen, og deretter på "**Indekser**". På den nye siden som vises, klikker du på "**Opprett indekssett**".



![Image](assets/fr/005.webp)



Gi indeksen et navn, for eksempel "**Linux Index**", og legg til en beskrivelse og et prefiks før du bekrefter. Her vil vi **lagre alle Linux-logger i denne indeksen**. Det er også mulig å opprette spesifikke indekser for å lagre bare bestemte logger (bare [SSH]-logger (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), webtjenestelogger osv.).



![Image](assets/fr/006.webp)



Nå må vi opprette en ny strøm for å rute meldinger til denne indeksen.



#### C. Opprett en strøm



For å opprette en ny strøm klikker du på "**Streams**" i Graylogs hovedmeny. Klikk deretter på knappen "**Opprett strøm**" til høyre. I vinduet som vises, gir du strømmen et navn, for eksempel "**Linux Stream**", og velger indeksen "**Linux Index**" i feltet "**Index Set**". Bekreft valget ditt.



**Merk: Meldinger som tilhører denne strømmen, vil også bli inkludert i "**Standardstrøm**", med mindre du merker av for alternativet "**Fjern treff fra 'Standardstrøm'**".



![Image](assets/fr/002.webp)



Deretter klikker du på knappen "**Legg til strømregel**" i dampinnstillingene for å legge til en ny regel for ruting av meldinger. Hvis du ikke finner dette vinduet, klikker du på "**Streams**" i menyen, og deretter på linjen som tilsvarer strømmen din, klikker du på "**More**" og deretter på "**Manage Rules**".



Velg typen "**match input**", og velg den tidligere opprettede **Rsyslog-inngangen i UDP**. Bekreft med knappen "**Create Rule**". Alle meldinger til den nye inngangen vil nå bli sendt til Index for Linux.



![Image](assets/fr/003.webp)



Den nye strømmen skal vises i listen, og den skal være i tilstanden "**Running**". Meldingsbåndbredden viser "**0 msg/s**", ettersom vi for øyeblikket ikke sender noen logger til Rsyslog UDP-inngangen. Hvis du vil se loggene til en strøm, klikker du bare på navnet.



![Image](assets/fr/004.webp)



**Alt er klart på Graylog-siden**. Neste trinn er å konfigurere Linux-maskinen.



### III. Installere og konfigurere Rsyslog på Linux



Logg på Linux-maskinen, enten lokalt eller eksternt, og bruk en brukerkonto med rettigheter til å heve rettighetene (via sudo). Ellers bruker du "root"-kontoen direkte.



#### A. Installere Rsyslog-pakken



Begynn med å oppdatere pakkebufferen og installere pakken med navnet "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Sjekk deretter tjenestens status. I de fleste tilfeller er den allerede i gang.



```
sudo systemctl status rsyslog
```



#### B. Konfigurere Rsyslog



Rsyslog har en hovedkonfigurasjonsfil som ligger her:



```
/etc/rsyslog.conf
```



I tillegg brukes katalogen "**/etc/rsyslog.d/**" til å lagre flere konfigurasjonsfiler for Rsyslog. I hovedkonfigurasjonsfilen finnes det et Include-direktiv som importerer alle "**.conf**"-filer som ligger i denne katalogen. Dette gjør det mulig å ha flere filer for konfigurering av Rsyslog uten å endre hovedfilen.



I denne katalogen må du bruke tall for å definere innlastingsrekkefølgen, fordi filene lastes inn i alfabetisk rekkefølge. Ved å legge til et numerisk prefiks kan du styre prioriteten mellom flere konfigurasjonsfiler. Her har vi bare én ekstra fil, så det er ikke noe problem.



I denne katalogen oppretter vi en fil som heter "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



I denne filen setter du inn denne linjen:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Slik skal du tolke denne linjen:





- `*.*`: betyr at alle Syslog-logger fra Linux-maskinen sendes til Graylog.
- `@`: angir at transporten utføres i UDP. Du må angi "**@@@**" for å bytte til TCP.
- `192.168.10.220:12514`: angir Address for Graylog-serveren, og porten som loggene sendes på (tilsvarer Input).
- `RSYSLOG_SyslogProtocol23Format`: tilsvarer formatet på meldingene som skal sendes til Graylog.



Når du er ferdig, lagrer du filen og starter Rsyslog på nytt.



```
sudo systemctl restart rsyslog.service
```



Etter denne handlingen bør de første meldingene komme inn på Graylog-serveren din!



### IV. Visning av Linux-logger i Graylog



Fra Graylog kan du klikke på "**Streams**" og velge din nye strøm for å se relaterte meldinger. Alternativt kan du klikke på "**Søk**", velge Steam og starte et søk.



Her er noen av de viktigste egenskapene til Interface:



**1** - Velg perioden som meldingene skal vises for. Som standard vises meldinger fra de siste 5 minuttene.



**2** - Velg strømmen(e) som skal vises.



**3** - Aktiver automatisk oppdatering av meldingslisten (for eksempel hvert 5. sekund). Ellers er den statisk, og du må oppdatere den manuelt.



**4** - Klikk på forstørrelsesglasset for å starte søket etter at du har endret periode, strøm eller filter.



**5** - Inndatafelt for å spesifisere søkefiltre. Her angir jeg "**source:srv\-docker**" for å vise bare loggene fra den nye maskinen som jeg nettopp har satt opp Rsyslog på.



Logger sendes av Linux-maskinen:



![Image](assets/fr/015.webp)



### V. Identifisere en SSH-tilkoblingsfeil



Graylogs styrke ligger i evnen til å indeksere logger og gjøre det mulig å utføre søk etter ulike kriterier: kildemaskin, Timestamp, meldingsinnhold osv. Vi kan for eksempel være ute etter å identifisere mislykkede SSH-tilkoblinger.



Prøv å koble deg til Linux-serveren du nettopp har konfigurert Rsyslog på, fra en ekstern maskin (for eksempel Graylog-serveren). For eksempel



```
ssh [email protected]
```



Deretter skriver du bevisst inn feil **brukernavn** og **passord**, for å **generate tilkoblingsfeil**. I filen "**/var/log/auth.log**" vil dette føre til generate-loggmeldinger som ligner på følgende:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Du bør finne disse meldingene på Graylog.



I Graylog kan du bruke følgende søkefilter for å vise bare samsvarende meldinger:



```
message:Failed password AND application_name:sshd
```



Hvis du har flere servere og ønsker å analysere loggene til en bestemt server, angir du navnet i tillegg til:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Her er en oversikt over resultatet på en maskin der jeg genererte flere tilkoblingsfeil, på ulike tider av døgnet:



![Image](assets/fr/009.webp)



Mislykkede tilkoblingsforsøk gjøres fra maskinen med IP Address "**192.168.10.199**". Hvis du vil vite mer om aktiviteten til denne verten, kan du **søke etter denne IP Address**. Graylog vil sende ut alle logger der denne IP Address er referert til, på alle verter (som loggsending er konfigurert for).



I dette tilfellet kan filteret som skal brukes, være:



```
message:"192.168.10.199"
```



Vi får flere resultater (ikke overraskende, siden vi ikke filtrerer på SSH-applikasjonen):



![Image](assets/fr/008.webp)



### VI. Konklusjon



Ved å følge denne veiledningen kan du konfigurere en Linux-maskin til å sende loggene sine til en Graylog-server. På denne måten kan du sentralisere loggene fra Linux-vertene dine i loggsamleren din!



Hvis du vil gå enda lenger, kan du vurdere å opprette dashbord og varsler for å motta varsling når et avvik oppdages.



![Image](assets/fr/007.webp)