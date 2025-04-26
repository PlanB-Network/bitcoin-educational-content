---
term: STILLE BETALINGER

---
Metode for å bruke statiske Bitcoin-adresser til å motta betalinger uten gjenbruk av adresser, uten interaksjon og uten en synlig kobling i kjeden mellom de ulike betalingene og den statiske adressen. Denne teknikken eliminerer behovet for å generere nye, ubrukte mottakeradresser for hver transaksjon, og dermed unngår man de vanlige interaksjonene i Bitcoin der mottakeren må oppgi en ny adresse til betaleren.

Med Silent Payments bruker betaleren mottakerens offentlige nøkler (spend public key og scan public key) og summen av sine egne private nøkler som input for å generere en ny adresse for hver betaling. Bare mottakeren, med sine private nøkler, kan beregne den private nøkkelen som svarer til denne betalingsadressen. ECDH (*Elliptic-Curve Diffie-Hellman*), en kryptografisk nøkkelutvekslingsalgoritme, brukes til å etablere en delt hemmelighet som deretter brukes til å utlede mottakeradressen og den private nøkkelen (kun på mottakerens side). For å identifisere Silent Payments må mottakerne skanne blokkjeden og undersøke hver transaksjon som samsvarer med protokollens kriterier. I motsetning til BIP47, som bruker en varslingstransaksjon for å etablere betalingskanalen, eliminerer Silent Payments dette trinnet og sparer en transaksjon. Kompromisset er imidlertid at mottakeren må skanne alle potensielle transaksjoner for å avgjøre, ved å bruke ECDH, om de er adressert til dem.

Bobs statiske adresse $B$ representerer for eksempel sammenkjedningen av den offentlige skannøkkelen og den offentlige utgiftsnøkkelen hans:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Disse nøklene er ganske enkelt avledet fra følgende sti:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Denne statiske adressen publiseres av Bob. Alice henter den for å foreta en stille betaling til Bob. Hun beregner Bobs betalingsadresse $P_0$ på denne måten:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$$

Hvor?

$$ \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A) $$$

Med:


- $B_{\text{scan}}$: Bobs offentlige nøkkel for skanning (statisk adresse);
- $B_{\text{spend}}$: Bobs offentlige nøkkel for spend (statisk adresse);
- $A$: Summen av de offentlige nøklene i inndata (tweak);
- $a$: Den private nøkkelen til tilpasningen, det vil si summen av alle nøkkelparene som brukes i `scriptPubKey` i UTXO-ene som brukes som inndata i Alices transaksjon;
- $\tekst{utgangspunkt}_L$: Den minste UTXO-en (leksikografisk) som brukes som input i Alices transaksjon;
- $\text{ ‖ }$: Konkatenering (operasjonen for å koble sammen operander fra ende til ende);
- $G$: Generatorpunktet til den elliptiske kurven `secp256k1`;
- $\text{hash}$: SHA256-hashfunksjonen merket med `BIP0352/SharedSecret`;
- $P_0$: Den første offentlige nøkkelen / unike adressen for betaling til Bob;
- $0$: Et heltall som brukes til å generere flere unike betalingsadresser.

Bob skanner blokkjeden for å finne sin Silent Payment på denne måten:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$$

Med:


- $b_{\text{scan}}$: Bobs private skannøkkel.

Hvis han finner $P_0$ som en adresse som inneholder en Stille betaling adressert til ham, beregner han $p_0$, den private nøkkelen som gjør det mulig for ham å bruke pengene som Alice har sendt til $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$$

Med:


- $b_{\text{spend}}$: Bobs private utgiftsnøkkel;
- $n$: ordenen til den elliptiske kurven `secp256k1`.

I tillegg til denne grunnversjonen kan etikettene også brukes til å generere flere ulike statiske adresser fra samme statiske grunnadresse, slik at man kan skille flere bruksområder fra hverandre uten at det krever urimelig mye arbeid under skanningen.