---
term: NAPAD PONOVNIM PUŠTANJEM
---

U kontekstu Bitcoin, napad ponovnim puštanjem (replay attack) se dešava kada se validna transakcija na jednom Blockchain zlonamerno reprodukuje na drugom Blockchain koji ima istu istoriju transakcija. Drugim rečima, transakcija emitovana na jednom kanalu može biti replicirana na drugom bez pristanka pošiljaoca prve transakcije.


Hajde da uzmemo primer hipotetičkog Hard Fork sa Bitcoin, nazvanog "*BitcoinBis*". Ako izvršite plaćanje u bitkoinima da biste kupili baget od pekara na pravom Blockchain Bitcoin, taj isti pekar bi mogao ponoviti tu legitimnu transakciju na *BitcoinBis* da dobije isti iznos u kriptovalutama na ovom Fork, bez ikakve vaše akcije.


Ovaj tip napada može se desiti samo u slučaju Blockchain grananja sa 2 nezavisna lanca koji traju tokom vremena. Tipično, to bi bio slučaj sa Hard Fork. Da bi napad ponovnim puštanjem bio moguć, 2 blokčejna moraju imati zajedničku istoriju, a duplirana transakcija mora koristiti kao ulaze UTXO-e kreirane iz prethodnih transakcija koje su se desile pre nego što su se dva lanca razdvojila, ili iz prethodnih transakcija koje su već bile ponovo puštene u prethodnom napadu ponovnim puštanjem.


Generalno govoreći, u računarstvu, napad ponovnim puštanjem (replay attack) sastoji se od presretanja i ponovnog korišćenja validnih podataka kako bi se prevario sistem ponavljanjem originalnog prenosa. Ovo ponekad može dovesti do krađe identiteta na mreži.


> ► *U slučaju napada ponovnim puštanjem na Bitcoin transakciju, ovo se ponekad jednostavno naziva "ponovljena transakcija."*