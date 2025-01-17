---
term: TRANSAKCE (TX)

---
V kontextu Bitcoinu je transakce (zkráceně "TX") operace zaznamenaná v blockchainu, která převádí vlastnictví bitcoinů z jednoho nebo více vstupů na jeden nebo více výstupů. Každá transakce spotřebovává jako vstupy nespotřebované výstupy transakcí (UTXO), což jsou výstupy z předchozích transakcí, a vytváří nové UTXO jako výstupy, které lze použít jako vstupy v budoucích transakcích.

Každý vstup obsahuje odkaz na existující výstup spolu s podpisovým skriptem (`scriptSig`), který splňuje podmínky pro vydání (`scriptPubKey`) stanovené výstupem, na který odkazuje. To umožňuje odemknutí bitcoinů. Výstupy definují nové výdajové podmínky (`scriptPubKey`) pro převedené bitcoiny, často ve formě veřejného klíče nebo adresy, ke které jsou nyní bitcoiny přiřazeny.