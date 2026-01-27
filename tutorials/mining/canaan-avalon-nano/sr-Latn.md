---
name: Canaan Avalon Nano 3S
description: Konfigurisanje vašeg ASIC Avalon za solo rudarenje ili Miner pooling
---

![cover](assets/cover.webp)



U ovom vodiču ćemo pogledati kako postaviti Canaan Avalon Nano 3S, za jednostavnu kućnu upotrebu Miner.



Do sada su ASIC (*Application Specific Integrated Circuit*) mašine posebno dizajnirane za obavljanje određenog zadatka - u ovom slučaju, Hash proračun (SHA-256) za Miner od Bitcoin - bile posebno nepogodne za kućnu upotrebu. Buka, toplota koja se generiše i potreba za prilagođavanjem vaše električne instalacije kako bi podržala ogromnu snagu ovih uređaja sprečavali su većinu nas da učestvujemo.



Danas je Canaan, jedan od vodećih proizvođača ASIC mašina, odlučio da se pozabavi tržištem privatnih lica koja žele Miner kod kuće, nudeći niz proizvoda koji su relativno tihi i vrlo jednostavni za instalaciju (plug & play).



Ovi uređaji se reklamiraju ili kao pomoćni grejač u slučaju **Avalon Nano 3S (140W)**, ili kao mini radijator sa izlaznom snagom od **800W** u slučaju **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Imajte na umu da razlika u ceni u odnosu na tradicionalne grejače ekvivalentne snage u velikoj većini slučajeva ne omogućava ostvarivanje finansijskog profita. Satoši generisani aktivnošću Mining nikada neće nadoknaditi ovu razliku u ceni, osim ako nemate pristup besplatnoj (višak) ili veoma jeftinoj električnoj energiji.



Po mom mišljenju, ovi uređaji bi trebalo da se posmatraju više kao jednostavan način za Miner kod kuće za one koji to žele iz ličnih razloga: *dobijanje non-KYC Satss / igranje "lutrije" solominiranjem / učešće u Hashrate decentralizaciji itd..*, dok se **kao bonus** koristi toplota koja se generiše za grejanje sobe zimi. Ali ne kao način uštede novca u većini slučajeva barem (zapadne zemlje).



## Raspakivanje i karakteristike



Prvo, hajde da vidimo šta se nalazi unutar kutije Avalon Nano 3S.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Kada otvorite kutiju, pronaći ćete kartonski rukavac koji sadrži WIFI prijemnik koji, kao što ćemo kasnije videti, treba da priključite u USB port uređaja kako biste omogućili povezivanje na vašu lokalnu mrežu. Takođe je uključen priručnik za upotrebu i metalna igla za vraćanje uređaja na fabrička podešavanja ako je potrebno.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Kada je sve izvađeno iz kutije, evo šta imamo: sam uređaj naravno, korisnički priručnik, WIFI prijemnik, već pomenuti metalni vrh, i napajanje uređaja Supply. Kreditna kartica koja je priložena nije vredna pomena po našem mišljenju.



![image](assets/fr/05.webp)



Ispod je tabela koja rezimira opšte tehničke specifikacije Nano 3S :




| Karakteristika                                      | Vrednost                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Stopa hešovanja                                      | 6 Th/s +- 5%                                            |
| Potrošnja energije                               | 140 W                                                   |
| Buka                                                | 30 - 40 dB                                              |
| Opseg temperature vazduha na izlazu                 | 60-70°C (na temperaturi okoline 25°C)                |
| Zahtevi temperature okoline za upotrebu | -5 do 30°C                                            |
| Opseg ulaznog napona uređaja                         | 28V 5A kontinualno                                          |
| Opseg ulaznog napona adaptera                       | 110-240V AC 50/60Hz                                     |
| Veličina uređaja                                 | Dužina: 205 mm / Širina: 115 mm / Visina: 58.5 mm |
| Težina uređaja                                  | 0.86 kg                                                 |

## Uključivanje i povezivanje na lokalnu mrežu



Jednom kada ga raspakujete, postavite svoj Avalon Nano 3 S, ako je moguće, u relativno otvoren prostor kako bi se omogućila cirkulacija toplote. Zatim počnite umetanje malog WIFI prijemnog modula kao što je prikazano ispod:



![image](assets/fr/06.webp)


Zatim priključite USB-C priključak napajanja Supply u USB-C port uređaja da biste ga napajali.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Uređaj će se pokrenuti i Avalon Nano logo će se pojaviti na ekranu, nakon čega sledi logo "mobilnog telefona" sa rečima "Molimo Konfigurišite Mrežu Sa Avalon Family Aplikacijom".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Da biste to uradili, idite u prodavnicu mobilnih aplikacija, potražite i preuzmite aplikaciju **Avalon Family**.



![image](assets/fr/11.webp)


Kada instalirate, otvorite ga klikom na "Skip" u gornjem desnom uglu, zatim na dugme "Add" i na kraju na "Search". Uverite se da je Bluetooth omogućen na vašem pametnom telefonu, kako bi detekcija uređaja tekla glatko.



![image](assets/fr/12.webp)


Kada aplikacija detektuje uređaj, kliknite na njega i izaberite "Connect". Zatim ćete biti preusmereni na ekran gde možete uneti podatke za vašu WIFI konekciju.


![image](assets/fr/13.webp)


Kada je uređaj povezan na vašu lokalnu mrežu, ekran će sada izgledati ovako:



![image](assets/fr/14.webp)



Prikazuje "fiktivni" Hashrate, jer još nije konfigurisan nijedan bazen, i vreme uređaja, datum, napajanje i IP Address - veoma korisno ako želite da pristupite uređaju Interface putem računara i pregledača (više o tome kasnije).



