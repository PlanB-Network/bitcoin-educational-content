---
term: BIP8

---
BIP8, mis töötati välja pärast SegWitiga seotud arutelusid, mille aktiveerimiseks kasutati BIP9, on pehme kahvli aktiveerimise meetod, mis sisaldab automaatset UASF (*User-Activated Soft Fork*) mehhanismi. Nagu BIP9, kasutab ka BIP8 kaevandajate signalisatsiooni, kuid lisab parameetri `LOT` (*Lock-in On Time out*). Kui `LOT` on seatud `true`, käivitub signaalimisperioodi lõppemisel ilma nõutavat künnist saavutamata automaatselt UASF, mis sunnib soft forki aktiveerima. See lähenemisviis sunnib kaevandajaid olema koostöövalmis või riskida kasutajate poolt kehtestatud UASFiga. Erinevalt BIP9-st määratleb BIP8 signaalimisperioodi plokkide kõrguse alusel, välistades kaevurite võimalikud manipulatsioonid hash-kiiruse kaudu. BIP8 võimaldab ka muutuva hääletuskünnise määramist ja kehtestab aktiveerimiseks minimaalse plokikõrguse parameetri, mis annab kaevuritele aega ette valmistada ja anda oma nõusolekut eelnevalt märku, ilma et nad peaksid tingimata valmis olema. Kui soft fork aktiveeritakse BIP8 kaudu koos parameetriga `LOT=true`, kasutatakse väga agressiivset meetodit kaevurite vastu, kes pannakse kohe võimaliku UASF-i surve alla. Tõepoolest, see jätab neile ainult 2 valikut:


- Olge koostööaldis ja hõlbustage seeläbi aktiveerimisprotsessi;
- Olla koostööst keeldunud, millisel juhul teevad kasutajad automaatselt UASF-i, et kehtestada soft fork.