---
term: BTCPay Server

definition: Avatud lähtekoodiga maksetöötleja, mis võimaldab vastu võtta bitcoini makseid ilma vahendajata.
---

⚠️ **Kriitiline turvahoiatus (7. august 2026):** BTCPay Server'it mõjutavat kriitilist haavatavust kuritarvitatakse aktiivselt ja see võib kaasa tuua rahaliste vahendite kaotuse. Uuenda oma instants viivitamatult **versioonile 2.4.2** kaudu `Admin Dashboard > Server > Maintenance > Update` ning kontrolli seejärel, et jaluses kuvatakse `2.4.2`. Kui sa ei saa kohe uuendada, lülita oma BTCPay Server välja. Pärast uuendamist pead täielikult uuendama ka oma macaroons'id ja `macaroons.db`, täielikult uuendama kõigi teiste Lightning-taustasüsteemide autentimisstringid ning juhul, kui lõid BTCPay Server'i sees kuuma on-chain rahakoti, tuleb need vahendid mujale liigutada ja rahakott uuesti luua. Integreerijad peaksid uuendama ka NBXplorer'i versioonile 2.6.10. Allikas: [BTCPay Server 2.4.2 väljalaskemärkmed](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server on avatud lähtekoodiga makseprotsessor, mis võimaldab kaupmeestel ja kasutajatel aktsepteerida Bitcoini makseid, ilma et nad peaksid tehingu töötlemiseks toetuma kolmandale osapoolele. 2017. aastal käivitatud BTCPay Server pakub e-kaubanduse saitidele Bitcoini makseintegratsiooni lahendust, millel on täiustatud funktsioonid, näiteks toetus riistvaralistele rahakottidele, arveldus- ja raamatupidamistööriistad, samuti ühilduvus Lightning Networkiga. Selle arendamise algatas Nicolas Dorier vastuseks Bitpay tegevusele, mis tema sõnul oli eksitanud oma kasutajaid, lükates neid SegWit2x-i kasutuselevõtu suunas, mida ettevõte pidas ekslikult "tõeliseks" Bitcoiniks. See vastuseis oli kokku võetud Nicolas Dorier'i nüüdseks kuulsaks saanud säutsus 2017. aasta augustis:

> "See on vale, minu usaldus sinu vastu on murtud, ma teen sind iganenuks_".
