---
term: SCRIPTSIG
---

Kipengele katika muamala wa Bitcoin kilicho katika pembejeo. `scriptSig` hutoa data muhimu ili kukidhi masharti yaliyowekwa na `scriptPubKey` ya shughuli ya awali ambayo fedha zinatumika. Kwa hivyo ina jukumu la ziada kwa `scriptPubKey`. Kwa kawaida, `scriptSig` huwa na sahihi ya dijitali na ufunguo wa umma. Saini hiyo inatolewa na mmiliki wa bitcoins kwa kutumia ufunguo wao wa kibinafsi na inathibitisha kwamba wana idhini ya kutumia UTXO. Katika hali hii, `scriptSig` inaonyesha kuwa mmiliki wa ingizo ana ufunguo wa faragha unaolingana na ufunguo wa umma unaohusishwa na Address iliyobainishwa katika `scriptPubKey` ya shughuli ya awali inayotoka.


Muamala unapothibitishwa, data kutoka kwa `scriptSig` itatekelezwa katika `scriptPubKey` inayolingana. Ikiwa matokeo ni halali, inamaanisha kuwa masharti ya matumizi ya fedha yametimizwa. Iwapo maingizo yote ya muamala yatatoa `scriptSig` ambayo inathibitisha `scriptPubKey` yake, muamala ni halali na unaweza kuongezwa kwenye kizuizi kwa ajili ya utekelezaji.


Kwa mfano, hapa kuna P2PKH `scriptSig` ya kawaida:


```text
<signature> <public key>
```


`scriptPubKey` inayolingana itakuwa:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


![](../../dictionnaire/assets/35.webp)


> ► *The `scriptSig` pia wakati mwingine huitwa "unlocking script" kwa Kiingereza.*