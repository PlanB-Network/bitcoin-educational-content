---
term: COVENANT

---
En mekanisme som gjør det mulig å pålegge spesifikke betingelser for hvordan en gitt del av valutaen kan brukes, inkludert i fremtidige transaksjoner. Utover de betingelsene som vanligvis tillates av skriptspråket på en UTXO, håndhever pakten ytterligere begrensninger for hvordan denne Bitcoin kan brukes i påfølgende transaksjoner. Teknisk sett oppstår etableringen av en pakt når `scriptPubKey` av en UTXO definerer restriksjoner på `scriptPubKey` av utdataene til en transaksjon som bruker UTXO-en. Ved å utvide omfanget av skriptet, vil pakter muliggjøre en rekke utviklinger på Bitcoin, for eksempel bilateral forankring av drivkjeder, implementering av hvelv eller forbedring av overleggssystemer som Lightning. Paktforslag er differensiert basert på tre kriterier:


- Deres omfang;
- Implementeringen av dem;
- Deres rekursivitet.

Det finnes mange forslag som åpner for bruk av pakter på Bitcoin. De mest avanserte i implementeringsprosessen er: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO), og `OP_VAULT`. Blant andre forslag er det: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, osv.

For å forstå begrepet pakt bedre, kan du tenke deg følgende analogi: Tenk deg en safe som inneholder 500 euro i små sedler. Hvis du klarer å låse opp safen med den riktige nøkkelen, står du fritt til å bruke pengene som du vil. Dette er den normale situasjonen med Bitcoin. Tenk deg nå at den samme safen ikke inneholder 500 euro i sedler, men i stedet måltidskuponger av tilsvarende verdi. Hvis du lykkes med å åpne safen, kan du bruke denne summen. Men du har begrenset frihet til å bruke pengene, ettersom du bare kan bruke disse kupongene til å betale på visse restauranter. Den første betingelsen for å bruke pengene er altså at du klarer å åpne safen med den riktige nøkkelen. Men det er også en ytterligere betingelse for fremtidig bruk av denne summen: Den må utelukkende brukes på partnerrestauranter, og ikke fritt. Dette systemet med begrensninger på fremtidige transaksjoner er det som kalles en pakt.

> på fransk finnes det ikke noe begrep som presist dekker betydningen av ordet "pakt". Man kan snakke om "klausul", "pakt" eller "forpliktelse", men disse begrepene tilsvarer ikke helt begrepet "pakt". Dette begrepet er lånt fra juridisk terminologi som gjør det mulig å beskrive en kontraktsklausul som pålegger en eiendom varige forpliktelser*