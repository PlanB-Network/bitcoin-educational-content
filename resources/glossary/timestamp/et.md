---
term: AJATEMPEL
---

Ajatemplite kasutamine ehk "timestamp" inglise keeles, on mehhanism, mis hõlmab sündmuse, andmete või sõnumi seostamist täpse ajalise märgisega. Üldises arvutisüsteemide kontekstis kasutatakse ajatemplite kasutamist operatsioonide kronoloogilise järjestuse määramiseks ja andmete terviklikkuse kontrollimiseks ajas.

Bitcoini puhul kasutatakse ajatempleid tehingute ja plokkide kronoloogia kindlaksmääramiseks. Iga plokiahela plokk sisaldab ajatemplit, mis näitab selle loomise ligikaudset hetke. Satoshi Nakamoto isegi mainib oma Valges Paberis "ajatempli serverit", kirjeldamaks seda, mida me täna nimetame "plokiahelaks". Ajatemplite roll Bitcoini puhul on tehingute kronoloogia kindlaksmääramine, et määrata ilma keskse autoriteedi sekkumiseta, milline tehing toimus esimesena. See mehhanism võimaldab igal kasutajal kontrollida tehingu mitteolemasolu minevikus ja seeläbi vältida pahatahtliku kasutaja poolt topeltkulutamist. Satoshi Nakamoto õigustab seda mehhanismi oma Valges Paberis kuulsa fraasiga: "*Ainsaks viisiks tehingu puudumise kinnitamiseks on olla teadlik kõigist tehingutest.*" See standard põhineb Unixi ajal, mis esindab sekundite koguarvu alates 1. jaanuarist 1970.

> ► *Bitcoini ploki ajatemplite kasutamine on suhteliselt paindlik, kuna ajatempli kehtivuseks peab see olema suurem kui 11 eelneva ploki mediaanaeg (MTP) ja väiksem kui sõlmede tagastatud aegade mediaan pluss 2 tundi.*