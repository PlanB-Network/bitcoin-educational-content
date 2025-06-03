---
term: WITNESSSCRIPT
---

Skripta koja određuje uslove pod kojima se bitkoini mogu potrošiti iz P2WSH ili P2SH-P2WSH UTXO-a. Tipično, `witnessScript` određuje uslove multisignature Wallet prema SegWit standardu. U ovim skriptnim standardima, `scriptPubKey` UTXO (izlaz) sadrži Hash `witnessScript`. Da bi se ovaj UTXO koristio kao ulaz u novoj transakciji, vlasnik mora otkriti originalni `witnessScript`, kako bi dokazao njegovo podudaranje sa otiskom prsta u `scriptPubKey`. `witnessScript` zatim mora biti uključen u transakcijski `scriptWitness`, koji takođe sadrži Elements neophodan za validaciju skripte, kao što su potpisi. Dakle, `witnessScript` je ekvivalent za SegWit `redeemscript` u P2SH transakciji, sa razlikom da je smešten u svedoku transakcije, a ne u `scriptSig`.


> ► *Oprez, `witnessScript` ne treba mešati sa `scriptWitness`. Dok `witnessScript` definiše uslove trošenja P2WSH ili P2SH-P2WSH UTXO i predstavlja skriptu za sebe, `scriptWitness` sadrži podatke svedoka bilo kog SegWit ulaza.*