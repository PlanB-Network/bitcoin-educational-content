---
term: P2SH-P2WSH
definition: SegWit-skript (P2WSH) inbakat i P2SH för kompatibilitet, adresser börjar på 3.
---

P2SH-P2WSH står för *Pay to Script Hash - Pay to Witness Script Hash*. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO, även känd som "Nested SegWit".


P2SH-P2WSH introducerades i samband med implementeringen av SegWit i augusti 2017. Det här skriptet beskriver en P2WSH som är inkapslad i en P2SH. Det låser bitcoins baserat på Hash i ett skript. Skillnaden från en klassisk P2WSH är att skriptet är inslaget i `redeemscript` i en klassisk P2SH.


Detta skript skapades vid lanseringen av SegWit för att underlätta dess införande. Det gör det möjligt att använda denna nya standard även med tjänster eller plånböcker som ännu inte är kompatibla med SegWit. Idag är det därför inte längre särskilt relevant att använda dessa typer av omslutna SegWit-skript, eftersom de flesta plånböcker har implementerat inbyggd SegWit. P2SH-P2WSH-adresser skrivs med `Base58Check`-kodning och börjar alltid med `3`, som alla P2SH Address.