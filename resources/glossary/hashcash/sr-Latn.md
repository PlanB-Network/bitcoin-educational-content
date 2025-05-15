---
term: HASHCASH
---

HashCash je Proof-of-Work sistem koji je dizajnirao Adam Back 1997. godine za borbu protiv spama i DoS napada. Zasniva se na principu da pošiljalac mora izvršiti računarski zadatak (konkretno, pronaći delimičnu koliziju na kriptografskoj Hash funkciji) kako bi dokazao svoj rad. Ovaj zadatak je skup u smislu vremena i energije za pošiljaoca, ali je verifikacija rezultata od strane primaoca brza i jednostavna. Ovaj protokol se pokazao posebno pogodnim za borbu protiv spama u email komunikacijama, jer je minimalno opterećujući za legitimne korisnike, dok predstavlja značajnu prepreku za spamera. Naime, slanje jednog emaila zahteva nekoliko sekundi računanja, ali ponavljanje ove operacije milion puta postaje izuzetno skupo u smislu energije i vremena, što često negira ekonomski interes spam kampanja, bilo da su u marketinške svrhe ili zlonamerne. Štaviše, omogućava očuvanje anonimnosti pošiljaoca.


HashCash je brzo usvojen od strane cypherpunks-a koji su želeli da razviju anoniman elektronski sistem valute bez posrednika. Zaista, inovacija Adama Back-a je po prvi put uvela koncept oskudice u digitalnom svetu. Koncept Proof of Work se zatim nalazi u nekoliko elektronskih sistema valute koji su prethodili Bitcoin, uključujući:


- b-money od Wei Daija objavljen 1998;
- R-POW od Hal Finney objavljen 2004;
- BitGold od Nick Szabo objavljen 2005.


Princip je HashCash-a takođe prisutan unutar Bitcoin protokola, gde se koristi kao mehanizam zaštite protiv Sybil napada.