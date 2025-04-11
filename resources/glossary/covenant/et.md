---
term: COVENANT

---
Mehhanism, mis võimaldab kehtestada konkreetsed tingimused selle kohta, kuidas antud rahaühikut võib kulutada, sealhulgas tulevastes tehingutes. Lisaks UTXO käsikirjakeeles tavaliselt lubatud tingimustele kehtestab leping täiendavad piirangud sellele, kuidas seda Bitcoini saab järgmistes tehingutes kulutada. Tehniliselt toimub lepingu kehtestamine siis, kui UTXO "scriptPubKey" määratleb piirangud UTXOd kulutava tehingu väljundite "scriptPubKey" jaoks. Skripti kohaldamisala laiendades võimaldaksid lepingud Bitcoini arvukaid arenguid, nagu näiteks drivechains'i kahepoolne ankurdamine, võlvade rakendamine või selliste overlay-süsteemide nagu Lightning täiustamine. Paktiettepanekuid eristatakse kolme kriteeriumi alusel:


- Nende reguleerimisala;
- Nende rakendamine;
- Nende rekursiivsus.

On palju ettepanekuid, mis võimaldaksid kasutada Bitcoini klausleid. Kõige kaugemale jõudnud rakendamisprotsessis on järgmised: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) ja `OP_VAULT`. Muude ettepanekute hulgas on: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT` jne.

Et paremini mõista lepingu mõistet, vaadake järgmist analoogiat: kujutage ette seifi, milles on 500 eurot väikeste rahatähtedena. Kui teil õnnestub see seif õige võtmega avada, siis võite seda raha kasutada nii, nagu soovite. See on tavaline olukord Bitcoini puhul. Nüüd kujutage ette, et sama seif ei sisalda 500€ pangatähtedena, vaid hoopis samaväärse väärtusega söögikupongid. Kui teil õnnestub see seif avada, saate seda summat kasutada. Siiski on teie kulutamisvabadus piiratud, sest saate neid vautšereid kasutada ainult teatud restoranides maksmiseks. Seega on selle raha kulutamiseks esimene tingimus, mis seisneb selles, et sul õnnestub seif vastava võtmega avada. Kuid selle summa edasise kasutamise kohta on ka lisatingimus: seda tuleb kulutada ainult partnerrestoranides, mitte vabalt. Seda tulevaste tehingute piirangute süsteemi nimetatakse lepinguks.

> ► *Fransi keeles ei ole olemas terminit, mis täpselt väljendaks sõna "leping" tähendust. Võib rääkida "klauslist", "paktist" või "kohustusest", kuid need ei vasta täpselt mõistele "leping". See termin on laenatud juriidilisest terminoloogiast, mis võimaldab kirjeldada lepingulist klauslit, mis paneb kinnisvarale püsivaid kohustusi*