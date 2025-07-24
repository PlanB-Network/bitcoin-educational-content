---
name: pfSense
description: Installere Pfsense
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian BURNEL publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det er gjort store endringer i forfatterens opprinnelige tekst for å oppdatere veiledningen



___



![Image](assets/fr/027.webp)



## I. Presentasjon



pfSense er et gratis operativsystem med åpen kildekode som forvandler en hvilken som helst datamaskin, dedikert server eller maskinvareappliance til en høytytende, konfigurerbar ruter og brannmur. PfSense er basert på FreeBSD og er kjent for sin stabile og robuste nettverksarkitektur. I over femten år har pfSense satt standarden for brannmurer med åpen kildekode for bedrifter, kommuner og krevende hjemmebrukere.



Hovedfunksjonene har utviklet seg betydelig gjennom årene, og har blitt forbedret med hver nye versjon. Til dags dato tilbyr pfSense :





- Komplett, sentralisert administrasjon via en moderne, intuitiv og sikker Interface-web Interface.
- Tilstandsbrannmur med høy ytelse, avansert NAT-støtte (inkludert NAT-T) og detaljert regeladministrasjon.
- Native multi-WAN-støtte, noe som muliggjør aggregering eller redundans av Internett-tilkoblinger.
- Integrert DHCP-server og relé.
- Høy tilgjengelighet takket være CARP-protokollen for failover og muligheten for å konfigurere pfSense-klynger.
- Lastbalansering mellom flere tilkoblinger eller servere.
- Full VPN-støtte: IPsec, OpenVPN og WireGuard (erstatter L2TP, som nå er foreldet).
- Konfigurerbar portal for tilgangskontroll for gjester, spesielt i offentlige miljøer eller hotellmiljøer.



pfSense har også et utvidbart pakkesystem som gjør det enkelt å legge til avanserte funksjoner som en transparent proxy (Squid), URL-filtrering eller IDS/IPS (Snort eller Suricata) direkte fra Interface-nettverket.



pfSense distribueres kun for 64-bits plattformer, i tråd med gjeldende FreeBSD-anbefalinger. Det kan installeres på standard maskinvare (PC-er, rackservere) eller på innebygde plattformer med lavt strømforbruk, for eksempel Netgate-apparater eller visse x86-bokser med lav profil, som er langt kraftigere enn eldre Alix-bokser.



Til slutt er det verdt å huske at pfSense krever minst to fysiske nettverksgrensesnitt: ett dedikert til den eksterne sonen (WAN) og ett dedikert til det interne nettverket (LAN). Avhengig av hvor kompleks infrastrukturen din er (DMZ, VLAN, flere WAN-er), kan det være nødvendig med flere grensesnitt for å dra full nytte av funksjonene.



## II. Last ned bilde



Den siste stabile versjonen av pfSense, i skrivende stund, er 2.8 (utgitt i juni 2025). Du kan laste ned ISO-bildet eller installasjonsfilen som er tilpasset ditt maskinvaremiljø direkte fra det offisielle nettstedet :





- [Last ned pfSense] (https://www.pfsense.org/download/)



Nedlastingsportalen lar deg velge :





- Arkitektur (vanligvis **AMD64** for all moderne maskinvare).
- Bildetype (**Installer USB Memstick** for installasjon via USB-minnepinne, **ISO Installer** for brenning eller virtuell redigering).
- Nærmeste nedlastingsspeil for å optimalisere overføringshastigheten.



For de som ønsker å distribuere pfSense i et virtualisert miljø (Proxmox, VMware ESXi, VirtualBox ...), er det også tilgjengelig et **OVA**-bilde. Denne bruksklare virtuelle maskinen forenkler installasjonen og den første konfigurasjonen. Bare sørg for at du justerer de tildelte ressursene (CPU, RAM, nettverksgrensesnitt) i henhold til forventet belastning og nettverkstopologi.



Før installasjon anbefaler vi at du kontrollerer integriteten til den nedlastede filen ved å verifisere **SHA256** som er oppgitt på den offisielle nedlastingssiden. Dette sikrer at bildet ikke har blitt endret eller ødelagt.



## III. Installasjon



I dette eksemplet utføres installasjonen på en virtuell maskin som kjører VirtualBox. Fremgangsmåten er helt identisk på en fysisk maskin eller en hvilken som helst annen hypervisor, med unntak av administrasjon av virtuelle enheter.



### 1. Minimumskrav til maskinvare



For en standard distribusjon anbefaler vi :





- minst 1 GB RAM** (2 GB eller mer anbefales for å aktivere tilleggspakker eller støtte for ZFS).
- 8 GB diskplass** (20 GB eller mer er å foretrekke for mer avanserte konfigurasjoner, spesielt hvis du installerer en proxy-cache, IDS/IPS eller detaljerte logger).
- Minst to virtuelle nettverksgrensesnitt** (ett for WAN og ett for LAN). I VirtualBox legger du dem til i VM-innstillingene før oppstart.



### 2. Oppstart av installasjonsprogrammet



Monter det nedlastede ISO-bildet som en virtuell optisk stasjon i VirtualBox, eller sett inn USB-nøkkelen hvis du installerer på en fysisk maskin. Ved oppstart vises en oppstartsmeny:



Hvis du ikke velger noen alternativer, vil pfSense automatisk starte opp med standardalternativene etter noen sekunder. Trykk på "**Enter**"-tasten for å starte normal oppstart.



![Image](assets/fr/027.webp)



Når hovedmenyen vises, trykker du raskt på "**I**"-knappen for å starte installasjonen.



![Image](assets/fr/001.webp)



### 3. Innledende installasjonsinnstillinger



I det første skjermbildet kan du angi noen få regionale parametere, for eksempel skrifttype og tegnkoding. Disse innstillingene er nyttige i spesielle tilfeller (tastaturer som ikke er standard, serielle skjermer, orientalske språk). For de fleste installasjoner bør du beholde standardverdiene og velge "**Accept these Settings**".



![Image](assets/fr/002.webp)



### 4. Valg av installasjonsmodus



Velg "**Quick/Easy Install**" for å kjøre en automatisert installasjon med de anbefalte alternativene. Denne metoden sletter den valgte disken og konfigurerer pfSense med standardpartisjoneringen.



![Image](assets/fr/003.webp)



Det vises en advarsel om at alle data på disken vil bli slettet. Bekreft med "**OK**".



Installasjonsprogrammet kopierer deretter de nødvendige filene til disken. Avhengig av maskinvaren din kan dette ta fra noen sekunder til noen minutter.



### 5. Kjerneutvalg



Når installasjonsprogrammet ber deg om å velge kjernetype, lar du "**Standard Kernel**" være valgt. Denne generiske kjernen passer perfekt til standardinstallasjoner, enten det er på en PC, server eller VM.



### 6. Avslutt installasjonen og start på nytt



Når installasjonen er fullført, velger du "**Reboot**" for å starte maskinen på nytt i den nye pfSense-forekomsten.



**Viktig merknad**: Fjern ISO-bildet eller koble fra USB-nøkkelen før du starter på nytt, slik at du unngår å starte installasjonsprogrammet på nytt neste gang du starter.



## IV. Starte pfSense for første gang



Ved første oppstart må pfSense konfigureres til å gjenkjenne og tilordne nettverksgrensesnittene (WAN, LAN, DMZ, VLAN osv.) på riktig måte. Det er viktig å identifisere nettverkskortene nøye for å unngå konfigurasjonsfeil som kan føre til at du ikke får tilgang til Interface-nettverket eller at brannmuren ikke fungerer.



Når pfSense startes, oppdager og lister den automatisk opp alle tilgjengelige nettverksgrensesnitt, med angivelse av MAC Address for hvert enkelt. Dette gjør det enkelt å skille mellom dem.



### 1. VLAN



Det første spørsmålet gjelder konfigurasjon av VLAN. På dette stadiet, for en grunnleggende konfigurasjon, vil vi ikke aktivere noen VLAN. Trykk derfor på "**N**"-tasten for å hoppe over dette trinnet.



![Image](assets/fr/004.webp)



### 2. WAN og LAN Interface Assignment



pfSense ber deg deretter om å definere hvilken Interface som skal brukes til WAN (Internett-tilgang). Du kan velge mellom :





- Skriv inn Interface-navnet manuelt (anbefales for virtuelle miljøer).
- Bruk automatisk deteksjon ved å trykke på "**A**". Dette alternativet er nyttig på en fysisk vert, forutsatt at nettverkskablene er tilkoblet og koblingene er aktive.



![Image](assets/fr/005.webp)



I dette eksemplet konfigurerer vi WAN manuelt. Skriv inn det nøyaktige navnet på Interface. For et Intel-kort vil navnet ofte være "**em0**" under FreeBSD, men det kan variere avhengig av maskinvaren. For eksempel vil et Realtek-kort ofte vises som "**re0**".



![Image](assets/fr/006.webp)



Gjenta samme operasjon for å definere Interface LAN. Her bruker vi "**em1**".



pfSense bekrefter at Interface LAN aktiverer både brannmur og NAT for å beskytte det interne nettverket og håndtere Address-oversettelse.



Hvis du har andre fysiske grensesnitt, kan du konfigurere flere grensesnitt (DMZ, Wi-Fi, spesifikke VLAN) på dette stadiet. Hver logiske Interface krever et tilsvarende nettverkskort eller en virtuell Interface. I den innledende konfigurasjonen begrenser vi oss til WAN og LAN.



Når tildelingen er fullført, viser pfSense en oversiktlig oppsummering av korrespondansen mellom de fysiske grensesnittene og de tildelte rollene. Bekreft med "**Y**".



### 3. PfSense-konsollen



Når dette trinnet er fullført, vises hovedmenyen i pfSense-konsollen. Den tilbyr flere nyttige alternativer for direkte administrasjon, for eksempel tilbakestilling av webpassordet, omstart, omlasting av konfigurasjonen eller ny tildeling av grensesnitt.



![Image](assets/fr/007.webp)



Du vil også se et sammendrag av gjeldende nettverksinnstillinger, inkludert Interface LANs standard IP Address, vanligvis **192.168.1.1**. Dette er Address du må skrive inn i nettleseren for å få tilgang til administrasjonsnettverket for Interface.



**Merknad**: Hvis ditt interne nettverk bruker et annet Address-område, velger du "**2)** Set Interface(s) IP Address" i menyen for å tilordne en IP Address som passer til ditt miljø.



Hvis Interface WAN er koblet til en DHCP-konfigurert boks eller modem, vil pfSense som standard automatisk hente en offentlig IP Address. Du kan derfor dra nytte av umiddelbar Internett-tilgang ved å koble en klient til pfSense Interface LAN.



## V. Første tilgang til Interface web



Når den første oppstarten er fullført og nettverksgrensesnittene er konfigurert, kan du gå inn på pfSense Interface web for å fullføre og finjustere konfigurasjonen.



### 1. Første tilkobling



Koble en datamaskin til LAN-porten (eller det virtuelle Interface-LAN-et i hypervisor), og tildel den en IP Address i samme område om nødvendig (som standard distribuerer pfSense automatisk en Address via DHCP på LAN).



Gå til Address i nettleseren din, som er angitt av konsollen (som standard `https://192.168.1.1`). Merk at pfSense krever HTTPS selv for den første tilkoblingen - så forvent en advarsel om et selvsignert sertifikat, som du kan ignorere ved å legge til et unntak.



Innloggingsskjermen vises. Standard påloggingsinformasjon er :




- Brukernavn:** `admin`
- Passord:** `pfsense`



Disse identifikatorene vil bli endret under den første konfigurasjonsveiviseren.



## VI. Veiviser for oppsett



Ved første tilkobling ber pfSense deg om å følge **Setup Wizard**. Vi anbefaler på det sterkeste at du bruker den for å sikre at alle viktige parametere er riktig definert.



### 1. Generelle parametere



Du kan :




- Angi et vertsnavn og et lokalt domene (eksempel: `pfsense` og `lan.local`).
- Definer DNS-servere, og velg om pfSense skal bruke Internett-leverandørens DNS eller en ekstern tjeneste (Cloudflare, OpenDNS, Quad9...).



### 2. Tidssone



Angi nettstedets tidssone slik at logger og tidsplaner er konsistente (f.eks. `Europe/Paris`).



### 3. WAN-konfigurasjon



Konfigurere WAN-tilkoblingen :




- Standardinnstillingen er **DHCP** (tilstrekkelig hvis du befinner deg bak en boks).
- Hvis du har en fast IP, må du angi parametrene (statisk IP, maske, gateway, DNS) manuelt.
- Definer om nødvendig et VLAN eller PPPoE-godkjenning (vanlig hos enkelte Internett-leverandører).



### 4. LAN-konfigurasjon



Veiviseren foreslår at du endrer standard LAN-delnett. Hvis du har en spesifikk adresseringsplan, er det nå på tide å tilpasse den.



### 5. Endre administratorpassord



Sikre pfSense ved å angi et sterkt passord for `admin`-brukeren med en gang.



## VII. Verifisering og oppdateringer



Før du tar i bruk brannmuren, må du sørge for at du har den nyeste versjonen av :





- Gå til **System > Oppdater**.
- Velg oppdateringskanal (vanligvis **Stable**).
- Se etter oppdateringer, og bruk dem.



Det er lurt å aktivere oppdateringsvarsler for å holde deg informert om sikkerhetsoppdateringer.



## VIII. Lagre konfigurasjonen



Før du gjør større endringer, bør du implementere en policy for sikkerhetskopiering:





- Gå til **Diagnostikk > Sikkerhetskopiering og gjenoppretting**.
- Last ned en kopi av den gjeldende konfigurasjonen (`config.xml`).
- Oppbevar den på et trygt sted (kryptert eksternt medium).



For virksomhetskritiske miljøer bør du vurdere automatisk sikkerhetskopiering av konfigurasjonen på en ekstern server eller via et programmert skript.



## IX. Beste praksis etter installasjon



For å avslutte utplasseringen med ro i sjelen :





- Endre brannmurregler**: pfSense tillater som standard all utgående trafikk på LAN og blokkerer innkommende trafikk på WAN. Juster disse reglene etter behov.
- Konfigurer sikker ekstern tilgang**: Hvis det er nødvendig, aktiverer du tilgang til Interface web fra WAN kun via VPN eller med IP-begrensninger.
- Aktiver varslinger**: Konfigurer en SMTP-server til å motta varsler (feil, oppdateringer, feil).
- Installer nyttige utvidelser**: for eksempel IDS/IPS (Snort, Suricata), proxy (Squid), DNS-filtrering (pfBlockerNG).



Din pfSense-brannmur er nå oppe og går, klar til å beskytte nettverket ditt. Takket være fleksibiliteten og det aktive fellesskapet har du et kraftig, skalerbart verktøy som kan tilpasses dine fremtidige behov (multi-WAN, VLAN, site-to-site VPN, captive portal osv.).



Les den offisielle dokumentasjonen ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) regelmessig for å oppdage nye funksjoner og sørge for at konfigurasjonen din er oppdatert og sikker.