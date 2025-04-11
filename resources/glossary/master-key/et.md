---
term: MASTER KEY

---
HD (Hierarhical Deterministic) rahakottide kontekstis on peamine privaatvõti unikaalne privaatvõti, mis on tuletatud rahakoti seemnest. Peavõti saamiseks rakendatakse seemne suhtes funktsiooni `HMAC-SHA512`, kasutades sõna otseses mõttes võtmeks sõnu "*Bitcoini seemne*". Selle operatsiooni tulemuseks on 512-bitine väljund, millest esimesed 256 bitti moodustavad üldvõtme ja ülejäänud 256 bitti moodustavad üldkoodi. Peavõti ja peahela kood on lähtepunktiks kõigi HD rahakoti puustruktuuri alla kuuluvate privaatsete ja avalike võtmete tuletamisel. Seetõttu on peavõti tuletamise sügavusel 0.

![](../../dictionnaire/assets/19.webp)