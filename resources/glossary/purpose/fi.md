---
term: TAVOITE
---

Deterministisissä ja hierarkkisissa (HD) salkuissa BIP43:n määrittelemä käyttötarkoitus edustaa tiettyä johdannaistasoa. Tämä indeksi, joka sijaitsee johdannaispuun ensimmäisellä syvyydellä (`m / purpose' /`), yksilöi salkun käyttämän johdannaisstandardin, jotta salkunhallintaohjelmistojen yhteensopivuus helpottuisi. Esimerkiksi SegWit-osoitteiden (BIP84) kohdalla tarkoitukseksi merkitään `/84'/`. Tämän menetelmän avulla avaimia voidaan järjestää tehokkaasti eri Address-tyyppien välillä yhden HD-salkun sisällä. Käytetyt vakioindeksit ovat :




- P2PKH: `44'` ;
- P2WPKH, joka on sijoitettu P2SH:een: `49'` ;
- P2WPKH: `84'` ;
- P2TR:n osalta: `86'`.