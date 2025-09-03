---
name: be-BOP
description: Praktisk guide til å tjene penger på virksomheten din med be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** er en e-handelsplattform designet for gründere som ønsker å selge online og offline, i full autonomi, samtidig som de aksepterer betalinger i Bitcoin, via en bankkonto og i kontanter. Løsningen er også nyttig for alle typer organisasjoner som ønsker å samle inn donasjoner eller tjene penger på sine ulike aktiviteter.



Løsningen er enkel, lett og autonom. Den gjør det mulig å opprette en nettbutikk, selv i et miljø der tradisjonelle finansielle tjenester er begrenset eller fraværende. **be-BOP** er designet for å fungere effektivt med eller uten tilgang til banker, ved hjelp av Bitcoin som betalingsinfrastruktur.



I denne opplæringen tar vi deg steg for steg gjennom:





- Opprett din første nettbutikk med **be-BOP**
- Gjør utstillingsvinduet og produktene dine personlige
- Konfigurer tilgjengelige betalingsmetoder
- Forstå de beste fremgangsmåtene for å selge effektivt på nett med **be-BOP**



Denne opplæringen krever ikke avanserte tekniske ferdigheter. Den er rettet mot utviklere så vel som håndverkere, kjøpmenn, kooperativer eller entreprenører som ønsker å begynne med digital handel på en suveren og robust måte.



## Forutsetninger for å installere be-BOP på din egen server



Før du begynner å installere be-BOP, må du sørge for at du har følgende tekniske infrastruktur. Disse Elements er avgjørende for at plattformen skal fungere korrekt:



### S3-kompatibel lagring



be-BOP bruker et lagringssystem for å administrere filer (for eksempel produktbilder). Dette krever tilgang til en S3-tjeneste, for eksempel:





- [MinIO](https://min.io/) selvbetjent
- Amazon S3 (AWS)
- Scaleway Object Storage



Du må konfigurere en bøtte og oppgi følgende informasjon:





- S3_BUCKET**: navn på skuffen
- S3_ENDPOINT_URL**: tilgangslenke til S3-tjenesten din
- S3_KEY_ID** og S3_KEY_SECRET: tilgangskodene dine
- S3_REGION**: regionen til S3-tjenesten din



### MongoDB-database i ReplicaSet-modus



be-BOP bruker MongoDB til å lagre butikk-, bruker-, produkt- og andre data.



Du har to alternativer:





- Installer MongoDB lokalt med **ReplicaSet-modus aktivert**
- Bruk en nettbasert tjeneste som **MongoDB Atlas**



Du trenger følgende variabler:





- MONGODB_URL**: databasetilkobling Address
- MONGODB_DB**: navn på databasen



## Node.js-miljø



be-BOP fungerer med Node.js. Sørg for at du har **Node.js** versjon 18 eller nyere og **Corepack** aktivert (nødvendig for å administrere pakkebehandlere som pnpm). Kommandoen som skal kjøres er `corepack enable`



### Git LFS installert



Noen ressurser (for eksempel store bilder) administreres via Git LFS (Large File Storage). Sørg for at du har Git LFS installert på maskinen din med kommandoen `git lfs install`. Når disse forutsetningene er på plass, er du klar til å gå videre til neste trinn: nedlasting og konfigurering av be-BOP.



**Merk:** En teknisk veiledning for programvaredistribusjon er tilgjengelig i en egen veiledning.



## Opprette en Super-Admin-konto



Første gang be-BOP startes, opprettes en **Super Admin**-konto. Denne kontoen har alle nødvendige autorisasjoner for å administrere backoffice-funksjoner. Følg disse trinnene for å opprette en konto:





- Gå til `yourresiteweb/admin/login`
- Opprett en superadmin-konto med sikker innlogging og passord



Denne kontoen gir deg tilgang til alle backoffice-funksjoner. Når du har opprettet kontoen, kan du logge inn ved å oppgi brukernavn og passord.



![login](assets/fr/001.webp)



## Back-Office-konfigurasjon og sikkerhet



Før du konfigurerer Interface-backoffice-tilkoblingen, må du opprette en unik Hash. Dette gir beskyttelse mot ondsinnede aktører som prøver å stjele tilkoblingslenken til Interface-administratoren din.



For å opprette Hash, gå til `/admin/Innstillinger`. I delen som er dedikert til sikkerhet (f.eks. "Admin Hash"), definerer du en unik streng (Hash). Når den er registrert, vil nettadressen til backoffice endres (f.eks. `/admin-yourhash/login`) for å begrense tilgangen for uautoriserte personer.



![hash-login](assets/fr/002.webp)



2.2. Aktiver vedlikeholdsmodus (om nødvendig)



Fortsatt i /admin/Innstillinger, (Innstillinger > Generelt via Interface-grafikk), sjekk alternativet "aktiver vedlikeholdsmodus" nederst på siden.



![maintenance-mode](assets/fr/003.webp)



Hvis det er nødvendig, kan du angi en liste over autoriserte IPv4-adresser (atskilt med komma) for å gi tilgang til frontkontoret under vedlikehold. Backoffice forblir tilgjengelig for administratorer.



![ip-bebop](assets/fr/004.webp)



## Oppsett av kommunikasjon



For at be-BOP skal kunne sende varsler (f.eks. om bestillinger, registreringer eller systemmeldinger), må du konfigurere minst én kommunikasjonsmetode. To alternativer er tilgjengelige: e-post (SMTP) eller Nostr.



### SMTP-konfigurasjon (e-post)



be-BOP kan sende e-post via en SMTP-server. Du trenger gyldig SMTP-legitimasjon, som ofte leveres av en e-posttjeneste (f.eks. Mailgun, Gmail osv.).



Her er det du trenger å vite:



SMTP_HOST: SMTP-server Address (f.eks. smtp.mailgun.org)



SMTP_PORT: porten som skal brukes (ofte 587 eller 465)



SMTP_USER: brukernavnet ditt (vanligvis en e-post Address)



SMTP_PASSWORD: ditt passord eller API-nøkkel



SMTP_FROM: e-posten Address som vises som avsender




### Nostr-konfigurasjon



be-BOP gjør det mulig å sende varsler via Nostr-protokollen, en desentralisert meldingsinfrastruktur. For å gjøre dette må du generate eller Supply en privat Nostr-nøkkel (NSEC). Du kan generate denne nøkkelen direkte via be-BOPs Interface, i delen som er dedikert til Nostr. Når disse Elements er riktig konfigurert, vil be-BOP automatisk kunne sende meldinger og varsler til brukerne dine.



## Kompatible betalingsmetoder



be-BOP er kompatibel med flere betalingsløsninger, slik at du kan tilby kundene dine større fleksibilitet. Her ser du hva du trenger for å sette opp den betalingsmetoden som passer deg best.



### Bitcoin Onchain



be-BOP lar deg ta imot Bitcoin-betalinger direkte på Blockchain (On-Chain), enkelt og sikkert.



**Konfigurasjonstrinn:**





- Gå til menyen **Betalingsinnstillinger**
- Klikk på **Bitcoin Nodeless** for å få tilgang til On-Chain betalingsparametere.
- Fyll ut følgende felter:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Tips:** For å få tak i den utvidede offentlige nøkkelen (Zpub), kan du se de avanserte innstillingene til din Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter osv.). Sørg for at din Wallet er **ikke skrivebeskyttet** hvis du har tenkt å bruke transaksjonshistorikk.



