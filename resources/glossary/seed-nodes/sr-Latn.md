---
term: seed NODES
---

Statička lista javnih Bitcoin čvorova, integrisana direktno u izvorni kod Bitcoin Core (`Bitcoin/src/chainparamsseeds.h`). Ova lista služi kao tačke povezivanja za nove Bitcoin čvorove koji se pridružuju mreži, ali se koristi samo ako DNS semena ne pruže odgovor u roku od 60 sekundi od njihovog zahteva. U tom slučaju, novi Bitcoin čvor će se povezati sa ovim seed čvorovima kako bi uspostavio prvu vezu sa mrežom i zatražio IP adrese drugih čvorova. Krajnji cilj je pribavljanje potrebnih informacija za obavljanje Inicijalnog Preuzimanja Bloka (IBD) i sinhronizaciju sa lancem koji ima najviše akumuliranog rada. Lista seed čvorova uključuje skoro 1000 čvorova, identifikovanih u skladu sa standardom uspostavljenim od strane BIP155. Tako, seed čvorovi predstavljaju treći metod povezivanja na mrežu za Bitcoin čvor, nakon moguće upotrebe `peers.dat` fajla, kreiranog od strane samog čvora, i traženja DNS semena.


> ► *Napomena, seed čvorovi ne treba da se mešaju sa "DNS semenkama," koje su drugi metod uspostavljanja veza.*