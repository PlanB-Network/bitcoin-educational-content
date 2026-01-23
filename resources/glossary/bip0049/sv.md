---
term: BIP0049
definition: Härledningsstandard för Nested SegWit-adresser (P2SH-P2WPKH), som använder index 49' i härledningssökvägen.
---

BIP49 är en informativ BIP som introducerar den härledningsmetod som används för generate Nested SegWit-adresser i en HD Wallet. Den föreslagna härledningsvägen följer standarderna i BIP43 och BIP44, med indexet "49" (härdad härledning) på djupet av målet. Till exempel skulle den första Address i ett P2SH-P2WPKH-konto härledas från sökvägen: `m/49'/0'/0'/0/0`. Nested SegWit-skript uppfanns vid lanseringen av SegWit för att underlätta dess införande. De gör det möjligt att använda den nya standarden även på plånböcker som ännu inte är kompatibla med SegWit.