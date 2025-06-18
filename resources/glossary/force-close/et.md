---
term: FORCE CLOSE
---

Mitte-kooperatiivne välgukanali sulgemismehhanism. Kui kaks kasutajat avavad kanali Multisig 2/2-ga, võib kumbki neist ühepoolselt sulgeda kanali, edastades viimase juba allkirjastatud Commitment Transaction, et saada tagasi oma ahelas olevad bitcoinid. Seda nimetatakse "sundsulgemiseks".


Seda meetodit kasutatakse tavaliselt juhul, kui üks osalejatest ei vasta enam või kui kanali koostööga sulgemine on võimatu. Kui sunniviisilist sulgemist on võimalik vältida, on see parim, kuna see võtab kauem aega, et saada tagasi ahelas olevaid vahendeid, ja võib olla palju kallim tasude poolest.


Sundühenduses edastab üks kahest kasutajast Commitment Transaction, mis kajastab välkekanali viimast teadaolevat seisundit. Seejärel toimub ajalukk, enne kui bitcoine saab ahelas tagasi saada, mis annab teisele osapoolele aega kontrollida, et tehing vastab kanali viimasele olekule. Kui kasutaja üritab petta, avaldades vananenud Commitment Transaction, saab teine pool kasutada tühistamissaladust, et karistada pettajat ja saada tagasi kõik kanalis olevad vahendid.