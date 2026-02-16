---
term: P2MS

definition: Multisignaturskript som låser bitcoin med flere offentlige nøkler som krever en terskel for signaturer.
---
P2MS står for *Pay to Multisig*, som kan oversettes til "betal til flere signaturer". Det er en standard skriptmodell som brukes til å etablere utgiftsbetingelser på en UTXO. Den gjør det mulig å låse bitcoins med flere offentlige nøkler. For å bruke disse bitcoinsene kreves det en signatur med et forhåndsdefinert antall tilknyttede private nøkler. For eksempel innebærer en `P2MS 2/3` `3` offentlige nøkler med `3` tilknyttede hemmelige private nøkler. For å bruke bitcoins som er låst med dette P2MS-skriptet, kreves det en signatur med minst "2" av de "3" private nøklene. Dette er et terskel-sikkerhetssystem.

Dette skriptet ble oppfunnet i 2011 av Gavin Andresen da han tok over vedlikeholdet av den viktigste Bitcoin-klienten. I dag brukes P2MS bare marginalt av noen applikasjoner. De aller fleste moderne multisignaturer bruker andre skript som P2SH eller P2WSH. Sammenlignet med disse er P2MS ekstremt trivielt. De offentlige nøklene den består av, avsløres ved mottak av transaksjonen. Det er også dyrere å bruke P2MS enn andre multisignaturskript.

