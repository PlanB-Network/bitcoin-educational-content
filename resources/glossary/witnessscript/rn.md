---
term: INYANDITSWE Y'ICABONA
---

Inyandiko igaragaza uko amafaranga y’ibiceri ashobora gukoreshwa avuye kuri P2WSH canke P2SH-P2WSH UTXOs. Mu bisanzwe, `witnessScript` igena ivyangombwa vy'umukono mwinshi Wallet munsi y'ingingo ngenderwako ya SegWit. Muri izo ngingo ngenderwako z'inyandiko, `inyandikoPubKey` ya UTXO (igisohoka) irimwo Hash ya `Inyandiko y'icabona`. Kugira ngo ukoreshe iyi UTXO nk'inyungu mu gucuruza gushasha, uwuyifise ategerezwa guhishura `witnessScript` y'umwimerere, kugira ngo yerekane ko ihuye n'ikimenyetso c'urutoke kiri muri `scriptPubKey`. `witnessScript` itegerezwa rero gushirwa mu `scriptWitness` y'isoko, na yo nyene irimwo Elements ikenewe kugira ngo yemeze inyandiko, nk'imikono. Rero, `witnessScript` ni ikingana kuri SegWit ya `redeemscript` mu gucuruza P2SH, n'itandukaniro ry'uko ishirwa mu gishingantahe c'ugucuruza, atari mu `scriptSig`.


> ► *Itonde, `inyandiko y'icabona` ntikwiye kuvyivangako n'inyandiko y'icabona`. Naho `witnessScript` isobanura ingene P2WSH canke P2SH-P2WSH UTXO ikoreshwa kandi ikaba igize inyandiko mu burenganzira bwayo bwite, `inyandikoWitness` irimwo amakuru y'icabona y'injiza yose ya SegWit.*