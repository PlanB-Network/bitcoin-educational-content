---
term: BIP143

---
Innfører en ny måte å hashe transaksjonen på for signaturverifisering i post-SegWit-skript. Målet er å minimere overflødige operasjoner under verifiseringen og å inkludere verdien av UTXO-ene i inndataene i signaturen. Dette løser to store problemer med den opprinnelige transaksjonshashingalgoritmen:


- Den kvadratiske veksten i datahashing med antall signaturer;
- Fraværet av å inkludere inngangsverdien i signaturen, noe som utgjorde en risiko for maskinvarelommebøker, spesielt med tanke på kunnskapen om påløpte transaksjonsgebyrer.

Siden SegWit-oppdateringen, som ble forklart i BIP141, introduserer en ny form for transaksjoner hvis skript ikke vil bli verifisert av gamle noder, benytter BIP143 anledningen til å løse dette problemet uten å kreve en hard fork. Derfor er BIP143 en del av SegWit soft fork.