---
term: BIP113

---
Kaikkien timelock-operaatioiden (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ja `OP_CHECKSEQUENCEVERIFY`) laskentaan on tehty muutos. Se määrittää, että aikalukkojen validiteetin arvioimiseksi niitä on nyt verrattava MTP:hen (*Median Time Past*), joka on 11 viimeisen lohkon aikaleimojen mediaani. Aiemmin käytettiin vain edellisen lohkon aikaleimaa. Tämä menetelmä tekee järjestelmästä ennustettavamman ja estää louhijoita manipuloimasta aikaviitteitä. BIP113 otettiin käyttöön pehmeällä haarautumisella 4. heinäkuuta 2016 BIP68:n ja BIP112:n ohella, ja se aktivoitiin ensimmäistä kertaa BIP9-menetelmällä.