---
term: Merkle Tree
---

Merkle Tree ni mkusanyiko wa kriptografia. Ni njia ya kuthibitisha uanachama wa sehemu fulani ya habari ndani ya seti kubwa zaidi. Ni muundo wa data ambao hurahisisha uthibitishaji wa habari katika umbizo la kompakt. Katika mfumo wa Bitcoin, Miti ya Merkle hutumiwa kupanga na kufupisha shughuli za block katika Hash moja, inayoitwa Merkle Root (au "*Root Hash*"). Kila muamala huharakishwa, kisha heshi zilizo karibu huharakishwa pamoja kwa mpangilio hadi Merkle Root ipatikane.


![](../../dictionnaire/assets/1.webp)


Muundo huu unaruhusu uthibitishaji wa haraka wa ikiwa muamala mahususi umejumuishwa kwenye kizuizi fulani bila kulazimika kuchanganua miamala yote. Kwa mfano, ikiwa nina Merkle Root pekee na ninataka kuthibitisha kuwa `TX 7` ni sehemu ya mti, ningehitaji tu uthibitisho ufuatao:


- `TX 7`;
- `Hash 8`;
- `Hash 5-6`;
- `Hash 1-2-3-4`.

Kwa vipande hivi vya habari, nina uwezo wa kuhesabu nodi za kati hadi Merkle Root.


![](../../dictionnaire/assets/2.webp)


Merkle Trees hutumiwa haswa kwa nukta nyepesi (zinazojulikana kama "SPV") ambazo huweka vichwa vya kuzuia pekee, lakini si shughuli za malipo. Muundo huu pia unapatikana katika itifaki ya UTREEXO, itifaki ambayo inaruhusu kupunguzwa kwa seti ya UTXO ya nodes, na katika MAST Taproot.


> ► *Merkle Tree inaitwa baada ya Ralph Merkle, mwandishi wa siri ambaye alitengeneza muundo huu mwaka wa 1979. Merkle Tree pia inaweza kuitwa "mti wa Hash". Kwa Kifaransa, inajulikana kama "Arbre de Merkle" au "arbre de hachage".*