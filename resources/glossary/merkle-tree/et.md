---
term: MERKLE PUU
---

Merkle puu on krüptograafiline akumulaator. See on meetod tõestamaks mingi konkreetse informatsiooni kuulumist suuremasse komplekti. See on andmestruktuur, mis hõlbustab informatsiooni kontrollimist kompaktses formaadis. Bitcoin süsteemis kasutatakse Merkle puid, et grupeerida ja kondenseerida bloki tehingud üheks räsi, mida nimetatakse Merkle juureks (või "*Root Hash*"). Iga tehing räsitakse, seejärel räsitakse kõrvuti asuvad räsid hierarhiliselt, kuni saadakse Merkle juur.

![](../../dictionnaire/assets/1.png)

See struktuur võimaldab kiiresti kontrollida, kas konkreetne tehing on antud blokis, ilma et peaks analüüsima kõiki tehinguid. Näiteks, kui mul on ainult Merkle juur ja ma tahan kontrollida, kas `TX 7` on tõesti puus, vajaksin ma ainult järgmisi tõendeid:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Nende teabeosadega suudan ma arvutada vahepealsed sõlmed kuni Merkle juureni.

![](../../dictionnaire/assets/2.png)

Merkle puid kasutatakse märkimisväärselt kerge nodes (tuntud kui "SPV"), mis hoiavad ainult bloki päiseid, kuid mitte tehinguid. Seda struktuuri leidub ka UTREEXO protokollis, protokollis, mis võimaldab sõlmede UTXO komplekti kondenseerida, ja MAST Taproot'is.

> ► *Merkle puu on nimetatud Ralph Merkle järgi, krüptograaf, kes kujundas selle struktuuri 1979. aastal. Merkle puud võib samuti nimetada "hash puuks". Prantsuse keeles viidatakse sellele kui "Arbre de Merkle" või "arbre de hachage".*