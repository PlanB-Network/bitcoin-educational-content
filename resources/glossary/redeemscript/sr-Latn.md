---
term: redeemscript
---

Skripta koja definiše specifične uslove koje ulazi moraju ispuniti da bi otključali sredstva povezana sa P2SH izlazom. U P2SH UTXO, `scriptPubKey` sadrži Hash od `redeemscript`. Kada transakcija želi da potroši ovaj UTXO kao ulaz, mora obezbediti jasan `redeemscript` koji odgovara Hash sadržanom u `scriptPubKey`. `redeemscript` se tako daje u `scriptSig` ulaza, zajedno sa drugim Elements potrebnim za ispunjavanje uslova skripte, kao što su potpisi ili javni ključevi. Ova inkapsulirana struktura osigurava da detalji uslova potrošnje ostanu skriveni dok bitkoini zapravo ne budu potrošeni. Posebno se koristi za Legacy P2SH multisignature novčanike.