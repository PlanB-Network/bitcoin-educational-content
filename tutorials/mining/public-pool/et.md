---
name: Public Pool
description: Sissejuhatus Avalikku Basseini
---

![signup](assets/cover.webp)

**Avalik Bassein** ei ole lihtsalt suvaline bassein; see on see, mida tuntakse ka **Solo Basseini** nime all. Kui sinu kaevur õnnestub blokki kaevandada, siis kogud sa terve bloki auhinna, mida ei jagata teiste basseini osalejatega ega basseiniga endaga.

**Avalik Bassein** pakub üksnes **bloki malli** sinu kaevurile, et see saaks oma ülesannet täita ilma, et sul oleks vaja omada **Bitcoin'i sõlme** ja tarkvara, mis suhtleb sinu kaevuriga. Kuna sa ei ühenda oma arvutusvõimsust teiste osalejate omaga, on sinu võimalused edukalt blokki kaevandada ilmselgelt väga madalad, meenutades veidi loteriisüsteemi, kus mõnikord võidab õnnelik isik jackpoti.

![signup](assets/1.webp)

**Avaliku Basseini** **Dashboard'il** on siiski mõned statistikad nagu basseini **Kogu Hashrate** ning erinevat tüüpi kaevurite jaotus, mis on basseiniga ühendatud.

![signup](assets/2.webp)

Esimestes ridadest näeme **Bitaxe**'i 1323 **Bitaxe**'iga, kokku 649TH/s. **Bitaxe** on **avatud lähtekoodiga** projekt, mis võimaldab lihtsalt taaskasutada kiipi **[ASIC](https://planb.academy/resources/glossary/asic)**'ist nagu **Antminer S19** avatud lähtekoodiga elektroonilisel plaadil, et teha väike kaevur 0.5TH/s 15W jaoks. See on kaevur, mida kasutame selle õpetuse näitena.

## Lisades **Töötaja** 👷‍♂️

![signup](assets/cover.webp)

Lehe ülaosas saad kopeerida basseini aadressi **stratum+tcp://public-pool.io:21496**.

Järgmiseks **kasutaja** väljal sisesta **Bitcoin** aadress, mis kuulub sulle.

Kui sul on mitu kaevurit, võid sisestada kõigile neile sama aadressi, nii et nende **hashrate'id** on ühendatud ja ilmuvad kui üks kaevur. Sa võid neid ka eristada, lisades igale kaevurile erineva nime. Selleks lihtsalt lisa **.workername** pärast **Bitcoin** aadressi.

Lõpuks **parooli** väljal kasuta **‘x’**.

Näide: Kui sinu **Bitcoin** aadress on **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** ja soovid oma kaevurile nimeks panna **« Brrrr »**, siis sisestaksid sa oma kaevuri liideses järgmise info:

- **URL**: stratum+tcp://public-pool.io:21496
- **KASUTAJA**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Parool**: **‘x’**
Kui sinu kaevur on **Bitaxe**, on väljad veidi erinevad, kuid info jääb samaks:
- **URL**: public-pool.io (siin pead eemaldama algusest **‘stratum+tcp://’** ja lõpust **‘:21496’**, mis kantakse üle pordi väljale)
- **Port**: 21496
- **Kasutaja**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Parool**: **‘x’**

![signup](assets/3.webp)
Mõni minut pärast kaevandamise alustamist saate oma andmeid **Public Pool** veebisaidil näha, otsides oma aadressi.

## Töölaud

![signup](assets/4.webp)

Kui olete ühendatud **Public Pool**'iga, pääsete oma **Töölauale** juurde, otsides oma **Bitcoin** aadressi, mille sisestasite **Kasutaja** väljale. Meie juhul on see **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

**Töölaual** kuvatakse erinevat teavet nii teie andmete kui ka võrgu kohta.

![signup](assets/5.webp)

Teil on **Võrgu Hash Rate**, mis vastab **Bitcoin** võrgu kogu töövõimsusele.

**Võrgu Raskus** näitab raskust, mis tuleb saavutada bloki valideerimiseks.

Ja **Teie Parim Raskus** on kõrgeim raskus, mille olete saavutanud. Kui juhuslikult 🍀 jõuate võrgu raskuseni, siis võidate terve bloki auhinna... pärast 100 blokki. Peaksite ootama 100 blokki, enne kui saate neid kulutada.

Teil on ka **Bloki Kõrgus**, mis on viimati kaevandatud bloki number, samuti selle kaal WU-des, maksimum olles 4,000,000.

Allpool näete kõigi oma seadmete individuaalseid statistikaid, kui olete neile andnud eristuva nime, lisades oma **Bitcoin** aadressile **Kasutaja** väljal **.nimi**.