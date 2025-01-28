---
term: TXID (TRANSAKSJONSIDENTIFIKATOR)

---
En unik identifikator knyttet til hver Bitcoin-transaksjon. Den genereres ved å beregne `SHA256d`-hashingen av transaksjonsdataene. TXID fungerer som en referanse for å finne en spesifikk transaksjon i blokkjeden. Den brukes også til å referere til en UTXO, som egentlig er en sammenkobling av en tidligere transaksjons TXID og indeksen for den utpekte utgangen (også kalt "vout"). For post-SegWit-transaksjoner tar TXID ikke lenger hensyn til transaksjonsvitnet, noe som eliminerer manipulerbarhet.