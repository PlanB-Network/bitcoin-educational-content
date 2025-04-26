---
name: Payjoin
description: Mis on Payjoin Bitcoinil?
---
![Payjoin thumbnail - steganograafia](assets/cover.webp)

***TÄHELEPANU:** Pärast Samourai Wallet'i asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil, toimivad Payjoins Stowaway'd Samourai Wallet'il ainult käsitsi PSBT vahetades huvitatud osapoolte vahel, eeldusel, et mõlemad kasutajad on ühendatud omaenda Dojoga. Sparrow puhul toimivad Payjoinsid BIP78 kaudu endiselt. Siiski on võimalik, et need tööriistad taaskäivitatakse lähinädalatel. Vahepeal võite siiski seda artiklit lugeda, et mõista payjoins'ide teoreetilist toimimist.*

_Jälgime selle juhtumi arenguid ning sellega seotud tööriistade arenguid tähelepanelikult. Kinnitame, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---
## Payjoin tehingute mõistmine Bitcoinil

Payjoin on Bitcoin'i tehingu spetsiifiline struktuur, mis suurendab kasutaja privaatsust makse sooritamisel, tehes koostööd makse saajaga.

2015. aastal mainis [LaurentMT](https://twitter.com/LaurentMT) esmakordselt seda meetodit kui "steganograafilisi tehinguid" dokumendis, mis on kättesaadav [siin](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Seda tehnikat võttis hiljem kasutusele Samourai Wallet, mis sai esimeseks kliendiks, kes selle 2018. aastal Stowaway tööriistaga rakendas. Payjoin'i kontseptsiooni leidub ka [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) ja [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki) dokumentides. Payjoin'i viitamiseks kasutatakse mitmeid termineid:
- Payjoin
- Stowaway
- P2EP (Pay-to-End-Point)
- Steganograafiline tehing

Payjoin'i ainulaadsus seisneb selle võimes genereerida tehing, mis esmapilgul tundub tavaline, kuid on tegelikult mini Coinjoin kahe osapoole vahel. Selle saavutamiseks hõlmab tehingu struktuur makse saajat koos tegeliku saatjaga sisendites. Saaja lisab tehingu keskele makse iseendale, mis võimaldab neil saada makstud.

Võtame konkreetse näite: kui ostate baguette'i `4000 satsi` eest, kasutades UTXO-d `10,000 satsi` ja valite Payjoin'i, lisab teie pagar sisendina `15,000 satsi` suuruse UTXO, mis kuulub neile, mille nad saavad täielikult väljundina, lisaks teie `4000 satsile`:
![Payjoin tehingu diagramm](assets/en/1.webp)
Selles näites tutvustab pagar sisendina `15,000 satsi` ja väljub `19,000 satsiga`, erinevusega täpselt `4000 satsi`, mis on bageti hind. Teie poolt sisestate `10,000 satsi` ja lõpetate `6,000 satsiga` väljundina, mis esindab `-4000 satsi` bilanssi, mis on bageti hind. Näite lihtsustamiseks jätsin tahtlikult kaevandamistasud sellest tehingust välja.
## Mis on Payjoin tehingu eesmärk?

Payjoin tehing teenib kahte eesmärki, mis võimaldavad kasutajatel oma makse privaatsust suurendada.
Esiteks, Payjoin eesmärk on eksitada välist vaatlejat, luues ahelaanalüüsis pettekujutise. See on võimalik tänu Ühise Sisendi Omandi Heuristikale (CIOH). Tavaliselt, kui blockchainis on tehingul mitu sisendit, eeldatakse, et kõik need sisendid kuuluvad tõenäoliselt samale isikule või kasutajale. Seega, kui analüütik uurib Payjoin tehingut, viib see neid uskuma, et kõik sisendid pärinevad samalt isikult. Siiski on see taju vale, kuna makse saaja lisab samuti sisendeid koos tegeliku maksjaga. Seetõttu suunatakse ahelaanalüüs tõlgendusele, mis osutub valeks.

Lisaks võimaldab Payjoin eksitada välist vaatlejat ka tegeliku makse summa osas. Tehingu struktuuri uurides võib analüütik arvata, et makse on võrdne ühe väljundi summaga. Tegelikkuses ei vasta makse summa ühelegi väljunditest. See on tegelikult erinevus saaja väljundi UTXO ja saaja sisendi UTXO vahel. Selles mõttes kuulub Payjoin tehing steganograafia valdkonda. See võimaldab peita tegeliku tehingu summa võlts tehingu sisse, mis toimib pettekujutisena.

> Steganograafia on tehnika, mis peidab informatsiooni teiste andmete või objektide sisse nii, et peidetud informatsiooni olemasolu ei ole tajutav. Näiteks võib salajase sõnumi peita teksti punkti sisse, mis ei ole sellega seotud, muutes selle palja silmaga tuvastamatuks (see on mikropunkti tehnika). Erinevalt krüpteerimisest, mis muudab informatsiooni ilma dekrüpteerimisvõtmeta mõistetamatuks, ei muuda steganograafia informatsiooni. See jääb nähtavale. Selle eesmärk on pigem peita salajase sõnumi olemasolu, samas kui krüpteerimine selgelt paljastab peidetud informatsiooni olemasolu, kuigi see on ilma võtmeta kättesaamatu.

Tagasi meie Payjoin tehingu näite juurde bageti eest maksmisel.
![Payjoin tehingu skeem väljastpoolt](assets/en/2.webp)
Seda tehingut blockchainis nähes tõlgendaks väline vaatleja, kes järgib tavalisi ahelaanalüüsi heuristikaid, seda järgmiselt: "*Alice ühendas 2 UTXOt sisenditena tehingus, et maksta `19,000 satsi` Bobile*."
![Vale tõlgendus Payjoin tehingust väljastpoolt](assets/en/3.webp)
See tõlgendus on ilmselgelt vale, kuna, nagu te juba teate, ei kuulu kaks sisend-UTXOt samale isikule. Lisaks ei ole tegelik makseväärtus mitte `19,000 satsi`, vaid pigem `4,000 satsi`. Välise vaatleja analüüs suunatakse seega valele järeldusele, tagades osapoolte konfidentsiaalsuse säilimise.![payjoin tehingu diagramm](assets/en/1.webp)
Kui soovite analüüsida päris Payjoin tehingut, siis siin on üks, mille ma sooritasin testvõrgus: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)  
[**-> Avasta meie õpetus, kuidas teha Payjoin tehingut Samourai Wallet'iga**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)  

[**-> Avasta meie õpetus, kuidas teha Payjoin tehingut Sparrow Wallet'iga**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)


**Välised ressursid:**
- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.