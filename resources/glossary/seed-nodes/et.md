---
term: SEED NODES

---
Avalike Bitcoini sõlmede staatiline nimekiri, mis on integreeritud otse Bitcoin Core'i lähtekoodi (`bitcoin/src/chainparamsseeds.h`). See nimekiri on ühenduspunktiks uutele Bitcoini sõlmedele, kes liituvad võrguga, kuid seda kasutatakse ainult siis, kui DNS-seemned ei anna vastust 60 sekundi jooksul pärast nende taotlust. Sellisel juhul võtab uus Bitcoini sõlmpunkt ühendust nende seemnesõlmedega, et luua esimene ühendus võrguga ja küsida teiste sõlmede IP-aadresse. Lõppeesmärk on hankida vajalik teave, et teostada esialgne plokkide allalaadimine (IBD) ja sünkroniseerida selle ahelaga, kus on kõige rohkem tööd kogunenud. Seemnesõlmede nimekiri sisaldab ligi 1000 sõlme, mis on kindlaks määratud vastavalt BIP155 kehtestatud standardile. Seega kujutavad seemnesõlmed Bitcoini sõlme jaoks kolmandat meetodit võrguga ühenduse loomiseks pärast võimalikku faili `peers.dat` kasutamist, mille sõlme ise on loonud, ja DNS-seemnete hankimist.

> ► *Märkus, seemnesõlmi ei tohi segi ajada "DNS-seemnetega", mis on teine meetod ühenduste loomiseks.*