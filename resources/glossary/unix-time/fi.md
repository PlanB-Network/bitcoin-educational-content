---
term: UNIX-AIKA
---

Unix-aika tai Unix-aikaleima edustaa sekuntien määrää, joka on kulunut tammikuun 1. päivästä 1970 keskiyöllä UTC-aikaa (Unix Epoch). Tätä järjestelmää käytetään Unix-käyttöjärjestelmissä ja niiden johdannaisissa merkitsemään aikaa universaalilla ja standardoidulla tavalla. Se mahdollistaa kellojen synkronoinnin ja aikaan perustuvien tapahtumien hallinnan riippumatta aikavyöhykkeistä.

Bitcoinin kontekstissa sitä käytetään solmujen paikallisen kellon ajan määrittämiseen, ja siten NAT:n (Network-Adjusted Time, verkon säätämä aika) laskentaan. Verkon säätämä aika on solmujen paikallisesti laskemien aikojen mediaani, ja tätä viitettä käytetään sitten lohkojen aikaleimojen kelvollisuuden tarkistamiseen. Todellakin, jotta solmu hyväksyisi lohkon, sen aikaleiman on oltava MTP:n (Median Time Past, viimeisten 11 louhitun lohkon keskiaika) ja NAT:n plus 2 tunnin välillä:

```text
MTP < Kelvollinen Aikaleima < (NAT + 2h)
```

Unix-aikaa käytetään myös aikalukkojen määrittämiseen, kun ne perustuvat todelliseen aikaan, eivät lohkojen määrään.