---
term: TAVOITE

---
Deterministisissä ja hierarkkisissa (HD) lompakoissa BIP43:n määrittelemä tavoite (tai englanniksi _purpose_) edustaa tiettyä johdannaistasoa. Tämä indeksi, joka sijaitsee derivaatiopuun ensimmäisessä syvyydessä (`m / purpose' /`), yksilöi lompakon käyttämän derivaatiostandardin, jotta eri lompakonhallintaohjelmistojen yhteensopivuus olisi helpompaa. Esimerkiksi SegWit-osoitteiden (BIP84) tapauksessa tavoite merkitään `/84'/`. Tämä menetelmä mahdollistaa avainten tehokkaan organisoinnin erityyppisten osoitteiden välillä saman HD-lompakon sisällä. Käytetyt vakioindeksit ovat:


- P2PKH:n osalta: `44'`;
- P2WPKH-nested-in-P2SH: `49'`;
- P2WPKH: `84'`;
- P2TR: `86'`.

![](../../dictionnaire/assets/20.webp)