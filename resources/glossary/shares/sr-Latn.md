---
term: DEONICE
---

U kontekstu Mining bazena, udeo je indikator koji se koristi za kvantifikaciju doprinosa pojedinačnog Miner unutar bazena. Ova mera služi kao osnova za izračunavanje nagrade koju bazen preraspodeljuje svakom Miner. Svaki udeo odgovara Hash koji zadovoljava cilj težine niži od onog u Bitcoin mreži.


Da objasnimo pomoću analogije, zamislite kockicu sa 20 strana. Na Bitcoin, pretpostavimo da Proof of Work zahteva bacanje broja manjeg od 3 da bi se validirao blok (to jest, postizanje rezultata 1 ili 2). Sada, zamislite da je unutar Mining pool, ciljna težina za deonicu postavljena na 10. Dakle, za pojedinačni Miner u bazenu, svaki rezultat bacanja kockice koji je manji od 10 računa se kao važeća deonica. Te deonice se zatim prenose u bazen od strane Miner, kako bi se zatražila njihova nagrada, čak i ako ne odgovaraju važećem rezultatu za blok na Bitcoin.


Za svaki izračunati Hash, pojedinačni Miner u bazenu može naići na tri različita scenarija:


- Ako je vrednost Hash veća ili jednaka postavljenom cilju težine za deonicu bazena, onda ovaj Hash nije od koristi. Tada Miner menja svoj Nonce kako bi pokušao novi Hash: `Hash > share > block`.
- Ako je Hash manji od ciljne težine dela, ali veći ili jednak ciljnoj težini Bitcoin, onda ovaj Hash predstavlja važeći deo koji, međutim, nije dovoljan za validaciju bloka. Miner može poslati ovaj Hash svom bazenu da zatraži nagradu povezanu sa delom: `share > Hash > block`.
- Ako je Hash niži od ciljne težine mreže Bitcoin, smatra se i važećim deljenjem i važećim blokom. Miner prenosi ovaj Hash svom bazenu, koji žuri da ga emituje na mreži Bitcoin. Ovaj Hash se takođe računa kao važeće deljenje za Miner: `share > bloc > Hash`.


![](../../dictionnaire/assets/32.webp)


Ovaj sistem deljenja se koristi za procenu rada koji obavi svaki pojedinačni Miner unutar bazena, bez potrebe da se pojedinačno ponovo izračunavaju svi heševi koje generiše Miner, što bi bilo potpuno neefikasno za bazen.


Mining bazeni prilagođavaju težinu deonica kako bi uravnotežili opterećenje verifikacije i osigurali da svaki Miner, bilo mali ili veliki, podnosi deonice otprilike svakih nekoliko sekundi. Ovo omogućava tačno izračunavanje svakog Miner-ovog Hashrate i raspodelu nagrada prema izabranom metodu izračunavanja kompenzacije (PPS, PPLNS, TIDES...).


> ► *U francuskom, "shares" se može prevesti kao "part".*