---
term: UTREEXO
---

Itifaki iliyoundwa na Tadge Dryja ili kusawazisha seti ya UTXO ya nodi za Bitcoin kwa kutumia kikusanyaji kulingana na miti ya Merkle. Tofauti na seti ya kawaida ya UTXO ambayo inahitaji nafasi kubwa ya kuhifadhi, Utreexo inapunguza sana kumbukumbu inayohitajika kwa kuhifadhi mizizi ya Merkle Tree pekee. Hii inaruhusu nodi kuthibitisha kuwepo kwa UTXO zinazotumika katika pembejeo za shughuli, bila kulazimika kuweka seti kamili ya UTXO. Kwa kutumia Utreexo, kila nodi hubaki na alama ya vidole ya kriptografia inayoitwa Merkle Root. Wakati muamala unafanywa, mtumiaji hutoa uthibitisho wa Ownership ya UTXO na njia zinazolingana za Merkle. Kwa hivyo, node inaweza kuthibitisha shughuli bila kuhifadhi seti nzima ya UTXO. Wacha tuchukue mfano na mchoro kuelewa utaratibu huu:


![](../../dictionnaire/assets/15.webp)


Katika mfano huu, nilipunguza kwa makusudi seti ya UTXO hadi 4 UTXO ili kuwezesha kuelewa. Kwa kweli, ni muhimu kufikiria kuwa kuna karibu UTXO milioni 140 kwenye Bitcoin wakati wa kuandika mistari hii. Katika mchoro huu, nodi ya Utreexo ingehitaji tu kuweka Merkle Root kwenye RAM. Iwapo itapokea matumizi ya muamala UTXO Na. 3 (nyeusi), uthibitisho utakuwa na Elements zifuatazo:


- UTXO 3;
- Hash 4;
- Hash 1-2.


Kwa habari hii inayotumwa na mtumaji wa muamala, nodi ya Utreexo hufanya uthibitishaji ufuatao:


- Inahesabu alama ya UTXO 3, ambayo inatoa Hash 3;
- Inaunganisha Hash 3 na Hash 4;
- Inahesabu alama yao, ambayo inatoa Hash 3-4;
- Inaunganisha Hash 3-4 na Hash 1-2;
- Inahesabu alama zao, ambayo huipa Merkle Root.


Ikiwa Merkle Root inapata kupitia mchakato wake ni sawa na Merkle Root iliyohifadhiwa kwenye RAM yake, basi ina hakika kwamba UTXO No. 3 ni kweli sehemu ya seti ya UTXO.

Njia hii inapunguza mahitaji ya RAM kwa waendeshaji wa Full node. Hata hivyo, Utreexo ina mapungufu, ikiwa ni pamoja na ongezeko la ukubwa wa kuzuia kutokana na uthibitisho wa ziada na utegemezi unaowezekana wa nodi za Utreexo kwenye Nodi za Bridge ili kupata uthibitisho unaokosekana. Nodi za Daraja ni nodi kamili za jadi ambazo hutoa uthibitisho muhimu kwa nodi za Utreexo, hivyo kuruhusu uthibitishaji kamili. Mbinu hii inatoa maelewano kati ya ufanisi na ugatuaji, na kufanya uthibitishaji wa shughuli kufikiwa zaidi na watumiaji walio na rasilimali chache.