---
name: Lynis
description: Utfør en sikkerhetsrevisjon av en Linux-maskin med Lynis
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Fares CHELLOUG publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___



## I. Presentasjon



**I denne veiledningen skal vi lære hvordan du utfører en sikkerhetsrevisjon på en Linux-maskin ved hjelp av Lynis! For de av dere som ikke kjenner **Lynis,** er det et lite kommandolinjeverktøy som analyserer serverens konfigurasjon og kommer med anbefalinger for å **forbedre sikkerheten på maskinen din.**



Lynis er et verktøy med åpen kildekode fra CISOFY, et selskap som spesialiserer seg på **systemrevisjon og herding**. Hvis du ønsker å gjøre fremskritt i herdingen av Linux og populære tjenester (SSH, Apache2 osv.), er Lynis din allierte! Lynis forteller deg ikke bare hva som går galt, men gir også anbefalinger som peker deg i riktig retning (og sparer deg for tid).



**Lynis** fungerer med de fleste Linux-distribusjoner, inkludert: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis er rettet mot Linux/UNIX-brukere, men er også **macOS**-kompatibel. Veldig rask å installere, det er ingen avhengighetsstyring på pakkenivå.



Den brukes til en rekke formål:





- Sikkerhetsrevisjoner
- Testing av samsvar (PCI, HIPAA og SOX)
- Tøffere systemkonfigurasjoner
- Oppdagelse av sårbarheter



Verktøyet er mye brukt av et bredt spekter av brukere, inkludert systemadministratorer, IT-revisorer og pentestere. For analyser er verktøyet basert på standarder som **CIS Benchmark, NIST, NSA, OpenSCAP** og på offisielle anbefalinger fra **Debian, Gentoo, Red Hat**.



