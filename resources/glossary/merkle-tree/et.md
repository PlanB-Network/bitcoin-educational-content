---
term: MERKLE TREE

---
Merkle Tree on krüptograafiline akumulaator. See on meetod, mille abil saab tõestada antud teabe liikmelisust suuremas kogumis. See on andmestruktuur, mis hõlbustab teabe kontrollimist kompaktses formaadis. Bitcoini süsteemis kasutatakse Merkle Trees'i selleks, et rühmitada ja koondada ploki tehingud ühte hash'i, mida nimetatakse Merkle Root'iks (või "*Root Hash*"). Iga tehing hashitakse, seejärel hakitakse kõrvuti olevad hashid hierarhiliselt kokku, kuni saadakse Merkle Root.

![](../../dictionnaire/assets/1.webp)

Selline struktuur võimaldab kiiresti kontrollida, kas konkreetne tehing kuulub antud plokki, ilma et oleks vaja analüüsida kõiki tehinguid. Näiteks, kui mul on ainult Merkle Root ja ma tahan kontrollida, et `TX 7` on tõepoolest osa puust, vajan ma ainult järgmisi tõendeid:


- "TX 7";
- "HASH 8";
- "HASH 5-6";
- `HASH 1-2-3-4`.

Nende andmete abil saan ma arvutada vahepealsed sõlmed kuni Merkle'i juureni.

![](../../dictionnaire/assets/2.webp)

Merkle Trees'i kasutatakse eelkõige kergete sõlmede (tuntud kui "SPV") puhul, mis säilitavad ainult plokkide päiseid, kuid mitte tehinguid. Seda struktuuri leidub ka UTREEXO protokollis, mis võimaldab UTXO-sõlmede kogumi tihendamist, ja MAST Taproot'is.

> ► *Märkle Tree on nimetatud Ralph Merkle'i järgi, kes on krüptograaf, kes töötas selle struktuuri välja 1979. aastal. Merkle Tree'i võib nimetada ka "hash tree". Prantsuse keeles nimetatakse seda "Arbre de Merkle" või "arbre de hachage "*