---
termi: VERKON-SÄÄDETTY AIKA (NAT)
---

Yleisen ajan arviointi, joka perustuu verkon solmujen kelloihin. Jokainen solmu laskee oman NAT:nsa ottamalla mediaanin aikaeroista oman paikallisen kellonsa (UTC) ja niihin solmuihin, joihin se on yhdistetty, välillä, ja lisäämällä sitten paikallisen kellonsa näiden erojen mediaaniin, enintään 70 minuuttia. Verkon-säädetty aika on siis solmujen aikojen mediaani, joka lasketaan paikallisesti kussakin solmussa. Tätä viitekehystä käytetään sitten lohkojen aikaleimojen kelvollisuuden tarkistamiseen. Todellakin, jotta solmu hyväksyisi lohkon, sen aikaleiman on oltava MTP:n (viimeisten 11 louhitun lohkon mediaaniaika) ja NAT:n plus 2 tuntia välillä:

```text
MTP < Kelvollinen Aikaleima < (NAT + 2h)
```