---
term: BIP49

---
BIP49 on informatiivne BIP, mis tutvustab tuletamismeetodit, mida kasutatakse HD rahakoti Nested SegWit-aadresside genereerimiseks. Kavandatav tuletamise tee järgib BIP43 ja BIP44 standardeid, kusjuures eesmärgi sügavuses on indeks `49'` (karastatud tuletamine). Näiteks P2SH-P2WPKH-konto esimene aadress tuletatakse tee järgi: `m/49'/0'/0'/0/0`. SegWit'i käivitamisel leiutati SegWit'i kasutuselevõtu hõlbustamiseks nested SegWit'i skriptid. Need võimaldavad kasutada seda uut standardit isegi rahakottides, mis ei ole veel algselt SegWitiga ühilduvad.