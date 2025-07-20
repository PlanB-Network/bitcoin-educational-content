---
term: POČETNO PREUZIMANJE BLOKA (IBD)
---

Odnosi se na proces kojim čvor preuzima i verifikuje Blockchain iz Genesis bloka, i sinhronizuje se sa drugim čvorovima u Bitcoin mreži. IBD mora biti sproveden prilikom pokretanja novog Full node. Na početku ove inicijalne sinhronizacije, čvor nema informacije o prethodnim transakcijama. Stoga preuzima svaki blok od drugih čvorova u mreži, verifikuje njegovu validnost, i zatim ga dodaje svojoj lokalnoj verziji Blockchain. Vredi napomenuti da IBD može biti dugotrajan i resursno zahtevan zbog rastuće veličine Blockchain i UTXO seta. Brzina njegovog izvršenja zavisi od računarskih sposobnosti računara koji hostuje čvor, kapaciteta njegove RAM memorije, brzine skladišnog uređaja i propusnog opsega. Da biste stekli predstavu, ako imate moćnu internet konekciju, a čvor je hostovan na najnovijem MacBook-u sa puno RAM-a, IBD će trajati samo nekoliko sati. Suprotno tome, ako koristite mikroračunar poput Raspberry Pi, IBD bi mogao trajati nedelju dana ili više.


> ► *U francuskom jeziku, generalno je prihvaćeno direktno referisati na IBD. Prevod koji se ponekad koristi je "synchronisation initiale", ili "téléchargement initial des blocs".*