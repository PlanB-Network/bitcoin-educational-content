---
term: SCRIPTPUBKEY
---

Hati iliyo katika sehemu ya matokeo ya muamala wa Bitcoin ambayo inafafanua masharti ambayo UTXO husika inaweza kutumika. Hati hii kwa hivyo inalinda bitcoins. Katika hali yake ya kawaida, `scriptPubKey` ina hali inayohitaji muamala unaofuata ili kutoa uthibitisho wa kumiliki ufunguo wa faragha unaolingana na Bitcoin Address iliyobainishwa. Hii mara nyingi hupatikana kwa hati inayodai saini inayolingana na ufunguo wa umma unaohusishwa na Address inayotumiwa kupata pesa hizi. Muamala unapojaribu kutumia UTXO hii kama ingizo, lazima itoe `scriptSig` ambayo, ikiunganishwa na `scriptPubKey`, inakidhi masharti yaliyowekwa na kutoa hati halali.


Kwa mfano, hapa kuna P2PKH `scriptPubKey` ya kawaida:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


`scriptSig` inayolingana itakuwa:


```text
<signature> <public key>
```


![](../../dictionnaire/assets/35.webp)


> ► *Hati hii pia wakati mwingine hujulikana kama "hati ya kufunga" kwa Kiingereza.*