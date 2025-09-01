---
name: WireGuard
description: Sette opp WireGuard VPN på Debian og Windows
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian BURNEL publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___



## I. Presentasjon



I denne veiledningen lærer vi hvordan du konfigurerer et VPN basert på WireGuard, en gratis VPN-løsning med åpen kildekode som øker ytelsen uten å gå på bekostning av sikkerheten.



WireGuard er en relativt ny løsning, som har vært tilgjengelig som en stabil versjon siden mars 2020, og har hatt æren av å være integrert direkte i **Linux-kjernen siden versjon 5.6**. Dette forhindrer ikke at den er tilgjengelig fra eldre Linux-distribusjoner som bruker en annen versjon av kjernen. Sammenlignet med løsninger som OpenVPN og IPSec, er WireGuard enklere å bruke og mye raskere, som vi vil se på slutten av denne artikkelen.



Noen viktige punkter om WireGuard:





- Enkel, lett og ultraeffektiv!
- Kun UDP-drift (noe som kan være en ulempe ved passering av visse brannmurer)
- Fungerer på en peer-to-peer-modell i stedet for en klient-server-modell
- Autentisering med nøkkel Exchange, etter samme prinsipp som SSH med private/offentlige nøkler
- Bruk av flere algoritmer: symmetrisk kryptering med ChaCha20, meldingsautentisering med Poly1305, samt andre algoritmer som Curve25519, BLAKE2 og SipHash24
- Støtter både IPv4 og IPv6
- Flere plattformer: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (og implementert i ProtonVPN)
- Bare 4000 kodelinjer, sammenlignet med hundretusener for andre løsninger



Når det gjelder den kryptografiske delen, er de ulike algoritmene som brukes, håndplukket, revidert på flere måter og undersøkt av sikkerhetsforskere som er spesialister på området.



