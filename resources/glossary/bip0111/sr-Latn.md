---
term: BIP0111
---

Predlaže se dodavanje servisnog bita nazvanog `NODE_BLOOM` kako bi čvorovi mogli eksplicitno signalizirati svoju podršku za Bloom filtere kao što je opisano u BIP37. Uvođenje `NODE_BLOOM` omogućava operaterima čvorova da onemoguće ovu uslugu kako bi smanjili rizike od DoS napada. Opcija BIP37 je podrazumevano onemogućena u Bitcoin Core. Da bi se omogućila, parametar `peerbloomfilters=1` mora biti unet u konfiguracioni fajl.