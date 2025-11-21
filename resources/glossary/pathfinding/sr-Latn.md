---
term: PATHFINDING
---

Proces koji koristi čvor za određivanje optimalne putanje za usmeravanje plaćanja kroz mrežu Lightning kanala. Pronalaženje putanje obavlja čvor platioca, koji mora odabrati najpogodnije međučvorove kako bi stigao do primaoca. Ovaj izbor se zasniva na brojnim kriterijumima, kao što su naknade, kapacitet kanala i vremenska ograničenja.


Algoritmi za pronalaženje puta grade grafikon topologije mreže iz podataka o glasinama i procenjuju različite moguće rute između čvora platioca i čvora primaoca. Ove rute se rangiraju od najbolje do najgore prema različitim kriterijumima. Čvor zatim testira ove rute dok ne uspe da izvrši plaćanje na jednoj od njih.