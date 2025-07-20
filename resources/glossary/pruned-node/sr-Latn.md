---
term: OBREZANI ČVOR
---

Pruned čvor, na engleskom "Pruned Node", je Full node koji vrši obrezivanje Blockchain. Ovo uključuje progresivno uklanjanje najstarijih blokova, nakon što su propisno verifikovani, kako bi se zadržali samo najnoviji blokovi. Granica zadržavanja je specificirana u `Bitcoin.conf` fajlu putem `prune=n` parametra, gde je `n` maksimalna veličina koju zauzimaju blokovi u megabajtima (MB). Ako je nakon ovog parametra navedeno `0`, obrezivanje je onemogućeno i čvor zadržava Blockchain u celosti.


Obrezani čvorovi se ponekad smatraju različitim tipovima čvorova u odnosu na pune čvorove. Korišćenje obrezanog čvora može biti posebno interesantno za korisnike koji se suočavaju sa ograničenjima kapaciteta skladištenja. Trenutno, Full node mora imati skoro 600 GB samo za skladištenje Blockchain. Obrezani čvor može ograničiti potrebnu memoriju na do 550 MB. Iako koristi manje prostora na disku, obrezani čvor održava nivo verifikacije i validacije sličan onom kod Full node. Obrezani čvorovi stoga nude više poverenja svojim korisnicima u poređenju sa lakim čvorovima (SPV).