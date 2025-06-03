---
term: OGRANIČENJE JAZA
---

Parametar koji se koristi u Bitcoin Wallet softveru za određivanje maksimalnog broja uzastopnih neiskorišćenih adresa do generate pre nego što se zaustavi pretraga za dodatnim transakcijama. Podešavanje ovog parametra je često neophodno prilikom oporavka Wallet kako bi se osiguralo da su sve transakcije pronađene. Nedovoljan Gap Limit može rezultirati propuštanjem nekih transakcija ako su adrese preskočene tokom faza derivacije. Povećanje Gap Limita omogućava Wallet da pretražuje dalje u Address sekvenci, kako bi se oporavile sve povezane transakcije.


Zaista, jedan `xpub` teoretski može generisati više od 4 milijarde adresa za primanje (kako internih, tako i eksternih adresa). Međutim, Wallet softver ne može generisati i proveriti sve njih za upotrebu bez ogromnih operativnih troškova. Stoga, oni nastavljaju redosledom indeksa, jer je to obično redosled u kojem sav Wallet softver generiše adrese. Softver beleži svaki korišćeni Address pre nego što pređe na sledeći, i zaustavlja svoju pretragu kada naiđe na određeni broj uzastopno praznih adresa. Taj broj se naziva Gap Limit.


Ako je, na primer, Granica Praznine postavljena na `20`, i Address `m/84'/0'/0'/0/15/` je prazan, Wallet će izvesti adrese do `m/84'/0'/0'/0/34/`. Ako ovaj opseg adresa ostane neiskorišćen, pretraga se tu zaustavlja. Shodno tome, transakcija koja koristi Address `m/84'/0'/0'/0/40/` ne bi bila otkrivena u ovom primeru.