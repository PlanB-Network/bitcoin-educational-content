---
name: Watch Tower
description: Kuelewa na kutumia Watch Tower
---

## Je! minara ya walinzi hufanya kazi gani?


Sehemu muhimu ya mfumo ikolojia wa Lightning Network, minara ya mwangalizi hutoa kiwango cha ziada cha ulinzi kwa njia za umeme za watumiaji. Wajibu wake mkuu ni kuangalia afya ya chaneli na kuingilia kati ikiwa chama kimoja kinajaribu kulaghai kingine.


Kwa hivyo Watchtower inawezaje kuamua ikiwa kituo kimeathiriwa? Watchtower hupokea taarifa inayohitaji kutoka kwa mteja, mmoja wa wahusika wa kituo, ili kutambua vizuri na kujibu ukiukaji wowote. Maelezo ya hivi majuzi zaidi ya malipo, hali ya sasa ya kituo, na maelezo yanayohitajika ili kuunda miamala ya adhabu hujumuishwa mara kwa mara katika maelezo haya. Kabla ya kusambaza data kwa Watchtower, mteja anaweza kuisimba kwa njia fiche ili kulinda faragha na usiri. Hii inazuia Watchtower kusimbua data iliyosimbwa isipokuwa kama ukiukaji umefanyika, hata kama inapata data. Faragha ya mteja inalindwa na mfumo huu wa usimbaji fiche, ambao pia huzuia Watchtower kufikia data ya faragha bila idhini.


## Jinsi ya kuanzisha Jicho lako la Satoshi na kuanza kuchangia


Jicho la Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos?ref=blog.summerofbitcoin.org)) ni Umeme usio na udhibiti wa Watchtower unaotii [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Inayo sehemu kuu mbili:


1. Teos: ikijumuisha CLI na utendakazi wa msingi wa upande wa seva wa mnara. Binari mbili-teosd na teos-CLI-zitatolewa wakati kreti hii itajengwa.

2. teos-common: Ikiwa ni pamoja na utendakazi wa upande wa seva na upande wa mteja (husaidia kuunda mteja).


Ili kuendesha mnara kwa mafanikio, utahitaji bitcoind kukimbia kabla ya kuendesha mnara kwa amri ya teosd. Kabla ya kutekeleza amri hizi zote mbili unahitaji kusanidi faili yako ya Bitcoin.conf. Hapa kuna hatua za jinsi ya kufanya hivi:-


1. Sakinisha msingi wa Bitcoin kutoka kwa chanzo au uipakue. Baada ya kupakua, weka faili ya Bitcoin.conf kwenye saraka ya msingi ya mtumiaji wa Bitcoin. Angalia kiungo hiki kwa maelezo zaidi kuhusu mahali pa kuweka faili kwani inategemea mfumo wa uendeshaji unaotumia.

2. Baada ya Kutambua mahali ambapo faili inahitaji kuundwa, ongeza chaguzi hizi:-


```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```

rpcuser=aniketh

rpcpassword=nenosiri kali```


Sasa, ikiwa unaendesha bitcoind inapaswa kuanza kuendesha nodi.


1. Kwa sehemu ya mnara, kwanza, unapaswa kufunga teos kutoka kwa chanzo. Fuata maagizo yaliyotolewa kwenye kiungo hiki.

2. Baada ya kusakinisha teos kwa ufanisi katika mfumo wako na kuendesha majaribio, unaweza kuendelea na hatua ya mwisho ambayo ni kusanidi faili ya teos.toml katika saraka ya mtumiaji wa teos. Faili inahitaji kuwekwa kwenye folda inayoitwa .teos (kumbuka nukta) chini ya folda yako ya nyumbani. Hiyo ni, kwa mfano, /home/<your-username>/.teos ya Linux. Mara tu unapopata mahali, unda faili ya teos.toml na uweke chaguo hizi zinazolingana na mambo ambayo tumebadilisha kwenye bitcoind.


```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```

btc_rpc_user = "aniketh"

btc_rpc_password = "nenosiri kali"```


Mara tu umefanya hivyo, unapaswa kuwa mzuri kwenda kuendesha mnara. Ikizingatiwa kuwa tunaendesha regtest, kuna uwezekano kwamba hakutakuwa na vitalu vyovyote vilivyochimbwa kwenye mtandao wa majaribio wa Bitcoin mara ya kwanza mnara unapounganishwa nao (kuna, kuna kitu kimezimwa). Mnara huunda akiba ya ndani ya vitalu 100 hivi karibuni kutoka bitcoind, kwa hivyo tunapoendesha kwa mara ya kwanza tunaweza kupata hitilafu ifuatayo:


_ERROR [teosd] Hakuna vitalu vya kutosha kuanzisha mnara (inahitajika: 100). Yangu angalau 100 zaidi_


Kwa kuzingatia kwamba tunaendesha regtest tunaweza kuzuia kwa kutoa amri ya RPC, bila hitaji la kungoja muda wa wastani wa dakika 10 ambao kwa kawaida tunaona katika mitandao mingine (kama Mainnet au Testnet). Angalia usaidizi wa bitcoin-cli na utafute jinsi ya kuchimba vitalu. Ikiwa unahitaji msaada, unaweza kupitia nakala hii.


![image](assets/2.webp)


Hiyo ni, umefanikiwa kukimbia mnara. Hongera sana. 🎉