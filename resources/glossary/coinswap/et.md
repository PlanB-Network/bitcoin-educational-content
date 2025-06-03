---
term: COINSWAP
---

Ownership salajase edastamise protokoll kasutajate vahel. Selle meetodi eesmärk on bitcoinide üleandmine ühelt isikult teisele ja vastupidi, ilma et see Exchange oleks Blockchain-l selgelt nähtav. Coinwap kasutab ülekande tegemiseks arukaid lepinguid, ilma et oleks vaja osapoolte vahelist usaldust.


Kujutame ette naiivset näidet (mis ei toimi) Alice'i ja Bobiga. Alice'il on 1 BTC, mis on kaitstud privaatvõtmega $A$, ja Bobil on samuti 1 BTC, mis on kaitstud privaatvõtmega $B$. Teoreetiliselt võiksid nad Exchange oma isiklikke võtmeid välise sidekanali kaudu salajase ülekande tegemiseks kasutada. See naiivne meetod kujutab endast siiski suurt usaldusriski. Mitte miski ei takista Alice'il pärast Exchange-i hoidmast privaatvõtme $A$ koopiat ja kasutamast seda hiljem bitcoinide varastamiseks, kui võti on Bobi käes. Veelgi enam, ei ole mingit garantiid, et Alice ei saa Bobi privaatvõtit $B$ ja ei anna Exchange-s kunagi edasi oma privaatvõtit $A$. See Exchange tugineb seega osapoolte vahelisele liigsele usaldusele ja on Ownership turvalise, salajase edastamise tagamiseks ebatõhus.


Nende probleemide lahendamiseks ja müntide vahetamise võimaldamiseks osapoolte vahel, kes üksteist ei usalda, kasutame Smart contract süsteeme, mis muudavad Exchange "aatomiks". Need võivad olla HTLC (*Hash ajaliselt lukustatud lepingud*) või PTLC (*Punkti ajaliselt lukustatud lepingud*). Need kaks protokolli toimivad sarnaselt, kasutades ajalukustussüsteemi, mis tagab, et Exchange on kas edukalt lõpetatud või täielikult tühistatud, kaitstes seega mõlema osapoole vahendite terviklikkust. Peamine erinevus HTLC ja PTLC vahel seisneb selles, et HTLC kasutab tehingu kindlustamiseks hash'e ja eelkujutisi, PTLC aga Adaptor-allkirju.


Mündivahetuse stsenaariumis, kus Alice ja Bob kasutavad HTLC või PTLC-d, toimub Exchange turvaliselt: kas see õnnestub ja kumbki saab teise BTC, või ebaõnnestub ja kumbki jätab oma BTC endale. See muudab võimatuks, et kumbki osapool saaks petta või teise BTC-d varastada.


Adaptori allkirjade kasutamine on selles kontekstis eriti huvitav, kuna see võimaldab loobuda traditsioonilistest skriptidest (mehhanism, mida mõnikord nimetatakse "skriptideta skriptideks"). See vähendab Exchangega seotud kulusid. Teine oluline eelis on see, et kohandajate allkirjade puhul ei ole vaja kasutada mõlemale tehingu osapoolele ühist Hash, mistõttu ei ole vaja teatavat tüüpi Exchange puhul nende vahelist otsest seost avaldada.