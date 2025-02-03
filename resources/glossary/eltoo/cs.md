---
term: ELTOO

---
Obecný protokol pro druhé vrstvy Bitcoinu, který definuje způsob společné správy vlastnictví UTXO. Eltoo navrhli Christian Decker, Rusty Russell a Olaoluwa Osuntokun, zejména proto, aby vyřešili problémy spojené s mechanismy vyjednávání stavů kanálů Lightning, tedy mezi otevřením a zavřením. Architektura Eltoo zjednodušuje proces vyjednávání zavedením lineárního systému správy stavů a nahrazuje zavedený přístup založený na sankcích pružnější a méně sankční metodou aktualizace. Tento protokol vyžaduje použití nového typu SigHash, který umožňuje ignorovat všechny vstupy v podpisu transakce. Tento SigHash se původně nazýval `SIGHASH_NOINPUT`, poté `SIGHASH_ANYPREVOUT` (*Každý předchozí výstup*). Jeho implementace je plánována v BIP118.

> ► *Eltoo se někdy označuje také jako "LN-Symetrie".*