### Lightning Network



be-BOP kan også godta øyeblikkelige Bitcoin-betalinger takket være Lightning Network. To konfigurasjonsalternativer er for øyeblikket tilgjengelige:



**Phoenixd**



Gå til menyen `Betalingsinnstillinger`, klikk på `Phoenixd`



![phoenixd](assets/fr/006.webp)



Deretter må du oppgi **passordet eller token-autentiseringen** som kobler deg til Phoenixd-forekomsten din, en backend utviklet av Acinq som lar deg administrere Lightning-betalinger med din egen node, men uten kompleksiteten ved å administrere betalingskanaler.



**Swiss Bitcoin Pay**



Hvis du ikke ønsker å administrere en Lightning-node selv, er **Swiss Bitcoin Pay** en løsning som er klar til bruk og enkel å konfigurere, og som er ideell for å begynne å ta imot Lightning-betalinger uten en kompleks infrastruktur.



Konfigurasjonstrinn:





- I menyen "Betalingsinnstillinger" klikker du på `Swiss Bitcoin Pay`
- Logg inn på din sveitsiske Bitcoin Pay-konto (eller opprett en hvis du ikke allerede har en).
- Skriv inn API-nøkkelen som leveres av Swiss Bitcoin Pay, og klikk deretter på "Lagre"



Når be-BOP er satt opp, vil be-BOP automatisk generate Lightning-fakturaer for kundene dine, og du vil motta betalinger direkte til din sveitsiske Bitcoin Pay-konto. Denne løsningen er ideell for brukere som ønsker å unngå den tekniske kompleksiteten ved en personlig node, samtidig som de ønsker å ta imot raske og rimelige betalinger.



![swissbtcpay](assets/fr/007.webp)



### PayPal



I tillegg til Bitcoin kan du med be-BOP også ta imot kontantbetalinger via PayPal, en velkjent og mye brukt internasjonal løsning.



Konfigurasjonstrinn:





- Gå til menyen `Betalingsinnstillinger`
- Klikk på `PayPal
- I Paypal-kontoen din (utviklerseksjonen) skriver du inn `Client ID` og `Secret`
- Velg den valutaen du ønsker (f.eks. **USD**, **EUR**, **XOF**, osv.)
- Klikk på `Lagre



![paypal](assets/fr/008.webp)



