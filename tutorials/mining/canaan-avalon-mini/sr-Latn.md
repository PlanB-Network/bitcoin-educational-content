---
name: Canaan Avalon Mini 3
description: Konfigurisanje vašeg ASIC Avalon za solo rudarenje ili Miner pooling
---

![cover](assets/cover.webp)



U ovom vodiču ćemo pogledati kako postaviti Canaan Avalon Mini 3, za jednostavnu kućnu upotrebu Miner.



Do sada su ASIC (*Application Specific Integrated Circuit*) mašine posebno dizajnirane za obavljanje određenog zadatka - u ovom slučaju, Hash proračun (SHA-256) za Miner od Bitcoin - bile posebno nepogodne za kućnu upotrebu. Buka, toplota koja se generiše i potreba za prilagođavanjem vaše električne instalacije kako bi podržala ogromnu snagu ovih uređaja sprečavali su većinu nas da učestvujemo.



Danas je Canaan, jedan od vodećih proizvođača ASIC mašina, odlučio da se usmeri na tržište privatnih korisnika koji žele Miner kod kuće, nudeći niz proizvoda koji su relativno tihi i veoma laki za instalaciju (plug & play).



Ovi uređaji se reklamiraju ili kao pomoćni grejač u slučaju **Avalon Nano 3S (140W)**, ili kao mini radijator sa izlaznom snagom od **800W** u slučaju **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Imajte na umu da razlika u ceni u odnosu na tradicionalne grejače ekvivalentne snage u velikoj većini slučajeva ne omogućava ostvarivanje finansijskog profita. Satoši generisani aktivnošću Mining nikada neće nadoknaditi ovu razliku u ceni, osim ako nemate pristup besplatnoj (višak) ili veoma jeftinoj električnoj energiji.



Po mom mišljenju, ovi uređaji bi trebalo da se posmatraju više kao jednostavan način za Miner kod kuće za one koji to žele iz ličnih razloga: *dobijanje non-KYC Satss / igranje "lutrije" solominiranjem / učešće u Hashrate decentralizaciji itd..*., dok se **kao bonus** koristi toplota koja se generiše za grejanje sobe zimi. Ali ne kao način uštede novca u većini slučajeva barem (zapadne zemlje).



## Raspakivanje i karakteristike



### Avalon Nano 3S



Prvo, da vidimo šta se nalazi unutar kutije Avalon Mini 3.



![image](assets/fr/24.webp)



Kada otvorite kutiju, uputstva za upotrebu su direktno ispred vas, ali što je još važnije, WIFI prijemni modul je sakriven ispod okrugle bele nalepnice levo od uputstava za upotrebu. Biće vam potreban kasnije.



![image](assets/fr/25.webp)



Ispod bloka od pene nalazi se uređaj, a kada se izvadi iz kutije, jedinica za napajanje Supply.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Uključivanje i povezivanje na lokalnu mrežu



Nakon raspakivanja, postavite svoj Avalon Mini 3 na relativno otvoreno područje, ako je moguće, kako bi se omogućila pravilna cirkulacija toplote. Zatim počnite tako što ćete umetnuti mali WIFI prijemni modul u USB port na donjoj strani uređaja, priključiti napajanje Supply i osigurati da je dugme za napajanje u položaju "1".



![image](assets/fr/28.webp)



Kada su ovi koraci završeni, LED displej uređaja se osvetljava i prikazuje simbol "Bluetooth", što ukazuje da je spreman za povezivanje sa vašom lokalnom mrežom putem Avalon Family aplikacije.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Da biste to uradili, idite u prodavnicu aplikacija na svom mobilnom uređaju, potražite i preuzmite aplikaciju **Avalon Family**.



![image](assets/fr/11.webp)


Kada instalirate, otvorite ga klikom na "Skip" u gornjem desnom uglu, zatim na dugme "Add" i na kraju na "Search". Uverite se da je Bluetooth omogućen na vašem pametnom telefonu, kako bi detekcija uređaja tekla glatko.



![image](assets/fr/12.webp)


Kada aplikacija detektuje uređaj, kliknite na njega i izaberite "Poveži". Zatim ćete biti preusmereni na ekran gde možete uneti podatke za vašu WIFI konekciju.


![image](assets/fr/13.webp)


Kada se povežete na vašu lokalnu mrežu, vaš Mini 3 će prikazati informacije kao što su IP Address, vreme, Hashrate i električna snaga.



Ispod je tabela sažetka opštih tehničkih specifikacija za Mini 3:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Povezivanje na Mining pool



**Ovaj deo je zajednički za Nano 3s i Mini 3 uređaje, jer su procesi strogo identični **



Bilo da želimo da "solominiramo" ili Miner "pool", moraćemo da se povežemo na Mining pool. U stvari, naš uređaj nije ništa drugo do Hash-pravitelj bez svesti o Bitcoin mreži. Povezivanje na pool mu omogućava pristup Bitcoin mreži i omogućava mu da prima blok šablone na kojima će raditi.



### Korišćenje aplikacije za povezivanje sa Mining pool



Na aplikaciji Avalon Family, izaberite uređaj kao što je prikazano ispod. Zatim će vam automatski biti zatraženo da promenite administratorsku lozinku mašine. Kliknite na "OK" ako želite to da uradite, ili na otkaži da ostavite podrazumevanu lozinku za pristup "admin".


![image](assets/fr/16.webp)


Zatim izaberite "Settings", zatim "Pool Config" i unesite parametre za 3 tražena pool-a.


