---
term: (NAT)

---
Verkon solmupisteiden kelloihin perustuva yleisaika-arvio. Kukin solmu laskee NAT:nsa ottamalla sen paikallisen kellon (UTC) ja niiden solmujen, joihin se on yhteydessä, välisen aikaeron mediaanin ja lisäämällä sitten oman paikallisen kellonsa näiden erojen mediaaniin enintään 70 minuuttiin. Verkkosovitettu aika on siis kunkin solmun paikallisesti laskemien solmuaikojen mediaani. Tätä viitekehystä käytetään sitten lohkojen aikaleimojen oikeellisuuden tarkistamiseen. Jotta solmu voi hyväksyä lohkon, sen aikaleiman on oltava MTP:n (11 viimeisimmän louhitun lohkon mediaaniaika) ja NAT:n plus 2 tunnin välillä:

```text
MTP < Valid Timestamp < (NAT + 2h)
```