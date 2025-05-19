---
name: Paraply LND
description: Avansert veiledning om installasjon og konfigurering av Lightning Network Daemon (LND) på Umbrel
---
![cover](assets/cover.webp)




## Innledning



Denne avanserte opplæringen tar deg steg for steg gjennom installasjon, konfigurasjon og bruk av Lightning Node (LND)-applikasjonen på Umbrel-noden din. Du lærer hvordan du åpner kanaler, administrerer likviditeten din og synkroniserer noden med en mobilapplikasjon.



## 1. Forutsetning: funksjonell Bitcoin Umbrel-node



Før du distribuerer Lightning, må du ha en fullt operativ Bitcoin-node på Umbrel. Dette innebærer å installere Umbrel (på Raspberry Pi, NAS eller en annen maskin) og synkronisere Blockchain Bitcoin fullt ut.



For å installere Umbrel og konfigurere Bitcoin-noden din, anbefaler vi at du følger vår egen veiledning :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Sørg for at Bitcoin-noden er oppdatert og fungerer som den skal, ettersom Lightning Network er avhengig av den for alle off-chain-transaksjoner.



## 2. Introduksjon til Lightning Network



Lightning Network er en annen Layer-protokoll som er utformet for å gjøre Bitcoin-transaksjoner raskere og billigere ved å utføre dem utenfor hoved-Blockchain.



Konkret bruker Lightning et nettverk av betalingskanaler mellom noder: To brukere åpner en kanal ved å blokkere On-Chain BTC (innledende transaksjon), og kan deretter umiddelbart foreta Exchange-betalinger innenfor denne kanalen. Disse off-chain-transaksjonene blir ikke registrert på Blockchain, og derfor er de raske og nesten kostnadsfrie.



Betalinger kan rutes gjennom flere kanaler (takket være mellomliggende noder) for å nå enhver mottaker i nettverket, noe som muliggjør en nesten ubegrenset skala av øyeblikkelige transaksjoner. Lightning tilbyr dermed svært raske og rimelige transaksjoner, noe som er ideelt for hverdagsbetalinger eller mikrotransaksjoner, samtidig som belastningen på Blockchain Bitcoin lettes.



For å fungere må en Lightning-node være permanent koblet til nettverket og samhandle med andre Lightning-noder. Det finnes ulike programvareimplementeringer (LND, Core Lightning, Eclair osv.), som alle er kompatible med hverandre. Umbrel bruker LND (Lightning Network Daemon) som en del av sin offisielle Lightning Node-applikasjon. Denne veiledningen fokuserer på LND.



For en fullstendig teoretisk innføring i Lightning Network anbefaler vi at du tar vårt eget kurs :



https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Dette kurset gir deg en grundig innføring i de grunnleggende konseptene i Lightning Network, før du går videre til å øve med LND-noden din.



## 3. Hvorfor selv-host LND?



Ved å drive din egen Lightning-node (LND) på Umbrel får du full råderett over midlene og kanalene dine, sammenlignet med depot- eller semi-depotløsninger.



### Sammenligning av Lightning-løsninger :



**Solutions custodiales (f.eks. Wallet av Satoshi)** :




- Dine Lightning-bitcoins administreres av en betrodd tredjepart
- Enkel å bruke, ingen teknisk kompleksitet
- Operatøren har pengene dine og kan spore transaksjonene dine
- Du gir avkall på kontroll og konfidensialitet



**Forbrukerporteføljer som ikke er råvarer (f.eks. Phoenix, Breez)** :




- Brukerne beholder sine private nøkler og dermed Ownership av sin BTC
- Ingen fullstendig nodeadministrasjon - applikasjonen administrerer kanaler i bakgrunnen
- Kompromiss mellom enkelhet og suverenitet
- Avhengighet av leverandørinfrastruktur for likviditet
- Tekniske begrensninger (én smarttelefon kan ikke dirigere betalinger for andre)



