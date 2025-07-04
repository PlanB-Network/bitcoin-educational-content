---
term: ANCHORS.DAT
---

Fil som används i Bitcoin Core-klienten för att lagra IP-adresserna för utgående noder som en klient var ansluten till innan den stängdes av. Anchors.dat skapas alltså varje gång noden stoppas och raderas när den startas om. De noder vars IP-adresser finns i den här filen används för att snabbt upprätta anslutningar när noden startas om.