---
term: TAASTUMISFRAAS

---
Taastamisfraas, mida mõnikord nimetatakse ka mnemoonikaks, seemnefraasiks või salajaks fraasiks, on tavaliselt 12 või 24 sõnast koosnev jada, mis genereeritakse pseudosrandomiliselt entroopia allikast. Pseudosuvanduslikku jada täiendatakse alati kontrollsummaga. Mälufraasi kasutatakse koos valikulise salasõnaga, et tuletada deterministlikult kõik HD (Hierarchical Deterministic) rahakotiga seotud võtmed. See tähendab, et sellest fraasist on võimalik deterministlikult genereerida ja taasluua kõik Bitcoini rahakoti privaat- ja avalikud võtmed ning sellest tulenevalt pääseda ligi sellega seotud rahalistele vahenditele. Taastamisfraasi eesmärk on pakkuda bitcoinide varundamise ja taastamise vahendit, mis on nii turvaline kui ka lihtne kasutada.

Oluline on hoida seda fraasi turvalises kohas, sest igaühel, kes seda mnemoonikat valdab, oleks juurdepääs vastava rahakoti rahalistele vahenditele. Kui seda kasutatakse traditsioonilise rahakoti kontekstis ja ilma valikulise tunnuslauseta, kujutab see sageli endast SPOF (Single Point Of Failure). Seega on taastamisfraas pseudosrandomjärjestuse ja kontrollsumma kodeerimine igapäevaseks sõnaks, et hõlbustada selle märkimist ja loetavust inimeste poolt. See koostatakse vastavalt standardile BIP39, mis määratleb ja korraldab 2048 sõnast koosneva loendi, mida kasutatakse selle kodeerimiseks.

> ► *BIP39 2048 sõna nimekiri on saadaval mitmes keeles, kuid soovitatav on kasutada ainult ingliskeelset versiooni, kuna see on rahakoti tarkvara poolt enim toetatud versioon