---
term: TEHINGUTASUD

---
Tehingutasud kujutavad endast summat, mille eesmärk on hüvitada kaevandajatele nende osalemine töö tõestusmehhanismis. Need tasud julgustavad kaevandajaid lisama tehinguid nende loodud plokkidesse. Need tulenevad tehingu sisendite kogusumma ja väljundite kogusumma vahest:

```text
fees = inputs - outputs
```

Need on väljendatud "sats/vBytes", mis tähendab, et tasud ei sõltu mitte saadetud bitcoinide summast, vaid tehingu kaalust. Need on tehingu saatja poolt vabalt valitud ja määravad oksjonimehhanismi kaudu selle plokki lisamise kiiruse. Oletame näiteks, et ma teen tehingu, mille sisendiks on "100 000 sats", väljundiks "40 000 sats" ja teiseks väljundiks "58 500 sats". Väljundite kogusumma on `98,500 sats`. Sellele tehingule eraldatud tasud on 1 500 sati. Kaevandaja, kes minu tehingusse kuulub, saab oma Coinbase'i tehingus luua `1 500 sats`, mille eest ma ei saanud oma väljundites tagasi `1 500 sats`.

Tehinguid, mille eest makstakse suuremaid tasusid, käsitletakse kaevurite poolt prioriteetsetena, mis võib kiirendada kinnitamisprotsessi. Seevastu madalama tasuga tehingud võivad suure ülekoormuse ajal viibida. Tasub märkida, et Bitcoini tehingutasud erinevad plokkide toetusest, mis on täiendav stiimul kaevandajatele. Plokkide tasu koosneb uutest bitcoinidest, mis luuakse iga kaevandatud plokiga (plokkide toetus), ning kogutud tehingutasudest. Kuigi blokisubsiidium väheneb aja jooksul bitcoinide kogupakkumise piirangu tõttu, mängivad tehingutasud jätkuvalt olulist rolli kaevandajate osalemise julgustamisel.

Protokolli tasandil ei takista miski kasutajaid lisamast plokki tehinguid ilma tasudeta. Tegelikkuses on selline tasuta tehing erandlik. Vaikimisi ei edasta Bitcoini sõlmede kaudu tehinguid, mille tasud on väiksemad kui `1 sat/vBytes`. Kui mõned tasuta tehingud on läbinud, siis selle põhjuseks on see, et võitnud kaevandaja integreeris need otse, ilma et nad oleksid läbinud sõlmede võrgustikku. Näiteks järgmine tehing ei sisalda tasusid:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Selles konkreetses näites oli tegemist F2Pooli kaevandamisbasseini direktori algatatud tehinguga. Tavakasutajana on praegune alumine piir seega `1 sat/vBytes`.

Samuti on vaja kaaluda puhastuse piire. Suure ülekoormuse ajal puhastavad sõlmede mempoolid oma pooleliolevad tehingud, mis jäävad alla teatava künnise, et pidada kinni neile eraldatud RAMi piirist. Selle piiri valib kasutaja vabalt, kuid paljud jätavad Bitcoin Core'i vaikimisi väärtuseks 300 MB. Seda saab muuta failis `bitcoin.conf` parameetriga `maxmempool`.

> ► *Inglise keeles nimetame seda "tehingutasuks"