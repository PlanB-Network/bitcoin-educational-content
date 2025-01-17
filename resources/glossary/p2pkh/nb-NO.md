---
term: P2PKH

---
P2PKH står for *Pay to Public Key Hash*. Det er en standard skriptmodell som brukes til å etablere utgiftsbetingelser på en UTXO. Det gjør det mulig å låse bitcoins på en hash av en offentlig nøkkel, det vil si på en mottakeradresse. Dette skriptet er knyttet til Legacy-standarden og ble introdusert i de tidlige versjonene av Bitcoin av Satoshi Nakamoto.

I motsetning til P2PK, der den offentlige nøkkelen er eksplisitt inkludert i skriptet, bruker P2PKH et kryptografisk fingeravtrykk av den offentlige nøkkelen. Dette skriptet inkluderer `RIPEMD160`-hashingen av `SHA256` av den offentlige nøkkelen, og bestemmer at for å få tilgang til midlene må mottakeren oppgi en offentlig nøkkel som samsvarer med denne hashen, samt en gyldig digital signatur som er generert fra den tilhørende private nøkkelen. P2PKH-adresser er kodet i `Base58Check`-format, noe som gjør dem robuste mot typografiske feil ved hjelp av en sjekksum. Disse adressene starter alltid med tallet "1".