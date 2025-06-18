---
term: SVEDOK TRANSAKCIJE
---

Odnosi se na komponentu Bitcoin transakcija koja je premeštena sa SegWit Soft Fork na Address pitanje promenljivosti transakcija. Svedok sadrži potpise i javne ključeve potrebne za otključavanje bitkoina potrošenih u transakciji. U Legacy transakcijama, svedok je predstavljao zbir `scriptSig` sa svih ulaza. U SegWit transakcijama, svedok predstavlja zbir `scriptWitness` za svaki ulaz, i ovaj deo transakcije je sada premešten u poseban Merkle Tree unutar bloka.


Pre SegWit, potpisi su mogli biti blago izmenjeni bez poništavanja pre nego što je transakcija potvrđena, što je menjalo identifikator transakcije. Ovo je otežavalo izgradnju različitih protokola, jer je nepotvrđena transakcija mogla promeniti svoj identifikator. Razdvajanjem svedoka, SegWit čini transakcije nepromenljivim, jer bilo kakva promena u potpisima više ne utiče na identifikator transakcije (txid), već samo na identifikator svedoka (WTXID). Pored rešavanja problema promenljivosti, ovo razdvajanje omogućava povećanje kapaciteta svakog bloka.


> ► *Na engleskom, "témoin" se prevodi kao "witness".*