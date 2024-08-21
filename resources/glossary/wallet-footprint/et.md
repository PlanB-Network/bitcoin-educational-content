---
term: RAHAKOTI JÄLG
---

Hulk eristatavaid omadusi, mida on täheldatav samast Bitcoin'i rahakotist tehtud tehingutes. Nende omaduste hulka võivad kuuluda sarnasused skriptitüüpide kasutamises, aadresside korduvkasutus, UTXO-de järjestus, vahetusväljundite paigutus, RBF (*Replace-by-Fee* ehk "Asenda-Tasuga") signaalimine, versiooninumber, `nSequence` väli ja `nLockTime` väli.

Rahakoti jälgi kasutavad analüütikud konkreetse entiteedi tegevuste jälgimiseks plokiahelas, tuvastades korduvaid mustreid tema tehingutes. Näiteks kasutaja, kes süstemaatiliselt saadab oma vahetusraha P2TR aadressidele (`bc1p…`), loob eristatava jälje, mida saab kasutada tema tulevaste tehingute jälgimiseks.

Nagu LaurentMT selgitab Space Kek #19-s (prantsuskeelne podcast), suureneb rahakoti jälgede kasulikkus ahela analüüsis aja jooksul märkimisväärselt. Tõepoolest, skriptitüüpide kasvav arv ja nende uute funktsioonide järkjärguline kasutuselevõtt rahakotitarkvaras rõhutavad erinevusi. On isegi võimalik täpselt tuvastada jälgitava entiteedi kasutatav tarkvara. Seetõttu on oluline mõista, et rahakoti jälje uurimine on eriti asjakohane hiljutiste tehingute puhul, veelgi enam kui 2010. aastate alguses algatatud tehingute puhul.