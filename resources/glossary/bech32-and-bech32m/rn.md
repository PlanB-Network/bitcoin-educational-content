---
term: BECH32 NA BECH32M
---

`Bech32` na `Bech32m` ni uburyo bubiri bwo gushiramwo amakuru Bitcoin Address. Bishingiye ku nsiguro yahinduwe gatoyi y’ishimikiro rya 32 kandi birimwo igiharuro c’igenzura gishingiye ku nzira y’ugutahura amakosa izwi nka BCH (*Bose-Chaudhuri-Hocquenghem*). Ugereranije n'amaderesi y'Iragi, ashizwe muri `Base58check`, aderesi za `Bech32` na `Bech32m` zifise umubare w'isuzuma ukora neza, ushobora gutuma amakosa amenyekana neza kandi, rimwe na rimwe, n'ubushobozi bwo gukosora amakosa yo kwandika. Ivyo bimenyetso biratuma kandi umuntu ashobora gusoma neza, kuko bikoresha inyuguti ntoyi gusa. Aha niho hari inyishu y'inyongezo y'iyi miterere kuva ku ntango 10:


| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 yashizweho na BIP173 mu 2017 nk'uburyo bwa Address bwagenewe cane cane SegWit.  Ikoresha inyuguti zitandukanye, zigizwe n’imibare n’inyuguti ntoyi, kugira ngo amakosa yo kwandika agabanuke kandi umuntu ashobore gusoma neza. Aderesi za Bech32 mu bisanzwe zitangura na bc1 kandi zikoreshwa gusa ku nyandiko za SegWit V0, ni ukuvuga P2WPKH (Urufunguzo rwa bose rwo kwishura ku cabona Hash) na P2WSH (Inyandiko yo kwishura ku cabona Hash).


Ariko rero, hariho akaga gatoyi, katategerezwa kwiharira ku buryo bwa Bech32. Igihe cose ikimenyetso ca nyuma ca Address ari `p`, kwongerako canke gukuraho umubare uwo ari wo wose w'inyuguti `q` ziyibanziriza ntibituma umubare w'igenzura udakora. Ivyo ntibigira ico bikoze kuri aderesi za SegWit V0 zisobanuwe na BIP173 kubera ko uburebure bwavyo bushingiye ku bunini bubiri bwihariye, ariko bishobora kugira ico bikoze ku bikorwa vyo muri kazoza vy’ugushiramwo amakuru ya Bech32.


Ku Address iki, Bech32m yashizweho na BIP350 mu 2020. Amaderesi ya Bech32m nayo atangura na bc1 ariko yagenewe cane cane SegWit V1 (Taproot) n’inyandiko zo muri kazoza, cane cane P2TR (Ishura Taproot).