---
term: BIP0147
definition: Itegeko NULLDUMMY risaba ko dummy element ya multisig opcodes iba ubusa, mu gukuraho malleability vector.
---

Iciyumviro cashizwe muri SegWit Soft Fork kigamije gutorera umuti ikibazo c'ubushobozi bujanye n'ikintu c'ikinyoma gikoreshwa n'ibikorwa vya `OP_CHECKMULTISIG` na `OP_CHECKMULTISIGVERIFY`. Kubera ikibazo c’amateka c’uguhagarika-ku-kimwe (ikosa ry’uguhindura igice), izo opcode 2 zikuraho ikintu c’inyongera mu kirundo congereye ku gikorwa zazo zigamije.

Kugira ngo inyandiko ntiyinanirwe, agaciro k'ikinyoma rero gategerezwa gushirwa ku ntango ya `scriptSig`. Naho aka gaciro ata ntumbero ikora, birakenewe kugira ngo inyandiko ifatwe ko ari ngirakamaro.

BIP11, yashizeho urugero rwa P2MS, yasavye gukoresha `OP_0` nk’ikintu c’ikinyoma ariko ivyo ntivyigeze bishirwa mu ngiro ku rugero rw’uguhurizako, bisobanura ko agaciro ako ari ko kose gashobora gukoreshwa, gutyo hakaba hariho umurongo w’ubushobozi bwo gukora.

Uko niko `OP_SUZUMAMULTISIG` na `OP_SUZUMAMULTISIGVERIFY` vyarimwo umurongo w'ubushobozi. BIP147 itanga itegeko rishasha ry'uguhurizako, ryitwa `NULLDUMMY`, risaba ko iki kintu c'ikinyoma kiba urutonde rw'ibice vy'ubusa (`OP_0`). Iyindi gaciro yose ituma isuzuma ry'inyandiko ridakora neza. Iryo hinduka rikoreshwa ku nyandiko z'imbere ya SegWit hamwe n'inyandiko za P2WSH kandi vyasaba Soft Fork.