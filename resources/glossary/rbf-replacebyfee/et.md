---
term: RBF (REPLACE-BY-FEE)

---
Tehingumehhanism, mis võimaldab saatjal asendada üks tehing teise tehinguga, makstes kõrgemat tasu, et kiirendada selle kinnitamist. Kui liiga madalate tasudega tehing jääb kinni, saab saatja kasutada *Replace-By-Fee*, et suurendada tasusid ja seada oma asendustehing mempoolsesse eelisjärjekorda.

RBF on kohaldatav seni, kuni tehing on mempools; kui see on kord plokis, ei saa seda enam asendada. Esimesel saatmisel peab tehing täpsustama oma asendatavust, kohandades `nSequence` väärtuse arvuks, mis on väiksem kui `0xfffffffffe`. Seda nimetatakse RBF "lipuks". See seadistus annab märku võimalusest uuendada tehingut pärast selle saatmist, mis võimaldab hiljem RBF-i. Mõnikord on siiski võimalik asendada tehing, mis ei ole RBFist märku andnud. Sõlmed, mis kasutavad konfiguratsiooniparameetrit `mempoolfullrbf=1`, aktsepteerivad seda asendamist isegi siis, kui RBF ei olnud algselt signaliseeritud.

Erinevalt CPFP-st (*Child Pays For Parent*), kus vastuvõtja saab tehingu kiirendamiseks ise tegutseda, võimaldab RBF (*Replace-By-Fee*) saatjal ise algatada oma tehingu kiirendamist, suurendades tasusid.
