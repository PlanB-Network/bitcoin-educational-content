---
term: UNIX TIME

---
Unix-aika tai Unix-aikaleima edustaa sekuntien lukumäärää, joka on kulunut 1. tammikuuta 1970 keskiyöstä UTC (Unix-aikakausi). Tätä järjestelmää käytetään Unix-käyttöjärjestelmissä ja niiden johdannaisissa merkitsemään aikaa yleismaailmallisella ja standardoidulla tavalla. Se mahdollistaa kellojen synkronoinnin ja aikapohjaisten tapahtumien hallinnan aikavyöhykkeistä riippumatta.

Bitcoinin yhteydessä sitä käytetään solmujen paikalliseen kelloon ja siten NAT:n (Network-Adjusted Time) laskemiseen. Verkkosovitettu aika on kunkin solmun paikallisesti laskemien solmuaikojen mediaani, ja tätä viitettä käytetään sitten lohkojen aikaleimojen oikeellisuuden tarkistamiseen. Jotta jokin solmu voisi hyväksyä lohkon, sen aikaleiman on oltava MTP:n (11 viimeisimmän louhitun lohkon menneen ajan mediaani) ja NAT:n plus 2 tunnin välillä:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Timea käytetään myös aikalukujen luomiseen, kun ne perustuvat reaaliaikaan eivätkä lohkojen määrään.