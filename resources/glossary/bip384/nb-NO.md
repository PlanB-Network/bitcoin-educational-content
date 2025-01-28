---
term: BIP384

---
Introduserer funksjonen `combo(KEY)` for deskriptorer. Denne funksjonen beskriver et sett med mulige utdataskript for en gitt offentlig nøkkel. Den dekker dermed flere typer skript samtidig, inkludert P2PK, P2PKH, P2WPKH og P2SH-P2WPKH. Hvis den gitte nøkkelen er komprimert, testes alle de fire skripttypene, og hvis den ikke er det, testes bare de to eldre skripttypene. Målet er å forenkle representasjonen av nøkler i deskriptorer ved å tilby en enkelt metode for å generere ulike varianter av utdataskript basert på samme offentlige nøkkel. BIP384 ble implementert sammen med alle andre deskriptorrelaterte BIP-er (unntatt BIP386) i versjon 0.17 av Bitcoin Core.