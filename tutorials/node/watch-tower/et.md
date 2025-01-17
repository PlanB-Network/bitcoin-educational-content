---
name: Watch Tower
description: Vaatetorni mõistmine ja kasutamine
---

## Kuidas vaatetornid töötavad?

Olles oluline osa Lightning Network ökosüsteemist, pakuvad vaatetornid kasutajate välkkanalitele lisakaitset. Nende peamine ülesanne on jälgida kanalite tervist ja sekkuda, kui üks kanalipooltest üritab teist petta.

Kuidas saab vaatetorn tuvastada, kui kanal on ohustatud? Vaatetorn saab vajaliku teabe kanalipooltelt, et õigesti tuvastada ja reageerida igasugustele rikkumistele. Sellesse teabesse kuuluvad sageli viimaste tehingute üksikasjad, praegune kanali seisund ja vajalik teave karistustehingute loomiseks. Enne andmete vaatetornile edastamist võib klient need krüpteerida, et kaitsta privaatsust ja saladust. See takistab vaatetornil krüpteeritud andmete dekrüpteerimist, isegi kui andmed on kätte saadud, välja arvatud juhul, kui rikkumine on tõesti toimunud. See krüpteerimissüsteem kaitseb kliendi privaatsust ja takistab vaatetornil juurdepääsu privaatsetele andmetele ilma loata.

## Kuidas seadistada oma Eye of Satoshi ja hakata panustama

Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) on hoiustamata Lightning vaatetorn, mis on kooskõlas [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) nõuetega. Sellel on kaks peamist komponenti:

1. teos: sisaldab CLI-d ja torni serveripoolset põhifunktsionaalsust. Selle koodi koostamisel saadakse kaks binaarfaili—teosd ja teos-cli.

2. teos-common: Sisaldab jagatud serveri- ja kliendipoolset funktsionaalsust (kasulik kliendi loomiseks).

Torni edukaks käitamiseks peate enne torni käivitamist teosd käsklusega käivitama bitcoind. Enne nende kahe käsu käivitamist peate seadistama oma bitcoin.conf faili. Siin on sammud, kuidas seda teha:-

1. Installige bitcoin core allikast või laadige see alla. Pärast allalaadimist asetage bitcoin.conf fail Bitcoin core kasutajakataloogi. Lisateabe saamiseks, kus faili paigutada, sõltuvalt teie operatsioonisüsteemist, vaadake seda linki.

2. Pärast faili loomise koha kindlaksmääramist lisage need valikud:-

'''
#RPC
server=1
rpcuser=<teie-kasutaja>
rpcpassword=<teie-parool>

#chain
regtest=1
'''

- server: RPC päringute jaoks
- rpcuser ja rpcpassword: RPC klientidel on võimalik serveriga autentida
- regtest: Pole nõutav, kuid kasulik, kui plaanite arendust.

rpcuser ja rpcpassword tuleb teie poolt valida. Need tuleb kirjutada ilma jutumärkideta. Näiteks:-

'''
rpcuser=aniketh
rpcpassword=tugevparool
'''

Nüüd, kui käivitate bitcoind, peaks see hakkama sõlme käitama.

1. Torni osa jaoks peate esmalt installima teos allikast. Järgige selle lingi juhiseid.

2. Pärast teos süsteemi edukat installimist ja testide läbimist võite jätkata viimase sammuga, mis on teos.toml faili seadistamine teos kasutajakataloogis. Fail tuleb paigutada kausta nimega .teos (tähelepanu punktile) teie kodukausta alla. Näiteks /home/<teie-kasutajanimi>/.teos Linuxi puhul. Kui olete koha leidnud, looge teos.toml fail ja seadistage need valikud vastavalt muudatustele, mida tegime bitcoind-s.
#bitcoindbtc_network = "regtest"
btc_rpc_user = <teie-kasutajanimi>
btc_rpc_password = <teie-parool>

Pange tähele, et siin tuleb kasutajanime ja parooli kirjutada jutumärkides, näiteks eelnevalt toodud näite puhul:

'''
btc_rpc_user = "aniketh"
btc_rpc_password = "tugevparool"
'''

Kui olete sellega valmis saanud, peaks kõik olema korras, et torni käivitada. Kuna me töötame regtest režiimis, on tõenäoline, et meie bitcoini testvõrgus ei pruugi esimesel ühendamisel torniga kaevandada ühtegi plokki (kui on, siis on kindlasti midagi valesti). Torn ehitab bitcoind'ist viimase 100 ploki sisemise vahemälu, nii et esmakordsel käivitamisel võime saada järgmise veateate:

> ERROR [teosd] Pole piisavalt plokke torni käivitamiseks (nõutav: 100). Kaevandage vähemalt 100 plokki juurde

Kuna me töötame regtest režiimis, saame plokke kaevandada, andes RPC käsu, ilma et peaksime ootama 10-minutilist keskmist aega, mida tavaliselt näeme teistes võrkudes (nagu mainnet või testnet). Vaadake bitcoin-cli abi ja otsige, kuidas plokke kaevandada. Kui vajate abi, võite lugeda seda artiklit.

![image](assets/2.webp)

Nii, olete edukalt torni käivitanud. Palju õnne. 🎉