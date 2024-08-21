---
term: PAYJOIN
---

Konkreetne Bitcoin'i tehingustruktuur, mis parandab kasutaja privaatsust kulutamise ajal, tehes koostööd makse saajaga. Payjoin'i ainulaadsus seisneb selle võimes genereerida tehing, mis esmapilgul tundub tavaline, kuid on tegelikult mini coinjoin kahe osapoole vahel. Selleks kaasab tehingustruktuur makse saaja sisenditesse koos tegeliku saatjaga. Seega lisab saaja tehingu keskele makse iseendale, mis võimaldab neil saada makstud. Näiteks, kui ostate baguette'i `6,000 sats` eest, kasutades UTXO-d `10,000 sats`, ja valite Payjoin'i, lisab teie pagar sisendina `15,000 sats` suuruse UTXO, mis kuulub neile, mille nad saavad täielikult väljundina tagasi, lisaks teie `6,000 sats`-ile.

Payjoin tehing täidab kaks eesmärki. Esiteks, selle eesmärk on eksitada välist vaatlejat, luues ahelaanalüüsis dekoi Common Input Ownership Heuristic (CIOH) alusel. Tavaliselt, kui blockchainis on tehingul mitu sisendit, eeldatakse, et kõik need sisendid kuuluvad tõenäoliselt samale isikule. Seega, kui analüütik uurib Payjoin tehingut, viiakse nad uskuma, et kõik sisendid pärinevad samalt isikult. Siiski on see taju vale, kuna makse saaja panustab sisenditesse koos tegeliku maksjaga. Teiseks, Payjoin eksitab välist vaatlejat ka tegeliku makse summa osas. Tehingu struktuuri uurides võib analüütik arvata, et makse on võrdne ühe väljundi summaga. Tegelikkuses ei vasta makse summa ühelegi väljunditest. See on tegelikult erinevus saaja UTXO vahel väljundis ja saaja UTXO sisendis. Selles osas langeb Payjoin tehing steganograafia valdkonda. See võimaldab peita tegeliku tehingu summa valetehingu sisse, mis toimib dekoina.

![](../../dictionnaire/assets/14.png)

> ► *Payjoin'i nimetatakse mõnikord ka "P2EP (Pay-to-End-Point)", "Stowaway" või "steganograafiline tehing".*