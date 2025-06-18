---
term: REKURZIVNO (SAVEZ)
---

Rekurzivni savez na Bitcoin je tip Smart contract koji nameće uslove ne samo na trenutnu transakciju već i na buduće transakcije koje troše izlaze ove transakcije. Ovo omogućava kreiranje lanaca transakcija gde svaka mora da se pridržava određenih pravila definisanih od strane prve u lancu. Rekurzivnost stvara sekvencu transakcija gde svaka nasleđuje ograničenja od svoje roditeljske transakcije. Ovo bi omogućilo složenu i dugoročnu kontrolu nad načinom na koji se bitkoini mogu trošiti, ali bi takođe uvelo rizike u pogledu slobode trošenja i fungibilnosti.


Da rezimiramo, nerekurzivni savez bi se ograničio samo na transakciju koja neposredno sledi onu koja je uspostavila pravila. Nasuprot tome, rekurzivni savez ima sposobnost da nameće specifične uslove na Bitcoin neograničeno. Transakcije mogu slediti jedna drugu, ali će Bitcoin o kojem je reč uvek zadržati početne uslove vezane za njega. Tehnički, uspostavljanje nerekurzivnog saveza se dešava kada `scriptPubKey` UTXO definiše ograničenja na `scriptPubKey` izlaza transakcije koja troši taj UTXO. S druge strane, uspostavljanje rekurzivnog saveza se dešava kada `scriptPubKey` UTXO definiše ograničenja na `scriptPubKey` izlaza transakcije koja troši taj UTXO, i na sve `scriptPubKey`-ove koji će slediti trošenje tog UTXO.


Općenitije, u računarstvu, ono što se naziva "rekurzivnost" je sposobnost funkcije da pozove samu sebe, stvarajući neku vrstu petlje.