Det offisielle nettstedet for prosjektet: [wireguard.com] (https://www.wireguard.com/)



Er du overbevist om denne løsningen etter å ha lest denne innledningen? Da gjenstår det bare å lese videre!



## II. Lab WireGuard-diagram



Før jeg presenterer min lab for å sette opp WireGuard, bør du vite at du kan tenke deg å **bruke WireGuard til å koble sammen to eksterne infrastrukturer**, men også til å **koble en ekstern klient til en infrastruktur som et bedriftsnettverk eller hjemmenettverket ditt**. Dette er i samme ånd som med OpenVPN, som vi nylig så i veiledningen "[OpenVPN på Synology] (https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Hvis WireGuard ikke er satt opp direkte på ruteren eller brannmuren, slik man kan tenke seg med OpenWRT, må du sette opp portvideresending slik at strømmen når WireGuard-paret.



![Image](assets/fr/034.webp)



Nå skal jeg fortelle deg om laben min og hva vi skal gjøre i dag.



Jeg kommer til å bruke en Debian 11-maskin som WireGuard-server og en Windows-klient som WireGuard VPN-klient. Selv om det er litt misvisende å snakke om et klient-server-forhold, fordi **WireGuard fungerer på en "peer-to-peer"**-modell. Det er litt misvisende når du prøver å sette opp en "klient-til-sted"-tilkobling. La oss i stedet si at jeg skal ha to par eller **to WireGuard-tilkoblingspunkter** om du vil: ett under Debian 11 og det andre under Windows.



Disse to parene kan kommunisere med hverandre i begge retninger, noe som betyr at jeg fra min Windows-maskin kan få tilgang til Debian 11-maskinens eksterne LAN, og vice versa: alt avhenger av konfigurasjonen av tunnelen og brannmuren til WireGuard-maskinen.



I dette eksempelet vil jeg fokusere på følgende tilfelle: **fra min Windows Peer 1 som er koblet til hjemmenettverket mitt, ønsker jeg å få tilgang til bedriftsnettverket mitt for å få tilgang til selskapets servere via WireGuard VPN-tunnelen**. Dette gir følgende diagram:



![Image](assets/fr/035.webp)



Når det gjelder IP-adresser, gir dette:





- Hjemmenettverk**: 192.168.1.0/24
- Bedriftsnettverk**: 192.168.100.0/24
- WireGuard-tunnelnettverk**: 192.168.110.0/24


+ IP Address til Peer 1 (Windows) i tunnelen: 192.168.110.2/24


+ IP Address til Peer 2 (Debian) i tunnelen: 192.168.110.121/24



Det er alt som trengs! La oss komme i gang med konfigurasjonen!



**Merk: WireGuard fungerer som standard i UDP-modus på **port 51820**.



## III Installasjon og konfigurasjon av WireGuard-server



Jeg kommer til å bruke begrepene "klient" for Windows-maskinen og "server" for Debian-maskinen i denne veiledningen, for selv om det er peer-to-peer, virker det mer meningsfylt.



### A. Installere WireGuard på Debian 11



WireGuard-installasjonspakken er tilgjengelig i de offisielle Debian 11-repositoriene, så alt vi trenger å gjøre er å oppdatere pakkebufferen og installere den:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



WireGuard-serverdelen installeres, sammen med ulike verktøy som gir tilgang til nyttige kommandoer for å administrere konfigurasjonen.



### B. Installere en Interface WireGuard



Ved hjelp av **kommandoen "wg"** må vi generate en privat nøkkel og en offentlig nøkkel: avgjørende for autentisering mellom to par, dvs. serveren og en klient (som også trenger et nøkkelpar).



Vi oppretter den private nøkkelen "**/etc/wireguard/wg-private.key**" og den offentlige nøkkelen "**/etc/wireguard/wg-public.key**" med denne kommandosekvensen:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Verdien av den offentlige nøkkelen vil bli returnert i konsollen. I WireGuard-konfigurasjonsfilen må vi **legge til verdien av vår private nøkkel**. For å hente denne verdien, skriv inn kommandoen nedenfor og kopier verdien:



```
sudo cat /etc/wireguard/wg-private.key
```



Det er på tide å opprette en konfigurasjonsfil i "**/etc/wireguard/**". Vi kan for eksempel kalle denne filen "**wg0.conf**", hvis vi tenker at Interface-nettverket som er tilknyttet WireGuard, skal være "wg0", etter samme prinsipp som for eksempel "eth0".



```
sudo nano /etc/wireguard/wg0.conf
```



I denne filen må vi først legge til følgende innhold (vi kommer tilbake til å fullføre det senere):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Seksjon `[Interface]` brukes til å deklarere serverdelen. Her er litt informasjon:





- Address**: IP Address til Interface WireGuard innenfor VPN-tunnelen (annet subnett enn det eksterne LAN)
- SaveConfig**: konfigurasjonen lagres (og beskyttes) så lenge Interface er aktiv
- ListenPort**: WireGuards lytteport. I dette tilfellet er 51820 standardporten, men du kan gjerne tilpasse den
- PrivateKey**: verdien av serverens private nøkkel (*wg-private.key*)



Lagre filen og lukk den. Med kommandoen "**wg-quick**" kan vi starte denne Interface ved å angi navnet (wg0, siden filen heter wg0.conf):



```
sudo wg-quick up wg0
```



Hvis du lister opp IP-adressene til Debian 11-serveren din, vil du se en ny Interface med navnet "wg0" med IP Address definert i konfigurasjonsfilen:



```
ip a
```



![Image](assets/fr/027.webp)



I samme ånd kan vi vise Interface "wg0"-konfigurasjonen via kommandoen "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Til slutt må vi aktivere automatisk oppstart av vår Interface wg0 WireGuard:



```
sudo systemctl enable wg-quick@wg0.service
```



For øyeblikket lar vi konfigurasjonen av WireGuards serverside ligge.



### C. Aktiver IP-videresending



For at Debian 11-maskinen vår skal kunne **rute pakker mellom forskjellige nettverk (som en ruter)**, dvs. mellom VPN-nettverket og det lokale nettverket, må vi aktivere [IP Forwarding] (https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Som standard er denne funksjonen deaktivert.



Endre denne konfigurasjonsfilen:



```
sudo nano /etc/sysctl.conf
```



Legg til følgende direktiv på slutten av filen, og lagre:



```
net.ipv4.ip_forward = 1
```



Det er alt det er.



### D. Aktiver IP Masquerade



For at serveren vår skal kunne rute pakker riktig og for at det eksterne LAN-nettverket skal være tilgjengelig for Windows-maskinen, må vi aktivere IP Masquerade på Debian-serveren vår. Dette er en slags NAT-aktivering. Jeg kommer til å utføre denne konfigurasjonen på Linux-brannmuren gjennom UFW, som jeg er vant til å bruke ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Hvis du ikke allerede har UFW og ønsker å sette det opp (du kan også bruke Nftables), begynner du med å installere:



```
sudo apt install ufw
```



Først og fremst må du aktivere SSH for ikke å miste kontrollen over den eksterne serveren (tilpasse portnummeret):



```
sudo ufw allow 22/tcp
```



Port 51820 i UDP må også autoriseres, ettersom vi bruker den til WireGuard (igjen, tilpass portnummeret):



```
sudo ufw allow 51820/udp
```



Nå fortsetter vi med konfigurasjonen for å aktivere IP-maskerade. For å gjøre dette må vi finne navnet på Interface som er koblet til det lokale nettverket. Hvis du ikke vet navnet, kan du kjøre "ip a" for å se navnet på kortet. I mitt tilfelle er det "**ens192**"-kortet.



![Image](assets/fr/036.webp)



Vi skal bruke denne informasjonen. Rediger følgende fil:



```
sudo nano /etc/ufw/before.rules
```



Legg til disse linjene på slutten av filen for å **aktivere IP-maskerade på Interface ens192** (tilpass Interface-navnet) i POSTROUTING-strengen i vår lokale brannmurs NAT-tabell:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Bildet viser:



![Image](assets/fr/037.webp)



Hold denne konfigurasjonsfilen åpen og fortsett til neste trinn. 😉



### E. Konfigurasjon av Linux-brannmur for WireGuard



Fortsatt i den samme konfigurasjonsfilen skal vi deklarere bedriftsnettverket "192.168.100.0/24", slik at vi kan kontakte det. Her er de to reglene som skal legges til (helst etter "*# ok icmp-kode for FORWARD*"-delen for å gruppere reglene sammen):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Hvis du bare vil autorisere én vert, for eksempel "192.168.100.11", er det enkelt:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Nå kan du lagre filen og lukke den. Nå gjenstår det bare å aktivere UFW og starte tjenesten på nytt for å ta endringene i bruk:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Den første delen av konfigurasjonen av Debian-serveren er nå fullført.



## IV. WireGuard-klient for Windows



WireGuard-klienten er tilgjengelig for Windows, macOS, Android osv. Dette er gode nyheter. Alle nedlastinger er tilgjengelige på denne siden: [WireGuard Client] (https://www.wireguard.com/install/). I dette eksemplet skal jeg sette opp klienten på Windows. For å sette opp WireGuard-klienten på Linux følger du samme prinsipp som for å opprette wg0.conf-filen på Debian-maskinen (uten alt NAT osv.).



### A. Installere WireGuard Windows-klienten



Når du har lastet ned den kjørbare filen eller MSI-pakken, er installasjonen enkel: bare start installasjonsprogrammet, og... voilà, det er gjort!



![Image](assets/fr/038.webp)



### B. Opprett en WireGuard-profil



Start med å åpne programvaren for å opprette en ny tunnel. Dette gjør du ved å klikke på pilen til høyre for "**Legg til tunnel**"-knappen og klikke på "**Legg til tom tunnel**"-knappen.



![Image](assets/fr/028.webp)



Et konfigurasjonsvindu åpnes. Hver gang en ny tunnelkonfigurasjon opprettes, genererer WireGuard et privat/offentlig nøkkelpar som er spesifikt for denne konfigurasjonen. **I denne konfigurasjonen må vi oppgi "peer", dvs. den eksterne serveren:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Vi må fullføre denne konfigurasjonen, spesielt for å deklarere IP Address på denne Interface (*Address*), men også for å deklarere den eksterne WireGuard-serveren via en [Peer]-blokk. Bildet nedenfor skal minne deg om konfigurasjonsfilen vi opprettet på Linux-serversiden.



La oss starte med `[Interface]`-blokken, og legge til IP Address "**192.168.110.2**"; husk at serveren har IP Address "**192.168.110.121**" på dette nettverkssegmentet. Dette gir:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Deretter må vi deklarere "Peer"-blokken med tre egenskaper, noe som resulterer i denne konfigurasjonen:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



I bilder:



![Image](assets/fr/029.webp)



**Noen få forklaringer om [Peer]-blokken:





- PublicKey**: dette er den offentlige nøkkelen til WireGuard Debian 11-serveren (du kan få tak i verdien med kommandoen "*sudo wg*")
- AllowedIPs**: dette er IP-adressene/undernettene som er tilgjengelige via dette WireGuard VPN-nettverket, i dette tilfellet undernettet som er spesifikt for mitt WireGuard VPN (*192.168.110.0/24*) og mitt eksterne LAN (*192.168.100.0/24*)
- Sluttpunkt**: dette er IP Address for Debian 11-verten, siden dette er vårt WireGuard-tilkoblingspunkt (du må angi den offentlige IP Address)



Skriv til slutt inn et navn i feltet "**Name**" (uten mellomrom), og kopier og lim inn klientens offentlige nøkkel, siden vi må deklarere den på serveren. Klikk på "**Register**".



### C. Deklarer klienten på WireGuard-serveren



Det er på tide å gå tilbake til Debian-serveren for å erklære "**Peer**", dvs. vår Windows-PC, i WireGuard-konfigurasjonen. Først og fremst må vi **stoppe Interface "wg0"** for å kunne endre konfigurasjonen:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Deretter endrer du den tidligere opprettede konfigurasjonsfilen:



```
sudo nano /etc/wireguard/wg0.conf
```



I denne filen, etter `[Interface]-blokken, må vi deklarere en `[Peer]-blokk:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Denne [Peer]-blokken inneholder Windows 10-PC-enes offentlige nøkkel (**PublicKey**) og IP Address på PC-enes Interface (**AllowedIPs**): Serveren vil kommunisere i denne WireGuard-tunnelen kun for å kontakte Windows-klienten, derav verdien "**192.168.110.2/32**".



Det eneste som gjenstår er å lagre filen (*CTRL+O og deretter Enter og CTRL+X via Nano*). Start Interface "wg0" på nytt:



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Du kan bruke denne kommandoen for å kontrollere at peer-erklæringen fungerer:



```
sudo wg show
```



Når den eksterne verten har konfigurert WireGuard-tilkoblingen, flyttes IP Address opp til "endepunkt"-verdien.



![Image](assets/fr/033.webp)



Til slutt sikrer vi konfigurasjonsfilene for å begrense root-tilgang:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Første WireGuard-tilkobling



Nå som konfigurasjonen er klar, kan vi starte den fra Windows-PC-en. For å gjøre dette, i "**WireGuard**"-klienten, klikker du på "**Activate**"-knappen: tilkoblingen vil **endre fra "Off" til "On"**, men det betyr ikke at den vil fungere. Alt avhenger av om konfigurasjonen din er riktig eller ikke. **Når forbindelsen er opprettet, kommuniserer våre to maskiner via Interface WireGuard som er konfigurert på hver side!



![Image](assets/fr/030.webp)



Hvis det oppstår et problem, vil dette være synlig i "**Logbook**"-fanen. De to vertene vil jevnlig sende ut Exchange-pakker for å sjekke statusen til forbindelsen, derav meldingene "*Receiving keepalive packet from peer 1*".



![Image](assets/fr/031.webp)



Hvis WireGuards "**Journal**"-fane viser en melding som den nedenfor, må du kontrollere at de offentlige nøklene som er oppgitt på begge sider, er korrekte.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Fra min eksterne PC kan jeg pinge IP Address til Interface WireGuard på serversiden, samt en vert på mitt eksterne LAN.



![Image](assets/fr/032.webp)



### E. Ytelse: OpenVPN vs WireGuard



Fra min eksterne PC som er koblet til WireGuard VPN, kunne jeg få tilgang til en filserver og overføre en fil via [SMB] (https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), for å se overføringshastigheten. **Med WireGuard når jeg maks 45 Mb/s, noe som er flott, siden jeg er på WiFi



![Image](assets/fr/025.webp)



Under de samme forholdene, men via en OpenVPN-tilkobling (i UDP) denne gangen, med samme operasjon, er gjennomstrømningen en helt annen: rundt 3 MB/s. Forskjellen er åpenbar!



![Image](assets/fr/026.webp)



Dette er interessant, for hvis du for eksempel bytter fra en WiFi-tilkobling til en 4G/5G-tilkobling, vil gjenoppkoblingen være så rask at avbruddet ikke vil være synlig.



### F. Bonus: WireGuard med full tunnel



Med den nåværende konfigurasjonen flyter en del av trafikken gjennom VPN-et, og resten gjennom kundens Internett-tilkobling, inkludert surfing på Internett. Hvis vi ønsker å bytte til WireGuard **full tunnelmodus**, slik at alt går gjennom VPN-tunnelen, må vi gjøre noen få endringer i konfigurasjonen vår....



Først må du installere pakken "resolvconf" på:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Når dette er gjort, må du endre "wg0.conf"-profilen på Debian-maskinen: stopp Interface, endre den, og start på nytt.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Deretter **legger vi til DNS-serveren som skal brukes** i blokken `[Interface]`. I mitt tilfelle er det laboratoriets domenekontroller, men vi kan også installere Bind9 på Debian-maskinen for å ha en lokal resolver.



```
DNS = 192.168.100.11
```



Lagre filen, og start deretter Interface på nytt:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Til slutt, i tunnelkonfigurasjonen på Windows 10-arbeidsstasjonen, må du endre delen "AllowedIPs" for å indikere at alt må passere gjennom tunnelen. Erstatt:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Av:



```
AllowedIPs = 0.0.0.0/0
```



Du kan se at dette også aktiverer alternativet "**Kill switch*".



![Image](assets/fr/040.webp)



Til slutt benyttet jeg den fulle tunnelen til å gjennomføre en liten strømningstest, og resultatene vises nedenfor:



![Image](assets/fr/039.webp)



WireGuards konfigurasjon er ganske enkel og lett å forstå, og fremfor alt å vedlikeholde. **WireGuard anses å være fremtiden for VPN**, så vi bør holde et godt øye med det! Vi kan også se at fordelen er betydelig når det gjelder ytelse, noe som er en stor fordel for WireGuard sammenlignet med OpenVPN.



Ytterligere dokumentasjon:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Kommando wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**WireGuard VPN er oppe og går! Vi gratulerer!