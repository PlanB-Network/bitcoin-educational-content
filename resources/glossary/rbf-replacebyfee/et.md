---
term: RBF (REPLACE-BY-FEE)
---

Tehingumehhanism, mis võimaldab saatjal asendada ühe tehingu teisega, makstes kõrgemaid tasusid, et kiirendada selle kinnitamist. Kui tehing madalate tasude tõttu toppama jääb, saab saatja kasutada *Replace-By-Fee'd* tasude suurendamiseks ja oma asendustehingu eelisjärjekorda seadmiseks mempuulides.

RBF on kohaldatav seni, kuni tehing on mempuulides; kord plokis, ei saa seda enam asendada. Esialgsel saatmisel peab tehing määrama oma asendatavuse võimaluse, kohandades `nSequence` väärtust numbrile, mis on väiksem kui `0xfffffffe`. Seda tuntakse RBF "lipuna". See seadistus annab märku võimalusest tehingut pärast selle levitamist uuendada, mis omakorda võimaldab RBF-i kasutamist. Siiski on mõnikord võimalik asendada tehingut, mis ei ole RBF-i märkinud. Sõlmed, mis kasutavad konfiguratsiooniparameetrit `mempoolfullrbf=1`, aktsepteerivad sellist asendust isegi kui RBF-i alguses ei märgitud.

Erinevalt CPFP-st (*Child Pays For Parent*), kus saaja saab toimida tehingu kiirendamiseks, võimaldab RBF (*Replace-By-Fee*) saatjal võtta initsiatiivi oma tehingu kiirendamiseks, suurendades tasusid.