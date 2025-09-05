---
name: OPNsense
description: Hvordan installerer og konfigurerer jeg en OPNsense-brannmur?
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian BURNEL publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___



## I. Presentasjon



I denne veiledningen skal vi ta en titt på OPNsense-brannmuren med åpen kildekode. Vi ser på hovedfunksjonene, forutsetningene og hvordan du installerer denne FreeBSD-baserte løsningen.



Før du begynner, bør du vite at **OPNsense og pfSense begge er brannmurer med åpen kildekode** basert på FreeBSD. Vi kan si at pfSense er en slags storebror til OPNsense, ettersom sistnevnte er en Fork som ble opprettet i 2015. Til slutt er det viktig å påpeke at siden 2017 har **OPNsense gått over til HardenedBSD i stedet for FreeBSD**. HardenedBSD er en forbedret versjon av FreeBSD, med avanserte sikkerhetsfunksjoner



OPNsense skiller seg ut med sin mer moderne bruker-Interface og **hyppigere oppdateringskadence**. OPNsense har nemlig to større utgivelser per år, som oppdateres omtrent annenhver uke (noe som resulterer i mindre utgivelser). Denne oppfølgingen er svært interessant sammenlignet med pfSense, hvis vi ser på community-versjonene av disse løsningene.



![Image](assets/fr/050.webp)



## II. OPNsense-funksjoner



OPNsense er et operativsystem som er utviklet for å fungere som brannmur og ruter, selv om det har mange funksjoner som kan utvides ved å installere tilleggspakker. Det egner seg for produksjonsbruk og brukes hovedsakelig til nettverkssikkerhet og flytstyring.



### A. Hovedfunksjoner



Her er noen av OPNsense' viktigste funksjoner:





- Brannmur og NAT**: OPNsense tilbyr avansert stateful brannmurfunksjonalitet med stateful filtrering, samt NAT-funksjoner (Network Address Translation).





- DNS/DHCP**: OPNsense kan konfigureres til å administrere DNS- og DHCP-tjenester i nettverket. Den kan fungere som en DHCP-server, men kan også brukes som en DNS-oppløser for maskiner i det lokale nettverket. Dnsmasq er også integrert som standard.





- VPN**: OPNsense støtter flere VPN-protokoller, inkludert IPsec, OpenVPN og WireGuard, noe som muliggjør sikre tilkoblinger for ekstern tilgang til mobile arbeidsstasjoner eller sammenkobling av nettsteder.





- Nettproxy**: OPNsense inkluderer en webproxy for å kontrollere og filtrere Internett-tilgang. Den kan også brukes til å filtrere innhold og administrere nettverkstilgang.





- Administrasjon av båndbredde (QoS)**: OPNsense tilbyr QoS-styringsfunksjoner (Quality of Service) for å prioritere nettverkstrafikk og administrere nettverksbåndbredde på en bedre måte.





- Captive portal**: Med denne funksjonen kan du administrere brukertilgang til nettverket via en autentiseringsside (lokal base, kuponger osv.). Dette er en funksjon som ofte brukes i offentlige Wi-Fi-nettverk.





- IDS/IPS**: OPNsense integrerer Suricata for å tilby IDS/IPS-funksjoner (intrusion detection and prevention) for å beskytte nettverket mot angrep.





- Høy tilgjengelighet (CARP)**: OPNsense støtter CARP (*Common Address Redundancy Protocol*) for høy tilgjengelighet mellom flere OPNsense-brannmurer, noe som sikrer at tjenesten forblir aktiv selv i tilfelle maskinvarefeil.





- Rapportering og overvåking**: OPNsense tilbyr rapporterings- og overvåkingsverktøy i sanntid for å spore nettverksytelsen (med NetFlow) og oppdage potensielle problemer, takket være loggene som opprettes. Dette inkluderer grafikk. Monit-verktøyet er integrert i OPNsense og gjør det mulig å overvåke selve brannmuren.



### B. Tilleggspakker



