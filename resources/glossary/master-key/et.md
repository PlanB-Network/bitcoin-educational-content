---
term: PEAVÕTI
---

HD (Hierarhiliselt Deterministlikud) rahakottide kontekstis on peavõti unikaalne privaatvõti, mis on tuletatud rahakoti seemnest. Peavõtme saamiseks rakendatakse seemnele `HMAC-SHA512` funktsiooni, kasutades sõnu "*Bitcoin seed*" sõna-sõnalt võtmena. Selle operatsiooni tulemusena saadakse 512-bitine väljund, millest esimesed 256 bitti moodustavad peavõtme ja ülejäänud 256 bitti moodustavad peamise ahelakoodi. Peavõti ja peamine ahelakood toimivad lähtepunktina kõigi laste privaat- ja avalike võtmete tuletamiseks HD rahakoti puustruktuuris. Seega on peavõti tuletamise sügavusel 0.

![](../../dictionnaire/assets/19.png)