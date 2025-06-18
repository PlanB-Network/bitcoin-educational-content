---
term: REPLAY ATTACK
---

Bitcoin kontekstis toimub kordusrünnak siis, kui ühes Blockchains tehtud kehtivat tehingut reprodutseeritakse pahatahtlikult teises Blockchains, millel on sama tehingulugu. Teisisõnu, ühes kanalis edastatud tehingut võib korrata teises kanalis ilma esimese tehingu saatja nõusolekuta.


Võtame näiteks hüpoteetilise Hard Fork Bitcoin-st, mille nimi on "*BitcoinBis*". Kui te teete bitcoinides makse, et osta pagarilt baguette'i reaalses Blockchain Bitcoin-s, siis võib seesama pagar seda seaduslikku tehingut *BitcoinBis*-s korrata, et saada sama summa krüptovaluutas selles Fork-s, ilma et te ise midagi ette võtaksite.


Seda tüüpi rünnak võib toimuda ainult Blockchain hargnemise korral, kus on 2 sõltumatut ahelat, mis püsivad aja jooksul. Tavaliselt oleks see Hard Fork puhul. Et kordusrünnak oleks võimalik, peab 2 plokiahelal olema ühine ajalugu ja dubleeritud tehing peab tarbima sisendina UTXOsid, mis on loodud eelnevatest tehingutest, mis toimusid enne kahe ahela jagunemist, või eelnevatest tehingutest, mis on ise juba kordusrünnaku käigus uuesti läbi mängitud.


Üldiselt tähendab replay-rünnak arvutite puhul kehtivate andmete pealtkuulamist ja korduvkasutamist, et petta süsteemi, kordades algset edastust. See võib mõnikord viia identiteedivarguse toimumiseni võrgus.


> ► * Bitcoin tehingu kordusrünnaku puhul nimetatakse seda mõnikord lihtsalt "kordustehinguks". "*