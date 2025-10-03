---
name: BitcoinVoucherBot
description: En Telegram-bot for å kjøpe Bitcoin i konfidensialitet
---
![image](assets/cover.webp)

_Denne veiledningen er skrevet av_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

## Introduksjon

BitcoinVoucherBot er et verktøy som Bitcoins kan kjøpes i Exchange for euro.

### KYC Light

Å bytte euro til Bitcoin er det første og mest grunnleggende skrittet for å begynne å studere dette emnet, men det er tilsynelatende også det vanskeligste og mest komplekse. Det kan være mange alternativer: å tilby Bitcoin gjennom sentraliserte børser, Bitcoin-temamøter, venner, bekjente og mer. Vi slutter oss til Bitcoiner-samfunnet, og **vi anbefaler absolutt bruk av sentraliserte utvekslinger** for å ivareta mer oppmerksomhet på personvernet.

Selv om dette valget kan være mindre praktisk, er det viktig å forstå at børser håndhever KYC-forordningen (Know Your Cutomer), og dermed tilordner en identitet, så vel som en fysisk plassering, til hver Satoshi som kjøpes fra dem. "Bekvemmelighet" har noen slående bivirkninger.

### Hvordan gjør man det?

Her kommer tjenesten [BitcoinVoucherBot:] (https://t.me/BitcoinVoucherBot), en Telegram-bot som fungerer som en kanal mellom våre SEPA-overføringer og Sats-kjøp.

### Forkunnskaper

For å begynne å bruke BitcoinVoucherBot, er det ikke nødvendig å oppgi sensitive personopplysninger til Bot-personalet. **Ingen autorisasjon nødvendig**.

Alt som trengs er en allerede aktiv Telegram-konto og en bankkonto. **Merknad**: En konto som er åpnet hos Poste Italiane (for italienske kunder) eller, mer generelt, med henvisning til et oppladbart kort, er ikke egnet.

I Telegram-chatten forbereder vi en bestilling, med en bankoverføring betaler vi for den, og til slutt gjennom boten får vi en kupong utstedt av et tredjepartsfirma som ikke kjenner gjenstanden for kjøpet.

### Bot-aktivering og meny

Aktivering er en enkel engangsoperasjon. Fra Telegram, søk etter _@BitcoinVoucherBot_, og så snart du kommer til Bot's chat, skiller en stor _Start / Start_-knapp seg ut nederst. Operasjonen får Bot til å svare, som presenterer en meny med de viktigste kommandoene som er tilgjengelige for den. De første velkomstmeldingene vises også, og vi anbefaler at du leser dem nøye.

**Advarsel**: det finnes flere svindlere som utgir seg for å være den originale VoucherBot. Hvis du ikke er sikker på søket via Telegram, gå til BitcoinVoucherBot-lenken fra [offisiell side](https://www.bitcoinvoucherbot.com/)

![image](assets/it/01.webp)

Alternativene vises ved å klikke på _Menu_-knappen i nedre venstre hjørne: Du kan klikke på ordet som tilsvarer kommandoen, eller skrive inn skråstreken `/` etterfulgt av kommandoen i meldingsboksen.

![image](assets/it/02.webp)

Viktige operasjoner inkluderer:


- _/purchase_: er den faktiske kjøpsprosedyren. Når transaksjonen er fullført, genereres QR-koden automatisk av boten, klar for innløsning.
- _/refill_: tilgjengelig på det tidspunktet denne veiledningen ble skrevet, men vi kommer ikke til å ta for oss dette alternativet, fordi det av tekniske årsaker kan bli fjernet senere.
- _/swap_: åpner bytteprosedyren, tilgjengelig enten med en praktisk Telegram-bot eller via nettet.
- _/ap_: Akkumuleringsplan, som gjør det mulig å sette opp en **Constant Accumulation Plan (CAP)**.
- _/lnaddress_: som vi blir bedt om å koble en egen LN Address til, for en bestemt prosedyre som vi skal se senere.
- _/credits_: for å sjekke hvor mye kreditt som er igjen til generate-kuponger.
- _/myorders_: viser bestillinger som er lagt inn med boten (**Advarsel** systemet sporer bare de siste 10 bestillingene som er lagt inn, og ikke hele historikken).
- _/fees_: en kommando for å sjekke nettverksavgifter. For å evaluere dem er det alltid best å stole på Mempool.space.
- _/support_: ved behov dukker det opp kontakter for å rapportere problemer til supportteamet.

## Prosedyre for kjøp av Bitcoin

### Forberedelse av bestillingen

Klikk på _/kjøpe_ i kommandomenyen

![image](assets/it/03.webp)

En rekke muligheter dukker opp, men vi velger _BTC Vouchers_

![image](assets/it/04.webp)

BitcoinVoucherBot lar deg kjøpe Bitcoin onchain, Lightning og Liquid.

På dette stadiet velger du _Onchain & Lightning 🔗⚡️_

![image](assets/it/05.webp)

Skjermen endres raskt, og VoucherBot foreslår kjøpsbetegnelser. De starter fra minimum kr 1.00 opp til kr 900.00.

Ved et første kjøp tilbys kun valørene 100,00 €, Onchain og Lightning. For å øke konfidensialiteten foreslår vi at du velger _Lightning ⚡️_

![image](assets/it/06.webp)

VoucherBot varsler oss om at et førstevalg er gjort, og at vi må velge _Proceed_ for å bekrefte det

![image](assets/it/07.webp)

Det er nå et spørsmål om å velge betalingsmetode. Overføringen skjer ved bankoverføring **(aksepteres kun SEPA)**. VoucherBot foreslår som mottaker et selskap som tilbyr to bankkontoer, den ene i Storbritannia og den andre i Sveits. Den sveitsiske banken ble valgt for å utføre denne opplæringen

![image](assets/it/08.webp)

På dette tidspunktet blir vi bedt om å oppgi IBAN-nummeret vårt, det som overføringen til den valgte banken vil starte fra. Denne informasjonen utgjør et puslespill som gjør det mulig for boten, det vil si en maskin, å sette sammen informasjon for å få kjøpsprosessen til å flyte uten behov for menneskelig inngripen.

IBAN-nummeret må skrives i meldingsfeltet, kontrolleres og sendes til boten.

![image](assets/it/09.webp)

Det vises nå en kontrollmelding i chatten med VoucherBot.

Hvis alt er i orden, fortsetter du ved å klikke på _Proceed_.

![image](assets/it/10.webp)

### Betaling

Etter noen få øyeblikk, som er nødvendig for å behandle dataene, svarer VoucherBot med en melding som inneholder alle detaljene som er nødvendige for å fullføre bestillingen. Avhengig av hva banken din krever, er den relevante informasjonen:


- iBAN, som er avgjørende for innskuddet, samt mottakerens Address;
- `det valgte beløpet` tidligere gjennom cutoff, som må være oppfylt for at VoucherBot skal kunne gjenkjenne bestillingen når betalingen er mottatt;
- betalingsårsak, som er årsaken til betalingen. **Må kopieres og limes inn uten å fjerne eller legge til noe i det aktuelle feltet i overføringen. Eventuelle "." eller "-" i betalingsårsaken kan erstattes av `hvit plass'**.
- en unik `OrderID` å referere til når du ber om hjelp.

Deretter kan du gjennomføre betalingen via appen eller banken din. Når betalingen er akseptert av banken, er det viktig å huske å trykke på _Notify payment_ i chatten med VoucherBot. Denne enkle operasjonen varsler deg om at en betaling er på vei.

![image](assets/it/11.webp)

VoucherBot svarer med en melding som inneholder en svært viktig advarsel: **Ikke slett chatten**, i hvert fall ikke før kupongen er mottatt, for det er den eneste måten å rekonstruere bestillingen på og holde den i gang.

![image](assets/it/12.webp)

---
Vær oppmerksom på dette:


- kun SEPA-overføringer godtas;
- ventetiden er utelukkende knyttet til hvordan bankene (som ikke jobber 24/7/365 som Bitcoin) behandler kupongen. Det kan ta fra noen timer opp til tre virkedager å motta kupongen;
- for alle behov, Bitcoin VoucherBot har en utmerket [support] (https://t.me/BitcoinVoucherGroup) service på Telegram.

---
### Innløsning

Så snart betalingen er vellykket, sender Bitcoin VoucherBot kupongen direkte inn i chatten. Lynkupongen er i form av en QR-kode, trykt på en oransje bakgrunn.

![image](assets/it/31.webp)

Det er alle dataene som trengs for å innløse den:


- beløpet i Sats, tilsvarende det som sendes via bankoverføring, ekskludert service- og nettverksgebyrer;
- en referanse-ID for bilaget;
- datoen da kupongen må være innløst, ellers vil midlene gå tapt, dvs. 25 dager etter utstedelse.

Du kan løse inn kupongen ved å ramme inn QR-koden med skannefunksjonen på en kompatibel Wallet Lightning Network, eller via LNURL, som også vises under QR-koden.

For denne veiledningen brukte vi Wallet Of Satoshi, med skannefunksjonen aktivert av _Send_-knappen.

![image](assets/it/32.webp)

Med mobilkameraet aktivert, rammer du inn QR-koden i chatten, og åpner Telegram fra PC

![image](assets/it/34.webp)

Før du fortsetter, viser Wallet Of Satoshi en bekreftelsesskjerm som inkluderer beløpet, som nøyaktig tilsvarer det som er angitt på kupongen, og som beskrivelse, BitcoinVoucherBot. For å løse inn kupongen er det bare å klikke på _Receive_.

![image](assets/it/35.webp)

Wallet Of Satoshi behandler i noen øyeblikk.

![image](assets/it/36.webp)

og til slutt rapporteres innsamlingen og er umiddelbart tilgjengelig i Wallet-saldoen.

**Wallet of Satoshi er en forvarings-app: rett etter innløsning av kupongen anbefales det å flytte satsene til en ikke-forvarings-lommebok.**

![image](assets/it/37.webp)

### Slik løser du inn en onchain-kupong

Som vi så i ordreforberedelsen, tillater VoucherBot at Sats kan kjøpes direkte på kjeden, med valg av den eponymiske kupongen.

**Merknad**: Ordreforberedelse og betaling endres ikke, de er alltid de samme. Det som endres, er hvordan en kupong i kjeden innløses.

Etter at du har fullført bestillingen, foretatt betalingen, trykket på _Notify payment_ og ventet på bankenes tekniske tid til å overføre overføringen, vil VoucherBot svare ved å sende kupongen direkte inn i chatten.

Denne kupongen er også i form av en QR-kode, men hovedfargen er kanarigul og - viktigst av alt - i beskrivelsen er det godt forklart at det er en onchain-kupong, som du kontanter direkte på Wallet onchain, og for å starte utbetalingsprosedyren, må du klikke på _Redeem on Telegram_. Onchain-kupongen inneholder også informasjonen som allerede er sett for lynet:


- beløpet i Sats, tilsvarende det som sendes via bankoverføring, unntatt service- og nettverksgebyrer;
- en kupongkode;
- en referanse-ID for bilaget;
- datoen da kupongen må være innløst, ellers vil midlene gå tapt, dvs. 25 dager etter utstedelse.

![image](assets/it/22.webp)

** ADVARSEL ⚠️:** klikket som forklart, åpnes popup-vinduet til en annen bot: **Voucher RedeemBot.**

Voucher RedeemBot er verktøyet som er gjort tilgjengelig for dette formålet. Enten dette er første gangs bruk eller om det er tidligere bestillinger, er det alltid nødvendig å klikke på _START_ hver gang en ny innløsning foretas.

![image](assets/it/23.webp)

På dette tidspunktet laster RedeemBot inn kupongen i kjeden, lett gjenkjennelig med kupongkode og referanse-ID. Det låser også opp baren for å skrive meldinger og begynne å chatte med boten, som faktisk inviterer oss til å fortelle den en onchain Address av vår Wallet.

**Merknad**: Denne Address må være av typen SegWit.

![image](assets/it/24.webp)

Vi åpner Wallet på dette tidspunktet, og generate en SegWit Address

![image](assets/it/25.webp)

vi kopierer det

![image](assets/it/26.webp)

og lim den inn i chatten med RedeemBot

![image](assets/it/27.webp)

Vi har nå et kontrollskjermbilde for å verifisere at kupongkoden er riktig, samt Address vi har kommunisert til RedeemBot. La oss sjekke det godt, for ved å klikke på _Proceed_ starter transaksjonen, og det vil ikke være mulig å finne den igjen hvis vi for eksempel har kommunisert feil Address.

![image](assets/it/28.webp)

Transaksjonen har startet, og Redeem-prosedyren for onchain-voucheren er dermed avsluttet.

![image](assets/it/29.webp)

mens beløpet kan sees komme i historien til vår Wallet.

![image](assets/it/30.webp)