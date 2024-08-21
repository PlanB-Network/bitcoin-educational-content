---
termi: TAVOITE
---

Deterministisissä ja hierarkisissa (HD) lompakoissa tavoite (tai _purpose_ englanniksi), jonka BIP43 määrittelee, edustaa tiettyä johdannaisuuden tasoa. Tämä indeksi, joka sijaitsee johdannaispuun ensimmäisellä tasolla (`m / purpose' /`), tunnistaa lompakon käyttämän johdannaisstandardin, jotta eri lompakonhallintaohjelmistojen välinen yhteensopivuus helpottuisi. Esimerkiksi SegWit-osoitteiden (BIP84) tapauksessa tavoite merkitään muotoon `/84'/`. Tämä menetelmä mahdollistaa avainten tehokkaan järjestämisen eri tyyppisten osoitteiden kesken samassa HD-lompakossa. Käytetyt standardi-indeksit ovat:
* P2PKH:lle: `44'`;
* P2WPKH-nested-in-P2SH:lle: `49'`;
* P2WPKH:lle: `84'`;
* P2TR:lle: `86'`.

![](../../dictionnaire/assets/20.png)