![image](assets/fr/15.webp)




## Povezivanje na Mining pool



**Ovaj deo je zajednički za Nano 3s i Mini 3, jer su procesi strogo identični**.



Bilo da želimo da "solominiramo" ili Miner "pool", moraćemo da se povežemo na Mining pool. U stvari, naš uređaj nije ništa drugo do Hash-pravitelj bez svesti o Bitcoin mreži. Povezivanje na pool mu omogućava pristup Bitcoin mreži i omogućava mu da prima blok šablone na kojima će raditi.



### Korišćenje aplikacije za povezivanje sa Mining pool



Na aplikaciji Avalon Family, izaberite uređaj kao što je prikazano ispod. Zatim će vam automatski biti zatraženo da promenite administratorsku lozinku mašine. Kliknite na "OK" ako želite to da uradite, ili na otkaži da ostavite podrazumevanu lozinku za pristup "admin".


![image](assets/fr/16.webp)


Zatim izaberite "Settings", zatim "Pool Config" i unesite parametre za 3 tražena bazena.


Bazen #2 i #3 će služiti kao rezervne opcije u slučaju da jedan od njih zakaže, kako vaš Miner ne bi radio uzalud. Po defaultu, Hashrate će biti usmeren na bazen #1.



U našem slučaju biramo:




- 1 - Javna Plaža,
- 2 - CkPool,
- 3 - Okean.



![image](assets/fr/17.webp)



Za više detalja o tome kako se povezati na Mining pool, pogledajte ove tutorijale :



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Da sumiramo, mi treba da





- bazen Address, obično **stratum+tcp://xxxxxxxx:port**.





- ime "radnika" sastavljeno od *vaš Bitcoin Address* i *pseudonima* koji izaberete za vaš uređaj, a ta 2 su odvojena *tačkom*, na primer:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- lozinka, koja je obično uvek "**x**"



Kada su informacije o bazenu unete, kliknite na "Sačuvaj".



![image](assets/fr/18.webp)


Ponovo pokrenite uređaj prema uputstvima i sačekajte nekoliko minuta dok vaš Hashrate ne bude usmeren ka željenom bazenu (#1).



### Korišćenje pregledača za povezivanje sa Mining pool



Takođe se možete povezati sa Mining pool i, generalno, pristupiti sistemu za upravljanje Interface vašeg uređaja putem omiljenog pregledača.



Da biste to uradili, upišite u pretraživač IP Address uređaja prikazanog na ekranu ispod, u našem primeru **192.168.144.6**



![image](assets/fr/15.webp)



Pojaviće se sledeća stranica, tražeći od vas da otvorite Avalon Family aplikaciju i skenirate QR kod prikazan u aplikaciji.



![image](assets/fr/20.webp)



Otvorite aplikaciju i kliknite na 3 crtice u gornjem desnom uglu, zatim na skeniraj. Skenirajte QR kod pregledača, zatim unesite administratorsku lozinku aplikacije i kliknite OK.



![image](assets/fr/21.webp)



Ovde ste na veb stranici koja vam omogućava interakciju sa vašim Avalon-om. To je više kontrolna tabla za prikazivanje metrika mašine, nego sredstvo za njeno konfigurisanje.



Ali podešavanja bazena i dalje mogu biti dostupna na ovaj način, klikom na **"Pool Config "** u donjem desnom uglu.



![image](assets/fr/22.webp)



Na isti način kao sa mobilnom aplikacijom, ovde možete uneti parametre vašeg bazena.



![image](assets/fr/23.webp)



## Kontrolišite svoj uređaj putem Avalon Family aplikacije



Sada smo povezali naš kućni Miner na našu lokalnu mrežu i usmerili naš Hashrate ka bazenima Minings. Sada hajde da otkrijemo osnovne karakteristike naše mašine putem Avalon Family aplikacije.



U aplikaciji Avalon porodice, kliknite na ikonu koja odgovara Avalon Nano 3S.


zatim vam se prikazuju 3 menija: "Work Mode", "Light control" i "Settings". Prvo, kliknite na "Work Mode". Zatim će vam biti ponuđena 3 režima napajanja za vašu mašinu.



**Nizak**: donosi vam oko 3 Th/s Hashrate uz potrošnju energije od 70W


**Medium**: donosi vam približno 4.5 Th/s Hashrate uz potrošnju od 100W


**High**: će vam dati oko 6 Th/s Hashrate pri maksimalnoj potrošnji od 140W



![image](assets/fr/31.webp)


Hajde da se povučemo korak unazad i istražimo meni "Light Control". Ovo je isključivo kozmetički. Dostupan je čitav niz opcija za variranje boje, intenziteta, toplote, isključivanje LED dioda uređaja noću itd... Lako je saznati sami.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Konačno, poslednji meni koji nam je dostupan je meni "Settings" koji smo već videli za povezivanje sa našim Mining bazenima. Ovde možete upravljati svojim bazenima, promeniti administratorsku lozinku uređaja i pratiti razne metrike kao što su datum isteka garancije, čistoća filtera ili kako kontaktirati podršku u slučaju kvara.



![image](assets/fr/35.webp)


Za održavanje i kako bi filter bio što čistiji, preporučujemo korišćenje usisivača i redovno usisavanje ulaza i izlaza vazduha kako bi se sprečilo začepljenje.



Došli smo do kraja ovog tutorijala, koji nas je naučio kako da povežemo naš Avalon Nano 3 S na našu lokalnu mrežu, kako da usmerimo naš Hashrate na Mining bazene, i kako da se krećemo kroz opcije i postavke koristeći Avalon Family aplikaciju.



Da biste saznali više, pogledajte naš vodič o superiornoj verziji Avalona: Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7