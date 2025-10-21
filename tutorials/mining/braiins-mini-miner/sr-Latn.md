---
name: Braiins Mini Miner
description: Pravljenje Mining lako od kuće.
---
![cover](assets/cover.webp)



## Uvod



Mini Miner braiins BMM 100 je proizvod koji je kreirao Mining pool Braiins. Ovaj uređaj ima atraktivan dizajn i izuzetno je tih. Proizvodi 1.1 Th/s računarske snage i troši oko 40 vati. Za razliku od drugih uređaja, nije open source, ali je zaista jednostavan za instalaciju, stvarno je potrebno samo nekoliko klikova! Mini Miner BMM 100 je prva verzija koja je objavljena. Sada je u proizvodnji verzija 2, nazvana BMM 101, koja se razlikuje od prve po većem ekranu i prisustvu Wi-Fi-ja, ali su procedure instalacije iste.



Takođe možete pronaći mnogo važnije informacije pregledom kompletnog vodiča direktno na [sajtu proizvođača](https://braiins.com/hardware/mini-Miner-bmm-100).



## Pregled BMM 100



uređaj izgleda kao paralelepiped sa ekranom na prednjoj strani



![image](assets/en/01.webp)



ventilator na gornjoj strani



![image](assets/en/02.webp)



dok na zadnjoj strani imamo: otvor za napajanje, prostor za SD karticu (koja može biti potrebna za bilo kakva ažuriranja), malo dugme koje kaže `IP REPORT` koje vam omogućava da saznate IP Address mini Miner, koji Address je potreban za pristup kontrolnoj tabli uređaja. Kada se dugme pritisne, IP Address se prikazuje oko 5 sekundi, zatim nestaje i ponovo se pojavljuje početni ekran. Međutim, ako trebate promeniti neka podešavanja, jednostavno ponovo pritisnite dugme i IP Address će se ponovo pojaviti na ekranu. Nastavljajući sa listom, nalazimo Ethernet port i pristup za resetovanje uređaja, za šta će vam biti potreban igla koju ćete držati 10 sekundi kako biste resetovali sva podešavanja mini Miner. Na kraju nalazimo dva indikatorska svetla, jedno Green i jedno crveno, koja nam ukazuju na status Miner.



![image](assets/en/03.webp)



## Povezivanje Mini Miner



Moraćete da povežete uređaj na internet putem ethernet-a, imajte na umu da sa novom verzijom (BMM 101) ovo više nije neophodno. Vraćajući se na ovaj mini Miner, kada pronađemo lokaciju, prvo ćemo ga morati povezati na internet liniju, a zatim na napajanje: uređaj će se automatski uključiti i prikazati svoj IP Address na ekranu.



## Konfiguracija



Moramo otvoriti pregledač i uneti IP Address koji nam prikazuje mini Miner u traci za pretragu. Podsećam vas da, kako biste pronašli uređaj na mreži, morate biti lokalni, tako da ćete morati imati računar koji koristite povezan na istu mrežu kao i mini Miner. Kada unesemo IP Address, pritisnemo enter i na ekranu će se pojaviti stranica za prijavu u operativni sistem mini Miner, koji je Braiins OS.



![image](assets/en/06.webp)



Da biste se prijavili, moraćete da unesete `root` kao svoje korisničko ime, dok lozinku možete ostaviti praznu. Kliknite na prijavu i pojaviće se vaša mini Miner kontrolna tabla.



![image](assets/en/07.webp)



## Opšta podešavanja



Hajde da idemo u Sistem



![image](assets/en/24.webp)



unutar postavki nalazimo neke opšte postavke kao što su tema (svetla ili tamna), jezik, vremenska zona i promena lozinke.



![image](assets/en/25.webp)



Ako odemo na "Mini Miner Ekran" umesto toga imamo postavke našeg mini Miner, kao što je prikaz ekrana. Možemo izabrati da li ćemo prikazati vreme, ili cenu Bitcoin, ili ekran sa informacijama o statusu mašine kao što su proizvod Hash, temperatura, potrošeni vati, i tako dalje. Ovde je na vama da izaberete šta želite da vidite na ekranu; takođe možemo promeniti osvetljenost ekrana, postaviti noćni režim, i prikazati vreme u 12-satnom ili 24-satnom formatu.



![image](assets/en/26.webp)



Kada izvršite izmene, kliknite na `Save Changes` i videćete izmene na ekranu vašeg uređaja.



![image](assets/en/27.webp)



## Povezivanje sa Mining pool



Sada još nismo operativni, jer se moramo povezati na bazen kako bismo pokrenuli Mining, pa moramo otići na "Konfiguracija"



![image](assets/en/08.webp)



i prvi unos je samo `Pools`.



![image](assets/en/09.webp)



Ovde ćemo morati da odlučimo koji bazen da koristimo. U ovom vodiču pokazaću vam dve opcije. Prva je da se povežemo na Mining pool Braiins koji takođe koriste profesionalni rudari, kao što možete videti iz ovog vodiča:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Druga opcija je da nas povežete sa Mining pool koji mina solo, kao Public Pool, pratite ovaj vodič da to uradite:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Braiins pool



Da bismo se povezali na ovaj bazen, potrebno je da napravimo nalog. ovaj bazen takođe vrši isplate koristeći Lightning Network, tako da ćemo moći da primimo nekoliko Sats dnevno. Da bismo to uradili, potrebno je da postavimo Address lightning na koji ćemo primati nagrade. Ako ne znate kako da napravite nalog na braiins bazenu ili kako da postavite svoj Address lightning, možete pratiti ovaj vodič:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Jednom kada je to urađeno, nalazimo se na Braiins pool kontrolnoj tabli. Ono što treba da uradimo je da kažemo pool-u da želimo da se povežemo sa jednim od naših Minera, tako da ćete na levoj strani ekrana pronaći nekoliko unosa. Treba da odemo na "workers."



![image](assets/en/04.webp)



i treba da kliknemo na ljubičasto dugme sa desne strane koje kaže "Connect workers."



![image](assets/en/05.webp)



Evo dolazi prozor sa informacijama koje su nam potrebne da povežemo naš mini Miner na bazen. Ovde jedina promena koju možemo napraviti je da izaberemo Stratum V2. Da biste saznali šta je Stratum v2 pogledajte ovaj unos u [glosaru](https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Sada treba da kopiramo ovaj string koji počinje sa stratumv2. Dakle, kliknemo na mali simbol "kopiraj", zatim idemo na kontrolnu tablu našeg mini Miner koji smo ostavili u konfiguraciji i bazenima. Kliknemo na dodaj novi bazen.



![image](assets/en/11.webp)



i nalepite niz koji smo kopirali u prostor ispod Pool URL.



![image](assets/en/12.webp)



Sada treba da dodamo korisničko ime i lozinku. Hajde da se vratimo na kontrolnu tablu bazena. Ispod takođe imamo userID i lozinku. UserID i naše korisničko ime, ono koje smo dali prilikom kreiranja naloga, plus ime Miner koje želimo da unesemo. možete odlučiti da li želite ili ne želite da date ime uređaju koji povezujete sa bazenom, to je opcionalno, ali je preporučljivo da ga unesete, tako da ako povežete više uređaja biće lakše odmah ih identifikovati. Ako ne želite da unesete ništa umesto toga možete ostaviti `workerName`.



![image](assets/en/13.webp)



Zatim idemo na naš mini Miner i unosimo korisničko ime. Ovde ćemo uneti u mom slučaju "finalstepbitcoin" što je moj userID, miniminer tačka. Ovo je ime koje sam odlučio da dam uređaju. Ako ne želite da ga imenujete, samo napišite userid tačka ime radnika. U mom slučaju to bi bilo finalstepbitcoin.ime radnika. Kada unesete korisničko ime, možete izabrati lozinku i upisati je u prazno polje. Takođe možete staviti anithing123, što je ono što je prikazano na ekranu bazena, ali to jednostavno želi da naznači da možete staviti bilo koju lozinku koju želite.



Kada unesete sve podatke, morate pritisnuti dugme za čuvanje sa desne strane (ono u obliku diskete) i na taj način ste konfigurisali podatke bazena u mini Miner.



![image](assets/en/14.webp)



Sada morate da se vratite na kontrolnu tablu bazena i kliknete na "Povezano! Vrati se nazad."



![image](assets/en/15.webp)



Povezali smo naš mini Miner sa braiins pool-om! Sada ga možete videti na listi radnika. Ako se ne pojavi, samo osvežite stranicu i sačekajte nekoliko trenutaka. Kada se pojavi, proverite da li ima status "OK" sa Green oznakom.



![image](assets/en/17.webp)



ako se vratite na kontrolnu tablu, trebali biste početi da primećujete kretanje na grafiku i videti Hashrate našeg uređaja. To znači da bazen prima naš rad i stoga mi, u suštini, potkopavamo.



![image](assets/en/16.webp)



### Javni bazen



Kroz ovaj pool možete okušati sreću i rudarenje solo, oslanjajući se na pool. U ovom slučaju nećemo dobiti nagradu, ali ćemo dobiti punu nagradu ako ikada uspemo da izrudarimo blok. Zatim ćemo se povezati sa javnim pool-om, Mining-only pool-om koji je potpuno open source. Otvaramo novi prozor u pretraživaču i idemo na [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



tamo ide stranica sa svim informacijama koje su nam potrebne. Zatim tamo kopiramo sloj Address



![image](assets/en/19.webp)



zatim se vraćamo na kontrolnu tablu našeg mini Miner, idemo na konfiguraciju i na bazene, kliknemo na dodaj novi bazen (isti proces kao što je gore prikazano) i nalepimo 'stratum Address pod URL bazena.



![image](assets/en/20.webp)



Sada se vratimo na stranicu bazena i vidimo da kao korisničko ime moramo uneti Bitcoin Address, što će biti ono na kojem ćemo primiti nagradu u slučaju da iskopamo blok, zatim tačku i zatim ime našeg uređaja, kao što smo to prethodno uradili sa Braiins Pool, dok lozinku možemo sami izabrati.



![image](assets/en/21.webp)



Vraćamo se na mini Miner i pod korisničko ime nalepimo Address Bitcoin praćeno tačkom i imenom, ja ću staviti `miniminer`. U lozinku ću umesto toga staviti test, vi unesite šta god želite.



![image](assets/en/22.webp)



Sada čuvamo postavke i onemogućavamo Braiins pool.



![image](assets/en/23.webp)



Dobro! Sada smo Mining na javnom bazenu!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)