Bazen #2 i #3 će služiti kao rezervne opcije u slučaju da jedan od njih zakaže, kako vaš Miner ne bi radio uzalud. Po defaultu, Hashrate će biti usmeren na bazen #1.



U našem slučaju biramo:




- 1 - Javani bazen,
- 2 - CkPool,
- 3 - Okean.



![image](assets/fr/17.webp)



Za više detalja o tome kako se povezati na Mining pool, molimo pogledajte ove tutorijale :



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Da sumiramo, potrebni su nam





- bazen Address, obično **stratum+tcp://xxxxxxxx:port**.





- ime "worker"-a sastoji se od *tvog Bitcoin Address* i *pseudonima* koji izabereš za svoj uređaj, pri čemu su ta 2 dela odvojena *tačkom*, na primer:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- lozinka, koja je obično uvek "**x**"



Kada su informacije o bazenu unete, kliknite na "Sačuvaj".



![image](assets/fr/18.webp)


Ponovo pokrenite uređaj prema uputstvima i sačekajte nekoliko minuta dok vaš Hashrate ne bude usmeren ka željenom bazenu (#1).



### Korišćenje pregledača za povezivanje sa Mining pool



Takođe se možete povezati sa Mining pool i, generalno, pristupiti sistemu upravljanja Interface vašeg uređaja putem omiljenog pregledača.



Da biste to uradili, upišite u pretraživač IP Address uređaja prikazanog na ekranu ispod, u našem primeru **192.168.144.6**



![image](assets/fr/15.webp)



Pojaviće se sledeća stranica, tražeći od vas da otvorite Avalon Family aplikaciju i skenirate QR kod prikazan u aplikaciji.



![image](assets/fr/20.webp)



Otvorite aplikaciju i kliknite na 3 crtice u gornjem desnom uglu, zatim na skeniraj. Skenirajte QR kod pregledača, zatim unesite administratorsku lozinku aplikacije i kliknite OK.



![image](assets/fr/21.webp)



Ovde ste na veb stranici koja vam omogućava interakciju sa vašim Avalon-om. To je više kontrolna tabla za prikazivanje metrika mašine, nego sredstvo za njeno konfigurisanje.



Ali postavke bazena i dalje se mogu pristupiti na ovaj način, klikom na **"Pool Config "** u donjem desnom uglu.



![image](assets/fr/22.webp)



Na isti način kao sa mobilnom aplikacijom, ovde možete uneti parametre vašeg bazena.



![image](assets/fr/23.webp)



## Kontrolišite svoj uređaj putem Avalon Family aplikacije



Sada smo povezali naš kućni Miner na našu lokalnu mrežu i usmerili naš Hashrate ka bazenima Minings. Sada hajde da otkrijemo osnovne karakteristike naše mašine putem Avalon Family aplikacije.



U glavnom meniju aplikacije Avalon porodice, kliknite na ikonu koja odgovara Avalon Mini 3. Bićete direktno preusmereni na meni za upravljanje režimima rada.



Dostupne su 3 opcije: režim "Heater", režim "Mining" ili režim "Night".





- U režimu "Grejač" imate 2 nivoa snage "Eco" ili "Super".


Nivo "Eco" odgovara grejnoj snazi od 500W za Hashrate od oko 25 Th/s i 40 dB za nivo zvuka.


Nivo "Super" odgovara izlaznoj snazi od 650 W pri približno 30Th/s i 45 dB. Ovaj režim vam omogućava da postavite maksimalnu temperaturu okoline iznad koje će jedinica prestati sa radom.



![image](assets/fr/36.webp)




- U režimu "Mining", jedinica radi na maksimalnoj brzini, bez mogućnosti postavljanja ciljne temperature (osim ugrađenog ograničenja pregrevanja, naravno). Cilj je iskoristiti performanse Miner na najbolji način. Ovde, izlazna snaga prilazi 800 W pri oko 37.5 Th/s i nivou buke od 50-55 dB.



![image](assets/fr/37.webp)


Konačno, u režimu "Noć", vaš Mini 3 radi na najnižoj mogućoj brzini uz minimalnu buku. 400 W, 20 Th/s i približno 33 dB.



Ovde takođe možete postaviti ciljnu temperaturu iznad koje uređaj prelazi u neaktivan režim i zaustavlja Miner. Ako temperatura padne, uređaj će se ponovo pokrenuti i nastaviti grejanje i Miner. U ovom režimu, LED diode na displeju su isključene po defaultu, ali ih možete uključiti ako je potrebno da osvetlite prostoriju u mraku, poput noćnog svetla (pogledajte fotografiju ispod).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Konačno, možete upravljati LED svetlima vašeg Avalona putem menija "Display". Možete izabrati da se prikazuju relevantne informacije o radu, da se prikazuje vreme, ili čak prilagođena (pikselizovana) slika.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Kao i kod Avalon Nano 3S, meni "Settings" vam omogućava da promenite administratorsku lozinku, postavke bazena, proverite blokadu filtera (nalazi se na donjoj strani uređaja), kontaktirate podršku ili pregledate logove uređaja.



![image](assets/fr/42.webp)



Još jednom, filter na dnu jedinice može se očistiti usisivačem, što redovnije to bolje.



Došli smo do kraja ovog vodiča, koji nas je naučio kako da povežemo naš Avalon Mini 3 na našu lokalnu mrežu, kako da usmerimo naš Hashrate ka Mining bazenima, i kako da se krećemo kroz opcije i postavke koristeći Avalon Family aplikaciju.



Da biste saznali više, pogledajte naš vodič o manjoj verziji Avalona: Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6