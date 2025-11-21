---
term: CISA
---

Lühend "Cross-Input Signature Aggregation". See on tehniline ettepanek, mille eesmärk on optimeerida Bitcoin tehingute suurust, vähendades nende valideerimiseks vajalike allkirjade arvu.


Praegu peab Bitcoin-s olema iga tehingu sisendil eraldi allkiri, enne kui seda saab tarbida. See tõestab, et kõnealuse UTXO omanik on tehingu autoriseerinud. CISA eesmärk on ühendada ühe tehingu kõigi sisendite allkirjad üheks kõiki sisendeid hõlmavaks allkirjaks. See võimaldaks vähendada paljude sisenditega tehingute mahtu ja seega ka nende kulusid. See oleks eriti kasulik neile, kes viivad läbi coinjoine või konsolideerimisi, võimaldades samal ajal rohkemate tehingute kinnitamist Bitcoin-s, ilma et see muudaks plokkide suurust või intervalle. CISA põhineb Schnorr'i protokollil, mis võimaldab allkirjade lineaarset koondamist. See tähendab, et üks allkiri võib tõendada mitme sõltumatu võtme olemasolu.


Siiski on CISA rakendamine Bitcoin-s väga keeruline, sest see nõuab põhjalikke muudatusi skriptide tööpõhimõtetes. Praegu toimub skriptide kontrollimine Bitcoins sisendi kaupa. Üleminek mudelile, kus kogu tehingut kontrollitakse korraga, nagu CISA pakub, ei ole kaugeltki triviaalne muudatus.