**Du må ha en PayPal-virksomhetskonto for å kunne bruke generate-identifikatorene. Du kan få tak i dem via [developer]-portalen (https://developer.paypal.com)



### SumUp



Programvaren integrerer nå betalingsløsningen **SumUp**, slik at du kan ta imot kredittkortbetalinger på en enkel, sikker og effektiv måte. For å dra nytte av denne funksjonaliteten er det nødvendig med en innledende konfigurasjon. Her er trinnene som skal følges, nummerert for en oversiktlig og progressiv implementering:





- Begynn med å skrive inn **API-nøkkelen**, en konfidensiell nøkkel som du fikk av SumUp da du opprettet utviklerkontoen din. Den etablerer en sikker forbindelse mellom SumUp-kontoen din og programvaren.
- Fyll ut feltet `Merchant Code` med den unike koden som identifiserer virksomheten din på SumUp-plattformen. Denne koden er viktig for å knytte transaksjoner til virksomheten din.
- I feltet "Valuta" velger du hovedvalutaen du bruker for transaksjonene dine (f.eks. **EUR**, **USD**, **CDF**, osv.).
- Når alle feltene er fylt ut korrekt, klikker du på "Lagre"-knappen for å lagre innstillingene. Systemet oppretter deretter koblingen til SumUp-kontoen din, og programvaren din er klar til å ta imot betalinger.



![payment-sumup](assets/fr/009.webp)



Etter denne konfigurasjonen vil **SumUp**-integrasjonen være aktiv og i drift, slik at du raskt kan ta ut penger og spore transaksjonene dine direkte fra programvaren.



### Stripe



be-BOP tilbyr også full integrasjon med **Stripe**, en av de mest populære betalingsplattformene på nettet. Stripe lar deg akseptere nettbetalinger via kredittkort, digital Wallet og flere andre betalingsmetoder. Slik aktiverer du det:





- Skriv inn den **hemmelige nøkkelen** som er oppgitt i Stripe-dashbordet.
- Fyll ut feltet **Public Key**, som også leveres av Stripe.
- Velg **hovedvaluta**.
- Lagre konfigurasjonen, og klikk deretter på `Lagre`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Vær oppmerksom på:** Det er viktig å vite hvilket MVA-regime som gjelder for din aktivitet (f.eks. salg under MVA i selgerens land, fritak under begrunnelse, eller salg til MVA-satsen i kjøperens land) for å kunne konfigurere faktureringsalternativene i **be-BOP** korrekt.



## Valutakonfigurasjon



**be-BOP** tilbyr avansert valutahåndtering og er tilpasset miljøer med flere valutaer og spesifikke regnskapskrav. For å sikre konsistens i den økonomiske driften og rapporteringen er det viktig å konfigurere de ulike valutaene som brukes i systemet på riktig måte. Her er trinnene du må følge for denne konfigurasjonen:





- Velg **hovedvaluta** (`Hovedvaluta`)
- Velg `Sekundær valuta
- Definer **referansevaluta** (`Price reference currency`)
- Angi `Regnskapsvaluta



Når alle valutaer er riktig konfigurert, sørger programvaren for automatisk og nøyaktig konvertering av transaksjoner i flere valutaer, samtidig som den sørger for at regnskapet er konsekvent.



![settings-currencies](assets/fr/011.webp)



## Konfigurasjon av gjenopprettingstilgang via e-post eller Nostr



I `/admin/settings`, via **ARM**-modulen, må du sørge for at superadmin-kontoen inneholder en **email Address** eller en **recovery pub**, slik at det blir lettere å komme videre hvis du glemmer passordet ditt.



![settings-users](assets/fr/012.webp)



## Språkinnstillinger



Programvaren har flerspråklig funksjonalitet for å tilpasse seg et internasjonalt publikum og forbedre brukeropplevelsen. For å aktivere flerspråklig funksjonalitet er det viktig å konfigurere de tilgjengelige språkene og definere et **standardspråk**.



![settings-languages](assets/fr/13.webp)



## Interface og identitetskonfigurasjon i be-BOP



**be-BOP** gir designere alle verktøyene de trenger for å designe et nettsted. Det første trinnet er å åpne `/Admin > Merch > Layout` i innstillingene. Begynn med å konfigurere **Top Bar**, **Navbar** og **Footer**.



### Le Top Bar



Med **Top Bar**-konfigurasjonen kan du tilpasse programvarens visuelle identitet ved å vise nøkkelinformasjon allerede på første linje i Interface. Dette forsterker merkevaregjenkjennelsen og gir en tydelig kontekst for brukerne.



#### Konfigurasjonstrinn:





- I feltet "Merkenavn" skriver du inn navnet på bedriften, organisasjonen eller produktet ditt. Dette navnet vil vises øverst på Interface og vil representere din viktigste visuelle identitet.
- Angi nettstedets tittel**: Tittelen som velges, bør oppsummere formålet med plattformen. Tittelen kan vises i toppteksten eller i nettleserfanen.
- Legg til beskrivelse av nettstedet**: Her kan du legge inn en kort beskrivelse av initiativet ditt. Denne beskrivelsen bidrar til å kontekstualisere verktøyet for brukerne og kan også brukes til SEO-formål.



Når denne informasjonen er lagt inn, vil **Top Bar** vise en tydelig, profesjonell og sammenhengende presentasjon av løsningen din.



#### Lenker i topplinjen



I Topplinjens "Lenker"-del kan du legge til snarveier til viktige sider i applikasjonen din eller på eksterne nettsteder. Disse lenkene vises direkte i topplinjen, slik at brukerne får rask og strukturert tilgang.



#### Konfigurasjonstrinn:





- Skriv inn lenkenavn (tekst)**: I feltet `Tekst` skriver du inn navnet eller etiketten på lenken slik den skal vises (f.eks. Hjem, Kontakt, Hjelp...).
- Angi lenke Address (Url)**: I feltet `Url` skriver du inn hele Address for målsiden (intern eller ekstern).
- Legg til andre lenker om nødvendig**: På hver konfigurasjonslinje kan du legge til en ekstra lenke ved hjelp av feltene `Text` og `Url`.
- Lagre lenker**: Når alle lenkene er lagt inn, klikker du på knappen "Legg til lenke i topplinjen" for å lagre dem.



Med denne konfigurasjonen kan du tilby tydelig, flytende og tilgjengelig navigering gjennom de ulike delene av nettstedet ditt eller til utfyllende ressurser.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



I **Navbar**-delen kan du konfigurere be-BOPs hovednavigasjonsmeny, som vanligvis er plassert på siden eller toppen av Interface. Denne menyen leder brukerne til programmets ulike sider og funksjoner. Konfigurasjonen av lenken er enkel og intuitiv. Slik fungerer det:





- Skriv inn lenkenavn (`Text`)**: På konfigurasjonslinjen begynner du med å fylle ut feltet `Text`. Dette tilsvarer navnet på lenken som vises i navigasjonsfeltet (eksempler: *Dashboard*, *Users*, *Settings*...).
- Skriv inn lenkens Address (`Url`)**: Ved siden av feltet `Text` finner du feltet `Url`. I dette feltet skriver du inn Address for siden som lenken skal viderekoble til. Dette kan være en intern rute eller en lenke til en ekstern side.
- Legg til flere lenker om nødvendig**: Under den første linjen er det nye `Text`- og `Url`-felt der du kan legge til så mange lenker som du ønsker. Hver linje representerer en ekstra navigasjonslenke.
- Lagre lenker**: Når du har lagt inn alle Elements, klikker du på knappen "Legg til lenke i navigeringsfeltet" for å lagre og vise resultatene i navigeringsfeltet.



Denne konfigurasjonen gjør det mulig å strukturere tilgangen til ulike deler av programvaren på en effektiv måte, noe som forbedrer ergonomien og brukeropplevelsen.



![navbar](assets/fr/015.webp)



### Bunnteksten



I delen **Foter** kan du tilpasse bunnteksten i programvaren ved å legge til nyttig informasjon eller lenker. Før du konfigurerer lenkene, må du starte med å aktivere et bestemt alternativ:





- Aktiver visning av etiketten "Powered by be-BOP"**: Aktiver knappen "Vis Powered by be-BOP" for å vise denne etiketten i bunnteksten.
- Skriv inn navnet på lenken (`Text`)**: Fyll ut feltet `Text`, som tilsvarer ordlyden til lenken i bunnteksten (eksempler: *Vilkår*, *Privacy*, *Kontakt*...).
- Angi lenke Address (`Url`)**: I `Url`-feltet skriver du inn Address for målsiden (intern eller ekstern).
- Legg til flere lenker ved behov**: Bruk de ekstra linjene til å opprette så mange lenker du vil.
- Lagre lenker**: Klikk på knappen "Legg til bunntekstlenke" for å lagre lenker.



![footer](assets/fr/016.webp)



### Visuell personalisering



**⚠️ Ikke glem å angi logoene for de lyse og mørke temaene, samt faviconet, via** `Admin > Merch > Pictures`.



Slik tilpasser du utseendet og følelsen på nettstedet ditt:



#### Gå til seksjonen Bilder



Meny `Admin` > `Merch` > `Bilder`.



#### Legg til et nytt bilde



Klikk på `Nytt bilde`.



#### Velg en lokal fil



Klikk på `Velg filer`, og velg deretter et bilde fra Hard-disken din.



#### Velg filen som skal importeres



Dobbeltklikk på bildet som skal importeres (lys logo, mørk logo eller favicon).



#### Navngi bildet



Fyll ut feltet `Bildets navn`.



#### Legg til bilde



Klikk på "Legg til" for å fullføre importen.



![pictures](assets/fr/017.webp)



### Oppsett av selgeridentitet



#### Identitetsinnstillinger



Denne delen er tilgjengelig via `Admin > Identitet` (eller `Innstillinger > Identitet`), og her kan du konfigurere bedriftens administrative og juridiske informasjon.



#### Juridisk informasjon





- Firmanavn**: offisielt firmanavn.
- Virksomhets-ID**: juridisk identifikator eller registreringsnummer (RCCM, SIRET...).



#### Virksomhet Address





- Street**: postadresse Address (gate, nummer...).
- Land**: land.
- Delstat**: provins eller region.
- By**: by.
- Postnummer**: postnummer.



#### Kontaktinformasjon





- E-post**: profesjonell e-post Address.
- Telefon**: bedriftens telefonnummer.



#### Bankkonto





- Kontoinnehaverens navn**: navnet på kontohaveren.
- Kontoinnehaver Address**: innehaverens Address.
- IBAN**: Internasjonalt bankkontonummer.
- BIC**: SWIFT/BIC-kode.



![bank-account](assets/fr/019.webp)



#### Fakturering





- Klikk på `Fyll ut med hovedbutikkinformasjon` for å forhåndsutfylle dataene.
- Utstederinformasjon**: felt for juridisk/skattemessig informasjon som er synlig på fakturaer.
- Klikk på `Oppdater` for å lagre endringene.



**Du kan også legge inn tilleggsinformasjon som skal vises på Invoice, alt etter dine behov.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Fysisk butikk Address



For de som har en fysisk butikk, kan du legge til en spesifikk full Address i `Admin > Innstillinger > Identitet` eller en egen seksjon. Dette vil gjøre det mulig å vise den på offisielle dokumenter og i bunnteksten om nødvendig.



![seller-id](assets/fr/021.webp)



## Produktledelse



### Opprettelse av et nytt produkt



Gå til `Admin > Merch > Produkter` for å legge til eller endre et produkt. Fyll ut følgende felt:



#### Grunnleggende informasjon





- Produktnavn**: navnet på produktet (f.eks. *BOP T-skjorte i begrenset opplag*).
- Slug**: URL-identifikator uten mellomrom (f.eks. `tshirt-bop-edition-limitee`).
- Alias** *(valgfritt)*: nyttig for rask tilføyelse til kurven via et eget felt.



![product-config](assets/fr/028.webp)



#### Prising





- Prisbeløp**: produktpris (f.eks. `25,00`).
- Prisvaluta**: valuta (EUR, USD, BTC osv.).
- Spesialprodukter**:
  - dette er et gratis produkt.
  - dette er et betal-hva-du-vil-produkt.



#### Produktalternativer





- Enkeltprodukt (frittstående)**: kun ett tillegg mulig per bestilling (f.eks. donasjon, inngangsbillett).
- Produkt med variasjoner**:
  - Ikke sjekk `Standalone`.
  - Kryss av for `Produktet har lette variasjoner (ingen lagerforskjell)`.
  - Legg til:
    - Navn** (f.eks. *Størrelse*),
    - Verdier** (f.eks.: S, M, L, XL),
    - Eventuelle prisforskjeller** (f.eks.: `+2 USD` for XL).



![product-details](assets/fr/029.webp)



## Lagerstyring



### Avanserte alternativer når du oppretter et produkt (lager, levering, billetter osv.)



#### Produkt med begrenset lagerbeholdning



Hvis produktet ikke er tilgjengelig i ubegrenset antall, merker du av for `Produktet har et begrenset lager`. Dette aktiverer automatisk sporing av gjenværende antall. Når denne boksen er merket av, vises et felt for å angi **tilgjengelig lagerbeholdning**.



Systemet administrerer:





- Reserverte varer** → produkter i kurver som ennå ikke er betalt
- Solgt lager** → allerede kjøpte produkter



**Reservasjonstid for handlekurven**: Når en kunde legger et produkt i handlekurven sin, blir det "reservert" i en begrenset periode. Du kan endre denne tiden i: `Admin > Config > Cart reservation` (verdi i minutter)



#### Produkt som skal leveres?



Kryss av for `Produktet har en fysisk komponent som skal sendes til kundens Address`. Dette er nyttig for alle produkter som skal sendes fysisk (bøker, t-skjorter osv.)



#### Andre alternativer





- Billett**: Kryss av hvis produktet er en billett til et arrangement
- Booking**: sjekk om dette er en reservasjonstid (f.eks. økt, avtale)



![product-options](assets/fr/030.webp)



### Handlingsinnstillinger (nederst)



Denne delen bestemmer **hvor** og **hvordan** produktet kan vises og kjøpes:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Kryss bare av for de kanalene du ønsker å bruke.



## Opprettelse og tilpasning av CMS-sider og widgets



### Obligatoriske CMS-sider



Gå til `Admin > Merch > CMS`. Du vil se en liste over eksisterende sider og kan legge til nye med **Legg til CMS-side**.



CMS-sider er viktige for:





- Informer de besøkende (f.eks. brukervilkår)
- Overholde loven (f.eks. personvernregler)
- Forklar visse funksjoner i butikken (f.eks. IP-henting, 0 % moms)



Du kan legge til andre sider etter behov:





- Om oss / Hvem vi er
- Støtt oss / Donasjoner
- VANLIGE SPØRSMÅL
- Kontakt
- osv.



**Tips: Klikk på hver lenke eller hvert ikon for å endre **innholdet**, **tittelen** eller **synligheten** på hver side.



### Layout og grafikk Elements



Gå til: `Admin > Merch > Layout`. Du kan tilpasse den visuelle Elements på nettstedet ditt:



![product-options](assets/fr/032.webp)



#### Topp Bar





- Endre eller slette lenker (f.eks. HJEM, OM OSS, ...)
- Navigasjon mellom viktige deler av nettstedet



#### Navbar (hovednavigasjonslinje)





- Til stede i det grå området under den øverste linjen
- Inneholder rask tilgang til: `Config`, `Payment Settings`, `Transaction`, `Node Management`, `Widgets`, etc.
- Kun for styremedlemmer



#### Bunntekst





- Kan redigeres fra `Admin > Merch > Layout`
- Inneholder: kontaktinformasjon, nyttige lenker, juridiske merknader...



#### Tilpass grafikken



Gå til `Admin > Merch > Bilder`



Du kan:





- Endre **hovedlogoen**
- Endre eller legg til layout **bilder**



#### Beskrivelse av nettstedet



Den kan også endres i `Pictures`, og lar deg vise et **sammendrag eller slagord** i topp- eller bunnteksten, avhengig av tema.



**Merk:** Dette gir deg mulighet til å tilpasse utseendet til din merkevareidentitet (utdanning, reklame eller lokalsamfunn).



### Integrering av widgeter i CMS-sider



Widgets** beriker CMS-sidene dine med dynamisk eller visuell Elements.



#### Opprettelse av widgeter



Gå til `Admin > Widgets`



Eksempler på tilgjengelige widgeter:





- Utfordringer**: utfordringer eller oppdrag
- Tagger**: kategorier eller nøkkelord
- Slidere**: bildekaruseller
- Spesifikasjoner**: Spesifikasjonstabeller
- Skjemaer**: skjemaer (kontakt, tilbakemelding osv.)
- Nedtellinger**: tidtakere
- Gallerier**: bildegallerier
- Ledertavler**: brukerrangeringer



![widgets](assets/fr/033.webp)



#### Integrering i CMS-sider



Bruk **kortkoder** i innholdet på CMS-sidene dine:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Gjeldende parametere**:





- `slug`: unik widgetidentifikator
- `display=img-1`: produktspesifikt bilde
- `width`, `height`, `fit`: bildedimensjoner og stil
- autoplay=3000`: tid i ms mellom to lysbilder



**Fordeler**:





- Enkelt å sette inn (kopier og lim inn)
- Dynamisk: alle endringer i widgeten gjenspeiles automatisk
- Ingen utvikler nødvendig



## Ordrehåndtering og rapportering



### Sporing av ordre



For å se og administrere tidligere bestillinger, gå til: `Admin > Transaksjon > Ordrer`



Her finner du en **fullstendig liste over bestillinger** som er lagt inn på nettstedet ditt.



![orders](assets/fr/034.webp)



#### Visualisering og søk



Interface lar deg søke og filtrere bestillinger i henhold til flere kriterier:





- ordrenummer: ordrenummer
- produktalias: produktidentifikator eller produktnavn
- betalingsmiddel": betalingsmåte som brukes (kort, krypto osv.)
- `Email`: kundens e-postadresse



Disse filtrene gjør det enklere å gjøre raske søk og målrettet administrasjon.



#### Detaljer om hver bestilling



Ved å klikke på en ordre får du tilgang til en komplett fil som inneholder:





- Bestilte produkter
- Kundeinformasjon
- Levering Address (hvis aktuelt)
- Eventuelle merknader knyttet til bestillingen



#### Mulige handlinger på en ordre



Du kan:





- Bekreft bestillingen (hvis den er under behandling)
- Kansellere en bestilling (i tilfelle et problem eller en kundeforespørsel)
- Legg til **etiketter** (for intern organisering)
- Konsultere/legge til **interne notater**



**Denne delen er avgjørende for god logistikk og gode kunderelasjoner.



### Rapportering og eksport



For å få tilgang til salgs- og betalingsstatistikk:


administrator > Innstillinger > Rapportering



![reporting](assets/fr/035.webp)



Her finner du en oversikt over virksomheten din, i form av **måneds- og årsrapporter**.



#### Innhold i rapporten



Rapportene er delt inn i seksjoner:





- Ordredetaljer**: antall ordrer, status (bekreftet, kansellert, ventende), utvikling
- Produktdetaljer**: solgte produkter, antall, populære produkter
- Betalingsdetaljer**: innsamlede beløp, fordelt på betalingsmåte



#### Eksport av data



Hver seksjon inneholder en **Eksporter CSV**-knapp, som lar deg:





- Last ned data i CSV-format
- Åpne dem i Excel, Google Sheets osv.
- Arkivering for administrativ eller regnskapsmessig bruk
- Bruk dem til interne rapporter



**Ideell for resultatoppfølging, regnskap og presentasjoner.



## Konfigurasjon av Nostr Messaging (valgfritt)



![nostr-config](assets/fr/036.webp)



Plattformen støtter **Nostr**-protokollen for visse avanserte funksjoner:





- Desentraliserte varsler
- Logg inn uten passord
- Interface lett administrasjon



### Genererer og legger til den private Nostr-nøkkelen



Gå til:


admin > Nodeadministrasjon > Nostr





- Klikk på **Opprett nsec** hvis du ikke har en.
- Systemet kan generate det automatisk.
- Alternativt kan du bruke en eksisterende nøkkel (f.eks. fra Damus eller Amethyst).



Neste:





- Kopier `nsec`-nøkkelen
- Legg det til i filen `.env.local` (eller `.env`): ```env NOSTR_PRIVATE_KEY=DinNsecIciKey



### Funksjoner aktivert med Nostr



Når den er konfigurert, er flere funksjoner tilgjengelige:



**Varsler via Nostr**





- Send varsler om bestillinger, betalinger eller systemhendelser
- For administratorer eller brukere



**Interface lett administrasjon**





- Tilgjengelig via en Nostr-klient
- Muliggjør rask og mobilvennlig administrasjon



**Tilkobling uten passord**





- Innlogging via sikker lenke (sendt via Nostr)
- Større brukersikkerhet og bedre flyt



## Design og tematilpasning



For å tilpasse butikkens utseende til ditt grafiske charter, gå til: `Admin > Merch > Tema`



Her finner du alle alternativene for å **opprette** og **konfigurere** et egendefinert tema.



### Opprette et tema



![theme](assets/fr/037.webp)



Når du oppretter eller endrer et tema, kan du definere:





- Farger**: for knapper, bakgrunner, tekst, lenker osv.
- Skrifttyper**: valg av skrifttyper for titler, avsnitt og menyer
- Grafiske stiler**: rammer, marginer, mellomrom, blokkformer



### Tilpassbare seksjoner



Hver del av nettstedet kan justeres uavhengig av hverandre:





- Header**: øverste navigasjonslinje
- Brødtekst**: hovedinnhold
- Footer**: nederst på siden



**Denne detaljeringsgraden sikrer konsistens mellom nettstedets visuelle uttrykk og merkevareidentiteten din.



### Aktivering av tema



Når temaet er konfigurert:





- Klikk på **Lagre**
- Aktiver det som butikkens **hovedtema**



**Det aktive temaet er det som vil være synlig for besøkende.



## Konfigurere e-postmaler



Plattformen lar deg tilpasse e-postene som sendes automatisk til brukerne. Gå til: `Admin > Innstillinger > Maler`



![emails-templates](assets/fr/038.webp)



### Opprette/redigere maler



Hver e-post (ordrebekreftelse, glemt passord osv.) har:





- Emne**: emnet for e-posten (f.eks. "Bestillingen din er validert")
- HTML-tekst**: HTML-innhold som vises i e-posten



**Du kan sette inn tekst, bilder, lenker osv. etter behov.



### Bruk av dynamiske variabler



For å gjøre e-poster dynamiske kan du sette inn variabler som:





- `{orderNumber}}`: erstattes av det faktiske ordrenummeret
- `{invoiceLink}}`: lenke til Invoice
- `{websiteLink}}`: URL-adressen til nettstedet ditt



**Merk:** Disse taggene erstattes automatisk når de sendes.



### Avanserte tips





- Lag e-poster som er **responsive** for enkel lesing på mobile enheter
- Legg til **handlingsknapper** (betal, last ned, spor bestilling)
- Test e-postene dine ved å sende dem til deg selv før publisering



## Konfigurere spesifikke tagger og widgets



### Håndtering av tagger



Tagger kan brukes til å strukturere og berike innholdet ditt. Slik får du tilgang til dem: `Admin > Widgets > Tag`



![tags-config](assets/fr/039.webp)



### Opprette en tagg



Fyll ut følgende felter:





- Tagnavn**: tagnavn som vises
- Slug**: unik identifikator (ingen mellomrom eller aksenter)
- Tag Family**: grupperer tagger etter kategori



![targsconfig](assets/fr/040.webp)



#### Tilgjengelige familier:





- skapere`: forfattere eller produsenter
- forhandlere: selgere eller utsalgssteder
- `Temporal`: perioder eller datoer
- hendelser: tilknyttede hendelser



### Valgfrie felt



Disse feltene kan brukes til å berike en tagg som om den var en innholdsside:





- Tittel
- Undertittel
- Kort** innhold
- Fullstendig innhold** (på fransk)
- CTAer** (handlingsknapper)



### Bruke tagger



Tagger kan være:





- Allokert til produkter
- Integrert i CMS-sider med en tag: [Tag=slug?display=var-1]



## Konfigurasjon av nedlastbare filer



For å tilby nedlastbare dokumenter til kundene dine: `Admin > Merch > Files`



### Legge til en fil



1. Klikk på **Ny fil**


2. Informer:




   - Filnavn** (f.eks. *Installasjonsveiledning*)
   - Fil som skal lastes opp** (PDF, bilde, Word...)



**Note:** Når den er lagt til, genererer plattformen automatisk en **permanent lenke**.



### Bruke lenken



Denne lenken kan deretter settes inn i:





- CMS**-side (som tekstlenke eller knapp)
- En **e-postklient** (via en mal)
- Et **produktark** (f.eks. nedlasting av bruksanvisning)



Den er ideell for å levere *brukerhåndbøker, tekniske veiledninger, produktark...* uten behov for ekstern hosting.



## Nostr-bot



Plattformen tilbyr avansert integrasjon med **Nostr**-protokollen, via en automatisert bot.



Gå til: node Management > Nostr



### Hovedfunksjoner



#### Stafettstyring





- Legg til eller fjern **reléer** som brukes av boten
- Optimaliser **rekkevidden** og **påliteligheten** til sendte meldinger



#### Automatisk introduksjonsmelding





- Aktiver en automatisk melding ved **første brukerinteraksjon**
- Ideell for:
  - Presentasjon av tjenesten din
  - Send en nyttig lenke (f.eks. vanlige spørsmål, kontakt, bestilling)



#### Sertifisering av din `npub





- Legg til en **logo** og et **offentlig navn**
- Lenke til et **verifisert nettdomene**
- Øker troverdigheten og gjenkjennelsen av Nostr-identiteten din



### Bruksområder for Nostr-bot





- Sender **ordrebekreftelser** til deg
- Automatisk respons på **hendelser (f.eks. ny ordre)**
- Skape en **desentralisert kundeinteraksjon**



## Overbelastning av oversettelsesetiketter



be-BOP er flerspråklig (FR, EN, ES...), men du kan tilpasse oversettelsene til dine behov.



Dette gjør du ved å gå til `Innstillinger > Språk`



### Lasting og redigering



Oversettelsesfilene er i JSON-format. Du kan:





- Last ned** språkfiler
- Endre** eksisterende tekster
- Legg til** dine egne oversettelser



Lenke til originalfiler:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Eksempel:** erstatt `Add to cart` med `Ajouter au panier` eller `Acheter`.



## Teamarbeid og POS (Point of Sale)



### Administrasjon av bruker- og tilgangsrettigheter



#### Opprette roller



Gå til `Admin > Innstillinger > ARM`



Klikk på **Opprett en rolle** for å opprette en rolle (f.eks. `Superadministrator`, `POS`, `Billettkontrollør`).



Hver rolle inneholder:





- skrivetilgang**: skrivetilgang
- lesetilgang**: lesetilgang
- forbudt adgang**: seksjoner interdites



#### Opprettelse av brukere



I samme meny `Admin > Innstillinger > ARM`, legg til en bruker med:





- innlogging
- alias
- gjenoppretting av e-post
- (valgfritt) `recovery npub` for tilkobling via Nostr



Tilordne en tidligere definert rolle.



![pos-users](assets/fr/045.webp)



Skrivebeskyttede** brukere vil se menyene i *kursiv skrift* og vil ikke kunne endre innholdet.



## Konfigurasjon av salgssted (POS)



### Tildeling av POS-rollen



For å gi en bruker tilgang til POS, tilordner du rollen `Point of Sale (POS)` i: `Admin > Konfig > ARM`



Han kan koble seg til via den sikre URL-en: `/pos` eller `/pos/touch`



### POS-spesifikke funksjoner



Be-BOP tilbyr en Interface dedikert til fysisk salg (butikk, arrangement osv.).



#### Rask tilsetning via alias



I `/cart` kan du legge til et produkt i et felt:





- Ved å skanne en **strekkode** (ISBN, EAN13)
- Ved å angi et **produktalias** manuelt



**Merk:** produktet legges automatisk i handlekurven.



#### Betalingsmåte



POS støtter:





- Arter
- Kredittkort
- Lightning Network (krypto)
- Andre i henhold til konfigurasjon



To avanserte alternativer er tilgjengelige:





- Fritak for merverdiavgift**: gjelder på grunnlag av begrunnelse (frivillige organisasjoner, utlendinger...)
- Gaverabatt**: eksepsjonell rabatt med obligatorisk kommentar



#### Visning på klientsiden



URL-en `/pos/session` er beregnet på en **sekundær skjerm** (HDMI, nettbrett ...):



Plakat:





- Produkter under utvikling
- Totalt beløp
- Betalingsmåte
- Rabatter anvendt



**Kunden følger ordren live, mens selgeren registrerer den på `/pos`.



### POS-sammendrag



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Takk for at du følger denne veiledningen nøye.