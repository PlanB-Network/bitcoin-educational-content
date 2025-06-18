---
term: MITMEPOOLSED MAKSED (MPP)
---

Üldine termin kõigi Lightningi maksetehnikate kohta, mis võimaldavad tehingu jaotada mitmeks väiksemaks osaks ja suunata seda erinevate marsruutide kaudu. Teisisõnu, iga maksefraktsioon võtab erineva sõlme tee. See võimaldab mööduda likviidsuspiirangutest ühe kanali marsruudil.


Mitmekordsed maksed pakuvad ka mõningaid eeliseid konfidentsiaalsuse osas, kuna vaatlejal on raskem seostada iga maksefragmenti kogu tehinguga. Põhiversioonis jagavad kõik fragmendid siiski HTLCde puhul sama saladust, mis võib muuta tehingu jälgitavaks, kui vaatleja viibib mitmel marsruudil. Veelgi enam, kuna saladus on kõigi maksefragmentide jaoks unikaalne, ei ole see aatomne. See tähendab, et mõned makse osad võivad olla edukalt sooritatud, samas kui teised võivad ebaõnnestuda. Need puudused on parandatud "Atomic Multi-Path Payment" abil.