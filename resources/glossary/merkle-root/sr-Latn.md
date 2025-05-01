---
term: Merkle Root
---

Digest ili "top Hash" od Merkle Tree, što predstavlja rezime svih informacija prisutnih u stablu. Merkle Tree je kriptografska akumulatorska struktura, ponekad se naziva i "Hash stablo". U kontekstu Bitcoin, Merkle stabla se koriste za organizovanje transakcija unutar bloka i za olakšavanje brze verifikacije uključivanja određene transakcije. Tako se u Bitcoin blokovima, Merkle Root dobija sukcesivnim heširanjem transakcija u parovima sve dok ne ostane samo jedan Hash (Merkle Root). Ovo se zatim uključuje u zaglavlje odgovarajućeg bloka. Ovo Hash stablo se takođe nalazi u UTREEXO, strukturi koja omogućava kondenzovanje UTXO skupa čvorova, i u MAST Taproot.