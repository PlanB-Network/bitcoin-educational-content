---
term: OUTPUT SCRIPT DESCRIPTORS

---
Output script descriptors, eller bare descriptors, er strukturerte uttrykk som fullt ut beskriver et output script (`scriptPubKey`) og gir all nødvendig informasjon for å spore transaksjoner til eller fra et bestemt script. Disse deskriptorene gjør det enklere å administrere nøkler i HD-lommebøker ved hjelp av en standardbeskrivelse av strukturen og adressetypene som brukes.

Det interessante med deskriptorer er at de kan innkapsle all viktig informasjon for gjenoppretting av en lommebok i én enkelt streng (i tillegg til gjenopprettingsfrasen). Ved å lagre en deskriptor med de tilsvarende mnemoniske frasene er det mulig å gjenopprette ikke bare de private nøklene, men også den nøyaktige strukturen til lommeboken og de tilhørende skriptparameterne. For å gjenopprette en lommebok kreves det ikke bare kunnskap om det opprinnelige frøet, men også spesifikke indekser for avledning av underordnede nøkkelpar, samt `xpub` for hver faktor i tilfelle en multisig-lommebok. Tidligere ble det antatt at denne informasjonen var implisitt kjent av alle. Men med mangfoldet av skript og fremveksten av mer komplekse konfigurasjoner kan denne informasjonen bli vanskelig å ekstrapolere, noe som gjør disse dataene til privat informasjon som er vanskelig å bryte ut. Bruken av deskriptorer forenkler prosessen betraktelig: Det er nok å kjenne til gjenopprettingsfrasen(e) og den tilhørende deskriptoren for å gjenopprette alt på en pålitelig og sikker måte.

En deskriptor består av flere elementer:


- Skriptfunksjoner som `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignatur), og `sortedmulti` (Multisignatur med sorterte nøkler);
- Avledningsstier, for eksempel `[d34db33f/44h/0h/0h]`, som angir en avledet sti og et bestemt hovednøkkelfingeravtrykk;
- Nøkler i ulike formater, for eksempel heksadesimale offentlige nøkler eller utvidede offentlige nøkler (`xpub`);
- En sjekksum, innledet av en hash, for å verifisere deskriptorens integritet.

En deskriptor for en P2WPKH-lommebok kan for eksempel se slik ut:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

I denne deskriptoren angir avledningsfunksjonen `wpkh` en Pay-to-Witness-Public-Key-Hash-skriptype. Den etterfølges av avledningsbanen som inneholder:


- `cdeab12f`: fingeravtrykket til hovednøkkelen;
- `84h`: som betyr bruk av et BIP84-formål, beregnet for SegWit v0-adresser;
- `0h`: som indikerer at det er en BTC-valuta på hovednettet;
- `0h`: som refererer til det spesifikke kontonummeret som brukes i lommeboken.

Deskriptoren inneholder også den utvidede offentlige nøkkelen som brukes i denne lommeboken:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Notasjonen `/<0;1>/*` angir at deskriptoren kan generere adresser fra den eksterne (`0`) og interne (`1`) kjeden, med et jokertegn (`*`) som muliggjør sekvensiell avledning av flere adresser på en konfigurerbar måte, på samme måte som en "gap limit" i tradisjonell lommebokprogramvare.

Til slutt representerer `#jy0l7nr4` sjekksummen for å verifisere integriteten til deskriptoren.