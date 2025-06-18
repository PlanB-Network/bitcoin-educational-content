---
term: HORODATAGE
---

Ajatemping ehk Timestamp on mehhanism, mille abil seostatakse sündmuse, andmete või sõnumiga täpne ajamärk. Arvutisüsteemide üldises kontekstis kasutatakse ajatemplit operatsioonide kronoloogilise järjestuse määramiseks ja andmete terviklikkuse kontrollimiseks aja jooksul.


Bitcoin puhul kasutatakse ajatemplite abil tehingute ja plokkide kronoloogiat. Iga plokk Blockchain-s sisaldab Timestamp, mis näitab selle loomise ligikaudset aega. Satoshi Nakamoto räägib oma valges raamatus isegi "Timestamp serverist", et kirjeldada seda, mida me täna nimetaksime "Blockchain". Bitcoin ajatempli roll on määrata tehingute kronoloogiat, et ilma keskasutuse sekkumiseta oleks võimalik kindlaks teha, milline tehing saabus esimesena. See mehhanism võimaldab igal kasutajal kontrollida, kas tehing ei ole toimunud minevikus, ja seega takistada pahatahtlikul kasutajal topeltkulutuste tegemist. Seda mehhanismi põhjendab Satoshi Nakamoto oma valges raamatus kuulsa lausega: " *See standard põhineb Unixi ajal, mis kujutab endast alates 1. jaanuarist 1970 möödunud sekundite koguarvu.


> ► *Blokkide ajamärgid on Bitcoin puhul suhteliselt paindlikud, sest selleks, et Timestamp oleks kehtiv, peab see lihtsalt olema suurem kui sellele eelneva 11 ploki mediaan (MTP) ja väiksem kui sõlmede poolt tagastatud aegade mediaan (võrguga kohandatud aeg) pluss 2 tundi.*