Dette er bare en oversikt over funksjonene som OPNsense tilbyr. I tillegg kan du via **pakkekatalogen**, som er tilgjengelig fra OPNsense-administrasjonen Interface, **berike brannmuren med tilleggsfunksjoner**. Disse inkluderer en ACME-klient, en Wazuh-agent, NTP Chrony-tjenesten og Caddy som en omvendt proxy.



![Image](assets/fr/051.webp)



## III. Forutsetninger for OPNsense



Først og fremst må du bestemme deg for hvor du skal installere OPNsense. Det finnes flere mulige løsninger, blant annet installasjon på:





- En hypervisor som en virtuell maskin, enten det er Hyper-V, Proxmox, VMware ESXi osv.
- En maskin som et *bare-metal*-system. Dette kan være en mini-PC som fungerer som brannmur.



Du kan også kjøpe **et OPNsense rackmonterbart apparat** i nettbutikken vår.



Du må ta hensyn til maskinvareressursene som kreves for å kjøre OPNsense. Dette er beskrevet på [denne dokumentasjonssiden] (https://docs.opnsense.org/manual/hardware.html).



**Minimum og anbefalte ressurser for produksjon:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Til slutt: **Ressursbehovet ditt avhenger først og fremst av antall tilkoblinger som skal administreres**, og dermed av **båndbreddebehovet**. I tillegg må du **ha i tankene hvilke tjenester som skal aktiveres og brukes** (proxy, inntrengingsdeteksjon osv.), ettersom de kan være CPU- og/eller RAM-krevende.



Du trenger også OPNsense-installasjonens ISO-bilde, som du kan laste ned fra [det offisielle nettstedet] (https://opnsense.org/download/). For installasjon på en virtuell maskin velger du "**dvd**" som avbildningstype for å få et ISO-bilde (og gjør hva du vil med det ...). For installasjon via en oppstartbar USB-nøkkel velger du alternativet "**vga**" for å få en "**.img**"-fil.



![Image](assets/fr/048.webp)



Du trenger også en datamaskin for å administrere og teste OPNsense.



## IV. Målkonfigurasjon



Vårt mål er å





- Opprett et internt virtuelt nettverk (192.168.10.0/24 - LAN)**, som har tilgang til Internett via OPNsense-brannmuren. For produksjonsbruk kan dette være ditt lokale nettverk, kabel og/eller Wi-Fi.
- Aktiver og konfigurer NAT** slik at VM-er i det interne virtuelle nettverket får tilgang til Internett
- Aktiver og konfigurer DHCP-serveren på OPNsense** for å distribuere en IP-konfigurasjon til fremtidige maskiner som er koblet til det interne virtuelle nettverket
- Konfigurer brannmuren** slik at den kun tillater utgående LAN til WAN-strømmer i HTTP (80) og HTTPS (443).
- Konfigurer brannmuren** slik at det virtuelle LAN-et kan bruke OPNsense som DNS-oppløser (53).



Hvis du bruker Hyper-V-plattformen, får du følgende fremstilling:



![Image](assets/fr/033.webp)



## V. Installere OPNsense-brannmuren



### A. Klargjøring av oppstartbar USB-nøkkel



Det første trinnet er å klargjøre installasjonsmediet: **den oppstartbare USB-nøkkelen med OPNsense**. Dette er selvsagt valgfritt hvis du jobber i et virtuelt miljø, men du må uansett laste ned ISO-bildet for OPNsense-installasjonen.



Etter nedlasting får du **et arkiv som inneholder et bilde i ".img"**-format. Du kan **opprette en oppstartbar USB-pinne** med forskjellige programmer, inkludert **balenaEtcher**: ultraenkelt å bruke. Programmet vil dessuten gjenkjenne avbildningen i arkivet, slik at du ikke trenger å dekomprimere den på forhånd.





- [Last ned balenaEtcher] (https://etcher.balena.io/)



Når programmet er installert, velger du bildet ditt, USB-nøkkelen din og klikker deretter på "Flash! Vent et øyeblikk.



![Image](assets/fr/049.webp)



Nå er du klar til å installere.



### B. Installere OPNsense-systemet



Start opp maskinen som er vert for OPNsense. Du bør se en velkomstside som ligner på den nedenfor. I noen sekunder vil skjermbildet som vises, være synlig i vinduet. La prosessen gå sin gang...



![Image](assets/fr/019.webp)



OPNsense-bildet lastes inn på maskinen, slik at systemet kan brukes i "**live**"-modus, dvs. midlertidig lagret i minnet.



![Image](assets/fr/025.webp)



Da kommer du til en Interface som ligner på den nedenfor. Logg inn med innlogging "**installer**" og passord "**opnsense**". Vær oppmerksom på at tastaturet for øyeblikket er **QWERTY**. Nå skal vi **starte installasjonsprosessen for OPNsense**.



![Image](assets/fr/026.webp)



En ny veiviser vises på skjermen. Det første trinnet er å velge tastaturoppsettet som passer til din konfigurasjon. For et AZERTY-tastatur velger du alternativet "**Fransk (aksenttaster)**" fra listen, og dobbeltklikker deretter på**.



![Image](assets/fr/027.webp)



Det andre trinnet er å velge hvilken oppgave som skal utføres. Her skal vi utføre en installasjon ved hjelp av **ZFS-filsystemet**. Still deg på linjen "**Install (ZFS)**", og bekreft med **Enter**.



![Image](assets/fr/028.webp)



I det tredje trinnet velger du "**stripe**", ettersom maskinen vår er utstyrt med **kun én disk**: Det er ikke mulig å sikre brannmurlagringen og dataene der uten redundans. Dette er spesielt relevant ved installasjon på en fysisk maskin for å beskytte mot maskinvarefeil på en disk, via RAID-prinsippet.



![Image](assets/fr/029.webp)



I det fjerde trinnet trykker du bare på **Enter** for å bekrefte.



![Image](assets/fr/030.webp)



Bekreft til slutt ved å velge "**YES**" og deretter trykke på tasten **Enter**.



![Image](assets/fr/031.webp)



Nå må du vente mens OPNsense installeres. Denne prosessen tar omtrent 5 minutter.



![Image](assets/fr/032.webp)



Når installasjonen er fullført, kan vi endre "**root**"-passordet før vi starter på nytt. Velg "**Root Password**", trykk **Enter** og skriv inn passordet "**root**" to ganger.



![Image](assets/fr/020.webp)



Til slutt velger du "**Complete Install**" og trykker på **Enter**. Benytt anledningen til å **skrive ut disken fra VM-ens DVD-stasjon**. I VM-innstillingene kan du også angi første oppstart til disk.



![Image](assets/fr/021.webp)



Den virtuelle maskinen vil starte på nytt og laste inn OPNsense-systemet fra disken, siden vi nettopp har installert det. Logg inn med "root"-kontoen i konsollen og det nye passordet ditt (ellers er standardpassordet "**opnsense**").



### D. Koble sammen nettverksgrensesnitt



Skjermbildet nedenfor vises. Velg "**1**" og trykk **Enter** for å knytte maskinens nettverkskort til OPNsense-grensesnittene.



![Image](assets/fr/022.webp)



Først ber veiviseren deg om å konfigurere koblingsaggregering og VLAN. Angi "**n**" for å nekte, og bekreft svaret ditt hver gang med **Enter**. Deretter må du tilordne de to grensesnittene "**hn0**" og "**hn1**" til **WAN** og **LAN**. I prinsippet tilsvarer "**hn0**" WAN og den andre Interface tilsvarer LAN.



Slik fungerer det:



![Image](assets/fr/023.webp)



Vi har nå:





- Interface **LAN** tilknyttet nettverkskortet "**hn1**" og med OPNsense standard IP Address, dvs. **192.168.1.1/24**.
- Interface **WAN** tilknyttet nettverkskortet "**hn0**" og med en IP Address hentet via **DHCP** på det lokale nettverket (takket være den eksterne virtuelle svitsjen vår).



Som standard er OPNsense-administrasjonen Interface bare tilgjengelig fra LAN Interface, av åpenbare sikkerhetsgrunner. Du må derfor koble deg til brannmurens Interface LAN for å utføre administrasjon. Hvis dette ikke er mulig, kan du midlertidig administrere OPNsense fra WAN. Dette innebærer å deaktivere brannmurfunksjonen.



Dette gjør du ved å bytte til skallmodus via alternativet "**8**" og kjøre følgende kommando:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Tilgang til OPNsense Interface-styringssystemet



Du får tilgang til OPNsense Administration Interface via HTTPS, ved hjelp av IP Address på LAN** Interface (eller WAN). Nettleseren din tar deg til en påloggingsside. Logg inn med "root"-kontoen og passordet du valgte tidligere.



![Image](assets/fr/034.webp)



Vent noen sekunder... Du blir bedt om å følge en veiviser for å utføre den grunnleggende konfigurasjonen. Klikk på "**Neste**" for å fortsette.



![Image](assets/fr/036.webp)



Det første trinnet er å definere vertsnavnet, domenenavnet, velge språk og definere DNS-serveren(e) som skal brukes til navneoppløsning. Hvis du beholder alternativet "**Enable Resolver**", kan brannmuren brukes som DNS-oppløser, noe som vil være nyttig for maskinene i vårt virtuelle LAN.



![Image](assets/fr/037.webp)



Gå videre til neste trinn. Veiviseren gir deg muligheten til å **definere en NTP-server for synkronisering av dato og klokkeslett**, selv om det allerede er konfigurert servere som standard. I tillegg er det viktig å velge tidssonen som tilsvarer din geografiske plassering (med mindre du har spesielle krav).



![Image](assets/fr/038.webp)



Deretter kommer et viktig trinn: **konfigurere Interface WAN**. For øyeblikket er den konfigurert i DHCP og vil forbli i denne konfigurasjonsmodusen, med mindre du ønsker å angi en statisk IP for Address.



![Image](assets/fr/039.webp)



På konfigurasjonssiden for Interface WAN må du fortsatt fjerne merket for alternativet "**Block access to private networks via WAN**" hvis nettverket på WAN-siden bruker privat adressering. Dette vil sannsynligvis være tilfelle hvis du kjører en lab, og kan dermed hindre deg i å få tilgang til Internett.



![Image](assets/fr/040.webp)



Deretter kan du **definere et "root"**-passord, men dette er valgfritt fordi vi allerede har gjort det.



![Image](assets/fr/041.webp)



Fortsett til slutten for å starte konfigurasjonsinnlastingen. Hvis du trenger å fortsette å ta kontroll via WAN, starter du kommandoen ovenfor på nytt når denne prosessen er fullført.



![Image](assets/fr/042.webp)



Det er alt som skal til!



![Image](assets/fr/035.webp)



### E. DHCP-konfigurasjon



Målet vårt er å bruke OPNsense DHCP-serveren til å distribuere IP-adresser på det virtuelle LAN-et. For å gjøre dette må vi få tilgang til denne menyplasseringen:



```
Services > ISC DHCPv4 > [LAN]
```



**Som du ser, er DHCP allerede aktivert som standard på LAN ** Hvis du ikke er interessert i denne tjenesten, bør du deaktivere den. Selv om den allerede er aktivert og vi ønsker å bruke den, er det viktig å gå gjennom konfigurasjonen.



Om nødvendig kan du endre utvalget av IP-adresser som skal distribueres: **192.168.10.10** til **192.168.10.245**, avhengig av gjeldende innstillinger.



![Image](assets/fr/046.webp)



Vi kan også se at feltene "**DNS servers**", "**Gateway**", "**Domain name**" osv. er tomme som standard. Det er faktisk en automatisk arv av visse alternativer og standardverdier for disse ulike feltene. For eksempel, for DNS-serveren vil IP Address i Interface LAN bli distribuert, slik at OPNsense-brannmuren kan brukes som DNS-oppløser.



Lagre konfigurasjonen etter at du har gjort eventuelle endringer.



![Image](assets/fr/047.webp)



For å teste DHCP-serveren må du koble en maskin til brannmurens LAN-nettverk.



Denne maskinen må få en IP Address fra OPNsense DHCP-serveren, og maskinen vår må ha tilgang til nettverket. Internett-tilgangen må fungere. Vær oppmerksom på at hvis du har deaktivert brannmurfunksjonen for å få tilgang til OPNsense fra WAN, vil dette deaktivere NAT, slik at du ikke får tilgang til nettet.



**Merknad**: Utstedte DHCP-leiekontrakter er synlige fra OPNsense-administrasjonen Interface. For å gjøre dette går du til følgende sted: **Tjenester > ISC DHCPv4 > Leiekontrakter**.



![Image](assets/fr/045.webp)



### F. Konfigurere NAT og brannmurregler



Den gode nyheten er at vi nå kan få tilgang til OPNsense-administrasjonen Interface fra LAN.



```
https://192.168.1.10
```



Etter å ha logget på OPNsense, la oss finne NAT-konfigurasjonen. Gå til denne plasseringen: **Brannmur > NAT > Utgående**. Her kan du velge mellom automatisk (standard) og manuell oppretting av utgående NAT-regler.



Velg automatisk modus via alternativet "**Automatisk generering av utgående NAT-regler**", og klikk på "**Lagre**" (i prinsippet er denne konfigurasjonen allerede den aktive). I automatisk modus oppretter OPNsense selv en NAT-regel for hvert av nettverkene dine.



![Image](assets/fr/043.webp)



Inntil videre kan alle datamaskiner som er koblet til det virtuelle LAN "**192.168.10.0/24**", få ubegrenset tilgang til Internett. Målet vårt er imidlertid å begrense tilgangen til WAN til HTTP- og HTTPS-protokoller, samt DNS på brannmurens Interface LAN.



Vi må derfor opprette brannmurregler... Bla gjennom menyen på følgende måte: **Brannmur > Regler > LAN**.



**Som standard er det to regler for å autorisere all utgående LAN-trafikk, i IPv4 og IPv6**. Deaktiver disse to reglene ved å klikke på Green-pilen helt til venstre, i begynnelsen av hver linje.



Deretter oppretter du tre nye regler for å autorisere **LAN-nettverket** (dvs. "**LAN net**") til:





- få tilgang til alle destinasjoner ved hjelp av **HTTP**.
- få tilgang til alle destinasjoner med **HTTPS**.
- be om **OPNsense** på sitt **Interface LAN** (dvs. "**LAN Address**"), via **DNS-protokollen** (dette innebærer å bruke brannmuren som DNS), ellers autoriserer du DNS-oppløseren din via IP Address.



Dette gir følgende resultat:



![Image](assets/fr/044.webp)



Det eneste som gjenstår, er å klikke på "**Apply changes**" for å overføre de nye brannmurreglene til produksjon. **Vær oppmerksom på at alle strømmer som ikke er eksplisitt autorisert, vil bli blokkert som standard



LAN-maskinen kan få tilgang til Internett ved hjelp av HTTP og HTTPS. Alle andre protokoller vil bli blokkert.



![Image](assets/fr/018.webp)



## IV. Konklusjon



Ved å følge denne veiledningen kan du installere OPNsense og komme i gang med en gang. OPNsense tilbyr et bredt spekter av funksjoner for å sikre og administrere nettverkstrafikken på en effektiv måte, og er egnet for bruk i profesjonelle miljøer.



Denne installasjonen er bare begynnelsen: Utforsk gjerne menyene og konfigurer andre funksjoner for å tilpasse OPNsense til dine behov.