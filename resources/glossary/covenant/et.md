---
term: COVENANT
---

Mehhanism, mis võimaldab kehtestada konkreetseid tingimusi selle kohta, kuidas teatud valuutatükki võib kulutada, sealhulgas tulevastes tehingutes. Lisaks tavaliselt UTXO skriptikeeles lubatud tingimustele kehtestab covenant lisapiiranguid selle kohta, kuidas seda Bitcoini saab järgnevates tehingutes kulutada. Tehniliselt toimub covenant'i loomine siis, kui UTXO `scriptPubKey` määratleb piirangud tehingu väljundite `scriptPubKey` suhtes, mis kulutab nimetatud UTXO-d. Skripti ulatuse laiendamisega võimaldaksid covenant'id Bitcoinis mitmeid arenguid, nagu näiteks drivechainide kahepoolne ankurdamine, vaultide rakendamine või ülekatte süsteemide, nagu Lightning, parendamine. Covenant'i ettepanekuid eristatakse kolme kriteeriumi alusel:
* Nende ulatus;
* Nende rakendamine;
* Nende rekursiivsus.

On mitmeid ettepanekuid, mis võimaldaksid Bitcoinis covenant'ide kasutamist. Rakendusprotsessis kõige kaugemale jõudnud on: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) ja `OP_VAULT`. Teiste ettepanekute hulgas on: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT` jne.

Covenant'i kontseptsiooni paremaks mõistmiseks kaaluge järgmist analoogiat: kujutage ette seifi, mis sisaldab 500€ väikestes rahatähtedes. Kui õnnestub see seif õige võtmega avada, siis võite seda raha kasutada, nagu soovite. See on tavaline olukord Bitcoiniga. Nüüd kujutage ette, et samas seifis ei ole 500€ pangatähtedes, vaid söögikupongides samaväärse väärtusega. Kui õnnestub see seif avada, võite seda summat kasutada. Siiski on teie vabadus kulutada piiratud, kuna neid kuponge saab kasutada ainult teatud restoranides maksmiseks. Seega on raha kulutamiseks esimene tingimus, et õnnestub seif õige võtmega avada. Kuid on ka täiendav tingimus tuleviku summa kasutamise kohta: seda tuleb kulutada ainult partnerrestoranides, mitte vabalt. See tulevaste tehingute piirangute süsteem on see, mida nimetatakse covenant'iks.

> ► *Prantsuse keeles ei ole terminit, mis täpselt hõlmaks sõna "covenant" tähendust. Võiks rääkida "klauslist", "paktist" või "kohustusest", kuid need ei vastaks täpselt terminile "covenant". See termin on laenatud õigusterminoloogiast, mis võimaldab kirjeldada lepingulist klauslit, mis paneb varale püsivad kohustused.*