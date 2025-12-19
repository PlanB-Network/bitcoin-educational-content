---
name: Ashigaru - Whirlpool Coinjoin
description: Hvordan lager jeg coinjoins i Ashigaru-applikasjonen?
---

![cover](assets/cover.webp)



"*en bitcoin wallet for gatene*"



I denne opplæringen lærer du hva en coinjoin er, og hvordan du lager en med Ashigaru Terminal-applikasjonen og Whirlpool-implementeringen, en coinjoin-protokoll som er arvet fra Samourai Wallet.



## Slik fungerer Whirlpool sammenføyninger



I denne opplæringen vil jeg ikke gå tilbake til begrepet coinjoin, nytten av det eller den teoretiske driften av Whirlpool, ettersom disse emnene allerede er forklart i detalj i del 5 av BTC 204-kurset på Plan ₿ Academy. Hvis du ennå ikke har forstått hvordan Whirlpool fungerer eller prinsippet om coinjoin, anbefaler jeg på det sterkeste at du leser denne del 5 før du fortsetter :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Her er imidlertid noen raske fakta og tall som kan være nyttige.



Whirlpool-kompatible porteføljer bruker fire separate kontoer for å oppfylle behovene i coinjoin-prosessen:




- Kontoen **Deposit**, identifisert med indeksen `0'` ;
- Kontoen **Dårlig bank** (eller *doksisk veksling*), identifisert med indeksen `2,147,483,644'` ;
- Kontoen **Premix**, identifisert med indeksen `2 147 483 645'` ;
- Kontoen **Postmix**, identifisert med indeksen "2 147 483 646".



På Ashigaru, i november 2025, er to poolbetegnelser tilgjengelige (denne listen vil sannsynligvis utvikle seg i løpet av de kommende månedene: så husk å sjekke verdiene mens du leser):