**Selvbetjent LND-node (Umbrel)** :




- Maksimal suverenitet: dine On-Chain og off-chain BTC-er er helt under din kontroll
- Ingen tredjeparter er involvert i å åpne kanaler eller administrere betalingene dine
- Økt konfidensialitet (kanalene og transaksjonene dine er kun kjent for deg og dine direkte kolleger)
- Fri bruk: Koble til dine egne tjenester og lommebøker
- Mulighet for å dirigere transaksjoner for andre (mikrogebyr)
- Økt teknisk ansvar (vedlikehold, likviditetsstyring, sikkerhetskopiering)



Kort sagt gir selvhosting av LND deg maksimal kontroll, men krever mer teknisk kompetanse. Det er en avveining mellom bekvemmelighet og suverenitet.



## 4. Trinn-for-trinn-veiledning



### 4.1 Installere og konfigurere Lightning Node-applikasjonen på Umbrel



Når Umbrel-noden (Bitcoin) er synkronisert, følger du disse trinnene :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Installer Lightning Node-applikasjonen fra "App Store"-delen av Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) vil bli distribuert på din Umbrel som en applikasjon. Når du åpner den første gang, ser du en advarsel om at Lightning er en eksperimentell teknologi.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Du kan velge mellom å opprette en ny node eller å gjenopprette en node fra en sikkerhetskopi/seed. For en førstegangsinstallasjon velger du å opprette en ny node. Lightning Node-appen vil generate en Mnemonic-frase på 24 ord (din seed Lightning): Skriv den nøye ned (ideelt sett offline, på papir), da den vil bli brukt til å gjenopprette Lightning-midlene dine om nødvendig.



**Merk: På nyere versjoner av Umbrel gir installasjonen av Lightning-appen denne seed med 24 ord (det gjør ikke selve Umbrel-noden Bitcoin).



![Interface principale de Lightning Node](assets/fr/04.webp)



Etter initialisering får du tilgang til Lightning Node's hoved-Interface.



