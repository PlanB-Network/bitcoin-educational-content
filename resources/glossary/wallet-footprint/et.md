---
term: RAHAKOTI JALAJÄLG

---
Ühe ja sama Bitcoini rahakoti poolt tehtud tehingute puhul täheldatavate eristavate tunnuste kogum. Nende tunnuste hulka võivad kuuluda sarnasused skriptitüüpide kasutamises, aadresside taaskasutuses, UTXOde järjekorras, muutuste väljundi paigutuses, RBF (*Replace-by-Fee*) signalisatsioonis, versiooni numbris, väljal `nSequence` ja väljal `nLockTime`.

Analüütikud kasutavad rahakoti jalajälgi, et jälgida konkreetse üksuse tegevust plokiahelas, tuvastades selle tehingute korduvad mustrid. Näiteks kasutaja, kes süstemaatiliselt saadab oma raha P2TR-aadressidele (`bc1p...`), loob eristuva jalajälje, mida saab kasutada tema tulevaste tehingute jälgimiseks.

Nagu LaurentMT selgitab Space Kek #19 (prantsuskeelne podcast), suureneb rahakoti jalajälgede kasulikkus ahelate analüüsis aja jooksul märkimisväärselt. Tõepoolest, skripttüüpide kasvav arv ja nende uute funktsioonide üha järkjärgulisem kasutuselevõtt rahakoti tarkvara poolt rõhutavad erinevusi. On isegi võimalik täpselt tuvastada jälgitava üksuse poolt kasutatud tarkvara. Seetõttu on oluline mõista, et rahakoti jalajälje uurimine on eriti oluline hiljutiste tehingute puhul, rohkem kui 2010. aastate alguses algatatud tehingute puhul.