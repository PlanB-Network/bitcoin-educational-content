---
term: BIP143
---

Tutvustab uut viisi tehingu räsistamiseks allkirjade kontrollimiseks pärast SegWiti skriptide kasutuselevõttu. Eesmärk on vähendada kontrollimise ajal tarbetuid operatsioone ja lisada sisendis olevate UTXO-de väärtus allkirja. See lahendab kaks peamist probleemi algse tehingu räsistamise algoritmiga:
* Andmete räsistamise kvadratuurne kasv allkirjade arvu suurenedes;
* Sisendväärtuse mittekaasamine allkirjas, mis kujutas endast ohtu riistvaralistele rahakottidele, eriti seoses tehingutasude teadmistega.
Kuna SegWiti uuendus, mida selgitatakse BIP141-s, tutvustab uut tüüpi tehinguid, mille skripti vanad sõlmed ei kontrolli, kasutab BIP143 seda võimalust probleemi lahendamiseks ilma kõva kahvli nõudmiseta. Seega on BIP143 osa SegWiti pehmest kahvlist.