---
term: SEED

---
Hierarhilise deterministliku Bitcoini rahakoti kontekstis on seemne 512-bitine teave, mis on tuletatud juhuslikkusest. Seda kasutatakse Bitcoini rahakoti jaoks privaatvõtmete ja vastavate avalike võtmete kogumi deterministlikuks ja hierarhiliseks genereerimiseks. Seeme aetakse sageli segamini taastamislausega. Tegemist on siiski erineva teabega. Seeme saadakse, rakendades funktsiooni `PBKDF2` mnemofraasile ja mis tahes potentsiaalsele parafraasile.

Seeme leiutati koos BIP32 kasutuselevõtuga, mis määratleb hierarhilise deterministliku rahakoti alused. Selles standardis oli seemne suurus 128 bitti. See võimaldab tuletada kõik rahakoti võtmed ühest teabest, erinevalt JBOK (*Just a Bunch Of Keys*) rahakottidest, mis nõuavad iga genereeritud võtme jaoks uusi varukoopiaid. BIP39 võttis hiljem kasutusele selle seemne kodeerimise, et lihtsustada selle loetavust inimeste poolt. See kodeerimine toimub fraasi kujul, mida tavaliselt nimetatakse mnemooniliseks fraasiks või taastamisfraasiks. See standard aitab vältida vigu seemne varundamisel, eelkõige kontrollsumma kasutamise kaudu.

Üldisemalt on krüptograafias seemne all mõnes juhuslikus andmes, mida kasutatakse lähtepunktina krüptograafiliste võtmete, krüpteeringute või pseudosuvandiliste jadade genereerimiseks. Paljude krüptograafiliste protsesside kvaliteet ja turvalisus sõltuvad seemne juhuslikkusest ja konfidentsiaalsusest.

> ► *Ingliskeelne tõlge "graine" on "seed". Prantsuse keeles kasutavad paljud otseselt ingliskeelset sõna, et viidata seemnele.*