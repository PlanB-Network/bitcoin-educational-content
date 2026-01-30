---
term: P2MS
definition: Multisignaturskript som låser bitcoin med flera publika nycklar som kräver ett visst antal signaturer.
---

P2MS står för *Pay to Multisig*, vilket översätts till "betala till flera signaturer". Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO. Den gör det möjligt att låsa bitcoins med flera offentliga nycklar. För att spendera dessa bitcoins krävs en signatur med ett fördefinierat antal associerade privata nycklar. Till exempel innebär en `P2MS 2/3` `3` publika nycklar med `3` associerade hemliga privata nycklar. För att spendera de bitcoins som är låsta med detta P2MS-skript krävs en signatur med minst `2` av de `3` privata nycklarna. Detta är ett tröskelsäkerhetssystem.


Detta skript uppfanns 2011 av Gavin Andresen när han tog över underhållet av Bitcoin:s huvudklient. Idag används P2MS endast marginellt av vissa applikationer. De allra flesta moderna multisignaturer använder andra skript som P2SH eller P2WSH. Jämfört med dessa är P2MS extremt trivialt. De publika nycklar som den består av avslöjas när transaktionen tas emot. Att använda en P2MS är också dyrare än andra multisignaturskript.


