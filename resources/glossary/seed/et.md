---
term: GRAIN
---

Bitcoin hierarhilise deterministliku portfelli kontekstis on seed 512-bitine teave, mis on saadud juhuslikust sündmusest. Seda kasutatakse deterministlikult ja hierarhiliselt generate privaatvõtmete ja nende vastavate avalike võtmete kogumi jaoks Bitcoin portfelli jaoks. seed aetakse sageli segamini taastamislausega ise. Kuid see ei ole sama asi. seed saadakse funktsiooni `PBKDF2` kohaldamisel Mnemonic fraasile ja mis tahes passphrase-le.


seed leiutati koos BIP32-ga, mis määratles hierarhilise deterministliku portfelli alused. Selles standardis mõõtis seed 128 bitti. See võimaldab kõiki portfelli võtmeid tuletada ühest teabest, erinevalt JBOK (*Just a Bunch Of Keys*) portfellidest, mis nõuavad iga genereeritud võtme jaoks uusi varukoopiaid. BIP39 pakkus seejärel välja selle seed kodeerimise, et lihtsustada selle lugemist inimeste poolt. See kodeerimine toimub fraasi kujul, mida üldiselt nimetatakse Mnemonic fraasiks või taastamisfraasiks. Selle standardiga välditakse vigu seed salvestamisel, eelkõige tänu kontrollsumma kasutamisele.


Väljaspool Bitcoin konteksti on seed krüptograafias üldiselt generate krüptograafiliste võtmete või laiemalt mis tahes tüüpi andmete puhul, mida toodab pseudosrandomnumbri generaator. See algväärtus peab olema juhuslik ja ettearvamatu, et tagada krüptosüsteemi turvalisus. seed toob tõepoolest süsteemi sisse entroopia, kuid järgnev genereerimisprotsess on deterministlik.


> ► *Kasutatavas kõnepruugis viitab enamik bitcoin'i kasutajatest Mnemonic fraasile, kui nad räägivad "seed", mitte aga tuletamise vahepealsele seisundile, mis asub Mnemonic fraasi ja peavõti vahel.*