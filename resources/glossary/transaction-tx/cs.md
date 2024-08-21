---
term: TRANSAKCE (TX)
---

V kontextu Bitcoinu je transakce (zkráceně "TX") operace zaznamenaná na blockchainu, která převádí vlastnictví bitcoinů z jednoho nebo více vstupů na jeden nebo více výstupů. Každá transakce spotřebovává nevyužité výstupy transakcí (UTXOs) jako vstupy, které jsou výstupy z předchozích transakcí, a vytváří nové UTXOs jako výstupy, které mohou být použity jako vstupy v budoucích transakcích.

Každý vstup zahrnuje odkaz na existující výstup spolu se skriptem podpisu (`scriptSig`), který splňuje podmínky pro výdaj (`scriptPubKey`) stanovené výstupem, na který odkazuje. To umožňuje odemknutí bitcoinů. Výstupy definují nové podmínky pro výdaj (`scriptPubKey`) pro převedené bitcoiny, často ve formě veřejného klíče nebo adresy, se kterou jsou nyní bitcoiny spojeny.