- 0.25 BTC`, med en påmeldingsavgift på `0,0125 BTC`;
- 0.025 BTC, med en påmeldingsavgift på 0,00125 BTC.



Hver miksesyklus kan involvere mellom 5 og 10 UTXO-er i inngang og utgang.



![Image](assets/fr/01.webp)



## Krav til programvare



For å lage coinjoins med Whirlpool trenger du tre separate programmer:





- Ashigaru Terminal**, som lar deg administrere coinjoins direkte fra datamaskinen din;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, applikasjonen på smarttelefonen din som du kan bruke bitcoins i *postmix* fra hvor som helst ;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, en Bitcoin-nodeimplementering som garanterer deg en suveren tilkobling til nettverket, uten avhengighet av en tredjepartsserver.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Installer hvert av disse verktøyene ved å følge de respektive veiledningene, og deretter kan du begynne å lage dine første coinjoins.



## Motta bitcoins



Når du har opprettet porteføljen din, starter du med en enkelt konto, identifisert med indeksen "0". Dette er `Deposit`-kontoen. Det er til denne kontoen du sender bitcoins til coinjoins. Du kan motta dem enten via Ashigaru-applikasjonen (se del 5 av den dedikerte veiledningen), eller via Ashigaru Terminal (også beskrevet i del 5 av den dedikerte veiledningen).



Når innskuddskontoen din inneholder minst det beløpet som trengs for å delta i den minste puljen (pluss servicegebyrer og minimumsbeløpet som kreves for å dekke mining-kostnader), er du klar til å starte dine første coinjoins.



![Image](assets/fr/02.webp)



## Gjør Tx0



Når pengene har kommet inn på innskuddskontoen din og transaksjonen er bekreftet, kan du starte coinjoin-prosessen. For å gjøre dette åpner du menyen `Wallets` på Ashigaru Terminal, og velger deretter din wallet. Hvis wallet er låst, vil programvaren be deg om passordet ditt og passphrase.



![Image](assets/fr/03.webp)



Velg deretter kontoen `Deposit`.



![Image](assets/fr/04.webp)



Gå til menyen `UTXO`.



![Image](assets/fr/05.webp)



Her ser du en liste over alle UTXO-er på innskuddskontoen din. Velg de du ønsker å sende i coinjoin-syklusene.



For å oppnå større konfidensialitet og for å unngå *Common Input Ownership Heuristic (CIOH)*, anbefales det å bruke kun én UTXO per inngang i Whirlpool (en detaljert forklaring av dette prinsippet finnes i BTC 204).



Trykk på tasten `ENTER` på tastaturet for å velge en UTXO: en stjerne `(*)` vises ved siden av den for å indikere at den er valgt.



![Image](assets/fr/06.webp)



Klikk deretter på knappen `Mix Selected`.



![Image](assets/fr/07.webp)



Hvis du har en UTXO som er stor nok til å delta i en av de to tilgjengelige poolene, kan du velge destinasjonspoolen ved hjelp av pilene. På denne siden ser du detaljene for din Tx0 :




- antall UTXO-er som skal inn i bassenget;
- de ulike avgiftene (serviceavgifter og mining-avgifter) ;
- mengden av den *doksiske endringen*.



Kontroller informasjonen nøye, og klikk deretter på `Broadcast` for å kringkaste Tx0.



![Image](assets/fr/08.webp)



Ashigaru viser deretter TXID for din Tx0, og bekrefter at transaksjonen har blitt kringkastet i nettverket.



![Image](assets/fr/09.webp)



## Lage sammenføyninger



Når Tx0 har blitt sendt, går du tilbake til startsiden for innskuddskontoen din, klikker på `Kontoer` og velger `Premix`-kontoen.



![Image](assets/fr/10.webp)



I menyen `UTXOs` ser du de ulike utjevnede delene, klare til å gå inn i cojoin-syklusene. Så snart Tx0 er bekreftet, vil Ashigaru Terminal automatisk starte sin første blandingssyklus.



![Image](assets/fr/11.webp)



Når Tx0 er bekreftet, vil den første coinjoin-transaksjonen opprettes og sendes automatisk av Ashigaru Terminal. Ved å gå til `Kontoer > Postmix > UTXO` kan du se dine utlignede UTXO-er, i påvente av bekreftelse av deres første syklus.



![Image](assets/fr/12.webp)



Du kan nå la Ashigaru Terminal kjøre i bakgrunnen: Den vil fortsette å mikse og remikse sporene dine automatisk.



## Etterbehandling av sammenføyninger



Nå kan du la myntene dine remikse seg selv automatisk. Whirlpool-modellen betyr at det ikke er noen ekstra kostnader for remixing: ingen serviceavgifter, ingen mining-avgifter. Så det å la myntene dine delta i flere blandingssykluser kan bare være til fordel for konfidensialiteten din.



For en bedre forståelse av denne mekanismen og hvor mange sykluser det er verdt å vente på, anbefaler jeg å lese denne artikkelen:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Hvis du vil se antall remikser som er utført av hvert av stykkene dine, åpner du menyen `UTXOs` i `Postmix`-kontoen.



![Image](assets/fr/13.webp)



For å bruke de blandede myntene dine går du til Ashigaru-applikasjonen, som bruker samme wallet som Ashigaru Terminal-programvaren din. wallet som vises ved åpning, tilsvarer innskuddskontoen din. For å få tilgang til `Postmix`-kontoen, som inneholder dine blandede UTXO-er, klikker du på Whirlpool-symbolet øverst i høyre hjørne.



![Image](assets/fr/14.webp)



På denne kontoen ser du alle myntene dine som for øyeblikket blandes. For å bruke dem trykker du på symbolet `+` nederst til høyre på skjermen, og velger deretter `Send`.



![Image](assets/fr/15.webp)



Fyll ut detaljene for transaksjonen: mottakerens adresse, beløpet som skal sendes, og hvis du ønsker det, kan du velge en spesifikk transaksjonsstruktur for å øke konfidensialiteten ytterligere (se de tilhørende veiledningene).



![Image](assets/fr/16.webp)



Kontroller transaksjonsdetaljene nøye, og dra deretter pilen nederst på skjermen for å bekrefte forsendelsen.



![Image](assets/fr/17.webp)



Transaksjonen din er signert og sendt på Bitcoin-nettverket.



![Image](assets/fr/18.webp)



## Bruk Doxxic Change



Husk på dette: Whirlpools modell er basert på utjevning av brikkene dine ved Tx0, før de går inn i puljene. Det er denne mekanismen som bryter sporingen av UTXO-er. Etter min mening er dette den mest effektive coinjoin-modellen, men den har én ulempe: Den genererer en *endring* som ikke går gjennom coinjoin-prosessen.



Denne endringen tilsvarer en UTXO som er opprettet for hver Tx0. Den er isolert i en spesifikk konto som heter `Doxxic Change` eller `Bad Bank`, avhengig av programvaren, for å unngå at den brukes sammen med andre UTXO-er. Dette er svært viktig, fordi disse UTXO-ene ikke har blitt blandet: sporbarhetskoblingene deres forblir intakte, og de kan kompromittere konfidensialiteten din ved å etablere en forbindelse mellom deg og coinjoin-aktiviteten din. Så håndter dem med forsiktighet, og **bruk dem aldri sammen med andre UTXO-er**, uansett om de er blandet eller ikke. Hvis du kombinerer en giftig UTXO med en blandet UTXO, vil det utslette alle personverngevinstene du har oppnådd ved coinjoining.



For øyeblikket tilbyr ikke Ashigaru direkte tilgang til denne `Doxxic Change`-kontoen (jeg har i hvert fall ikke funnet den). Denne funksjonen vil sannsynligvis bli lagt til i en fremtidig oppdatering. I mellomtiden er den eneste måten å hente disse midlene på å importere seed til Sparrow Wallet. Sistnevnte vil normalt automatisk oppdage at dette er en wallet som brukes sammen med Whirlpool, og gi deg tilgang til alle fire kontoene, inkludert `Doxxic Change`-kontoen. Du kan deretter bruke disse UTXO-ene som vanlige bitcoins fra Sparrow.



Her er flere mulige strategier for å administrere UTXO-er i utenlandsk valuta fra coinjoins uten at det går på bekostning av personvernet ditt:





- Slå dem sammen til mindre bassenger:** Hvis din giftige UTXO er stor nok til å bli med i et mindre basseng, er dette vanligvis det beste alternativet. Vær imidlertid forsiktig så du aldri slår sammen flere giftige UTXO-er for å oppnå dette, da dette vil skape en kobling mellom de ulike oppføringene dine i Whirlpool.





- Merk dem som ikke-brukbare:** En annen forsiktig tilnærming er å beholde dem som de er på sin egen konto og la dem stå urørt. Dette forhindrer at du bruker dem ved et uhell. Hvis verdien av bitcoin øker, kan det bli åpnet nye bassenger som er tilpasset størrelsen.





- Gi donasjoner:** Du kan velge å gjøre disse giftige UTXO-ene om til donasjoner til Bitcoin-utviklere, åpen kildekode-prosjekter eller foreninger som godtar BTC. På denne måten kan du kvitte deg med dem på en nyttig måte og samtidig støtte økosystemet.





- Kjøp forhåndsbetalte gavekort eller Visa-kort:** Plattformer som [Bitrefill] (https://www.bitrefill.com/) lar deg veksle inn bitcoins i gavekort eller oppladbare Visa-kort som kan brukes i butikker. Dette kan være en enkel og diskret måte å bruke giftige UTXO-er på.





- Bytt dem mot Monero:** Samourai Wallet pleide å tilby en nå nedlagt BTC/XMR atomic swap-tjeneste. Hvis det finnes en lignende tjeneste (jeg kjenner ikke til noen personlig), er det en utmerket løsning for å isolere disse UTXO-ene, konvertere dem til Monero, og deretter sende dem tilbake til Bitcoin. Denne metoden var imidlertid dyr og avhengig av tilgjengelig likviditet.





- Overfør dem til Lightning Network:** Å overføre disse UTXO-ene til Lightning Network for å dra nytte av reduserte transaksjonsgebyrer er et potensielt interessant alternativ. Denne metoden kan imidlertid avsløre visse opplysninger avhengig av hvordan du bruker Lightning, og bør derfor brukes med forsiktighet.



## Hvordan kan jeg finne ut mer om kvaliteten på våre coinjoin-sykluser?



For at en coinjoin skal være virkelig effektiv, må den ha en høy grad av ensartethet mellom inngående og utgående beløp. Denne ensartetheten øker antallet mulige tolkninger for en utenforstående observatør, noe som i sin tur øker usikkerheten om transaksjonen. For å måle denne usikkerheten bruker vi begrepet entropi anvendt på transaksjonen. Whirlpool-modellen er anerkjent som en av de mest effektive i så måte, ettersom den garanterer utmerket homogenitet mellom deltakerne. For en grundigere gjennomgang av dette prinsippet anbefaler jeg at du leser det siste kapittelet i del 5 av BTC 204-kurset.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Ytelsen til flere coinjoin-sykluser måles ut fra størrelsen på mengdene som en mynt er skjult i. Disse settene definerer det som kalles *anonsett*. Det finnes to typer: Den første måler konfidensialitet i møte med retrospektiv analyse (fra nåtid til fortid), og den andre måler motstand mot prospektiv analyse (fra fortid til nåtid). For en fullstendig forklaring av disse to indikatorene, vennligst les følgende veiledning (eller, nok en gang, BTC 204-kurset):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Hvordan håndtere postmixen?



Etter å ha kjørt flere coinjoin-sykluser er den beste strategien å beholde UTXO-ene dine på `Postmix`-kontoen, og la dem remixes på ubestemt tid til du virkelig trenger å bruke dem.



Noen brukere foretrekker å overføre sine blandede bitcoins til en wallet sikret av wallet-maskinvare. Dette alternativet er mulig, men krever en viss grad av strenghet for å sikre at konfidensialiteten som er oppnådd med coinjoins ikke kompromitteres.



Sammenslåing av UTXO-er er den hyppigste feilen. Det er viktig å aldri kombinere blandede UTXO-er med ublandede UTXO-er i samme transaksjon, ellers risikerer du å utløse *Common Input Ownership Heuristic (CIOH)*. Dette innebærer streng håndtering av UTXO-er, særlig gjennom tydelig og presis merking. Generelt sett er sammenslåing av UTXO-er en dårlig praksis som ofte fører til tap av konfidensialitet når den håndteres dårlig.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Du bør også være forsiktig med å konsolidere blandede UTXO-er. Begrensede konsolideringer kan vurderes hvis UTXO-ene har betydelige anonsett, men de vil uunngåelig redusere konfidensialitetsnivået. Unngå massive eller forhastede konsolideringer som utføres før et tilstrekkelig antall remikser, ettersom de kan etablere inferensielle koblinger mellom delene før og etter remiksen. I tvilstilfeller er det best å ikke konsolidere postmix-UTXO-ene, men overføre dem én etter én til wallet-maskinvaren, og generere en ny tom mottaksadresse hver gang. Ikke glem å merke hver overført UTXO.



Vi fraråder på det sterkeste å flytte postmix UTXO-er til porteføljer som bruker minoritetsskript. Hvis du for eksempel deltok i Whirlpool fra en multi-sig-portefølje i `P2WSH`, vil det være få av dere som deler denne typen skript. Ved å sende postmix UTXO-er til samme type skript, reduserer du anonymiteten din betraktelig. Utover skripttypen kan andre spesifikke wallet-fingeravtrykk kompromittere konfidensialiteten din, så det beste du kan gjøre er å bruke dem fra Ashigaru-applikasjonen.



Til slutt, som med alle Bitcoin-transaksjoner, må du aldri gjenbruke en mottakeradresse. Hver betaling må sendes til en ny, unik, tom adresse.



Den enkleste og tryggeste metoden er å la de blandede UTXO-ene hvile på "Postmix"-kontoen, la dem remixes naturlig, og bare bruke dem fra Ashigaru når det er nødvendig.



Ashigaru- og Sparrow-lommebøkene inneholder ekstra sikkerhetstiltak mot de vanligste feilene knyttet til blokkjedeanalyse, slik at du kan bevare konfidensialiteten til transaksjonene dine.