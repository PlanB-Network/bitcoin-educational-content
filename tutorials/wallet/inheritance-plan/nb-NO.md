---
name: Arveplan Bitcoin
description: Slik overfører du bitcoins til dine nærmeste
---

![cover](assets/cover.webp)



Overføringen av bitcoins representerer en stor teknisk utfordring som mange innehavere overser. I motsetning til tradisjonelle bankmidler, der en finansinstitusjon kan overføre midlene til de rettmessige eierne, fungerer Bitcoin uten mellomledd. Dine nærmeste vil aldri kunne få tilgang til midlene dine uten den nødvendige tekniske informasjonen, uavhengig av deres juridiske legitimitet.



Denne veiledningen guider deg gjennom opprettelsen av en teknisk arveplan. Du lærer hvordan on-chain-mekanismene for automatisert overføring fungerer, hvordan du dokumenterer konfigurasjonene dine, og hvordan du velger de riktige løsningene for å sikre at Bitcoin-arven din forblir tilgjengelig for dine nærmeste.



## Hvorfor en plan for teknisk kulturarv er viktig



Bitcoin er basert på et grunnleggende kryptografisk prinsipp: Den som har de private nøklene, kontrollerer midlene. Denne suvereniteten blir en stor sårbarhet når innehaveren forsvinner uten å ha overført den nødvendige informasjonen.



En Bitcoin-arvplan må oppfylle to tilsynelatende motstridende mål: å la dine nærmeste få tilgang til midlene dine når tiden er inne, samtidig som du forhindrer at andre får tilgang til dem for tidlig. Denne delikate balansen er avhengig av Bitcoins innebygde programmeringsmuligheter.



Teknisk kompleksitet legger til et ekstra lag med vanskeligheter. Arvingene dine må manipulere begreper som gjenvinningsfraser, porteføljebeskrivelser eller avledningsstier. Uten tilstrekkelige forberedelser risikerer selv en velmenende arving å gjøre irreversible feil.



## Hvordan on-chain-arven fungerer



Bitcoin bruker skriptspråket sitt til å kode utgiftsbetingelser direkte i transaksjoner. on-chain-arven utnytter denne programmerbarheten til å skape alternative gjenopprettingsveier som aktiveres automatisk.



### Tidssperrer



Tidssperrer er den grunnleggende mekanismen i Bitcoin-arven. De gjør det mulig å låse midler til en tidsbetingelse er oppfylt.



**CLTV (CheckLockTimeVerify)**: Denne absolutte tidslåsen kontrollerer at et bestemt tidspunkt (dato eller blokkhøyde) er nådd før utgiften godkjennes. For eksempel "disse midlene kan bare brukes etter blokk 900000" eller "etter 1. januar 2026". Fordelen med CLTV er at den tillater lange forsinkelser (flere år), men datoen er fast og gjelder identisk for alle UTXO-er i porteføljen. For å beholde kontrollen over midlene dine må du med jevne mellomrom opprette en ny portefølje med en utvidet utløpsdato og overføre midlene dine til den.



**CSV (CheckSequenceVerify)**: Denne relative tidslåsen verifiserer at det har gått et visst antall blokker siden UTXO ble opprettet. For eksempel "disse midlene kan bare brukes 52560 blokker (~1 år) etter mottak". Fordelen med CSV er at hver UTXO har sin egen uavhengige teller. Hver gang du utfører en transaksjon, tilbakestiller de nyopprettede UTXO-ene sin egen tidsgrense. Den tekniske grensen på 65535 blokker (~15 måneder maksimalt) begrenser imidlertid de mulige tidsrammene. Denne tilnærmingen er mer naturlig for daglig bruk, siden den normale aktiviteten din automatisk forskyver tidsfristene.



### Flere utgiftsveier



En arvportefølje kombinerer flere utgiftsveier på hver adresse:





- Hovedsti** : Eieren kan bruke pengene sine når som helst med hovednøkkelen sin, uten tidsbegrensninger.
- Gjenopprettingsbane(r)**: En eller flere alternative nøkler kan bare bruke midler etter at en bestemt tid er utløpt.



Hver transaksjon som utføres av eieren, "oppdaterer" UTXO og skaper nye utganger med tilbakestilte tidslåser. Denne mekanismen sikrer at gjenopprettingsveiene aldri aktiveres så lenge eieren er aktiv.



### Miniscript og Taproot



**Miniscript** er et strukturert språk utviklet av Andrew Poelstra, Pieter Wuille og Sanket Kanjalkar, som gjør det enkelt å skrive og analysere komplekse Bitcoin-skript. Det gjør det mulig å komponere lesbare og verifiserbare utgiftsbetingelser, noe som er avgjørende for arvekonfigurasjoner som involverer flere nøkler og tidslåser.



