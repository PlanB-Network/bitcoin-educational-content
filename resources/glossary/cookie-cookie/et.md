---
term: COOKIE (.COOKIE)
---

Fail, mida kasutatakse RPC (*Remote Procedure Call* ehk kaugprotseduurikõne) autentimiseks Bitcoin Core'is. Kui bitcoind käivitub, genereerib see unikaalse autentimisküpsise ja salvestab selle faili. Kliendid või skriptid, kes soovivad suhelda bitcoind'iga RPC liidese kaudu, saavad seda küpsist kasutada turvaliseks autentimiseks. See mehhanism võimaldab turvalist suhtlust bitcoind'i ja väliste rakenduste (näiteks rahakott-tarkvara) vahel, ilma et oleks vaja käsitsi hallata kasutajanimi ja paroole. `.cookie` fail genereeritakse uuesti iga bitcoind'i taaskäivitamisel ja kustutatakse väljalülitamisel.