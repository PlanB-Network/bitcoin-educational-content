---
term: TEHINGUTASUD
---

Tehingutasud esindavad summat, mille eesmärk on kompenseerida kaevurite osalust töötõendusmehhanismis. Need tasud julgustavad kaevureid lisama tehinguid blokkidesse, mida nad loovad. Need tulenevad sisendite kogusumma ja väljundite kogusumma erinevusest tehingus:

```text
tasud = sisendid - väljundid
```

Need on väljendatud `sats/vBytes`, mis tähendab, et tasud ei sõltu saadetud bitcoinide hulgast, vaid tehingu kaalust. Tasud valib vabalt tehingu saatja ja need määravad tema tehingu lisamise kiiruse blokki läbi oksjonimehhanismi. Näiteks, öelgem, et teen tehingu, mille sisend on `100,000 sats`, väljund on `40,000 sats` ja teine väljund on `58,500 sats`. Väljundite kogusumma on `98,500 sats`. Sellele tehingule eraldatud tasud on `1,500 sats`. Kaevur, kes minu tehingu lisab, saab luua `1,500 sats` oma coinbase tehingus vastutasuks `1,500 sats` eest, mida ma oma väljundites tagasi ei saanud.

Tehingud, mille tasud on suhteliselt nende suurusega võrreldes kõrgemad, käsitletakse kaevurite poolt prioriteetsena, mis võib kiirendada kinnitamisprotsessi. Vastupidiselt võivad madalamate tasudega tehingud kõrge ummikuse perioodidel viibida. On oluline märkida, et Bitcoin'i tehingutasud on erinevad bloki subsiidiumist, mis on kaevuritele lisastimulatsioon. Bloki preemia koosneb iga kaevandatud blokiga loodud uutest bitcoinidest (bloki subsiidium) ning kogutud tehingutasudest. Kuigi bloki subsiidium väheneb aja jooksul bitcoinide kogupakkumise piirangu tõttu, jätkavad tehingutasud olulist rolli kaevurite osalemise julgustamisel.

Protokolli tasandil ei takista miski kasutajatel lisamast tehinguid ilma tasudeta blokki. Tegelikkuses on sellised tasuta tehingud erandlikud. Vaikimisi ei edasta Bitcoin'i noodid tehinguid, mille tasud on madalamad kui `1 sat/vBytes`. Kui mõned tasuta tehingud on läbinud, on see sellepärast, et need integreeriti otse võiduka kaevuri poolt, ilma noodivõrgust läbimata. Näiteks järgmine tehing ei sisalda tasusid:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Konkreetse näite puhul oli see tehing algatatud F2Pooli kaevandusbasseini direktori poolt. Tavalise kasutaja jaoks on praegune alumine piir seega `1 sat/vBytes`.
On vajalik ka arvestada puhastamise piirangutega. Kõrge ummikuse perioodidel puhastavad noodid oma ootel olevaid tehinguid teatud lävendi all, et austada nende eraldatud RAM-i piiri. See piir on kasutaja poolt vabalt valitud, kuid paljud järgivad Bitcoin Core'i vaikimisi väärtust 300 MB. Seda saab muuta `bitcoin.conf` failis parameetriga `maxmempool`.
> ► *Inglise keeles viitame sellele kui "transaction fees".*