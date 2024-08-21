---
termi: BIP113
---

Toi muutoksen kaikkien aikalukitusoperaatioiden (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ja `OP_CHECKSEQUENCEVERIFY`) laskentaan. Se määrittelee, että aikalukkojen voimassaolon arvioimiseksi ne on nyt verrattava MTP:hen (*Median Time Past*, menneisyyden mediaaniaika), joka on viimeisten 11 lohkon aikaleimojen mediaani. Aiemmin käytettiin vain edellisen lohkon aikaleimaa. Tämä menetelmä tekee järjestelmästä ennustettavamman ja estää aikaviitteen manipuloinnin louhijoilta. BIP113 otettiin käyttöön pehmeän haarukan kautta 4. heinäkuuta 2016 yhdessä BIP68:n ja BIP112:n kanssa, ja se aktivoitiin ensimmäistä kertaa käyttäen BIP9-menetelmää.