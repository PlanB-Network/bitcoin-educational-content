---
term: MAANDIKO YA USHAHIDI
---

Hati inayobainisha masharti ambayo bitcoins zinaweza kutumika kutoka P2WSH au P2SH-P2WSH UTXOs. Kwa kawaida, `witnessScript` hubainisha masharti ya Wallet yenye saini nyingi chini ya kiwango cha SegWit. Katika viwango hivi vya hati, `scriptPubKey` ya UTXO (matokeo) ina Hash ya `witnessScript`. Ili kutumia UTXO hii kama ingizo katika muamala mpya, ni lazima mmiliki afichue `hati ya shahidi` asili, ili kuthibitisha ulinganifu wake na alama ya kidole katika `scriptPubKey`. Kisha `shahidiScript` lazima ijumuishwe kwenye `script Witness` ya shughuli hiyo, ambayo pia ina Elements inayohitajika ili kuthibitisha hati, kama vile saini. Kwa hivyo, `hati ya shahidi` ni sawa na SegWit ya `redeemscript` katika shughuli ya P2SH, kwa tofauti kuwa imewekwa kwenye shahidi wa shughuli hiyo, na si katika `scriptSig`.


> ► *Tahadhari, `hati ya shahidi` isichanganywe na `Shahidi wa hati`. Ingawa `hati ya shahidi` inafafanua masharti ya matumizi ya P2WSH au P2SH-P2WSH UTXO na kuunda hati yenyewe, `scriptWitness` ina data ya shahidi ya ingizo lolote la SegWit.*