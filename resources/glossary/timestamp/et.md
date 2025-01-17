---
term: TIMESTAMP

---
Ajastustempliks nimetatakse mehhanismi, mis hõlmab täpse ajalise tähise seostamist sündmuse, andmete või sõnumiga. Arvutisüsteemide üldises kontekstis kasutatakse ajatemplit operatsioonide kronoloogilise järjestuse määramiseks ja andmete terviklikkuse kontrollimiseks aja jooksul.

Bitcoini puhul kasutatakse ajatemplite abil tehingute ja plokkide kronoloogiat. Iga plokk plokiahelas sisaldab ajatemplit, mis näitab selle loomise ligikaudset hetke. Satoshi Nakamoto räägib oma valges raamatus isegi "ajatempli serverist", et kirjeldada seda, mida me täna nimetaksime "plokiahelaks" Ajastustempli roll Bitcoinis on tehingute kronoloogia kindlaksmääramine, et ilma keskasutuse sekkumiseta kindlaks teha, milline tehing oli esimene. See mehhanism võimaldab igal kasutajal kontrollida, kas minevikus on toimunud tehing, ja seega takistada pahatahtlikul kasutajal topeltkulutusi teha. Seda mehhanismi põhjendab Satoshi Nakamoto oma valges raamatus kuulsa fraasiga: "*Ainsaks viisiks kinnitada tehingu puudumist on olla teadlik kõigist tehingutest." See standard on kehtestatud Unixi aja alusel, mis kujutab endast alates 1. jaanuarist 1970 möödunud sekundite koguarvu.

> ► *Bitcoini plokkide ajatempel on suhteliselt paindlik, sest selleks, et ajatempel oleks kehtiv, peab see lihtsalt olema suurem kui 11 eelneva ploki mediaan (MTP) ja väiksem kui sõlmede poolt tagastatud aegade mediaan (võrguga korrigeeritud aeg) pluss 2 tundi.*