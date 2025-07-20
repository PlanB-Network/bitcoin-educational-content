---
name: Javni bazen
description: Uvod u javni bazen
---

![signup](assets/cover.webp)


**Public Pool** nije samo bilo koji bazen; to je ono što je takođe poznato kao **Solo Pool**. Ako vaš Miner uspe u Mining bloku, onda prikupljate ceo Block reward, koji se ne deli sa drugim učesnicima bazena ili sa samim bazenom.


**Public Pool** isključivo pruža **blok šablon** za vaš Miner kako bi mogao obavljati svoj zadatak bez potrebe da imate **Bitcoin čvor** i softver koji komunicira sa vašim Miner. Pošto ne udružujete svoju računarsku snagu sa snagom drugih učesnika, vaše šanse da uspešno Mining blok su očigledno vrlo male, podsećajući donekle na sistem lutrije, gde ponekad srećni pojedinac osvoji džekpot.


![signup](assets/1.webp)


Na **Dashboardu** **Public Pool-a**, i dalje imate neke statistike kao što je **Total Hashrate** bazena, kao i distribuciju različitih tipova rudara koji su povezani sa bazenom.


![signup](assets/2.webp)


U prvim redovima možemo videti **Bitaxe** sa 1323 **Bitaxe** povezanih za ukupno 649TH/s. **Bitaxe** je **Open source** projekat koji omogućava jednostavno ponovno korišćenje čipa iz **ASIC** poput **Antminer S19** na **opensource** elektronskoj ploči kako bi se napravio mali Miner od 0.5TH/s za 15W. Ovo je Miner koji ćemo koristiti kao primer za ovaj tutorijal.


## Dodavanje **Radnika** 👷‍♂️


![signup](assets/cover.webp)


Na vrhu stranice, možete kopirati pool Address **stratum+tcp://public-pool.io:21496**.


Dalje, za polje **user**, unesite **Bitcoin** Address koji posedujete.


Ako imate više minera, možete uneti isti Address za sve njih kako bi se njihove **hashrates** kombinovale i prikazale kao jedan Miner. Takođe ih možete razlikovati dodavanjem posebnog imena svakom. Da biste to uradili, jednostavno dodajte **.workername** nakon **Bitcoin** Address.


Konačno, za polje **password**, koristite **‘x’**.


Primer: Ako je vaš **Bitcoin** Address **„bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv“** i želite da imenujete vaš Miner **„Brrrr“**, onda biste uneli sledeće informacije u Interface vašeg Miner:



- URL**: stratum+tcp://public-pool.io:21496
- KORISNIK**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- Lozinka**: **‘x’**

Ako je vaš Miner **Bitaxe**, polja su malo drugačija, ali informacije ostaju iste:


- URL**: public-pool.io (ovde, treba da uklonite deo na početku **‘stratum+tcp://’** i deo na kraju **‘:21496’** koji će biti naveden u polju za port)
- Port**: 21496
- Korisnik**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- Lozinka**: **‘x’**


![signup](assets/3.webp)


Nekoliko minuta nakon što pokrenete Mining, moći ćete da vidite svoje podatke na vebsajtu **Public Pool** pretraživanjem vašeg Address.


## Kontrolna tabla


![signup](assets/4.webp)


Jednom kada se povežete na **Public Pool**, možete pristupiti svom **Dashboard**-u pretraživanjem sa vašim **Bitcoin** Address koji ste uneli u polje **User**. U našem slučaju ovde, to je **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.


Na **Dashboardu**, prikazane su različite informacije kako o vašim podacima, tako i o mreži.


![signup](assets/5.webp)


Imate **Network Hash Rate** što odgovara ukupnoj radnoj snazi mreže **Bitcoin**.


**Težina mreže** označava težinu koju treba dostići da bi se blok validirao.


I **Vaša Najbolja Težina** je najveća težina koju ste dostigli. Ako, slučajno 🍀, dostignete težinu mreže, tada osvajate ceo Block reward... nakon 100 blokova. Morali biste da sačekate 100 blokova pre nego što budete mogli da ih potrošite.


Takođe imate **Visinu Bloka** koja je broj poslednjeg bloka koji je iskopan, kao i njegovu težinu izraženu u WU, pri čemu je maksimum 4,000,000.


Ispod možete videti sve statistike svakog od vaših uređaja pojedinačno ako ste im dali različita imena dodavanjem **.name** iza vašeg **Bitcoin** Address u polju **User**.