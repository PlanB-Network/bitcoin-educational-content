---
term: MOTTAKSADRESSE

---
Informasjon som brukes til å motta bitcoins. En adresse konstrueres vanligvis ved å hashe en offentlig nøkkel ved hjelp av `SHA256` og `RIMPEMD160`, og legge til metadata i dette sammendraget. De offentlige nøklene som brukes til å konstruere en mottakeradresse, er en del av brukerens lommebok og er derfor avledet fra deres seed. SegWit-adresser består for eksempel av følgende informasjon:


- En HRP for å betegne "bitcoin": `bc`;
- Et skilletegn: `1`;
- Versjonen av SegWit som brukes: `q` eller `p`;
- Nyttelasten: fordøyelsen av den offentlige nøkkelen (eller direkte den offentlige nøkkelen i tilfellet Taproot);
- Sjekksummen: en BCH-kode.

En mottakeradresse kan imidlertid også representere noe annet, avhengig av hvilken skriptmodell som brukes. P2SH-adresser konstrueres for eksempel ved hjelp av skriptets hash. Taproot-adresser inneholder derimot den finjusterte offentlige nøkkelen direkte uten å hashe den.

En mottakeradresse kan representeres i form av en alfanumerisk streng eller som en QR-kode. Hver adresse kan brukes flere ganger, men dette frarådes på det sterkeste. For å opprettholde et visst nivå av personvern anbefales det å bruke hver Bitcoin-adresse bare én gang. En ny adresse bør genereres for hver innkommende betaling til lommeboken. En adresse er kodet i `Bech32` for SegWit V0-adresser, i `Bech32m` for SegWit V1-adresser og i `Base58check` for Legacy-adresser. Fra et teknisk ståsted betyr det å motta bitcoin at man har den private nøkkelen som er knyttet til en offentlig nøkkel (og dermed en adresse). Når noen mottar bitcoins, oppdaterer avsenderen den eksisterende begrensningen på pengebruken, slik at bare mottakeren nå kan ha denne makten.

![](../../dictionnaire/assets/23.webp)