![Paramètres de l'application](assets/fr/05.webp)



I programinnstillingene finner du en rekke viktige alternativer:




   - Se Node-ID-en din (nodens unike identifikator)
   - Koble til en ekstern Wallet (Koble til Wallet)
   - Se hemmelige ord
   - Få tilgang til avanserte innstillinger
   - Gjenopprett kanaler
   - Last ned kanalens sikkerhetskopifil
   - Aktiver automatisk sikkerhetskopiering
   - Konfigurere sikkerhetskopiering via Tor (Backup over Tor)



Disse alternativene er avgjørende for sikkerheten og administrasjonen av Lightning-noden din. Sørg for at du aktiverer automatiske sikkerhetskopier og holder de hemmelige ordene dine trygge.



**Nyttige ressurser:**




- [Umbrel Community](https://community.umbrel.com) - Diskusjonsforum for brukere som ønsker å dele problemer og løsninger knyttet til Umbrel og dets økosystem


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Beskrivelse av Lightning Node-appens funksjoner på Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Offisiell LND-dokumentasjon

### 4.2 Åpne en Lightning-kanal



Når LND er oppe og går, kan du åpne din første Lightning-kanal. Slik finner du kvalitetsnoder å koble deg til:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space] (https://amboss.space/) er en utforsker for å finne pålitelige noder for å åpne kanaler.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



For eksempel er [ACINQ-noden] (https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) en anerkjent node med utmerket tilgjengelighet og likviditetsstatistikk.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



For denne opplæringen åpner vi en kanal med [Swiss Bitcoin Pay] (https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Informasjonen som kreves for tilkobling (pubkey@ip:port) er gitt på deres Amboss-side.



For å åpne kanalen :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Klikk på "+ OPEN CHANNEL"-knappen på startsiden til Lightning Node



![Configuration du canal](assets/fr/10.webp)



På kanalkonfigurasjonssiden :




   - Lim inn node-ID-en som er kopiert fra Amboss (format: pubkey@ip:port)
   - Definer mengden kanalkapasitet (noen noder, som ACINQ, har minimumskrav, f.eks. 400k Sats)
   - Juster åpningstransaksjonsgebyrene om nødvendig



![Canal en cours d'ouverture](assets/fr/11.webp)



Når transaksjonen er sendt, vil kanalen vises som "åpning" på startsiden. Vent på bekreftelse av GW 52-transaksjonen.



![Détails du canal](assets/fr/12.webp)



Klikk på kanalen for å se detaljer om den:




   - Nåværende status
   - Total kapasitet
   - Fordeling av likviditet (inngående/utgående)
   - Offentlig nøkkel til ekstern node
   - Og annen teknisk informasjon



### Bruk av Lightning Network+ for å innhente innkommende likviditet



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ er tilgjengelig i Umbrel App Store for å gjøre det enklere å få tak i innkommende kontanter.



![Interface principale de LN+](assets/fr/14.webp)



Interface tilbyr tre viktige alternativer:




- "Likviditetsswapper: Utforsk de tilgjengelige swaptilbudene
- "Open For Me": filtrer byttene du er kvalifisert for
- "To Docs": få tilgang til dokumentasjon



![Message d'erreur LN+](assets/fr/15.webp)



Merk: Hvis du ikke har en kanal åpen ennå, vil du se denne feilmeldingen når du klikker på "Open For Me".



![Liste des swaps disponibles](assets/fr/16.webp)



Siden "Liquidity Swaps" viser alle tilgjengelige swaptilbud i nettverket.



![Swaps éligibles](assets/fr/17.webp)



"Open For Me" filtrerer bare de byttene som noden din oppfyller de nødvendige vilkårene for.



![Détails d'un swap](assets/fr/18.webp)



Eksempel på byttedetaljer :




- Pentagon-konfigurasjon (5 deltakere)
- Kapasitet på 300 000 Sats per kanal
- Forutsetning: minst 10 åpne kanaler med 1M Sats total kapasitet
- Ledige plasser: 4/5



### 4.3 Synkronisering med en mobilapplikasjon (Zeus)



For å fjernstyre Lightning-noden (smarttelefon) kan du bruke Zeus (åpen kildekode-applikasjon tilgjengelig på iOS/Android).



**Zeus-konfigurasjon med Umbrel :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Sørg for at Umbrel-noden din er tilgjengelig (som standard via Tor).


Åpne Lightning Node-appen i Interface Umbrel, og klikk deretter på "Koble til Wallet"-knappen som indikert av pilen.



![Page de connexion avec QR code](assets/fr/20.webp)



En QR-kode vises, som inneholder dine LND-tilgangsdata i lndconnect-format. Denne QR-koden inneholder mye informasjon, så ikke nøl med å forstørre den for å gjøre den lettere å lese.



![Configuration initiale de Zeus](assets/fr/21.webp)



På telefonen din :




   - Åpne Zeus
   - Klikk på "Avansert oppsett" på startsiden for å koble til din egen Lightning-node
   - I parametrene velger du "Opprett eller koble til en Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



I Zeus:




   - Velg "LND (REST)" som tilkoblingstype
   - Du kan enten skanne QR-koden (anbefalt metode) eller skrive inn informasjonen manuelt. (Ikke nøl med å zoome inn på Umbrel QR-koden, da den er veldig tett)
   - Viktig: Aktiver alternativet "Bruk Tor" hvis Umbrel kun er tilgjengelig via Tor (standard)
   - Lagre konfigurasjon



Zeus er nå koblet til Umbrel-noden din og lar deg foreta lynbetalinger, se kanalene dine, saldoer osv. samtidig som du er helt selvadministrert.



**Avanserte tilkoblingsalternativer:**



Som standard går Zeus ↔ Umbrel-forbindelsen via Tor. For en raskere tilkobling finnes det to alternativer:



**Lightning Node Connect (LNC)** :




   - Lightning Labs' krypterte tilkoblingsmekanisme
   - Installer Lightning Terminal-appen på Umbrel (inkluderer tilgang til LNC)
   - generate en tilkoblings QR-kode i Lightning Terminal (Koble til → Koble til Zeus via LNC)
   - Skann den inn i Zeus (velg "LNC" som tilkoblingstype)



**VPN Tailscale**:




   - Enkel å konfigurere mesh VPN
   - Installer Tailscale på Umbrel (App Store) og på mobiltelefonen din
   - Koble til Zeus via Tailscale privat IP i stedet for Tor Address



Disse alternativene er ikke obligatoriske, og Tor + Zeus-løsningen fungerer bra i de fleste tilfeller.



> **Nyttige ressurser:**
> - [Zeus Documentation - Umbrel Connection] (https://community.umbrel.com/t/zeus-LN-mobile/7619) - Offisiell guide til hvordan du kobler Zeus til Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus-prosjektet med åpen kildekode
> - [Umbrel Community - Tilkobling av Zeus via Tailscale] (https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Guide til hvordan du kobler Zeus til Umbrel ved hjelp av Tailscale

## 5. Sikkerhet og beste praksis



Administrasjon av en selvdrevet Lightning-node krever særlig oppmerksomhet på sikkerhet.



### Sikkerhetskopiering og sikkerhet for noden din



**Viktige typer sikkerhetskopier**



Lightning Umbrel-noden krever to typer sikkerhetskopier:



**seed-setningen (24 ord)**




- Gjenvinner On-Chain-midler
- Nødvendig for å gjenskape din Wallet Lightning
- For svært sikker lagring (offline, på papir)



**Statisk sikkerhetskopiering av kanaler (SCB)**-fil




- Inneholder informasjon om Lightning-kanalen
- Muliggjør tvungen stenging av kanaler i tilfelle krasj
- Viktig:** Aldri lagre filen `channel.db` manuelt (risiko for bøter)



**Manuell sikkerhetskopieringsprosedyre



Slik lagrer du kanalene dine manuelt :


1. Åpne Lightning Node-menyen (tre prikker "⋮" ved siden av "+ Åpne kanal")


2. Last ned sikkerhetskopifilen for kanalen


3. Eksporter en ny SCB etter hver kanalendring


4. Lagre SCB på en sikker måte (krypterte medier, ekstern kopi)



**Umbrel** automatisk backup-system



Umbrel har et sofistikert automatisk backup-system som sikrer :



*Personvern:*




- Kryptering på klientsiden før overføring
- Sende via Tor-nettverket
- Data supplert med tilfeldig utfylling
- Krypteringsnøkkel som er unik for enheten din



*Forbedret sikkerhet:*




- Øyeblikkelig sikkerhetskopiering ved statusendringer
- Sikkerhetskopier med tilfeldige intervaller
- Skjul endringer i sikkerhetskopistørrelsen
- Beskyttelse mot tidsanalyse



*Restaureringsprosess:*




- Identifikator og nøkkel utledet fra din seed Umbrel
- Fullstendig restaurering er kun mulig med Mnemonic-frasen
- Automatisk gjenoppretting av siste sikkerhetskopier
- Gjenopprett kanalinnstillinger og data



### Restaurering av krasj



Hvis noden går tapt (maskinvarefeil, ødelagt SD-kort) :




- Monter paraplyen på nytt
- Skriv inn de 24 ordene seed i Lightning-appen
- Importer SCB-filen under restaurering



LND vil kontakte hver partner i de gamle kanalene dine for å stenge dem og inndrive din andel av On-Chain-midler. Kanalene vil bli stengt permanent (og kan åpnes igjen om nødvendig).



### Tilgjengelighet og beskyttelse mot svindel



Ideelt sett bør du legge igjen knuten din på nettet så ofte som mulig. I tilfelle langvarig fravær:




- En ondsinnet motpart kan forsøke å kringkaste en gammel kanalstatus
- Lightning gir en "protestperiode" (ca. 2 uker på LND)
- Hvis du skal være borte lenge, bør du sette opp en Watchtower



**Watchtower-konfigurasjon:**




- I avanserte innstillinger for LND legger du til URL-adressen til en klarert Watchtower-server
- Du kan bruke en offentlig tjeneste eller installere din egen Watchtower




Hvis du vil vite mer om hvordan du konfigurerer og bruker vakttårn, anbefaler vi at du tar en titt på vår egen veiledning :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Annen beste praksis





- Programvareoppdateringer:** Hold Umbrel og LND oppdatert (sikkerhetsoppdateringer)
- Maskinvarebeskyttelse:** Bruk et stabilt system (Raspberry Pi med SSD, mini-PC) og en UPS
- Nettverkssikkerhet:** Behold standard Tor-konfigurasjon, endre Umbrel-administratorpassordet (standard: "moneyprintergobrrr")
- Kryptering:** Aktiver diskkryptering hvis mulig



## 6. Ytterligere verktøy



Umbrels Lightning Node-app inneholder det viktigste for å administrere kanalene dine, men tredjepartsverktøy tilbyr avansert funksjonalitet.



### ThunderHub



Interface er et moderne, nettbasert Lightning node-styringssystem som kan installeres via Umbrel App Store.



**Funksjoner:**




- Visualisering av kanaler i sanntid (kapasitet, saldoer)
- Integrerte verktøy for rebalansering
- Støtte for multi-path billing (MPP)
- Generering av QR-kode LNURL
- Transaksjonshåndtering On-Chain



ThunderHub er ideell for å overvåke en aktiv rutingsnode og utføre enkel rebalansering.



### Ride The Lightning (RTL)



Interface webkompatibel med flere Lightning-implementeringer (LND, Core Lightning, Eclair).



**Høydepunkter:**




- Administrasjon av flere noder
- Kontekstsensitive instrumentpaneler
- Støtte for ubåtbytter (Lightning Loop)
- 2-faktor autentisering
- Eksporter/importer sikkerhetskopier av kanaler



RTL er en komplett "sveitserkniv" for administrasjon av en Lightning-node med en mer ekspertorientert tilnærming.



### Andre nyttige verktøy





- Lightning Shell** : Kommandolinje (lncli) via nettleser
- BTC RPC Explorer og Mempool** : Overvåking Blockchain
- LNmetrics og Torq**: Analyse av rutingytelse
- Amboss & 1ML**: "Sosial" administrasjon av noden din (aliaser, kontakter, nettverksanalyse)



Disse verktøyene kan installeres med bare noen få klikk via Umbrel App Store, uten noen komplisert konfigurasjon.



**Ytterligere verktøyressurser:**




- [ThunderHub.io - Funksjoner](https://thunderhub.io) - Oversikt over ThunderHub-funksjoner
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL-dokumentasjon
- [David Kaspar - Rebalance via ThunderHub] (https://blog.davidkaspar.com) - En praktisk guide til rebalansering
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) - Avansert dokumentasjon for strømbrukere



## Konklusjon



Å drive din egen LND-node på Umbrel er et viktig skritt mot finansiell suverenitet. Selv om det krever mer teknisk involvering enn en depotløsning, er fordelene med hensyn til kontroll, konfidensialitet og aktiv deltakelse i Lightning Network betydelige.



Ved å følge denne veiledningen bør du nå være i stand til å installere LND, åpne kanaler, administrere likviditeten din og få fjerntilgang til noden din. Utforsk gjerne avanserte funksjoner og tilleggsverktøy etter hvert som du blir mer kjent med økosystemet.



Husk at sikkerheten til midlene dine avhenger av dine egne sikkerhetstiltak og rutiner. Ta deg tid til å sette deg inn i alle aspekter før du forplikter deg til å investere store summer.