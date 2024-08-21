---
termi: BIP35
---

Ehdotus, joka sallii Bitcoin-solmun avata tietoja sen mempoolista, eli vahvistusta odottavista transaktioista. Tämän ansiosta muut osallistujat voivat vastaanottaa reaaliaikaista tietoa vahvistamattomista transaktioista lähettämällä tietyn viestin solmulle. Ennen BIP35:n hyväksymistä solmut pystyivät pääsemään käsiksi vain jo vahvistettujen transaktioiden tietoihin. Tämä parannus tarjoaa SPV-lompakoille mahdollisuuden vastaanottaa tietoja vahvistamattomista transaktioista, mahdollistaa louhijan välttää korkeiden maksujen transaktioiden missaamisen uudelleenkäynnistyksen aikana, ja helpottaa mempool-tiedon analysointia ulkoisten palveluiden toimesta.