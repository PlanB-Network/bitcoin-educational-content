---
name: PayJoin
description: PayJoin kwenye Bitcoin ni nini?
---
![Payjoin thumbnail - steganography](assets/cover.webp)


***TAZAMA:** Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kukamatwa kwa seva zao tarehe 24 Aprili, Payjoins Stowaway kwenye Samourai Wallet hufanya kazi pekee kwa kubadilishana PSBT kati ya pande zinazohusika, mradi tu watumiaji wote wawili wameunganishwa kwenye Dojo yao wenyewe. Kuhusu Sparrow, Payjoins kupitia BIP78 bado inafanya kazi. Hata hivyo, inawezekana kwamba zana hizi zitazinduliwa tena katika wiki zijazo. Kwa sasa, bado unaweza kusoma makala haya ili kuelewa utendakazi wa kinadharia wa viungo vya malipo.*


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


---
## Kuelewa Miamala ya PayJoin kwenye Bitcoin


PayJoin ni muundo mahususi wa shughuli ya Bitcoin ambayo huongeza faragha ya mtumiaji wakati wa malipo kwa kushirikiana na mpokeaji malipo.


Mnamo mwaka wa 2015, [LaurentMT](https://twitter.com/LaurentMT) alitaja njia hii kwa mara ya kwanza kama "shughuli za steganografia" katika hati inayoweza kufikiwa. [hapa](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Mbinu hii ilipitishwa baadaye na Samourai Wallet, ambayo ikawa mteja wa kwanza kuitekeleza kwa kutumia zana ya Stowaway mwaka wa 2018. Dhana ya PayJoin inapatikana pia katika [BIP79](https://github.com/Bitcoin/bips/blob/master/bip-0079.mediawiki) na [BIP78](https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki). Maneno kadhaa hutumika kurejelea PayJoin:


- PayJoin
- Stowaway
- P2EP (Pay-to-Mwisho-Point)
- Shughuli ya Steganographic


Upekee wa PayJoin upo katika uwezo wake wa generate muamala unaoonekana kuwa wa kawaida mwanzoni lakini kwa kweli ni CoinJoin ndogo kati ya pande mbili. Ili kufanikisha hili, muundo wa muamala unahusisha mpokeaji malipo pamoja na mtumaji halisi katika pembejeo. Mpokeaji hujumuisha malipo kwao wenyewe katikati ya shughuli, ambayo huwawezesha kulipwa.


Hebu tuchukue mfano halisi: ukinunua baguette kwa `4000 Sats` kwa kutumia UTXO ya `10,000 Sats` na kuchagua PayJoin, mwokaji wako ataongeza UTXO ya `15,000 Sats` ambayo ni mali yao kama nyongeza, ambayo pato lako la 0 atapokea kwa ukamilifu 0. Sats`:

![Payjoin transaction diagram](assets/en/1.webp)


Katika mfano huu, mwokaji huleta `15,000 Sats` kama pembejeo na hutoka na `19,000 Sats`, ikiwa na tofauti ya `4000 Sats` haswa, ambayo ni bei ya baguette. Kwa upande wako, unaingia na `10,000 Sats` na kuishia na `6,000 Sats` kama pato, ikiwakilisha salio la `-4000 Sats`, ambayo ni bei ya baguette. Ili kurahisisha mfano, niliacha ada za Mining kimakusudi katika muamala huu.


## Madhumuni ya muamala wa PayJoin ni nini?


Muamala wa PayJoin unatimiza malengo mawili ambayo huwaruhusu watumiaji kuimarisha faragha ya malipo yao.

Kwanza kabisa, PayJoin inalenga kupotosha mwangalizi wa nje kwa kuunda udanganyifu katika uchambuzi wa mnyororo. Hili linawezekana kupitia Common Input Ownership Heuristic (CIOH). Kwa kawaida, wakati shughuli kwenye Blockchain ina ingizo nyingi, inachukuliwa kuwa pembejeo hizi zote huenda ni za huluki au mtumiaji mmoja. Kwa hivyo, wakati mchambuzi anachunguza shughuli ya PayJoin, wanaongozwa kuamini kwamba pembejeo zote zinatoka kwa mtu mmoja. Hata hivyo, mtazamo huu si sahihi kwa sababu mpokeaji malipo pia huchangia pembejeo pamoja na mlipaji halisi. Kwa hivyo, uchanganuzi wa mnyororo huelekezwa kwa tafsiri ambayo inageuka kuwa ya uwongo.


Zaidi ya hayo, PayJoin pia inaruhusu kudanganya mwangalizi wa nje kuhusu kiasi halisi cha malipo ambayo yamefanywa. Kwa kuchunguza muundo wa muamala, mchambuzi anaweza kuamini kuwa malipo ni sawa na kiasi cha moja ya matokeo. Walakini, kwa ukweli, kiasi cha malipo hakilingani na matokeo yoyote. Kwa kweli ni tofauti kati ya pato la mpokeaji UTXO na ingizo la mpokeaji UTXO. Kwa maana hii, shughuli ya PayJoin inaangukia katika uwanja wa steganografia. Huruhusu kuficha kiasi halisi cha muamala ndani ya muamala ghushi unaofanya kazi kama udanganyifu.


Tafadhali, kumbuka ufafanuzi wetu wa **Stenography**:

> Steganografia ni mbinu ya kuficha habari ndani ya data au vitu vingine kwa njia ambayo uwepo wa habari iliyofichwa hauonekani. Kwa mfano, ujumbe wa siri unaweza kujificha ndani ya dot katika maandishi ambayo hayana uhusiano wowote nayo, na kuifanya kuwa haijulikani kwa jicho la uchi (hii ni mbinu ya micropoint). Tofauti na usimbaji fiche, ambao hufanya habari isieleweke bila ufunguo wa usimbuaji, steganografia haibadilishi habari. Inabaki kuonyeshwa kwa macho wazi. Kusudi lake ni kuficha uwepo wa ujumbe wa siri, wakati usimbaji fiche unaonyesha wazi uwepo wa habari iliyofichwa, ingawa haipatikani bila ufunguo.

Hebu turudi kwenye mfano wetu wa shughuli ya PayJoin ya malipo ya baguette.

![Payjoin transaction schema from the outside](assets/en/2.webp)

Kwa kuona muamala huu kwenye Blockchain, mwangalizi wa nje ambaye anafuata kanuni za kawaida za uchanganuzi wa mnyororo angeweza kufasiri kama ifuatavyo: "*Alice aliunganisha UTXO 2 kama pembejeo za muamala ili kulipa `19,000 Sats` kwa Bob*."

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

Ufafanuzi huu ni wazi sio sahihi kwa sababu, kama unavyojua tayari, UTXO mbili za pembejeo sio za mtu yule yule. Zaidi ya hayo, thamani halisi ya malipo si `19,000 Sats`, bali ni `4,000 Sats`. Uchambuzi wa mwangalizi wa nje kwa hivyo unaelekezwa kwenye hitimisho potofu, kuhakikisha uhifadhi wa usiri wa washikadau.![PayJoin transaction diagram](assets/sw/1.webp)

Ikiwa ungependa kuchambua muamala halisi wa PayJoin, hapa kuna ule niliofanya kwenye Testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.s pace/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)


[**-> Gundua mafunzo yetu kuhusu jinsi ya kutengeneza PayJoin ukitumia Samourai Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)


[**-> Gundua mafunzo yetu kuhusu jinsi ya kutengeneza PayJoin ukitumia Sparrow Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)



**Nyenzo za nje:**


- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki.