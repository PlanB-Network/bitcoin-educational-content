---
term: STATIČKI Address
---

U kontekstu Silent Payments, odnosi se na jedinstveni identifikator koji omogućava primanje uplata bez ponovne upotrebe Address, bez interakcije i bez vidljive veze On-Chain između različitih uplata i statičkog Address. Ova tehnika eliminiše potrebu za generate novim, neiskorišćenim adresama za primanje za svaku transakciju, čime se izbegavaju uobičajene interakcije u Bitcoin gde primalac mora da obezbedi novi Address platiocu. To je donekle ekvivalentno ponovnom upotrebljivom kodu za plaćanje u kontekstu BIP47.


Ovaj Address se sastoji od dva javna ključa: $B_{\text{scan}}$ za skeniranje i $B_{\text{spend}}$ za trošenje, koji su spojeni da formiraju statički Address $B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$. Primalac objavljuje ovaj Address, omogućavajući pošiljaocima da izvedu jedinstvene adrese za plaćanje bez daljih interakcija sa primaocem. Da bi se upravljalo sa više različitih izvora plaćanja, etiketa se može dodati na $B_{\text{spend}}$, čime se kreiraju različite označene statičke adrese od $B_1$, $B_2$, itd. Ovo omogućava segregaciju plaćanja koristeći jednu bazu Address, čime se smanjuje opterećenje za Blockchain skeniranje. Međutim, sve statičke adrese jednog entiteta mogu se lako povezati zbog zajedničke upotrebe $B_{\text{scan}}$.