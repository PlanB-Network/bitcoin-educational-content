---
term: P2SH-P2WPKH
definition: SegWit-skript (P2WPKH) inbakat i P2SH för kompatibilitet, adresser börjar på 3.
---

P2SH-P2WPKH står för *Pay to Script Hash - Pay to Witness Public Key Hash*. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO, även känd som "Nested SegWit".


P2SH-P2WPKH introducerades i samband med implementeringen av SegWit i augusti 2017. Detta skript är en P2WPKH förpackad i en P2SH. Det låser bitcoins baserat på Hash för en publik nyckel. Skillnaden från den klassiska P2WPKH är att skriptet är inslaget i `redeemscript` av en klassisk P2SH.


Detta skript skapades vid lanseringen av SegWit för att underlätta dess införande. Det gör det möjligt att använda den nya standarden även med tjänster eller plånböcker som ännu inte är kompatibla med SegWit. Det är ett slags övergångsskript mot den nya standarden. Idag är det därför inte längre särskilt relevant att använda dessa typer av omslutna SegWit-skript, eftersom de flesta plånböcker har implementerat inbyggd SegWit. P2SH-P2WPKH-adresser skrivs med `Base58Check`-kodning och börjar alltid med `3`, som alla P2SH Address.


> ► *`P2SH-P2WPKH` kallas ibland också `P2WPKH-inbäddad i-P2SH`.*