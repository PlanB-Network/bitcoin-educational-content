---
term: BIP12

---
Forslag av Gavin Andresen for å forbedre fleksibiliteten og personvernet til Bitcoin-transaksjonsskript. Denne BIP-en foreslår å implementere en ny skript-opkode, kalt `OP_EVAL`, som gjør det mulig å evaluere et skript som finnes i dataene til en `scriptSig` under transaksjonsvalideringsprosessen. Den viktigste endringen i BIP12 er å gjøre det mulig å inkludere et skript i et annet skript. Denne teknikken gjør det mulig å opprette mer komplekse betingelser som kan verifiseres på utgiftstidspunktet, uten å måtte avsløre dem for brukere som sender bitcoins til den brukte adressen. BIP12 ble senere erstattet av sikrere forslag, særlig BIP16 (P2SH), som tilbyr en annen metode for å oppnå de samme målene som `OP_EVAL`.