**Taproot** (aktivert i november 2021) forbedrer on-chain-arven betydelig. Takket være trestrukturen (MAST) avsløres bare den brukte utgiftsbetingelsen på blokkjeden. Hvis eieren bruker midlene sine normalt, forblir arveforholdene usynlige. Denne konfidensialiteten reduserer også transaksjonskostnadene for komplekse baner.



## Den avgjørende betydningen av deskriptorer



For eldre porteføljer er ikke gjenvinningsfrasen (seed) nok til å gjenopprette tilgangen til midler. Deskriptoren** blir det kritiske elementet.



En deskriptor er en streng som gir en uttømmende beskrivelse av strukturen til en portefølje: de offentlige nøklene som er involvert, utgiftsbetingelser, avledningsveier og konfigurerte tidssperrer. Her er et forenklet eksempel:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Denne deskriptoren sier: "enten kan hovednøkkelen brukes umiddelbart, eller gjenopprettingsnøkkelen kan brukes etter 52560 blokker".



La oss se nærmere på dette eksempelet:




- `wsh()` : Witness Script Hash, angir adressetype (P2WSH)
- or_d()`: "eller"-betingelse med en standardgren
- pk([fingeravtrykk/sti]xpub...)`: Den offentlige hovednøkkelen med fingeravtrykk og avledningssti
- og_v()`: "og"-betingelse som kombinerer gjenopprettingsnøkkel med tidslås
- `eldre(52560)`: Den relative tidslåsen på 52560 blokker



**Uten deskriptoren vil ikke arvingene dine kunne gjenoppbygge porteføljen, selv med alle gjenopprettingsfraser.** En standardportefølje kan bare gjenopprettes fra seed fordi den følger standardiserte avledningsstier (BIP44, BIP84). En eldre portefølje bruker derimot tilpassede skript som ikke kan gjettes. Sikkerhetskopien av deskriptoren (eller konfigurasjonsfilen som eksporteres av programvaren din) må følge med gjenopprettingsfrasene i arveplanen.



## Dokumentasjonskomponenter i en arvplan



Utover de tekniske mekanismene hviler en effektiv plan for arv på tre dokumentasjonspilarer.



### Arvebrevet



Dette personlige brevet er inngangen til planen din. Det er skrevet til arvingene dine og forklarer sammenhengen og hvilke forholdsregler som må tas.



Brevet ditt må inneholde eksplisitte sikkerhetsregler:




- Ikke forhast deg, ta deg tid til å lære før du flytter midler
- Kommuniser aldri en fullstendig gjenopprettingsfrase til en enkelt person
- Aldri skriv inn en gjenopprettingsfrase i en ubekreftet programvare eller datamaskin
- Pass deg for svindelforsøk og folk som tilbyr uoppfordret hjelp
- Søk råd fra minst to personer du stoler på før du tar en beslutning



Brevet inneholder også kontaktinformasjon til notaren og hvor testamentet ditt befinner seg. Det skal aldri inneholde gjenopprettingsfraser eller passord.



### Katalogen over pålitelige kontakter



Ingen arvinger bør stå alene med bitcoin-gjenoppretting. Denne katalogen inneholder en liste over personer som kan tilby teknisk eller juridisk hjelp.



For hver kontaktperson bør du dokumentere: fullt navn, relasjon til deg, rolle i planen, grad av tillit, Bitcoin-kompetanse og fullstendige kontaktopplysninger. Grunnregelen er at arvingene dine alltid bør rådføre seg med minst to forskjellige personer før de tar en viktig beslutning.



### Bitcoin inventering av eiendeler



Denne delen kartlegger alle bitcoinsene dine med den tekniske informasjonen som trengs for å gjenopprette dem.



For hver portefølje dokumenterer du :




- Porteføljetype**: maskinvare, programvare, konfigurasjon (single-sig, multisig, legacy)
- Enhetsplassering**: fysisk plassering av wallet-maskinvaren
- Descriptor/konfigurasjonsfilens plassering**: kritisk for avanserte porteføljer
- Plassering av gjenopprettingsfrase**: separat fra deskriptor
- Tilgangskoder**: hvor PIN-koder og passordfraser lagres
- Konfigurerte forsinkelser**: når gjenopprettingsbaner aktiveres



## Tekniske løsninger tilgjengelig



Flere programvarepakker implementerer on-chain-arvemekanismer. Hver av dem har sine egne tekniske egenskaper.



### Liana



Liana er en skrivebordsprogramvare (Linux, macOS, Windows) som bruker Miniscript til å lage porteføljer med tidsbestemte gjenopprettingsveier. Prosjektet er utviklet av Wizardsardine, som Antoine Poinsot (Bitcoin Core-bidragsyter) var med på å grunnlegge.



**Teknisk arkitektur**: Liana oppretter P2WSH-porteføljer (SegWit native) som standard, med Taproot-støtte tilgjengelig avhengig av kompatibiliteten til wallet-maskinvaren din. Arkitekturen er basert på en hovedbane og én eller flere gjenopprettingsbaner. Den genererte beskrivelsen koder for alle forhold og må lagres.



**Timelocks brukt**: Liana bruker relative tidssperrer (CSV), begrenset til 65535 blokker (~15 måneder). For å opprettholde kontrollen må du utføre en oppdateringstransaksjon før tidslåsen utløper.



**Hardware wallet-integrering**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY og andre enheter er kompatible for signering av transaksjoner.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper er en mobilapplikasjon (iOS, Android) som kombinerer multisig og tidslås via "Enhanced Vaults". Den mobile tilnærmingen med integrert veiledning gjør den tilgjengelig for mindre tekniske brukere.



**Teknisk arkitektur**: Enhanced Vaults bruker Miniscript til å opprette multisig-konfigurasjoner der tilleggsnøkler aktiveres etter definerte tidsfrister. Arvenøkkelen legger til det eksisterende beslutningsdyktige antallet, mens nødnøkkelen kan omgå multisig helt.



**Timelocks brukes**: Bitcoin Keeper bruker absolutte tidslåser (CLTV), noe som tillater ledetider på over 15 måneder. Aktiveringsdatoen settes ved opprettelsen av wallet og gjelder for alle UTXO-er. Programmet har en "revaulting"-funksjon som automatisk håndterer oppdateringen: Brukeren følger bare de veiledede trinnene, uten å måtte opprette en ny wallet manuelt.



**Ytterligere funksjoner**: Integrerte arvedokumenter, Canary Wallets for å oppdage nøkkelkompromittering og påminnelser om oppdatering.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Kulturarv



Heritage er en skrivebordsapplikasjon som bruker Taproot-skript til å kode arveforhold. Bruken av Taproot gir økt konfidensialitet, siden ubrukte stier forblir usynlige i blokkjeden.



**Teknisk arkitektur**: Hver Heritage-adresse inneholder en hovedbane og alternative baner for hver arving, med progressive tidsrammer. Den hierarkiske strukturen gjør det mulig å definere en personlig backup etter 6 måneder og familiearvinger etter 12-15 måneder.



**Bruksmåter**: Frittstående versjon med egen node (gratis) eller administrert tjeneste som legger til påminnelser og varsler til arvinger (0,05 %/år).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Arvingens restitusjonsprosess



Å forstå gjenopprettingsprosessen bidrar til å utarbeide en effektiv plan. Her er de tekniske trinnene en arving må følge.



### Krav til gjenoppretting



Arvingen trenger :


1. **Deskriptoren eller konfigurasjonsfilen** for den opprinnelige porteføljen (JSON- eller tekstformat, avhengig av programvaren)


2. **Din gjenopprettingsfrase** (den som er knyttet til arvenøkkelen, vanligvis 12 eller 24 ord)


3. **Kompatibel programvare** (Liana, Bitcoin Keeper, Heritage eller Sparrow/Specter for standarddeskriptorer)


4. **En tilkobling til en Bitcoin**-node for å sjekke status for tidslås og kringkaste transaksjonen



### Trinn for gjenoppretting



1. **Installer programvaren** på en sikker enhet og konfigurer tilkoblingen til Bitcoin-nettverket (personlig node eller Electrum-server)


2. **Importer deskriptoren** for å rekonstruere porteføljestrukturen. Programvaren vil automatisk generate alle adresser som brukes


3. **Gjenopprett arvenøkkel** fra gjenopprettingsfrasen. Programvaren vil kontrollere at denne nøkkelen tilsvarer en av nøklene som er autorisert i deskriptoren


4. **Synkroniser porteføljen** for å finne alle UTXO-er og deres utgiftsforhold


5. **Sjekk utløp av tidslås**: programvaren vil indikere for hver UTXO om gjenopprettingsbanen er aktiv


6. **Opprett gjenopprettingstransaksjonen** til en adresse som kun arvingen kontrollerer (ideelt sett en ny enkelt wallet)


7. **Signer og kringkast** transaksjonen på Bitcoin-nettverket



Hvis tidslåsen ennå ikke er utløpt, må arvingen vente. Programvaren viser datoen eller blokken der gjenoppretting blir mulig. I løpet av denne venteperioden forblir midlene sikre på blokkjeden.



### Punkter å holde øye med for arvingen



Arvingen må være spesielt oppmerksom på :




- Kontroller ektheten til nedlastet programvare** (sjekksummer, signaturer)
- Aldri del din recovery-frase** med noen som tilbyr hjelp
- Rådfør deg med minst to personer du stoler på** før du går i gang med gjenopprettingen
- Overfør midlene til en enkel portefølje** som han har full kontroll over etter at han er friskmeldt



## Beste praksis



### Separasjon av informasjon



Aldri lagre all informasjon på ett sted. Deskriptoren må være adskilt fra gjenopprettingsfrasene, som igjen er adskilt fra PIN-kodene. Denne fordelingen gjør det vanskeligere for en angriper å få tilgang til informasjonen, samtidig som den kan rekonstrueres av dine legitime arvinger.



### Gjenopprettingstester



Før du setter inn betydelige midler, må du teste hele gjenopprettingsprosessen med et lite beløp. Kontroller at du kan gjenopprette porteføljen fra beskrivelsen og gjenopprettingssetningene på en tom enhet. Dokumenter trinnene for arvingene dine.



### Vedlikehold av tidslås



Planlegg å oppdatere tidslåsene dine i god tid før de utløper. For en tidslås på 12 måneder bør du utføre en transaksjon hver 9.-10. måned. Programvaren tilbyr vanligvis påminnelser eller automatiske oppdateringsfunksjoner.



### Oppdatering av planen



Bitcoin-konfigurasjonen din utvikler seg. Alle vesentlige endringer (ny portefølje, endring av tidsfrister, tillegg av arvtager) må gjenspeiles i dokumentasjonen. Etabler en rutine for årlig gjennomgang.



## Velge tilnærming



Valget mellom de ulike løsningene avhenger av din tekniske profil og dine spesifikke behov.



**Liana** er egnet for skrivebordsbrukere som foretrekker programvare med åpen kildekode og full kontroll via sin egen node. Konfigurasjonen forblir tilgjengelig takket være det guidede grensesnittet. Relative tidssperrer (CSV) forenkler vedlikeholdet, ettersom normal aktivitet automatisk forskyver tidsfrister. Begrensning: maksimal forsinkelse på ca. 15 måneder (65535 blokker).



**Bitcoin Keeper** retter seg mot mobilbrukere som ønsker et intuitivt grensesnitt med integrerte ledsagende dokumenter. Applikasjonen tilbyr to typer spesialnøkler: arvenøkkelen (som bidrar til beslutningsdyktigheten) og nødnøkkelen (som omgår den helt). Absolutte tidslåser (CLTV) gir ledetid på over 15 måneder, med en integrert revalideringsfunksjon som gjør det enklere å oppdatere. Diamond Hands-abonnementet låser opp avanserte eldre funksjoner.



**Arv** er rettet mot tekniske brukere som setter pris på Taproot-konfidensialitet og hierarkisk arv med progressive forsinkelser. Taproots trestruktur skjuler arvebetingelser under normale transaksjoner, og avslører bare betingelsen som brukes under gjenoppretting.



Alle tre løsningene har én ting til felles: De krever periodisk oppdatering for å forhindre for tidlig aktivering av gjenopprettingsstier. Denne begrensningen er både prisen og garantien for on-chains upålitelige arv. Planlegg regelmessige påminnelser, og gjør dette vedlikeholdet til en del av din Bitcoin-administrasjonsrutine.



## Konklusjon



En teknisk Bitcoin-arvplan kombinerer kryptografiske mekanismer (tidslås, Miniscript, Taproot) med streng dokumentasjon. Avanserte lommebøker lar deg overføre bitcoins automatisk etter en periode med inaktivitet, uten tredjepartsintervensjon.



De viktigste elementene å gi videre til arvingene er: beskrivelses- eller konfigurasjonsfilen, gjenopprettingsfrasen, detaljerte gjenopprettingsinstruksjoner og kontaktinformasjon til kompetente personer som kan hjelpe dem.



Start med å velge en teknisk løsning som passer til din profil, test den med en liten mengde, og dokumenter deretter det hele i en strukturert plan. Den innledende kompleksiteten garanterer at dine Bitcoin-aktiva vil bli overført i full tillit.



## Ressurser



### Mal for arveplan





- [Bitcoin Arveplanmal (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Academy Dokumentasjonsmal



### Tekniske referanser





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Spesifikasjon av absolutte tidslåser (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Spesifikasjon av relative tidslåser (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Offisiell Miniscript-dokumentasjon av Pieter Wuille



### Offisielle nettsteder for løsningen





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7