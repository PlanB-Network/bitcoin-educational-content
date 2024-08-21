---
term: SEED
---

Konkreetse hierarhilise deterministliku Bitcoin rahakoti kontekstis on seeme 512-bitine informatsiooni tükk, mis on tuletatud juhuslikkusest. Seda kasutatakse deterministlikult ja hierarhiliselt privaatvõtmete komplekti ning nende vastavate avalike võtmete genereerimiseks Bitcoin rahakotis. Seemet sageli aetakse segi taastefraasiga. Siiski on tegemist erineva informatsiooniga. Seeme saadakse, rakendades `PBKDF2` funktsiooni mnemoonilisele fraasile ja igale võimalikule paroolifraasile.

Seeme leiutati koos BIP32 tutvustamisega, mis määratleb hierarhilise deterministliku rahakoti alused. Selles standardis oli seeme 128 bitti. See võimaldab kõigi rahakoti võtmete tuletamist ühest informatsioonitükist, erinevalt JBOK (*Just a Bunch Of Keys*) rahakottidest, mis nõuavad iga genereeritud võtme jaoks uusi varukoopiaid. BIP39 tutvustas hiljem selle seemne kodeerimist, et lihtsustada selle loetavust inimeste jaoks. See kodeerimine toimub fraasi kujul, mida tavaliselt nimetatakse mnemooniliseks fraasiks või taastefraasiks. See standard aitab vältida seemne varundamisel tekkivaid vigu, eriti tänu kontrollsumma kasutamisele.

Üldisemalt krüptograafias on seeme juhusliku andme tükk, mida kasutatakse lähtepunktina krüptograafiliste võtmete, krüpteeringute või pseudojuhuslike jadade genereerimiseks. Paljude krüptograafiliste protsesside kvaliteet ja turvalisus sõltuvad seemne juhuslikkusest ja konfidentsiaalsusest.

> ► *Inglise keele tõlge sõnale "graine" on "seeme". Prantsuse keeles kasutavad paljud otse inglise keelset sõna seemne viitamiseks.*