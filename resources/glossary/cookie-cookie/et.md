---
term: KÜPSIS (.COOKIE)

---
Fail, mida kasutatakse RPC (*Remote Procedure Call*) autentimiseks Bitcoin Core'is. Kui bitcoind käivitub, genereerib ta unikaalse autentimisküpsise ja salvestab selle sellesse faili. Kliendid või skriptid, kes soovivad suhelda bitcoindiga RPC-liidese kaudu, saavad seda küpsist kasutada turvaliseks autentimiseks. See mehhanism võimaldab turvalist suhtlust bitcoindi ja väliste rakenduste (näiteks rahakoti tarkvara) vahel, ilma et oleks vaja kasutajanimesid ja paroole käsitsi hallata. Faili `.cookie` luuakse uuesti bitcoindi iga kordsel taaskäivitamisel ja see kustutatakse sulgemisel.