Prosjektet er tilgjengelig på denne Address på **Github**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Last ned Lynis fra CISOFY] (https://cisofy.com/lynis/#download)



I denne trinnvise veiledningen skal jeg **bruke en VPS som kjører Debian 12**, og jeg skal konsentrere meg om SSH-delen, siden jeg ønsker å sjekke konfigurasjonen og forbedre den.



## II. Nedlasting og installasjon



Det finnes flere måter å laste ned og installere Lynis på. Velg den du foretrekker fra listen nedenfor.



### A. Installasjon fra Debian-arkiver



Denne installasjonsmodusen gjør at du kan bruke kommandoen **lynis** fra hvor som helst på systemet, i motsetning til installasjon fra kildekode, der du må befinne deg i katalogen.



Koble til serveren din via SSH, og skriv inn følgende kommandoer for å installere Lynis:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Dette er hva du får:



![Image](assets/fr/024.webp)



### B. Last ned fra det offisielle nettstedet



Du kan også laste den ned fra Cisofys nettsted:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Dette er hva du får:



![Image](assets/fr/032.webp)



Deretter pakker vi ut arkivet ved hjelp av følgende kommando:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Dette er hva du får:



![Image](assets/fr/020.webp)



La oss gå til mappen **lynis**:



```
cd lynis
```



Vi kan se etter oppdateringer med følgende kommando:



```
./lynis update info
```



Dette er hva du får:



![Image](assets/fr/023.webp)



### C. Last ned fra GitHub



Vi laster ned **Lynis** fra det offisielle GitHub-depotet ved å bruke følgende kommando (*git* må være til stede på maskinen din):



```
git clone https://github.com/CISOfy/lynis.git
```



Dette er hva du får:



![Image](assets/fr/060.webp)



## III. Bruk av Lynis



Lynis finnes på maskinen vår, så la oss lære å bruke den!



### A. Hovedkontroller og alternativer



Du kan vise de tilgjengelige kommandoene ved å skrive inn følgende kommando:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Dette er hva du får:



![Image](assets/fr/039.webp)



Og du får også følgende alternativer:



![Image](assets/fr/040.webp)



Du kan vise alle tilgjengelige kommandoer ved å skrive inn følgende kommando:



```
sudo lynis show
```



Dette er hva du får:



![Image](assets/fr/022.webp)



Hvis du ønsker å vise alle alternativene, må du taste inn:



```
sudo lynis show options
```



Dette er hva du får:



![Image](assets/fr/021.webp)



I resten av denne artikkelen lærer vi hvordan du bruker visse alternativer.



### B. Gjennomføring av systemrevisjonen



Vi skal be **Lynis** om å revidere systemet vårt, og finne ut hva som er riktig konfigurert og hva som kan forbedres. Dette gjør du ved å skrive inn følgende kommando:



```
sudo lynis audit system
# ou
./lynis audit system
```



Hvis du ikke er logget inn som root når du kjører denne kommandoen, vil verktøyet som standard kjøre med rettighetene til den brukeren som er logget inn. Noen tester vil ikke bli kjørt i denne konteksten:



![Image](assets/fr/052.webp)



Her er testene som ikke vil bli utført i denne modusen:



![Image](assets/fr/051.webp)



Når kommandoen er utført, starter analysen. Bare vent et øyeblikk.



På slutten av revisjonen får du dette (vi kan se at **Lynis** har identifisert **Debian 12**-systemet korrekt og vil bruke **Debian-plugin** for analysen):



![Image](assets/fr/017.webp)



Deretter lister Lynis opp et sett med punkter som tilsvarer alt han har sjekket i systemet vårt. Dette er organisert etter kategori, som vi skal se. Det er også verdt å merke seg at en fargekode brukes for å markere anbefalinger:





- Rød** for kritisk Elements eller beste praksis som ikke respekteres (for eksempel en manglende pakke), dvs. at serveren din ikke respekterer dette punktet
- Gul** for forslag eller delvis etterlevelse av anbefalingen (la oss si at det er et pluss å etterleve et punkt som er uthevet med denne fargen (ikke-prioritert))
- Green** for punkter der serverkonfigurasjonen din er kompatibel
- Hvit**, når den er nøytral



Her kan vi se at Lynis anbefaler å installere **fail2ban**:



![Image](assets/fr/057.webp)



I avsnittet "**Boot and services**" ser vi at tjenestebeskyttelsen via *systemd* kan forbedres. På den positive siden er Grub2 til stede, og det er ingen problemer med tillatelser på:



![Image](assets/fr/029.webp)



Deretter har du seksjonene "**Kernel**" og "**Memory and Processes**":



![Image](assets/fr/037.webp)



Neste avsnitt er "**Brukere, grupper og autentisering**". Verktøyet informerer oss om en advarsel om tillatelsene til katalogen "**/etc/sudoers.d**". For øyeblikket vet vi ikke mer, men vi vil kunne se hva anbefalingen er på slutten av analysen.



![Image](assets/fr/049.webp)



Her er hva du kan finne i seksjonene "**Shells", "Files Systems" og "USB Devices"**. Vi kan blant annet se at det finnes forslag til monteringspunkter, og at USB-enheter for øyeblikket er tillatt på denne maskinen.



![Image](assets/fr/048.webp)



Deretter seksjonene: "**Navnetjenester", "Porter og pakker", "Nettverk", Her står det at pakker som ikke lenger er i bruk, kan slettes, og at det ikke finnes noe verktøy som kan håndtere automatiske oppdateringer.



![Image](assets/fr/058.webp)



Vi kan se at brannmuren er aktivert (og ja, det er iptables!). I tillegg kan vi se at den har funnet ubrukte regler, og at en Apache-webserver er installert.



![Image](assets/fr/055.webp)



Deretter følger en analyse av selve webserveren, siden tjenesten er identifisert.



Vi kan se at den har funnet konfigurasjonsfiler for **Nginx**, og at for SSL/TLS-delen er **ciphers** konfigurert med bruk av en protokoll som ville være usikker. På den annen side, ifølge Lynis, er logghåndteringen korrekt.



![Image](assets/fr/038.webp)



SSH-tjenesten er til stede på VPS-serveren min. Konfigurasjonen er analysert av Lynis. Det må sies at SSH-sikkerheten lett kan forbedres! Vi kommer tilbake til dette området i detalj når vi har fått anbefalingene.



![Image](assets/fr/026.webp)



Her er seksjonene **"SNMP-støtte", "Databaser", "PHP", "Squid-støtte", "LDAP-tjenester", "Logging og filer"**.



Det er ett veldig viktig forslag når det gjelder logghåndtering: Det anbefales på det sterkeste at du ikke bare lagrer logger lokalt på maskinen din. Hvis maskinen blir ødelagt av en angriper, er det sannsynlig at han vil prøve å slette sporene sine... Så vi må eksternalisere loggene.



![Image](assets/fr/050.webp)



Her har vi revisjon av sårbare tjenester, kontoadministrasjon, planlagte oppgaver og NTP-synkronisering.det er indikert at nivået er lavt på banneret og identifikasjonsdelen: dette er forståelig, hvis du viser systemversjonen, gir det en indikasjon til en potensiell angriper. Dette er standardinnstillingen.



Det ville være interessant å aktivere **auditd** for å ha logger i tilfelle **forensisk** analyse. **NTP** er også sjekket, fordi for å søke i logger effektivt er det å foretrekke å ha systemer i tide, noe som forenkler søket.



![Image](assets/fr/036.webp)



Lynis ser deretter på kryptografiske Elements, virtualisering, containere og sikkerhetsrammeverk. Noen seksjoner er tomme fordi det ikke er noen korrespondanse med maskinen som er analysert. Vi kan imidlertid se at jeg har to utløpte SSL-sertifikater, og at jeg ikke har aktivert **SELinux**.



![Image](assets/fr/027.webp)



Også her er det rom for forbedringer: Det finnes ingen antivirus- eller antimalware-skanner, og vi har forslag til filtillatelser.



![Image](assets/fr/028.webp)



Deretter fokuserer Lynis på å stramme opp konfigurasjonen av Linux-kjernen (inkludert regler for IPv4-stakken), samt administrering av Linux-maskinens "Home"-kataloger.



![Image](assets/fr/035.webp)



Vi har kommet til slutten av analysen... Dette siste punktet viser at vi har alt å vinne på å ha ClamAV på denne maskinen.



![Image](assets/fr/030.webp)



## IV. Anbefalinger



Etter revisjonen er det på tide å lese og analysere anbefalingene. Det er her vi får anbefalingene og forklaringene for hver av testene som Lynis har utført.



Ta for eksempel SSH-anbefalingene. **For hvert forslag finner du den anbefalte parameteren og en lenke som forklarer sikkerhetshensynet ** Det er opp til deg å avgjøre, avhengig av kontekst og bruk.



La oss ta en titt på noen få eksempler på anbefalinger som er et direkte ekko av de punktene som ble fremhevet gjennom hele revisjonen...



### A. Eksempler på anbefalinger





- Som vi så tidligere, er NTP viktig for tidsstempling av logger:



![Image](assets/fr/043.webp)





- Lynis foreslår også å installere pakken **apt-listbugs** for å få informasjon om kritiske feil under pakkeinstallasjoner via **apt.**



![Image](assets/fr/041.webp)





- Verktøyet foreslår at vi installerer **needrestart for å kunne** se hvilke prosesser som bruker en gammel versjon av biblioteket og som må startes på nytt.



![Image](assets/fr/054.webp)





- Dette forslaget foreslår å installere **fail2ban** for automatisk å blokkere verter som ikke klarer å autentisere seg (særlig brute force).



![Image](assets/fr/044.webp)





- For å herde systemtjenester anbefaler han at vi kjører den blå kommandoen for hver tjeneste på maskinen vår.



![Image](assets/fr/056.webp)





- Han foreslår at du setter utløpsdatoer for alle passord for beskyttede kontoer.



![Image](assets/fr/031.webp)





- Dette forslaget går ut på å angi minimums- og maksimumsverdier for passordets alder. Dette vil blant annet sikre at passordene endres regelmessig.



![Image](assets/fr/042.webp)





- Vi anbefaler at du bruker separate partisjoner for å begrense konsekvensene av problemer med diskplass på én partisjon.



![Image](assets/fr/047.webp)





- Denne anbefalingen foreslår å deaktivere USB-lagring og firewire for å forhindre datalekkasje



![Image](assets/fr/033.webp)





- For å oppfylle denne anbefalingen kan du for eksempel installere og konfigurere **unnatended-upgrade**.



![Image](assets/fr/053.webp)



### B. Installere anbefalte pakker



For å forbedre systemkonfigurasjonen skal vi installere noen pakker på maskinen: noen som er anbefalt av Lynis, noen som jeg personlig anbefaler.



Du har et godt grunnlag å jobbe ut fra, så lenge du bruker litt tid på å konfigurere dem. For å gjøre dette kan du se på IT-Connect-nettstedet, andre artikler på nettet og verktøydokumentasjon.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Litt informasjon om de installerte pakkene:





- Clamav** er et antivirusprogram.
- unattend-upgrades** gjør at du kan administrere oppdateringene dine automatisk og til og med starte maskinen på nytt eller automatisk fjerne gamle pakker.
- rkhunter** er et anti-rootkit som skanner filsystemet ditt.
- Fail2ban** baserer seg på loggfilene dine i henhold til det du gir den tillatelse til å lese, og den fungerer med **iptables**, for eksempel for å utestenge IP-adresser som prøver å "brute force" serveren din i SSH.



### C. Anbefalinger for SSH



La oss ta en titt på SSH-anbefalingene. De er listet opp nedenfor. Ikke bekymre deg, vi vil umiddelbart forklare hvordan du kan forbedre konfigurasjonen.



![Image](assets/fr/034.webp)



La oss ta en nærmere titt på min nåværende **SSH**-konfigurasjon i:**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Konfigurasjonen som er foreslått nedenfor, kan fortsatt optimaliseres, men gir deg et godt utgangspunkt. *Vær oppmerksom på at jeg har fjernet en rekke kommentarer for bedre lesbarhet*.



Vi vil:





- Endre SSH-tilkoblingsport (glem standard 22)
- Øke loggenes ordrikhetsnivå, fra **INFO til VERBOSE**
- Sett **LoginGraceTime** til **2 minutter**



Hvis ingen tilkoblingsinformasjon legges inn i løpet av to minutter, blir tilkoblingen brutt.





- Aktiver **strictModes**



Angir om "sshd" skal sjekke modus og eier av brukerens filer samt brukerens hjemmekatalog før en tilkobling valideres. Dette er vanligvis ønskelig, fordi nybegynnere av og til ved et uhell lar katalogen eller filene sine være fullt tilgjengelige for alle. Standardinnstillingen er "yes".





- Sett **MaxAuthtries** til 3



Dette representerer antall mislykkede autentiseringsforsøk før kommunikasjonen avsluttes.





- Sett **MaxSessions** til 2



Dette representerer det maksimale antallet samtidige økter.





- Aktiver offentlig nøkkelautentisering



```
PubkeyAuthentication yes
```





- Behold passordgodkjenning:



```
PasswordAuthentication yes
```



Forby tomme passord og **Kerberos**-autentisering, samt **direkte root-autentisering**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Kontroller at du har "**PermitRootLogin no", hvis det er lik "yes", er det "absolutt ondt"**.





- Forby omdirigering av TCP-tilkoblinger



```
AllowTcpForwarding no
```



Angir om TCP-viderekoblinger er tillatt, med "yes" som standardinnstilling. Merk: Deaktivering av TCP-viderekoblinger forbedrer ikke sikkerheten hvis brukerne har tilgang til et skall, ettersom de fortsatt kan sette opp sine egne viderekoblingsverktøy.





- Forby X11-omdirigering



```
X11Forwarding no
```



Angir om X11-viderekoblinger godtas, med "no" som standardinnstilling. Merk: Selv om X11-omdirigeringer er deaktivert, øker ikke dette sikkerheten, ettersom brukere fortsatt kan sette opp sine egne omdirigeringer. X11-omdirigering deaktiveres automatisk hvis **UseLogin** er valgt.





- Angi tidsavbrudd for kommunikasjon mellom klienten og sshd



```
ClientAliveInterval  300
```



Definerer en tidsavbrudd i sekunder, og hvis det ikke mottas data fra klienten, sender sshd-tjenesten en melding med forespørsel om svar fra klienten. Som standard er dette alternativet satt til "0", noe som betyr at disse meldingene ikke sendes til klienten. Det er bare versjon 2 av SSH-protokollen som støtter dette alternativet.



```
ClientAliveCountMax 0
```



I følge [dokumentasjonen (*man page*) for sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html) betyr dette alternativet følgende: "Setter antall hold-meldinger (se ovenfor) som skal sendes uten svar fra klienten for **sshd**. Hvis denne terskelen nås mens hold-meldingene har blitt sendt, kobler **sshd** fra klienten og avslutter økten. Det er viktig å merke seg at disse hold-meldingene er svært forskjellige fra **KeepAlive**-alternativet (nedenfor). Hold-meldinger sendes gjennom den krypterte tunnelen, og kan derfor ikke forfalskes. Tilkoblingshold på TCP-nivå som aktiveres av **KeepAlive**, kan forfalskes. Mekanismen for å holde tilkoblingen er interessant når klienten eller serveren trenger å vite om tilkoblingen er inaktiv."





- Forhindre avsløring av informasjon ved å deaktivere **motd, banner, lastlog**



```
PrintMotd no
```



Angir om sshd skal vise innholdet i filen "/etc/motd" når en bruker logger seg på i interaktiv modus. På noen systemer kan dette innholdet også vises av skallet, via /etc/profile eller en lignende fil. Standardverdien er "yes".



```
Banner none
```



Det er verdt å merke seg at i enkelte jurisdiksjoner kan det å sende en melding før autentisering være en forutsetning for rettslig beskyttelse. Innholdet i den angitte filen overføres til den eksterne brukeren før tilkoblingsautorisasjon gis. Dette alternativet må konfigureres, ettersom det som standard ikke vises noen melding.



I bilder gir dette:



![Image](assets/fr/019.webp)



### D. Revisjonsresultat



Til slutt, la oss ikke glemme å sjekke **Lynis audit score**! Vi ser at **herdingsresultatet mitt er 63**, og at rapportfilen kan vises i "**/var/log/lynis-report.dat**". Det finnes også filen "**/var/log/lynis.log**".



**Med andre ord: Jo høyere poengsum, desto bedre! Du må derfor jobbe med konfigurasjonen for å oppnå høyest mulig poengsum, samtidig som du lar maskinen og de hostede tjenestene fungere normalt (det vil si at du må utføre funksjonstester).



![Image](assets/fr/046.webp)



La oss ta en titt på resultatene på den andre serveren min, der jeg brukte litt mer tid på å herde! Så det er normalt at poengsummen er høyere (**76**).



![Image](assets/fr/045.webp)



## V. Lynis automatisert planlegging



**Lynis** tilbyr også muligheten til å kjøre kontrollene via en planlagt oppgave. Det finnes faktisk et **"--cronjob"**-alternativ, som kjører alle Lynis-tester uten behov for validering eller brukerhandling. Du kan da enkelt lage et skript som kjører **Lynis** og legger utdataene i en tidsstemplet fil med navnet på den aktuelle serveren. Her er en slik fil som du kan legge i mappen */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Variabelen **"AUDITOR_NAME"** er ganske enkelt en variabel som vi angir i alternativet **"--auditor"** i **Lynis**, slik at dette navnet vises i rapporten:



![Image](assets/fr/059.webp)



Vi skal også opprette noen kontekstuelle variabler som hjelper oss med å organisere oss bedre, for eksempel vertsnavn og dato for å navngi rapporten og tidsstemple den, og banen til mappen vi vil legge rapportene våre i.



## VI. Konklusjon



Lynis er et svært praktisk verktøy som hjelper deg med å spare tid og bli mer effektiv når du vil vite mer om konfigurasjonen på en Linux-server, spesielt når det gjelder sikkerhet. Husk imidlertid at alle endringer må testes før de tas i bruk i produksjon, og at du må ta hensyn til din egen bruk og kontekst.



Du kommer sannsynligvis ikke til å bruke den samme konfigurasjonen for en VPS som er eksponert mot nettet, der du bare trenger én SSH-tilkobling (fordi du er den eneste som kobler til), i motsetning til en **bastion** eller **scheduler** som trenger flere **SSH.**-tilkoblinger



Når du har funnet en konfigurasjon som passer deg når det gjelder herding, er det lurt å ta i bruk et automatiseringsverktøy, slik at du slipper å gjøre oppgavene manuelt, noe som er tidkrevende og feilutsatt. Du kan for eksempel bruke **: Puppet, Chef, Ansible osv



Ikke glem å kommunisere med teamene dine før implementeringen: Du må få dem til å forstå hvorfor du gjør disse endringene, ikke bare fortelle dem at du gjør dem. Til syvende og sist handler det om å videreformidle god praksis, og det vil øke sjansene for å lykkes.



Til slutt kan du også sammenligne **Lynis** med andre verktøy, som det finnes flere av. Hvis du ønsker å gå i retning av sentralisert administrasjon samtidig som du vil beholde åpen kildekode, anbefaler jeg verktøyet [Wazuh] (https://wazuh.com/).



**Denne veiledningen er over, ha det gøy med Lynis!