---
name: Bitcoin Keeper - Arveplan
description: Planlegg bitcoin-overføringen din med Bitcoin Keeper
---

![cover](assets/cover.webp)



Overføring av Bitcoin-eiendeler er en av de utfordringene som er mest undervurdert av innehaverne. I motsetning til en bankkonto, der finansinstitusjonen kan overføre midlene til de rettmessige arvingene, er Bitcoin helt avhengig av private nøkler. En helt legitim arving vil aldri kunne få tilgang til midlene uten disse nøklene, mens en ondsinnet person som er i besittelse av hemmelighetene, vil kunne bruke dem uten noen formalitet.



I denne andre Bitcoin Keeper-veiledningen utforsker vi premiumfunksjonene som er dedikert til eiendomsplanlegging. Programmet tilbyr avanserte verktøy for å opprette Enhanced Vaults, med tidsbestemte beskyttelsesmekanismer takket være Miniscript, samt medfølgende dokumenter for å veilede dine nærmeste.



Denne veiledningen forutsetter at du allerede har lært deg det grunnleggende i Bitcoin Keeper (oppretting av porteføljer, klassisk multisig, legge til maskinvarenøkler) som forklart i vår første veiledning :



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

![video](https://youtu.be/tCld_-n2d30)



## Bitcoin Keeper abonnementsplaner



Bitcoin Keeper opererer på en freemium-modell med tre abonnementsnivåer som tilbyr progressiv funksjonalitet. Du får tilgang til abonnementene ved å gå til **More**-fanen og deretter trykke på det gjeldende abonnementet (standard er "Pleb") for å åpne skjermbildet **Manage Subscription**.



![Plans d'abonnement](assets/fr/01.webp)



**Pleb-planen** (gratis) gir tilgang til det viktigste: ubegrenset opprettelse av lommebøker med én og flere nøkler, kompatibilitet med alle større maskinvarelommebøker (Coldcard, Trezor, Ledger, Jade, Tapsigner...), myntkontroll, merking og tilkobling til en personlig Electrum-server. Denne planen er tilstrekkelig for standard bruk og til og med for klassiske multi-sig-konfigurasjoner.



**Hodler-abonnementet** (€ 9,99/måned, med 1 måned gratis hvis du betaler årlig) inkluderer alle Pleb-funksjonene og legger til krypterte sikkerhetskopier til skyen (iCloud eller Google Drive) for å gjenopprette safene dine på alle enheter, Server Key for å legge til automatiske retningslinjer for utgifter og 2FA over en viss terskel, og Canary Wallets for å oppdage uautorisert tilgang til nøklene dine.



**Diamond Hands plan** (€29,99/måned, med 1 måned gratis hvis du betaler årlig) er den komplette pakken for arveplanlegging. Den inkluderer hele Hodler-planen og låser opp arvenøkkelen (utsatt aktivering), nødnøkkelen (nødnøkkel for gjenoppretting i tilfelle tap), arveplanleggingsverktøyene og -dokumentene, og en støttesamtale med Concierge-teamet for å validere konfigurasjonen din. Dette er tilbudet for bitcoinere som ønsker å videreføre arven sin over flere generasjoner.



Viktig poeng: Hvelvene du har opprettet, forblir tilgjengelige selv om du bytter tilbake til gratisabonnementet. Konfigurasjonene dine er basert på åpne standarder (BSMS, Miniscript) og fungerer uavhengig av abonnementet ditt.



## Arvedokumenter



Når du har aktivert Diamond Hands abonnementet ditt, kan du gå til delen **Arvedokumenter** under fanen Mer. Bitcoin Keeper inneholder fem eksempeldokumenter for å strukturere arveplanen din, samt en tipsseksjon:



![Documents d'héritage](assets/fr/02.webp)





- Seed Words Template**: en mal for å notere ned recovery-fraser på en ryddig og organisert måte
- Betrodde kontakter**: en mal for å liste opp kontaktinformasjonen til betrodde personer som er involvert i planen din (notarius publicus, advokat, arvinger, nøkkelvoktere)
- Tilleggsdelingsnøkkel**: et dokument som inneholder teknisk informasjon om hver nøkkel: PIN-kode, avledningsbane, fysisk plassering, enhetstype og annen informasjon som er nyttig for å identifisere og bruke nøkkelen
- Instruksjoner for tilbakebetaling**: trinnvise instruksjoner for hvordan arvingen eller den begunstigede skal få pengene tilbake
- Brev til advokat**: et forhåndsutfylt brev som kan tilpasses advokaten eller notaren din



I **Arvetips** får du praktiske råd om hvordan du sikrer nøkler til arvingene og optimaliserer arveplanen din.



Tilpass disse dokumentene til din situasjon, og oppbevar dem på et trygt sted, atskilt fra selve nøklene.



## Konfigurere sikkerhetskopiering i skyen



Før du oppretter det gamle hvelvet, må du aktivere sikkerhetskopiering i skyen for å beskytte konfigurasjonsfilene dine. Trykk på **Personlig sikkerhetskopiering i nettskyen** i kategorien Mer.



![Configuration Cloud Backup](assets/fr/03.webp)



Velg et sterkt passord for å kryptere sikkerhetskopiene dine. Dette passordet beskytter bare wallet-konfigurasjonsfilene (ikke dine private nøkler). Bekreft passordet, og trykk på **Bekreft**. Sikkerhetskopiene lagres på iCloud eller Google Drive, avhengig av hvilken enhet du bruker. Trykk på **Backup Now** for å starte den første sikkerhetskopien.



## Importer maskinvarenøklene dine



I vårt eksempel oppretter vi en 2-av-3 safe med to ekstra nøkler (Arv og Nødssituasjon). Vi begynner med å importere alle nødvendige nøkler til fanen **Nøkler**.



![Import des clés hardware](assets/fr/04.webp)



Trykk på **Legg til tast**, og velg deretter **Legg til tast fra en maskinvare** for å koble til en wallet-maskinvare. Bitcoin Keeper støtter mange enheter: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner og Specter Solutions.



I vår konfigurasjon importerer vi :




- 2 **Kortnøkler** (MK4SP og MK4)
- 2 taster **Tapsigner** (Metro og Genesis)



For å legge til et Coldcard velger du det fra listen og følger instruksjonene på skjermen for å eksportere den offentlige nøkkelen via QR-kode, fil, USB eller NFC. Hvis du vil ha mer informasjon om hvordan du bruker et Coldcard eller Tapsigner, kan du se de dedikerte veiledningene våre:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Når alle nøklene dine er importert, finner du dem i fanen Nøkler med deres egendefinerte navn.



## Opprett eldre wallet



La oss gå videre til oppretting av koffert. Fra fanen **Wallets** trykker du på **Add Wallet**, velger **Bitcoin Wallet**, og deretter **Create Wallet**.



![Création du wallet](assets/fr/05.webp)



Velg type wallet. For vår eldre plan velger du **2 av 3 multitaster**. Nederst på skjermen aktiverer du **Avanserte sikkerhetsalternativer** og trykker deretter på **Fortsett**.



![Options de sécurité avancées](assets/fr/06.webp)



I popup-vinduet Enhanced Security Options (Utvidede sikkerhetsalternativer) merker du av for :




- Arvenøkkel**: en tilleggsnøkkel som vil bli lagt til i beslutningsdyktigheten etter en bestemt tidsperiode
- Nødnøkkel**: en nøkkel med utsatt total kontroll for å gjenopprette midler i tilfelle tap av nøkkel



Trykk på **Lagre endringer**. Velg deretter de tre tastene som skal utgjøre din wallet fra de importerte (f.eks. Seed Key, Coldcard MK4SP og Tapsigner Metro).



## Fastsettelse av spesielle nøkkelfrister



I neste skjermbilde kan du konfigurere nødnøkkelen og arvenøkkelen. Her definerer du tidsfrister for aktivering av disse spesialnøklene.



![Configuration des délais](assets/fr/07.webp)



For **Nødnøkkelen** velger du maskinvarenøkkelen som skal fungere som den ultimate sikkerhetskopien (her Coldcard MK4), og velger aktiveringsforsinkelsen (i vårt eksempel: 2 år). I motsetning til arvenøkkelen bidrar ikke nødnøkkelen til det beslutningsdyktige antallet: Den lar deg **omgå multisig** fullstendig, og gir deg full kontroll over midlene etter at tidsfristen er utløpt. Det er din siste utvei: Hvis flere nøkler går tapt eller ødelegges, kan du gjenopprette alt med denne ene nøkkelen. Den må derfor beskyttes med den ytterste strenghet.



For **Arvenøkkel** velger du nøkkelen som er tiltenkt arvingen (her Coldcard MK4SP), og velger forsinkelsen (i vårt eksempel: 1 år). Etter ett år uten bevegelse vil denne nøkkelen **bli lagt til i signaturkvorumet**. I praksis vil din wallet 2-av-3 bli en wallet 2-av-4 når denne perioden er utløpt, slik at arvingen kan delta i signeringen sammen med eksisterende nøkler.



### Hvordan fungerer tidslåser?



Bitcoin Keeper bruker **absolutte tidslåser** (CLTV - CheckLockTimeVerify), muliggjort av Miniscript. I motsetning til relative tidslåser (CSV), som starter når hver UTXO mottas, fungerer absolutte tidslåser med en **fast utløpsdato** som defineres når wallet opprettes.



Hvis du oppretter en wallet i dag med en arvenøkkel på 1 år, vil aktiveringsdatoen være "i dag + 1 år". Alle midler som er satt inn på denne wallet, uansett innskuddsdato, vil være tilgjengelige via arvenøkkelen på samme dato.



Fordelen med absolutte tidslåser er at de tillater ledetider på over 15 måneder (grensen for relative CSV-tidslåser), noe som forklarer hvorfor Bitcoin Keeper kan tilby alternativer som 2 år.



### Oppdateringsmekanismen



For å forhindre aktivering av spesialnøkler i løpet av levetiden din, må du "oppdatere" wallet med jevne mellomrom. Med absolutte tidslåser innebærer dette at du **oppretter wallet med en ny utløpsdato** som er skjøvet inn i fremtiden, og deretter overfører pengene dine til denne nye wallet.



Bitcoin Keeper forenkler denne prosessen med en integrert oppdateringsfunksjon. Programmet håndterer kompleksiteten automatisk i bakgrunnen: Du følger ganske enkelt de veiledede trinnene, uten å måtte opprette en ny wallet manuelt eller overføre midlene selv. Planlegg denne operasjonen regelmessig, i god tid før utløpet av den korteste tidsrammen som er konfigurert. Med en arvenøkkel på 1 år bør du for eksempel oppdatere hver 9.-10. måned for å opprettholde en sikkerhetsmargin.



## Lagre og eksporter konfigurasjon



Når wallet er opprettet, minner programmet deg om å lagre konfigurasjonsfilen. **Dette trinnet er kritisk**: Uten denne filen vil ikke arvingene dine kunne rekonstruere wallet multisig.



![Export de la configuration](assets/fr/08.webp)



Trykk på **Backup Wallet Recovery File**. Flere eksportalternativer er tilgjengelige:




- PDF-eksport**: genererer et komplett dokument med all wallet-informasjon
- Vis QR**: viser en QR-kode for å importere konfigurasjonen på en annen enhet
- Airdrop / File Export**: eksporterer filen via delingsalternativene
- NFC**: del via NFC med en kompatibel enhet



Multipliser kopiene: en hos notarius publicus, en i en banksafe og en kryptert digital versjon. Den nye wallet vises nå i Wallets-fanen med merkelappene "Multi-key", "2 av 3", "Arvenøkkel" og "Nødnøkkel".



## Opprett en Wallet Canary



Canary Wallet er et system for tidlig varsling. Ideen er at hver nøkkel som brukes i en wallet med flere nøkler, også kan brukes i en separat wallet med én nøkkel. Ved å sette inn en liten sum på denne wallet "kanarifuglen", signaliserer enhver uautorisert bevegelse at nøkkelen er kompromittert.



![Canary Wallets](assets/fr/09.webp)



Det finnes to måter å konfigurere en Wallet Canary på. Fra **More**-fanen trykker du på **Canary Wallets** i delen "Keys and Wallets". Skjermbildet forklarer prinsippet: Hvis noen får tilgang til en av nøklene dine og finner midler i den tilhørende wallet-enkeltnøkkelen, vil de forsøke å fjerne dem, noe som vil varsle deg.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Du kan også konfigurere Canary direkte fra en tast. I fanen **Nøkler** velger du en nøkkel (f.eks. Tapsigner Genesis), trykker på ikonet **Innstillinger** (tannhjul) og deretter **Kanariefugl Wallet**. Den tilhørende wallet-kanarifuglen åpnes, klar til å motta noen overvåkingssatoshier.



Sett inn en liten sum (noen tusen satoshier) på hver Canary Wallet. Hvis disse midlene flyttes uten ditt samtykke, må du umiddelbart fjerne den kompromitterte nøkkelen fra multisig-safeene dine.



## Beste praksis



**Test konfigurasjonen** med en liten sum penger før du setter inn en stor sum. Send noen tusen satoshier til hvelvet, og prøv deretter et utgående forbruk for å sjekke at du mestrer signeringsprosessen med hver enhet. Test også å importere konfigurasjonsfilen på en annen telefon for å sikre at sikkerhetskopien fungerer.



**Distribuer nøklene på en intelligent måte**. For Tapsigners, overlever dem i en forseglet konvolutt med PIN-koden kommunisert separat (f.eks. i Recovery Instructions-brevet som er lagret et annet sted). For klassiske maskinvarelommebøker oppbevarer du enheten hos en betrodd tredjepart og seed på papir eller metall hos deg eller en annen tredjepart. Noter fingeravtrykket til hver nøkkel og navnet på den i konfigurasjonsfilen for å unngå forvirring.



**Planlegg regelmessige tester** (brannøvelser). Sjekk årlig at du kan gjenoppbygge safen fra sikkerhetskopier på en tom telefon. Test Canary-varsler ved å sjekke saldoen. Simuler tapsscenarioer ("hva om jeg mister Coldcard?") for å bekrefte at de gjenværende nøkkelkombinasjonene er tilstrekkelige.



**Ikke glem oppdateringen**. Hvis du har satt arvenøkkelen til 1 år, må du oppdatere den hver 9.-10. måned. Dette er prisen du betaler for automatisk overføring uten innblanding fra tredjepart.



**Hold planen oppdatert**. Enhver endring (utskifting av en nøkkel, endring av arvinger, endring av tidsfrist) må gjenspeiles i alle sikkerhetskopier og dokumenter. Regenerer PDF-filer etter hver endring, og distribuer nye versjoner.



## Grenser og betraktninger



Til tross for kraften i disse verktøyene er det viktig å være klar over begrensningene for å kunne håndtere dem så effektivt som mulig.



Kompleksiteten** ved en multisig-safe med tidslås kan være en risiko i seg selv: feilkonfigurasjon, misforståelser fra arvinger, tap av et kritisk element blant de mange komponentene. Bitcoin Keeper forenkler opplevelsen så mye som mulig, men det er fortsatt en teknisk operasjon. Bruk denne planen bare hvis beløpet som skal beskyttes, rettferdiggjør det. For små beløp kan det være tilstrekkelig med en enklere plan.



Det er verdt å tenke på **applikasjonsavhengigheten**. Selv om koden er åpen kildekode og basert på åpne standarder (Miniscript, BSMS), er visse funksjoner avhengig av Keeper-økosystemet. Ta vare på en kopi av applikasjonen (Android APK eller iOS IPA) og dokumenter i brevene til arvingene dine muligheten for å bruke andre Miniscript-kompatible lommebøker (for eksempel Liana) for å få tilbake midler.



Betrodde meglere** innebærer en menneskelig risiko. Hva skjer hvis en slektning med onde hensikter bruker nøkkelen du har betrodd ham/henne før fristen? Eller hvis advokaten forlegger dokumentene dine? Velg disse personene med omhu, forklar ansvaret deres tydelig, og ha en plan B. Canary Wallets, redundante sikkerhetskopier og selve strukturen til multisig er fortsatt din beste beskyttelse mot disse farene.



## Konklusjon



Bitcoin Keeper, med sin Diamond Hands plan, tilbyr en komplett verktøykasse for eiendomsplanlegging: Enhanced Vaults med tidsinnstilte nøkler, medfølgende dokumenter, Canary Wallets og personlig støtte.



Det er mer enn bare et teknisk spørsmål: Det handler om å utforme arvearkitekturen, fordele nøkler og kunnskap på en intelligent måte og teste systemet regelmessig. En godt utformet Bitcoin-arvplan forvandler satoshiene dine til en ekte, overførbar arv.